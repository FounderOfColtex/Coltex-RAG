---
id: LINK-00263
title: "Graph Link: incident_command ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, data_pipeline]
related: [HUB-INCIDENT_COMMAND, HUB-DATA_PIPELINE]
see_also: [HUB-INCIDENT_COMMAND, HUB-DATA_PIPELINE]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → data_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `incident_command` is related to `data_pipeline`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
