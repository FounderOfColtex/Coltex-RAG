# Coltex Distributable Dataset Package

Audit samples and documentation for the Coltex knowledge base build.

## Contents

| Path | Description |
|------|-------------|
| `_samples/` | Audit sample markdown (first N from hyper stream) |
| `DATASET.md` | This file |
| `README.md` | Generation commands |

## Quick load (Python)

```python
import json

with open("data/product/chunks/chunks.jsonl") as f:
    chunks = [json.loads(line) for line in f]

with open("data/product/embeddings/embeddings.jsonl") as f:
    vectors = [json.loads(line) for line in f]

with open("data/product/graph/edges.jsonl") as f:
    edges = [json.loads(line) for line in f]

print(f"{len(chunks)} chunks, {len(vectors)} vectors, {len(edges)} edges")
```

## Build from source

```bash
pip install -r requirements.txt
make product
make product-hyper-smoke
make audit-distribution
```

## Compliance

- **License:** MIT — see [LICENSE](../../LICENSE)
- **Provenance:** `knowledge-base/PROVENANCE.md`
- **Audit:** `benchmarks/distribution_audit.json` (after build)
