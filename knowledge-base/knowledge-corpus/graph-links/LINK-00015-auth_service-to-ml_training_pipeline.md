---
id: LINK-00015
title: "Graph Link: auth_service ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, auth_service, ml_training_pipeline]
related: [HUB-AUTH_SERVICE, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-AUTH_SERVICE, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-AUTH_SERVICE]
---

# Graph Link: auth_service → ml_training_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `auth_service` documents `ml_training_pipeline`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
