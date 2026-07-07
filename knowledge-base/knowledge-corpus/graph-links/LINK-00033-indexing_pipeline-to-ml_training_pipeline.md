---
id: LINK-00033
title: "Graph Link: indexing_pipeline ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, ml_training_pipeline]
related: [HUB-INDEXING_PIPELINE, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-INDEXING_PIPELINE, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → ml_training_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `indexing_pipeline` depends on `ml_training_pipeline`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
