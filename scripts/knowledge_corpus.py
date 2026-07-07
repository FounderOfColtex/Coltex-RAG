#!/usr/bin/env python3
"""
Coltex Knowledge Corpus — build, organize, and wire the enterprise knowledge dataset.

Creates domain folders, knowledge clusters, graph links, and a catalog manifest.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from brain_schema import CATEGORIES, KNOWLEDGE_HUBS
from brain_architecture import (
    ROUTE_TYPES,
    domain_to_cluster,
    functional_clusters,
    hub_registry,
    load_architecture,
    memory_tiers,
    processing_layers,
)
from corpus_templates import TOPICS
from expand_curated_kb import (
    CURATED_DOC_TYPES,
    _chunk_id,
    _existing_chunk_max,
    _format_chunk_markdown,
    _slugify,
    iter_curated_jobs,
)
from generate_corpus import build_document

CORPUS_ROOT = ROOT / "knowledge-base" / "knowledge-corpus"
CATALOG_INDEX_PATH = ROOT / "data" / "brain" / "catalog-index.json"
ARCHITECTURE_PATH = ROOT / "data" / "brain" / "architecture-manifest.json"

ROUTE_TEMPLATE = """---
id: ROUTE-{route_id}
title: "Domain Route: {source_cluster} → {target_cluster} ({route_type})"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: {source_cluster}
cluster_target: {target_cluster}
route_type: {route_type}
tags: [domain-route, {route_type}, {source_cluster}, {target_cluster}]
related: [{source_anchor}, {target_anchor}]
see_also: [{source_anchor}, {target_anchor}]
synthesizes: [{source_anchor}]
---

# Domain Route: {source_cluster} → {target_cluster}

**Type:** `{route_type}` · **Tier:** association layer

## Route
Documents in cluster `{source_cluster}` connect to cluster `{target_cluster}` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `{source_anchor}` ({source_cluster})
- Target: `{target_anchor}` ({target_cluster})

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
"""

HUB_ANCHOR_TEMPLATE = """---
id: HUB-{hub_slug_upper}
title: "Knowledge Cluster: {hub_title}"
doc_type: architecture_decision
category: {category}
hub: {hub_slug}
cluster: {cluster}
tags: [hub, knowledge-cluster, {hub_slug}]
see_also: [ARCH-00001]
---

# {hub_title}

Central knowledge cluster for the Coltex corpus.

## Components
{components}

## Cluster assignment
**{cluster}** cluster · tier `{tier}`

## Document types in this hub
{doc_types}

## GraphRAG
All documents with `hub: {hub_slug}` form a traversable cluster.
Graph links and domain routes connect this hub to other knowledge clusters.
"""

DOMAIN_README = """# {name} Domain

Part of the **Coltex Knowledge Corpus** — `{category}` knowledge cluster.

Documents here are auto-generated, graph-linked, and indexed by Coltex.
Each file carries typed metadata (`doc_type`, `hub`, `related`) for GraphRAG traversal.

## Stats
- Category: `{category}`
- Parent: `knowledge-corpus/domains/{category}/`

Query this domain:
```bash
python3 -m brain retrieve "your question about {category}"
```
"""

HUB_README = """# {title}

Knowledge cluster `{slug}` — documents sharing `hub: {slug}` metadata.

## Components
{components}

## Linked doc types
{doc_types}
"""

GRAPH_LINK_TEMPLATE = """---
id: LINK-{link_id}
title: "Graph Link: {source_hub} ↔ {target_hub}"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, {source_hub}, {target_hub}]
related: [{source_doc}, {target_doc}]
see_also: [{source_doc}, {target_doc}]
depends_on: [{source_doc}]
---

# Graph Link: {source_hub} → {target_hub}

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**{relation}** — documents in `{source_hub}` {relation_desc} `{target_hub}`.

## Source hub
- Hub: `{source_hub}`
- Anchor: `{source_doc}`

