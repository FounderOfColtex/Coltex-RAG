---
id: LINK-00054
title: "Graph Link: payment_service ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, auth_service]
related: [HUB-PAYMENT_SERVICE, HUB-AUTH_SERVICE]
see_also: [HUB-PAYMENT_SERVICE, HUB-AUTH_SERVICE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → auth_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `payment_service` documents `auth_service`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
