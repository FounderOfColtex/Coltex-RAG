# Coltex — Setup Guide

Build, expand, and query the Coltex knowledge base.

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Bootstrap the corpus

```bash
make corpus-advanced
make corpus-mega
make expand-curated-kb COUNT=500
make corpus-report
```

## Build knowledge base

```bash
make product
make index
make audit-distribution
python3 examples/load_dataset.py
```

## Use the CLI

```bash
python3 -m runtime status
python3 -m runtime upload path/to/document.pdf
python3 -m runtime ask "your question"
python3 -m runtime search "query"
python3 -m runtime dashboard
```

## License

MIT — see [LICENSE](../LICENSE).
