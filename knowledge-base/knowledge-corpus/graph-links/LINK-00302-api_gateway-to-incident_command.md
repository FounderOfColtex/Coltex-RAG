---
id: LINK-00302
title: "Graph Link: api_gateway ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, api_gateway, incident_command]
related: [HUB-API_GATEWAY, HUB-INCIDENT_COMMAND]
see_also: [HUB-API_GATEWAY, HUB-INCIDENT_COMMAND]
depends_on: [HUB-API_GATEWAY]
---

# Graph Link: api_gateway → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `api_gateway` calls into `incident_command`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
