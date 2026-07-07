---
id: LINK-00051
title: "Graph Link: graphrag_engine ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, ml_training_pipeline]
related: [HUB-GRAPHRAG_ENGINE, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → ml_training_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `graphrag_engine` is related to `ml_training_pipeline`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
