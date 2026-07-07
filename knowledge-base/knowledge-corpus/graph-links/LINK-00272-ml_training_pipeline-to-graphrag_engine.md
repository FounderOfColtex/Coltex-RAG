---
id: LINK-00272
title: "Graph Link: ml_training_pipeline ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ml_training_pipeline, graphrag_engine]
related: [HUB-ML_TRAINING_PIPELINE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Graph Link: ml_training_pipeline → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `ml_training_pipeline` is related to `graphrag_engine`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
