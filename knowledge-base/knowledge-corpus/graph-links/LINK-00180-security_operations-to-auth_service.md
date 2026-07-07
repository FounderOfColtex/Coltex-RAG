---
id: LINK-00180
title: "Graph Link: security_operations ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, security_operations, auth_service]
related: [HUB-SECURITY_OPERATIONS, HUB-AUTH_SERVICE]
see_also: [HUB-SECURITY_OPERATIONS, HUB-AUTH_SERVICE]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Graph Link: security_operations → auth_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `security_operations` calls into `auth_service`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
