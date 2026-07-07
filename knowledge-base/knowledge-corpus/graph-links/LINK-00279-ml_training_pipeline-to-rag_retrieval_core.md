---
id: LINK-00279
title: "Graph Link: ml_training_pipeline ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ml_training_pipeline, rag_retrieval_core]
related: [HUB-ML_TRAINING_PIPELINE, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Graph Link: ml_training_pipeline → rag_retrieval_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `ml_training_pipeline` depends on `rag_retrieval_core`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
