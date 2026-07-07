---
id: LINK-00016
title: "Graph Link: auth_service ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, auth_service, api_gateway]
related: [HUB-AUTH_SERVICE, HUB-API_GATEWAY]
see_also: [HUB-AUTH_SERVICE, HUB-API_GATEWAY]
depends_on: [HUB-AUTH_SERVICE]
---

# Graph Link: auth_service → api_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `auth_service` depends on `api_gateway`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
