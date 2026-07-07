---
id: LINK-00273
title: "Graph Link: ml_training_pipeline ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ml_training_pipeline, payment_service]
related: [HUB-ML_TRAINING_PIPELINE, HUB-PAYMENT_SERVICE]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-PAYMENT_SERVICE]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Graph Link: ml_training_pipeline → payment_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `ml_training_pipeline` calls into `payment_service`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
