---
id: LINK-00008
title: "Graph Link: auth_service ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, auth_service, observability_stack]
related: [HUB-AUTH_SERVICE, HUB-OBSERVABILITY_STACK]
see_also: [HUB-AUTH_SERVICE, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-AUTH_SERVICE]
---

# Graph Link: auth_service → observability_stack

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `auth_service` depends on `observability_stack`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
