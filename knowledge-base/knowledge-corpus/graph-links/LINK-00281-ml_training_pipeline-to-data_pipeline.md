---
id: LINK-00281
title: "Graph Link: ml_training_pipeline ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ml_training_pipeline, data_pipeline]
related: [HUB-ML_TRAINING_PIPELINE, HUB-DATA_PIPELINE]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-DATA_PIPELINE]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Graph Link: ml_training_pipeline → data_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `ml_training_pipeline` calls into `data_pipeline`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
