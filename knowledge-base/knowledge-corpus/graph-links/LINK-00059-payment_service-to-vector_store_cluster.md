---
id: LINK-00059
title: "Graph Link: payment_service ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, vector_store_cluster]
related: [HUB-PAYMENT_SERVICE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-PAYMENT_SERVICE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `payment_service` depends on `vector_store_cluster`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