## Target hub
- Hub: `{target_hub}`
- Anchor: `{target_doc}`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
"""


def _ensure_structure() -> dict[str, Path]:
    """Create advanced knowledge-corpus folder tree (Knowledge Architecture v2)."""
    cfg = load_architecture()
    dirs: dict[str, Path] = {
        "root": CORPUS_ROOT,
        "domains": CORPUS_ROOT / "domains",
        "hubs": CORPUS_ROOT / "hubs",
        "graph_links": CORPUS_ROOT / "graph-links",
        "domain_routes": CORPUS_ROOT / "domain-routes",
        "processing_layers": CORPUS_ROOT / "processing-layers",
        "memory": CORPUS_ROOT / "memory",
        "quick_reference": CORPUS_ROOT / "quick-reference",
        "clusters": CORPUS_ROOT / "clusters",
        "retention": CORPUS_ROOT / "retention",
        "automation": CORPUS_ROOT / "automation",
        "operations": CORPUS_ROOT / "operations",
        "routing": CORPUS_ROOT / "routing",
        "priority": CORPUS_ROOT / "priority",
    }
    for key, path in list(dirs.items()):
        if key in ("root",):
            continue
        path.mkdir(parents=True, exist_ok=True)

    for layer in processing_layers(cfg):
        layer_path = CORPUS_ROOT / layer.path
        layer_path.mkdir(parents=True, exist_ok=True)
        readme = layer_path / "README.md"
        if not readme.exists():
            readme.write_text(
                f"# Processing Layer {layer.slug}\n\n**Role:** {layer.role}\n\n**Latency target:** {layer.latency_ms}ms\n",
                encoding="utf-8",
            )

    cluster_paths: dict[str, Path] = {}
    for cluster in functional_clusters(cfg):
        cp = CORPUS_ROOT / cluster.path
        cp.mkdir(parents=True, exist_ok=True)
        cluster_paths[cluster.slug] = cp
        readme = cp / "README.md"
        if not readme.exists():
            domains = ", ".join(cluster.domains) or "cross-domain"
            readme.write_text(
                f"# {cluster.slug.title()} Cluster\n\n**Role:** {cluster.role}\n\n**Domains:** {domains}\n",
                encoding="utf-8",
            )

    for tier in memory_tiers(cfg):
        mp = CORPUS_ROOT / tier.path
        mp.mkdir(parents=True, exist_ok=True)
        readme = mp / "README.md"
        if not readme.exists():
            cap = tier.capacity_docs or "unlimited"
            readme.write_text(
                f"# Memory: {tier.slug}\n\n**Role:** {tier.role}\n\n**Capacity:** {cap} docs\n",
                encoding="utf-8",
            )

    d2c = domain_to_cluster(cfg)
    all_domains = sorted(set(list(d2c.keys()) + list(CATEGORIES)))
    domain_paths: dict[str, Path] = {}
    for cat in all_domains:
        d = dirs["domains"] / cat
        d.mkdir(parents=True, exist_ok=True)
        readme = d / "README.md"
        cluster = d2c.get(cat, "general")
        if not readme.exists():
            readme.write_text(
                DOMAIN_README.format(name=cat.replace("_", " ").title(), category=cat)
                + f"\n\n**Cluster:** `{cluster}`\n",
                encoding="utf-8",
            )
        domain_paths[cat] = d

    hub_paths: dict[str, Path] = {}
    registry = {e.slug: e for e in hub_registry(cfg)}
    for hub in KNOWLEDGE_HUBS:
        h = dirs["hubs"] / hub.slug
        h.mkdir(parents=True, exist_ok=True)
        readme = h / "README.md"
        if not readme.exists():
            components = "\n".join(f"- {c}" for c in hub.components)
            doc_types = ", ".join(hub.doc_types)
            entry = registry.get(hub.slug)
            cluster_info = f"\n\n**Cluster:** `{entry.cluster}` · **Tier:** `{entry.tier}`" if entry else ""
            readme.write_text(
                HUB_README.format(
                    title=hub.title,
                    slug=hub.slug,
                    components=components,
                    doc_types=doc_types,
                )
                + cluster_info,
                encoding="utf-8",
            )
        hub_paths[hub.slug] = h

    identity_path = dirs["processing_layers"] / "L6-governance" / "CORPUS_IDENTITY.md"
    identity_path.parent.mkdir(parents=True, exist_ok=True)
    if not identity_path.exists():
        identity_path.write_text(_corpus_identity(), encoding="utf-8")

    root_readme = CORPUS_ROOT / "README.md"
    root_readme.write_text(_knowledge_corpus_readme(), encoding="utf-8")

    dirs["domain_paths"] = domain_paths  # type: ignore
    dirs["hub_paths"] = hub_paths  # type: ignore
    dirs["cluster_paths"] = cluster_paths  # type: ignore
    return dirs


def _corpus_identity() -> str:
    return """---
