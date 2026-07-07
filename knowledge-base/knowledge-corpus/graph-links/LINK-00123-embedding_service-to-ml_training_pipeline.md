---
id: LINK-00123
title: "Graph Link: embedding_service ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, embedding_service, ml_training_pipeline]
related: [HUB-EMBEDDING_SERVICE, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-EMBEDDING_SERVICE, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Graph Link: embedding_service → ml_training_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `embedding_service` is related to `ml_training_pipeline`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
