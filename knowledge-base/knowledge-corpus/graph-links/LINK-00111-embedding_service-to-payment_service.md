---
id: LINK-00111
title: "Graph Link: embedding_service ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, embedding_service, payment_service]
related: [HUB-EMBEDDING_SERVICE, HUB-PAYMENT_SERVICE]
see_also: [HUB-EMBEDDING_SERVICE, HUB-PAYMENT_SERVICE]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Graph Link: embedding_service → payment_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `embedding_service` is related to `payment_service`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
