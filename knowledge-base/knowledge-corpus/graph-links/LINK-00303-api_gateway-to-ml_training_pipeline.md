---
id: LINK-00303
title: "Graph Link: api_gateway ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, api_gateway, ml_training_pipeline]
related: [HUB-API_GATEWAY, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-API_GATEWAY, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-API_GATEWAY]
---

# Graph Link: api_gateway → ml_training_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `api_gateway` documents `ml_training_pipeline`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
