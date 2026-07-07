---
id: LINK-00283
title: "Graph Link: ml_training_pipeline ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ml_training_pipeline, knowledge_graph_store]
related: [HUB-ML_TRAINING_PIPELINE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Graph Link: ml_training_pipeline → knowledge_graph_store

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `ml_training_pipeline` depends on `knowledge_graph_store`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
