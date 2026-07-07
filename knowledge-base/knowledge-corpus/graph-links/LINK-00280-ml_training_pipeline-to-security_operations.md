---
id: LINK-00280
title: "Graph Link: ml_training_pipeline ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ml_training_pipeline, security_operations]
related: [HUB-ML_TRAINING_PIPELINE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Graph Link: ml_training_pipeline → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `ml_training_pipeline` is related to `security_operations`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
