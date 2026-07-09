# Coltex Mega RAG — SKU Matrix

Commercial packaging for the Coltex Mega RAG corpus (100,000,000+ data files).

| SKU | Documents | Price (USD) | License | Includes |
|-----|-----------|-------------|---------|----------|
| **Personal** | Sample pack (~25k) | $79 | Personal + EULA | Smoke corpus, benchmarks sample, MIT engine |
| **Professional** | Domain packs (1M–10M) | $999 | Professional + EULA | Selected domain shards, graph, embeddings export |
| **Enterprise** | Multi-domain (10M–50M) | Custom quote | Enterprise + EULA | Multi-team seats, private delivery, support SLA |
| **Mega** | **100,000,000+** | Custom quote | Mega + EULA | Full streaming corpus, all shards, catalog, GraphRAG edges |

---

## Add-on marketplace packs

Sold individually or bundled under Professional / Enterprise / Mega:

| Pack ID | Focus | Typical file count |
|---------|-------|--------------------|
| `pack-rag-core` | RAG, GraphRAG, embeddings, retrieval | Millions |
| `pack-languages` | Python, JS/TS, Go, Rust, Java, C#, SQL | Millions |
| `pack-cloud-devops` | AWS, Azure, GCP, K8s, Terraform, CI/CD | Millions |
| `pack-security-sre` | Security, observability, incidents, performance | Millions |
| `pack-architecture` | Microservices, DDD, API design, event-driven | Millions |

See `config/marketplace.yaml` for registry categories and publishing rules.

---

## Delivery formats

| Format | Path / artifact |
|--------|-----------------|
| Chunks JSONL | `data/product/chunks/chunks.jsonl` |
| Catalog JSONL | `data/product/catalog.jsonl` |
| Graph edges | `data/product/graph/edges.jsonl` |
| Embeddings | `data/product/embeddings/` |
| Manifest | `data/product/manifest.json` |
| Generation stats | `data/product/generation_stats.json` |
| Audit samples | `knowledge-base/distributable/_samples/` |

---

## Build targets

```bash
make product-mega-smoke   # capped commercial validation build
make product-mega         # full 100M+ Mega SKU build (cluster)
make product-hyper        # legacy hyper alias → Mega config
```
