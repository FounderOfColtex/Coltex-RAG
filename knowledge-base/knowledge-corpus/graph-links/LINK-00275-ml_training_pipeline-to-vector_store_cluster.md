---
id: LINK-00275
title: "Graph Link: ml_training_pipeline ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ml_training_pipeline, vector_store_cluster]
related: [HUB-ML_TRAINING_PIPELINE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Graph Link: ml_training_pipeline → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `ml_training_pipeline` depends on `vector_store_cluster`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