id: ARCH-00001
title: Coltex Knowledge Architecture — Corpus Identity
doc_type: deep_dive
category: rag
hub: coltex_knowledge_core
cluster: architecture
tags: [architecture, identity, knowledge-corpus, knowledge_architecture]
---

# Coltex Knowledge Architecture v2

The governance layer of Coltex — a **multi-tier knowledge architecture** for enterprise-scale RAG datasets.

## Processing tiers
| Tier | Regions |
|------|---------|
| Ingestion (L1) | Raw document intake, chunk signals |
| Association (L2-L4) | Domain linking, cluster assignment, GraphRAG |
| Executive (L5-L6) | Context assembly, governance |
| Operations | Quick reference, runbooks, health checks |

## Functional clusters
| Cluster | Role |
|---------|------|
| Architecture | ADRs, agentic systems, API design |
| Retrieval | RAG, embeddings, LLM integration |
| Data | SQL, vectors, indexing |
| Observability | Monitoring, MLOps |
| Security | Access control, incidents, compliance |
| Automation | CI/CD, infrastructure |

## Corpus report
```bash
python3 -m brain report
make corpus-report
```
"""


def _knowledge_corpus_readme() -> str:
    return """# Coltex Knowledge Architecture

Enterprise RAG knowledge corpus with **6 processing layers**, **10 functional clusters**, **4 memory tiers**, **18 knowledge hubs**, and **millions of graph edges**.

## Structure
```
knowledge-corpus/
├── processing-layers/L1-ingestion … L6-governance
├── clusters/                        # Functional domain groupings
├── domains/                         # 62+ technology domains
├── hubs/                            # 18 knowledge clusters
├── graph-links/                     # Hub-to-hub graph links
├── domain-routes/                   # Inter-cluster routes
├── memory/                          # Tiered retention stores
└── quick-reference/                 # FAQ index
```

## Build
```bash
make corpus-advanced              # Full architecture bootstrap
make corpus-grow COUNT=1000       # Add domain documents
make corpus-mega                  # 10,000 documents
```

