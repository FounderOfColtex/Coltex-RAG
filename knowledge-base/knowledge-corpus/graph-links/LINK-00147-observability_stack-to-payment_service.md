---
id: LINK-00147
title: "Graph Link: observability_stack ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, payment_service]
related: [HUB-OBSERVABILITY_STACK, HUB-PAYMENT_SERVICE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-PAYMENT_SERVICE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → payment_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `observability_stack` documents `payment_service`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
