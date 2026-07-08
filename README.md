# Coltex

**The AI Knowledge Platform for Modern Organizations**

Turn scattered business knowledge into AI-ready intelligence in under 10 minutes — from your terminal.

```bash
pip install -r requirements.txt
python3 -m runtime status
```

Coltex V1 is a **CLI tool**. No web UI. No cloud. Run it locally on your machine.

---

## Commands

| Command | Purpose |
|---------|---------|
| `python3 -m runtime status` | Runtime and engine status |
| `python3 -m runtime dashboard` | Documents, sources, searches, health |
| `python3 -m runtime upload file.pdf` | Upload and process a source |
| `python3 -m runtime sources` | List uploaded sources |
| `python3 -m runtime knowledge` | Browse knowledge objects |
| `python3 -m runtime search "query"` | Universal search |
| `python3 -m runtime ask "question"` | Ask Knowledge — answer with sources |
| `python3 -m runtime health` | Knowledge Health score |
| `python3 -m runtime settings` | View workspace settings |
| `python3 -m runtime curator` | Proactive knowledge alerts |
| `python3 -m runtime monitor` | Runtime metrics |
| `python3 -m runtime explain "query"` | Why a result was retrieved |

Supported uploads: **PDF · DOCX · Markdown · TXT · HTML · JSON**

---

## AI Processing (automatic)

```
Upload → Parse → Clean → Chunk → Metadata → Embeddings → Index → Done
```

Every upload runs the full pipeline automatically.

---

## Architecture

```
Knowledge Sources → Processing → Knowledge Store → Search → Ask Knowledge → Analytics
```

Full spec: [docs/product/coltex-v1.md](docs/product/coltex-v1.md)

---

## Build knowledge base (optional)

```bash
make product
make index
make runtime-health
```

---

## Documentation

| Doc | Description |
|-----|-------------|
| [Coltex V1](docs/product/coltex-v1.md) | CLI product spec |
| [Runtime](docs/platform/runtime.md) | Runtime architecture |

---

## License

MIT — see [LICENSE](LICENSE).
