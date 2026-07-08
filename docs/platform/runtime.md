# Coltex Runtime

Local CLI for the Coltex knowledge platform.

## Start here

```bash
python3 -m runtime status
python3 -m runtime dashboard
```

## Commands

| Command | Capability |
|---------|------------|
| `python3 -m runtime status` | Runtime and engine status |
| `python3 -m runtime dashboard` | Documents, sources, searches, health |
| `python3 -m runtime upload file.pdf` | Upload and process a source |
| `python3 -m runtime sources` | List uploaded sources |
| `python3 -m runtime knowledge` | Browse knowledge objects |
| `python3 -m runtime search "..."` | Universal search |
| `python3 -m runtime ask "..."` | Ask Knowledge |
| `python3 -m runtime health` | Knowledge Health scores |
| `python3 -m runtime settings` | Workspace settings |
| `python3 -m runtime curator` | Proactive knowledge alerts |
| `python3 -m runtime monitor` | Runtime monitoring |
| `python3 -m runtime explain "..."` | Retrieval explainability |
| `python3 -m runtime connector filesystem` | Filesystem connector sync |
| `python3 -m runtime ingest DOC` | Event pipeline |

---

## Runtime architecture

```
Coltex Runtime (CLI)
├── Intelligence Engine    — relationship discovery, quality analysis
├── Search Engine          — hybrid knowledge object search
├── Memory Engine          — working → archive memory tiers
├── Scheduler              — automated maintenance jobs
├── Event Bus              — event-driven pipeline
├── Plugin Manager         — extensibility registry
├── Processing Pipeline    — upload → parse → chunk → index
├── Ask Knowledge          — retrieve + answer with sources
├── Retrieval Engine       — intent-ready retrieval wrapper
├── Graph Engine           — topology and neighbors
├── AI Curator             — merge, staleness, regen recommendations
├── Analytics Engine       — knowledge quality metrics
└── Security               — access and audit gateway
```

Config: [config/runtime.yaml](../../config/runtime.yaml)

---

## License

MIT — see [LICENSE](../../LICENSE).
