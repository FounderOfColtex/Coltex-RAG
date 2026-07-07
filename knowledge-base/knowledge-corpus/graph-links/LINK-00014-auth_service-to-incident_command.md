---
id: LINK-00014
title: "Graph Link: auth_service ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, auth_service, incident_command]
related: [HUB-AUTH_SERVICE, HUB-INCIDENT_COMMAND]
see_also: [HUB-AUTH_SERVICE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-AUTH_SERVICE]
---

# Graph Link: auth_service → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `auth_service` calls into `incident_command`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
