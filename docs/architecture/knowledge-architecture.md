# Coltex Knowledge Architecture — Reference

Enterprise multi-layer RAG knowledge corpus with graph-linked domains, knowledge clusters, and advanced GraphRAG routing.

## System overview

```mermaid
flowchart TB
    subgraph layers [Processing Layers L1-L6]
        L1[L1 Ingestion]
        L2[L2 Metadata]
        L3[L3 Integration]
        L4[L4 Graph]
        L5[L5 Assembly]
        L6[L6 Governance]
        L1 --> L2 --> L3 --> L4 --> L5 --> L6
    end

    subgraph clusters [Functional Clusters]
        F[Architecture]
        T[Retrieval]
        P[Data]
        O[Observability]
        L[Security]
    end

    subgraph graph [Graph Layer]
        Domains[62+ Domains]
        Hubs[18 Knowledge Hubs]
        Links[Graph Links]
        Routes[Domain Routes]
    end

    layers --> clusters
    clusters --> graph
    graph --> Retrieve[Hybrid Retrieval]
```

## Directory layout

```
knowledge-corpus/
├── processing-layers/L1-ingestion … L6-governance
├── clusters/                        # Functional domain groupings
├── domains/                         # Technology categories
├── hubs/                            # Knowledge clusters
├── graph-links/                     # Hub-to-hub graph links
├── domain-routes/                   # Inter-cluster routes
├── memory/working|episodic|…        # Retention tiers
└── quick-reference/                 # FAQ index
```

## Knowledge hubs (18)

`auth_service`, `indexing_pipeline`, `graphrag_engine`, `vector_store_cluster`, `embedding_service`, `agent_orchestrator`, `observability_stack`, `rag_retrieval_core`, `security_operations`, `data_pipeline`, `llm_inference_gateway`, `knowledge_graph_store`, `incident_command`, `ml_training_pipeline`, `api_gateway`, `payment_service`, `ci_cd_platform`, `coltex_knowledge_core`

## Graph edge types (20)

Core: `related`, `depends_on`, `uses`, `implements`, `calls`, `see_also`

Advanced: `extends`, `validates`, `synthesizes`, `triggers`, `derived_from`, `tested_by`, `deployed_via`, and more.

## GraphRouter

Region-aware graph expansion in `brain/graph/graph_router.py`:

- Graph links and domain routes receive retrieval score boosts
- 4-hop traversal, 16 max expanded documents
- Enabled via `config/brain.yaml` → `graph.advanced_routing: true`

## Manifests

| File | Purpose |
|------|---------|
| `data/brain/catalog-index.json` | Catalog index with per-region counts |
| `data/brain/architecture-manifest.json` | Architecture registry |
| `config/brain_architecture.yaml` | Master architecture specification |

## Commands

```bash
make corpus-advanced
make index
python3 -m brain report
python3 -m brain retrieve "your query" --context
```
