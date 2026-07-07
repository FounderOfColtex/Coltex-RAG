---
id: LINK-00286
title: "Graph Link: ml_training_pipeline ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ml_training_pipeline, api_gateway]
related: [HUB-ML_TRAINING_PIPELINE, HUB-API_GATEWAY]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-API_GATEWAY]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Graph Link: ml_training_pipeline → api_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `ml_training_pipeline` documents `api_gateway`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
