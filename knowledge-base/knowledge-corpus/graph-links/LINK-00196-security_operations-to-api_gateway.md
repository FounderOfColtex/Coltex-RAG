---
id: LINK-00196
title: "Graph Link: security_operations ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, security_operations, api_gateway]
related: [HUB-SECURITY_OPERATIONS, HUB-API_GATEWAY]
see_also: [HUB-SECURITY_OPERATIONS, HUB-API_GATEWAY]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Graph Link: security_operations → api_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `security_operations` calls into `api_gateway`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
