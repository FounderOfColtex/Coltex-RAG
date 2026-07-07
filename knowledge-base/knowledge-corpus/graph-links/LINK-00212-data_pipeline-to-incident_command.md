---
id: LINK-00212
title: "Graph Link: data_pipeline ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, data_pipeline, incident_command]
related: [HUB-DATA_PIPELINE, HUB-INCIDENT_COMMAND]
see_also: [HUB-DATA_PIPELINE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-DATA_PIPELINE]
---

# Graph Link: data_pipeline → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `data_pipeline` is related to `incident_command`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
