# Distributable Corpus

Streaming-generated original synthetic documents for large-scale knowledge base builds.

| Path | Purpose |
|------|---------|
| `_samples/` | Audit sample markdown files |
| `DATASET.md` | Load instructions |
| `data/product/catalog.jsonl` | Document catalog metadata |
| `data/product/chunks/chunks.jsonl` | Vector-ready chunks |

## Generation

```bash
make corpus-mega
make product

# Hyper smoke validation (25,000 documents)
make product-hyper-smoke

# Full hyper tier (uncapped — run on cluster)
make product-hyper
```

All content is **original synthetic** · **MIT License** · passes distribution audit.

See [LICENSE](../../LICENSE).
