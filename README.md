# Coltex

**Enterprise RAG Knowledge Corpus** — the largest connected retrieval-augmented generation dataset with multi-layer architecture, graph-linked domains, knowledge clusters, and procedural expansion to unlimited scale.

Coltex delivers a production-grade knowledge layer: 62+ domain folders, thousands of typed documents, cross-reference graph links, and a distributable export pipeline for commercial datasets.

---

## Knowledge Architecture

```
                    ┌─── L6 Meta (Catalog & governance) ───┐
                    │   L5 Executive (Context assembly)      │
                    │   L4 Reasoning (GraphRAG)             │
                    │   L3 Integration (Cluster assignment)  │
                    │   L2 Association (Metadata)           │
                    │   L1 Ingestion (Document intake)      │
                    └─────────────────┬─────────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              ▼                       ▼                       ▼
         62+ Domains            18 Knowledge Hubs       4 Memory Tiers
              │                       │                       │
              └──────────► Graph Links + Pathways ◄──────────┘
                                   │
                    Vector + Metadata + GraphRouter
                                   │
                        brain retrieve / report
```

---

## Dataset Deliverables

Each product build exports a versioned, checksum-signed artifact set:

| Artifact | Path | Description |
|----------|------|-------------|
| Chunks | `data/product/chunks/chunks.jsonl` | Vector-ready text segments with metadata |
| Catalog | `data/product/catalog.jsonl` | Per-document index and provenance |
| Embeddings | `data/product/embeddings/embeddings.jsonl` | Pre-computed sentence-transformer vectors |
| Graph | `data/product/graph/edges.jsonl` | Typed relationship edges (`depends_on`, `see_also`, …) |
| Metadata | `data/product/metadata/documents.json` | Document-level schema index |
| Benchmarks | `benchmarks/*.jsonl` | FAQ pairs, retrieval gold, and RAG evaluation sets |
| Manifest | `data/product/manifest.json` | SHA-256 checksums, version, and build metadata |

All distributable content is original synthetic material. Purchasers receive a perpetual commercial use license — see `EULA` and `knowledge-base/LICENSE`.

---

## Quick Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

make corpus-advanced
make index
python3 -m brain retrieve "What is GraphRAG?" --context
python3 -m brain report
```

---

## Expand the Corpus

| Command | Output |
|---------|--------|
| `make corpus-advanced` | Full architecture bootstrap (500 docs + pathways + hubs) |
| `make corpus-grow COUNT=1000` | Add 1,000 domain documents |
| `make corpus-mega` | 10,000 documents |
| `make generate-mega` | 100,000 procedural documents |
| `make generate-ultra` | 1,000,000 documents |

Catalog index: `data/brain/neural-map.json` · Architecture manifest: `data/brain/architecture-manifest.json`

---

## Retrieval Engine

Hybrid RAG pipeline with optional **GraphRouter** (region-aware graph expansion):

```bash
python3 -m brain index --reindex
python3 -m brain retrieve "<query>" --context
python3 -m brain stats
python3 -m brain report
```

---

## Premium Dataset Export

```bash
make product-premium-smoke   # 25,000 documents
make product-premium         # Full pipeline
make evaluate                # Benchmark evidence
```

---

## Documentation

- [Knowledge architecture](docs/architecture/knowledge-architecture.md)
- [Product setup](docs/product-setup.md)
- [Quality standards](docs/product-quality.md)
- [Evaluation guide](docs/product-evaluation.md)

---

## License

Licensed under the [End User License Agreement](EULA). Third-party dependencies in [NOTICE](NOTICE).
