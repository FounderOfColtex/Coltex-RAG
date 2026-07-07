---
id: LINK-00267
title: "Graph Link: incident_command ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, ml_training_pipeline]
related: [HUB-INCIDENT_COMMAND, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-INCIDENT_COMMAND, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → ml_training_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `incident_command` is related to `ml_training_pipeline`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
