---
id: LINK-00159
title: "Graph Link: observability_stack ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, ml_training_pipeline]
related: [HUB-OBSERVABILITY_STACK, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → ml_training_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `observability_stack` documents `ml_training_pipeline`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
