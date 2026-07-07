# Coltex Knowledge Architecture

Enterprise RAG knowledge corpus with **6 processing layers**, **10 functional clusters**, **4 memory tiers**, **18 knowledge hubs**, and **millions of graph edges**.

## Structure
```
knowledge-corpus/
├── processing-layers/L1-ingestion … L6-governance
├── clusters/                        # Functional domain groupings
├── domains/                         # 62+ technology domains
├── hubs/                            # 18 knowledge clusters
├── graph-links/                     # Hub-to-hub graph links
├── domain-routes/                   # Inter-cluster routes
├── memory/                          # Tiered retention stores
└── quick-reference/                 # FAQ index
```

## Build
```bash
make corpus-advanced              # Full architecture bootstrap
make corpus-grow COUNT=1000       # Add domain documents
make corpus-mega                  # 10,000 documents
```

## Query
```bash
make index
python3 -m brain report
python3 -m brain retrieve "Explain domain route routing" --context
```
