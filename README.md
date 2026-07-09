# Coltex

**The largest commercial RAG corpus — 100,000,000+ sellable knowledge files.**

Coltex Mega RAG is an advanced, GraphRAG-native knowledge product: a streaming-generated,
embedding-ready corpus designed to power production retrieval systems and to be sold as
domain packs, industry shards, and the full **Mega (100M+)** SKU.

---

## What you get

| Deliverable | Description |
|-------------|-------------|
| **100M+ documents** | Commercial Mega floor — original synthetic knowledge files |
| **Vector chunks** | Metadata-rich JSONL for any vector store |
| **Knowledge graph** | Typed edges for GraphRAG routing |
| **Marketplace packs** | Sellable domain packs (RAG, languages, cloud, security, architecture) |
| **Benchmarks** | FAQ, retrieval gold, RAG eval sets |
| **Audit trail** | Provenance, EULA, distribution compliance |

Commercial packaging: [docs/commercial/product-overview.md](docs/commercial/product-overview.md) · [SKU matrix](docs/commercial/sku-matrix.md)

---

## Quick start

```bash
git clone https://github.com/FounderOfColtex/Coltex-Knowledge-Platform.git
cd Coltex-Knowledge-Platform
python -m venv .venv
source .venv/bin/activate
pip install -e .

# Validate the Mega commercial pipeline (capped smoke build)
make product-mega-smoke

# Inspect artifacts
python3 examples/load_dataset.py
make audit-distribution
```

Full Mega build (cluster / Vast.ai — uncapped 100M+):

```bash
make product-mega
```

---

## Commercial SKUs

| SKU | Scale | Price |
|-----|-------|-------|
| Personal | ~25k sample | $79 |
| Professional | 1M–10M domain packs | $999 |
| Enterprise | 10M–50M multi-domain | Custom |
| **Mega** | **100,000,000+** | Custom |

Licenses: [EULA.md](EULA.md) · [MEGA-LICENSE.md](MEGA-LICENSE.md) · [PERSONAL-LICENSE.md](PERSONAL-LICENSE.md) · [PROFESSIONAL-LICENSE.md](PROFESSIONAL-LICENSE.md) · [ENTERPRISE-LICENSE.md](ENTERPRISE-LICENSE.md)

Engine source remains **MIT** ([LICENSE](LICENSE)).

---

## Marketplace packs

Sell individually or bundle into SKUs — see [config/marketplace.yaml](config/marketplace.yaml):

- `pack-rag-core` — RAG / GraphRAG / embeddings / retrieval
- `pack-languages` — Python, JS/TS, Go, Rust, Java, C#, SQL
- `pack-cloud-devops` — AWS, Azure, GCP, K8s, Terraform, CI/CD
- `pack-security-sre` — Security, observability, incidents
- `pack-architecture` — Microservices, DDD, APIs, data stores

```bash
make marketplace-packs
```

---

## Self-hosted Knowledge Studio (included)

```bash
coltex serve                  # LAN default — http://<server-ip>:8080
coltex deploy                 # show access URLs
```

| Profile | Bind | Port |
|---------|------|------|
| `lan` | 0.0.0.0 | 8080 |
| `production` | 0.0.0.0 | 443 |

Docker: `docker compose up -d` — guide: [docs/deployment/self-hosted.md](docs/deployment/self-hosted.md)

---

## Why Coltex Mega RAG is advanced

1. **Hyper-scale streaming** — never loads 100M files into memory
2. **GraphRAG-native** — hubs + typed relationships on every document
3. **Hybrid retrieval ready** — dense vectors + metadata filters
4. **Quality gates** — substance checks, duplicate caps, commercial audit
5. **Sellable by design** — SKUs, packs, catalog, and EULA from day one
6. **Evaluation harness** — recall@k and metadata accuracy benchmarks

---

## Docs

| Doc | Purpose |
|-----|---------|
| [Commercial overview](docs/commercial/product-overview.md) | Buyer-facing product |
| [Datasheet](docs/commercial/datasheet.md) | Spec sheet |
| [SKU matrix](docs/commercial/sku-matrix.md) | Pricing & packs |
| [Platform overview](docs/platform/overview.md) | Runtime & intelligence |
| [Product setup](docs/product-setup.md) | Build & query |

---

## License

- **Engine / runtime:** MIT — [LICENSE](LICENSE)
- **Commercial Mega RAG dataset:** [EULA.md](EULA.md)
