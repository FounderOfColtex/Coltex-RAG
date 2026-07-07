---
id: LINK-00144
title: "Graph Link: observability_stack ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, auth_service]
related: [HUB-OBSERVABILITY_STACK, HUB-AUTH_SERVICE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-AUTH_SERVICE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → auth_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `observability_stack` depends on `auth_service`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
