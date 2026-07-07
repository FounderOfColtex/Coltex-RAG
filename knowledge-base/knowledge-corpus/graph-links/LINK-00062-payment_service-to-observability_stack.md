---
id: LINK-00062
title: "Graph Link: payment_service ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, observability_stack]
related: [HUB-PAYMENT_SERVICE, HUB-OBSERVABILITY_STACK]
see_also: [HUB-PAYMENT_SERVICE, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → observability_stack

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `payment_service` documents `observability_stack`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
