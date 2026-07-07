---
id: LINK-00064
title: "Graph Link: payment_service ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, security_operations]
related: [HUB-PAYMENT_SERVICE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-PAYMENT_SERVICE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `payment_service` is related to `security_operations`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