## Query
```bash
make index
python3 -m brain report
python3 -m brain retrieve "Explain domain route routing" --context
```
"""


def grow_domains(count: int, dry_run: bool = False) -> dict:
    """Generate documents into domain folders."""
    structure = _ensure_structure()
    domain_paths: dict[str, Path] = structure["domain_paths"]  # type: ignore

    start_num = _existing_chunk_max() + 1
    for path in CORPUS_ROOT.rglob("CHUNK-*.md"):
        m = re.match(r"CHUNK-(\d+)", path.name)
        if m:
            start_num = max(start_num, int(m.group(1)) + 1)

    jobs = iter_curated_jobs(count, start_num)
    written = 0
    by_domain: dict[str, int] = {}

    for chunk_num, topic, doc_type, variant in jobs:
        body, metadata = build_document(topic, doc_type, variant, scale=1000)
        metadata["hub"] = metadata.get("hub") or topic.hub or f"domain_{topic.category}"
        related = [_chunk_id(chunk_num - i) for i in range(1, min(4, chunk_num - start_num + 1))]
        content = _format_chunk_markdown(chunk_num, body, metadata, related)

        domain_dir = domain_paths.get(topic.category) or (structure["domains"] / topic.category)
        domain_dir.mkdir(parents=True, exist_ok=True)

        slug = _slugify(metadata["title"])
        filename = f"CHUNK-{chunk_num:05d}-{slug}.md"
        path = domain_dir / filename

        if not dry_run:
            path.write_text(content, encoding="utf-8")
        written += 1
        by_domain[topic.category] = by_domain.get(topic.category, 0) + 1

    return {
        "documents_written": written,
        "start_chunk": start_num,
        "end_chunk": start_num + written - 1 if written else start_num,
        "domains_touched": len(by_domain),
        "by_domain": by_domain,
        "dry_run": dry_run,
    }


def wire_graph_links(dry_run: bool = False) -> dict:
    """Create graph-link documents connecting knowledge hubs."""
    structure = _ensure_structure()
    link_dir: Path = structure["graph_links"]
    hubs = KNOWLEDGE_HUBS
    written = 0
    link_ids: list[str] = []

    relations = [
        ("depends_on", "depends on"),
        ("see_also", "is related to"),
        ("calls", "calls into"),
        ("documents", "documents"),
    ]

    for i, source in enumerate(hubs):
        for j, target in enumerate(hubs):
            if source.slug == target.slug:
                continue
            relation, relation_desc = relations[(i + j) % len(relations)]
            link_num = i * len(hubs) + j
            link_id = f"{link_num:05d}"
            source_doc = f"HUB-{source.slug.upper().replace('-', '_')}"
            target_doc = f"HUB-{target.slug.upper().replace('-', '_')}"

            content = GRAPH_LINK_TEMPLATE.format(
                link_id=link_id,
                source_hub=source.slug,
                target_hub=target.slug,
                source_doc=source_doc,
                target_doc=target_doc,
                relation=relation,
                relation_desc=relation_desc,
            )
            path = link_dir / f"LINK-{link_id}-{source.slug}-to-{target.slug}.md"
            if not dry_run:
                path.write_text(content, encoding="utf-8")
            written += 1
            link_ids.append(f"LINK-{link_id}")

    return {"graph_links_written": written, "link_ids": link_ids[:10], "dry_run": dry_run}


def seed_quick_reference(dry_run: bool = False) -> dict:
    """Quick-reference FAQ documents for common queries."""
    structure = _ensure_structure()
    faq_dir: Path = structure["quick_reference"]
    prompts = [
        ("What is Coltex?", "Coltex is an enterprise RAG knowledge corpus with hybrid retrieval."),
        ("What is GraphRAG?", "GraphRAG expands vector hits via typed document relationship edges."),
        ("How do I query the corpus?", "python3 -m brain retrieve \"your question\" --context"),
        ("How do I expand the corpus?", "make corpus-grow COUNT=500"),
        ("What is a graph link?", "A cross-hub edge in knowledge-corpus/graph-links/."),
    ]
    written = 0
    for i, (q, a) in enumerate(prompts):
        content = f"""---
id: FAQ-{i:05d}
title: "{q}"
doc_type: faq
category: rag
hub: coltex_knowledge_core
tags: [faq, quick-reference]
---

# {q}

{a}

