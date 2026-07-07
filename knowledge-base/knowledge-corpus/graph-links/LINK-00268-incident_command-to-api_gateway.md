---
id: LINK-00268
title: "Graph Link: incident_command ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, api_gateway]
related: [HUB-INCIDENT_COMMAND, HUB-API_GATEWAY]
see_also: [HUB-INCIDENT_COMMAND, HUB-API_GATEWAY]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → api_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `incident_command` calls into `api_gateway`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
