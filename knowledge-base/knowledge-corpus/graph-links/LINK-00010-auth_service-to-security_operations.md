---
id: LINK-00010
title: "Graph Link: auth_service ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, auth_service, security_operations]
related: [HUB-AUTH_SERVICE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-AUTH_SERVICE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-AUTH_SERVICE]
---

# Graph Link: auth_service → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `auth_service` calls into `security_operations`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