## Quick reference
FAQ entries optimized for common queries during corpus reporting and retrieval.
"""
        path = faq_dir / f"FAQ-{i:05d}-{ _slugify(q) }.md"
        if not dry_run:
            path.write_text(content, encoding="utf-8")
        written += 1
    return {"quick_reference_written": written, "dry_run": dry_run}


def wire_domain_routes(dry_run: bool = False) -> dict:
    """Create inter-cluster domain route documents."""
    structure = _ensure_structure()
    route_dir: Path = structure["domain_routes"]
    clusters = functional_clusters()
    written = 0

    for i, source in enumerate(clusters):
        for j, target in enumerate(clusters):
            if source.slug == target.slug:
                continue
            route_type = ROUTE_TYPES[(i + j) % len(ROUTE_TYPES)]
            rid = f"{i:02d}{j:02d}"
            source_anchor = f"CLUSTER-{source.slug.upper()}"
            target_anchor = f"CLUSTER-{target.slug.upper()}"
            content = ROUTE_TEMPLATE.format(
                route_id=rid,
                source_cluster=source.slug,
                target_cluster=target.slug,
                route_type=route_type,
                source_anchor=source_anchor,
                target_anchor=target_anchor,
            )
            path = route_dir / f"ROUTE-{rid}-{source.slug}-to-{target.slug}.md"
            if not dry_run:
                path.write_text(content, encoding="utf-8")
            written += 1

    return {"domain_routes_written": written, "dry_run": dry_run}


def seed_hub_anchors(dry_run: bool = False) -> dict:
    """Anchor document per knowledge hub."""
    structure = _ensure_structure()
    registry = {e.slug: e for e in hub_registry()}
    written = 0

    for hub in KNOWLEDGE_HUBS:
        entry = registry.get(hub.slug)
        cluster = entry.cluster if entry else "architecture"
        tier = entry.tier if entry else "association"
        components = "\n".join(f"- {c}" for c in hub.components)
        doc_types = ", ".join(hub.doc_types)
        content = HUB_ANCHOR_TEMPLATE.format(
            hub_slug_upper=hub.slug.upper().replace("-", "_"),
            hub_title=hub.title,
            hub_slug=hub.slug,
            category=hub.category,
            cluster=cluster,
            tier=tier,
            components=components,
            doc_types=doc_types,
        )
        path = structure["hub_paths"][hub.slug] / f"HUB-ANCHOR-{hub.slug}.md"  # type: ignore
        if not dry_run:
            path.write_text(content, encoding="utf-8")
        written += 1

    return {"hub_anchors_written": written, "dry_run": dry_run}


def seed_processing_layers(dry_run: bool = False) -> dict:
    """One architecture blueprint per processing layer."""
    cfg = load_architecture()
    written = 0
    for i, layer in enumerate(processing_layers(cfg)):
        content = f"""---
id: LAYER-{i + 1}
title: "Processing Layer {layer.slug}"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [processing-layer, {layer.slug}, knowledge_architecture]
---

# Processing Layer: {layer.slug}

**Role:** {layer.role}

## Processing latency target
{layer.latency_ms}ms

## Path
`{layer.path}`

## Integration
Layer {layer.slug} feeds forward into the next processing layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during graph routing.
"""
        layer_path = CORPUS_ROOT / layer.path / f"LAYER-{layer.slug}.md"
        if not dry_run:
            layer_path.write_text(content, encoding="utf-8")
        written += 1
    return {"processing_layers_written": written, "dry_run": dry_run}


def seed_memory_samples(dry_run: bool = False) -> dict:
    """Seed sample documents in each memory tier."""
    written = 0
    samples = [
        ("working", "Active query context buffer", "working memory for current retrieval session"),
        ("episodic", "Incident timeline 2026-07-07", "episodic record of indexing pipeline degradation"),
        ("semantic", "GraphRAG edge type taxonomy", "stable semantic fact about relationship types"),
        ("procedural", "Index rebuild runbook", "procedural steps for full corpus reindex"),
    ]
    for tier_slug, title, body in samples:
        for tier in memory_tiers():
            if tier.slug != tier_slug:
                continue
            content = f"""---
id: MEMORY-{tier_slug.upper()}
title: "{title}"
doc_type: guide
category: memory
hub: coltex_knowledge_core
memory_tier: {tier_slug}
tags: [memory, {tier_slug}]
---

# {title}

{body}

