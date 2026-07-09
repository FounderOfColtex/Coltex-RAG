# Coltex Mega RAG — Product Overview

**Commercial RAG corpus — 100,000,000+ documents for production retrieval.**

Coltex Mega RAG is a GraphRAG-ready knowledge corpus: streaming-generated,
embedding-ready, and packaged for commercial distribution as industry packs,
shards, and the full Mega SKU.

---

## Package contents

| Deliverable | Description |
|-------------|-------------|
| **Document corpus** | 100,000,000+ original synthetic knowledge documents across 50+ domains |
| **Vector chunks** | Chunked, metadata-rich JSONL for embedding stores |
| **Knowledge graph** | Typed edges (see_also, depends_on, routes_to) for GraphRAG |
| **Catalog** | Machine-readable inventory for pack and shard distribution |
| **Benchmarks** | FAQ pairs, retrieval gold sets, RAG evaluation sets |
| **Provenance and audit** | Distribution compliance artifacts for enterprise buyers |

---

## Technical capabilities

1. **Streaming generation** — procedural generation without loading the full corpus into memory
2. **GraphRAG-native** — hub routing and relationship edges with every document
3. **Hybrid retrieval** — metadata fields (doc_type, category, hub, tags) for dense and sparse search
4. **Quality gates** — substantive-content checks, duplicate caps, license and provenance audit
5. **Commercial packs** — marketplace packs by domain, industry, and document type
6. **Evaluation harness** — recall@k and metadata accuracy benchmarks included

---

## Buyers

| Segment | Use case |
|---------|----------|
| AI / ML teams | Production RAG bootstrap with a large, structured corpus |
| Platform vendors | Licensed shards in vertical AI products |
| Enterprises | Private RAG over engineering, cloud, security, and operations knowledge |
| Data marketplaces | Licensed industry packs under Coltex EULA terms |
| Researchers | Large-scale retrieval and GraphRAG evaluation |

---

## Build and inspect

```bash
# Capped validation build
make product-mega-smoke

# Full Mega commercial target (cluster)
make product-mega

# Inspect artifacts
python3 examples/load_dataset.py
make audit-distribution
```

---

## Related docs

- [SKU matrix](sku-matrix.md)
- [Datasheet](datasheet.md)
- [EULA](../../EULA.md)
- [Marketplace](../../config/marketplace.yaml)
