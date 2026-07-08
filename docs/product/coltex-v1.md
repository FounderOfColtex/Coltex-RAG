# Coltex V1

**Tagline:** The AI Knowledge Platform for Modern Organizations

**Goal:** Turn scattered business knowledge into AI-ready intelligence in under 10 minutes.

Coltex V1 is a **local CLI tool**. No website. No cloud service.

---

## CLI Commands

| Command | Purpose |
|---------|---------|
| `status` | Runtime and engine status |
| `dashboard` | Documents, sources, searches, AI queries, last sync, health |
| `knowledge` | Browse knowledge objects |
| `sources` | List uploaded sources |
| `upload <path>` | Upload and process a file |
| `search "<query>"` | Universal search |
| `ask "<question>"` | Ask Knowledge — sources, confidence, why |
| `health` | Knowledge Health metrics |
| `settings` | Workspace, embedding model, chunk size |
| `curator` | Proactive knowledge alerts |
| `monitor` | Runtime metrics |
| `explain "<query>"` | Retrieval explainability |

```bash
python3 -m runtime status
python3 -m runtime upload path/to/document.pdf
python3 -m runtime ask "What is our refund policy?"
python3 -m runtime search "authentication"
python3 -m runtime dashboard
```

---

## Knowledge Sources

### Supported (V1)

| Format | Extension |
|--------|-----------|
| PDF | `.pdf` |
| Word | `.docx` |
| Markdown | `.md` |
| Text | `.txt` |
| HTML | `.html` |
| JSON | `.json` |

```bash
python3 -m runtime upload path/to/document.pdf
python3 -m runtime sources
```

### Planned connectors

GitHub · Notion · Google Drive

```bash
python3 -m runtime connector filesystem
```

---

## AI Processing (automatic)

```
Upload → Parse → Clean → Chunk → Metadata → Embeddings → Index → Done
```

Triggered on every upload. Technical steps stay hidden unless you inspect pipeline output.

---

## Universal Search

One command searches documents, metadata, code references, APIs, and SQL patterns:

```bash
python3 -m runtime search "JWT authentication"
```

---

## Ask Knowledge

Not "Ask AI" — **Ask Knowledge**.

```
Question → Retrieve → Build Context → Answer → Sources + Confidence + Why
```

```bash
python3 -m runtime ask "How do we handle password resets?"
```

---

## Knowledge Health

```bash
python3 -m runtime health
python3 -m runtime dashboard
```

Shows honest metrics: knowledge score, document count, embeddings, duplicates, outdated content.

---

## Settings

```bash
python3 -m runtime settings
```

Workspace name, AI provider, embedding model, chunk size — stored locally in `data/runtime/settings.json`.

---

## V1 Architecture

```
Knowledge Sources → Processing → Knowledge Store → Search → Ask Knowledge → Analytics
```

Config: `config/v1.yaml`

---

## License

MIT — see [LICENSE](../../LICENSE).
