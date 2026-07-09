# Coltex Mega RAG — Datasheet

| Field | Value |
|-------|-------|
| **Product name** | Coltex Mega RAG |
| **Version** | 5.0.0 |
| **Positioning** | Largest commercial RAG knowledge corpus |
| **Scale target** | **100,000,000+ documents** |
| **Domains / categories** | 50+ (RAG, languages, cloud, security, architecture, …) |
| **Document types** | 20 premium types (guides, runbooks, ADRs, FAQs, benchmarks, …) |
| **Generation** | Streaming procedural synthetic (no scraped third-party docs) |
| **Graph** | Typed relationship edges for GraphRAG |
| **Embeddings model (default)** | `sentence-transformers/all-MiniLM-L6-v2` |
| **Chunking** | ~2000 chars, 200 overlap, split on `## ` |
| **Quality gates** | Substantive content, duplicate ratio ≤5%, provenance + license audit |
| **License (engine)** | MIT |
| **License (commercial dataset)** | [EULA.md](../../EULA.md) |
| **Provenance** | [knowledge-base/PROVENANCE.md](../../knowledge-base/PROVENANCE.md) |

---

## Architecture (buyer view)

```
Topics × Doc types × Variants × Mega shards
              │
              ▼
     Streaming generator (memory-safe)
              │
    ┌─────────┼─────────┐
    ▼         ▼         ▼
 Catalog   Chunks    Graph edges
    │         │         │
    └────► Embeddings + Manifest + Benchmarks
                    │
                    ▼
         Sellable SKUs / Marketplace packs
```

---

## Performance notes

- Full Mega builds are designed for multi-worker cluster runs (e.g. Vast.ai).
- Local validation uses `product_mega_smoke.yaml` with a file cap.
- Estimates are computed via `scripts/mega_scale.py` and `premium_generator.estimate_premium_documents`.

---

## Compliance checklist

- [x] Original synthetic content (no scraped docs)
- [x] Root `EULA.md` for commercial Dataset SKUs
- [x] `PROVENANCE.md` and `NOTICE`
- [x] `make audit-distribution` before release
