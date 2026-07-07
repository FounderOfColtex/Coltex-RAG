---
id: LINK-00276
title: "Graph Link: ml_training_pipeline ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ml_training_pipeline, embedding_service]
related: [HUB-ML_TRAINING_PIPELINE, HUB-EMBEDDING_SERVICE]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Graph Link: ml_training_pipeline → embedding_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `ml_training_pipeline` is related to `embedding_service`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
