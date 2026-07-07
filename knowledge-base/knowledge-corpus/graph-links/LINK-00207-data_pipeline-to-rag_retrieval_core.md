---
id: LINK-00207
title: "Graph Link: data_pipeline ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, data_pipeline, rag_retrieval_core]
related: [HUB-DATA_PIPELINE, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-DATA_PIPELINE, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-DATA_PIPELINE]
---

# Graph Link: data_pipeline → rag_retrieval_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `data_pipeline` depends on `rag_retrieval_core`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