## Memory tier: {tier_slug}
**Role:** {tier.role}
"""
            path = CORPUS_ROOT / tier.path / f"MEMORY-{tier_slug}-sample.md"
            if not dry_run:
                path.write_text(content, encoding="utf-8")
            written += 1
    return {"memory_samples_written": written, "dry_run": dry_run}


def build_architecture_manifest() -> dict:
    """Write architecture-manifest.json alongside catalog index."""
    cfg = load_architecture()
    arch = cfg.get("architecture", {})
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "codename": arch.get("codename", "knowledge_architecture"),
        "version": arch.get("version", "2.0"),
        "processing_layers": len(processing_layers(cfg)),
        "functional_clusters": len(functional_clusters(cfg)),
        "memory_tiers": len(memory_tiers(cfg)),
        "hubs": len(KNOWLEDGE_HUBS),
        "route_types": len(ROUTE_TYPES),
        "relationship_types": len(cfg.get("relationship_types", {}).get("core", []))
        + len(cfg.get("relationship_types", {}).get("advanced", [])),
        "scale_targets": cfg.get("scale", {}),
        "cluster_registry": [
            {"slug": c.slug, "domains": list(c.domains), "role": c.role}
            for c in functional_clusters(cfg)
        ],
    }
    ARCHITECTURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARCHITECTURE_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def build_catalog_index() -> dict:
    """Scan entire knowledge base and write catalog-index.json manifest."""
    kb_root = ROOT / "knowledge-base"
    domains: dict[str, int] = {}
    hubs: dict[str, int] = {}
    doc_types: dict[str, int] = {}
    total = 0
    graph_links = 0
    quick_reference = 0
    domain_routes = 0
    clusters: dict[str, int] = {}
    processing_layer_counts: dict[str, int] = {}
    memory_counts: dict[str, int] = {}

    region_markers = {
        "graph-links": "graph_links",
        "quick-reference": "quick_reference",
        "domain-routes": "domain_routes",
        "clusters": "clusters",
        "processing-layers": "processing_layers",
        "memory": "memory",
    }

    for path in kb_root.rglob("*.md"):
        if "_excluded" in path.parts or "_seed" in path.parts:
            continue
        total += 1
        parts = path.parts
        if "graph-links" in parts:
            graph_links += 1
        if "quick-reference" in parts:
            quick_reference += 1
        if "domain-routes" in parts:
            domain_routes += 1
        if "clusters" in parts:
            idx = parts.index("clusters")
            if idx + 1 < len(parts):
                clusters[parts[idx + 1]] = clusters.get(parts[idx + 1], 0) + 1
        for standalone in ("automation", "operations", "retention", "routing", "priority"):
            if standalone in parts:
                clusters[standalone] = clusters.get(standalone, 0) + 1
        if "processing-layers" in parts:
            idx = parts.index("processing-layers")
            if idx + 1 < len(parts):
                layer_dir = parts[idx + 1]
                if layer_dir.startswith("L") and "-" in layer_dir:
                    processing_layer_counts[layer_dir] = processing_layer_counts.get(layer_dir, 0) + 1
        if "memory" in parts:
            idx = list(parts).index("memory")
            if idx + 1 < len(parts):
                memory_counts[parts[idx + 1]] = memory_counts.get(parts[idx + 1], 0) + 1
        if "domains" in parts:
            idx = parts.index("domains")
            if idx + 1 < len(parts):
                cat = parts[idx + 1]
                domains[cat] = domains.get(cat, 0) + 1
        try:
            text = path.read_text(encoding="utf-8")[:2000]
            if "hub:" in text:
                for line in text.splitlines():
                    if line.strip().startswith("hub:"):
                        hub = line.split(":", 1)[1].strip().strip('"')
                        hubs[hub] = hubs.get(hub, 0) + 1
                        break
            if "doc_type:" in text:
                for line in text.splitlines():
                    if line.strip().startswith("doc_type:"):
                        dt = line.split(":", 1)[1].strip().strip('"')
                        doc_types[dt] = doc_types.get(dt, 0) + 1
                        break
        except OSError:
            pass

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "corpus": "coltex-knowledge_architecture",
        "architecture_version": "2.0",
        "codename": "knowledge_architecture",
        "total_documents": total,
        "domains": domains,
        "domain_count": len(domains),
        "hubs": hubs,
        "hub_count": len(hubs),
        "functional_clusters": clusters,
        "cluster_count": len(clusters),
        "processing_layers": processing_layer_counts,
        "memory_tiers": memory_counts,
        "doc_types": doc_types,
        "graph_links": graph_links,
        "domain_routes": domain_routes,
        "quick_reference": quick_reference,
        "categories_available": len(CATEGORIES),
        "topics_available": len(TOPICS),
        "hubs_registered": len(KNOWLEDGE_HUBS),
    }

    CATALOG_INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_INDEX_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    build_architecture_manifest()
    return manifest


def bootstrap_advanced(grow: int = 500, dry_run: bool = False) -> dict:
    """Knowledge Architecture v2 full bootstrap."""
    _ensure_structure()
    grow_stats = grow_domains(grow, dry_run=dry_run) if grow > 0 else {}
    return {
        "bootstrap": "knowledge_architecture-v2",
        "structure": True,
        "grow": grow_stats,
        "graph_links": wire_graph_links(dry_run=dry_run),
        "domain_routes": wire_domain_routes(dry_run=dry_run),
        "hub_anchors": seed_hub_anchors(dry_run=dry_run),
        "processing_layers": seed_processing_layers(dry_run=dry_run),
        "memory": seed_memory_samples(dry_run=dry_run),
        "quick_reference": seed_quick_reference(dry_run=dry_run),
        "catalog_index": {
            "total_documents": build_catalog_index().get("total_documents") if not dry_run else 0,
            "path": str(CATALOG_INDEX_PATH),
            "architecture_manifest": str(ARCHITECTURE_PATH),
        },
        "dry_run": dry_run,
    }


def bootstrap(grow: int = 300, dry_run: bool = False) -> dict:
    """Full knowledge corpus bootstrap: structure + grow + graph links + FAQs + catalog."""
    return bootstrap_advanced(grow=grow, dry_run=dry_run)


def main() -> None:
    parser = argparse.ArgumentParser(description="Coltex Knowledge Corpus orchestrator")
    sub = parser.add_subparsers(dest="command", required=True)

    p_boot = sub.add_parser("bootstrap", help="Scaffold + grow + wire + catalog index")
    p_boot.add_argument("--grow", type=int, default=300)
    p_boot.add_argument("--dry-run", action="store_true")

    p_grow = sub.add_parser("grow", help="Grow domain documents")
    p_grow.add_argument("--count", type=int, default=200)
    p_grow.add_argument("--dry-run", action="store_true")

    sub.add_parser("structure", help="Create folder tree only")
    sub.add_parser("graph-links", help="Wire hub graph links")
    sub.add_parser("quick-reference", help="Seed FAQ quick reference")
    sub.add_parser("map", help="Rebuild catalog-index.json")

    sub.add_parser("domain-routes", help="Wire inter-cluster domain routes")
    sub.add_parser("hubs", help="Seed hub anchor documents")
    sub.add_parser("layers", help="Seed processing layer blueprints")
    sub.add_parser("memory", help="Seed memory tier samples")

    p_adv = sub.add_parser("advanced", help="Full Knowledge Architecture v2 bootstrap")
    p_adv.add_argument("--grow", type=int, default=500)
    p_adv.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()

    if args.command == "bootstrap":
        result = bootstrap(grow=args.grow, dry_run=args.dry_run)
    elif args.command == "advanced":
        result = bootstrap_advanced(grow=args.grow, dry_run=args.dry_run)
    elif args.command == "grow":
        _ensure_structure()
        result = grow_domains(args.count, dry_run=args.dry_run)
        if not args.dry_run:
            result["catalog_index"] = build_catalog_index()
    elif args.command == "structure":
        result = {"structure": str(_ensure_structure()["root"])}
    elif args.command == "graph-links":
        result = wire_graph_links()
        result["catalog_index"] = build_catalog_index()
    elif args.command == "quick-reference":
        result = seed_quick_reference()
        result["catalog_index"] = build_catalog_index()
    elif args.command == "map":
        result = build_catalog_index()
    elif args.command == "domain-routes":
        result = wire_domain_routes()
        result["catalog_index"] = build_catalog_index()
    elif args.command == "hubs":
        result = seed_hub_anchors()
        result["catalog_index"] = build_catalog_index()
    elif args.command == "layers":
        result = seed_processing_layers()
        result["catalog_index"] = build_catalog_index()
    elif args.command == "memory":
        result = seed_memory_samples()
        result["catalog_index"] = build_catalog_index()
    else:
        result = {"error": "unknown command"}

    print(yaml.safe_dump(result, sort_keys=False))


if __name__ == "__main__":
    main()
