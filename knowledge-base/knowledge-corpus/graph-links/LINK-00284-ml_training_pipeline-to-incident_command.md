---
id: LINK-00284
title: "Graph Link: ml_training_pipeline ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ml_training_pipeline, incident_command]
related: [HUB-ML_TRAINING_PIPELINE, HUB-INCIDENT_COMMAND]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Graph Link: ml_training_pipeline → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `ml_training_pipeline` is related to `incident_command`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
