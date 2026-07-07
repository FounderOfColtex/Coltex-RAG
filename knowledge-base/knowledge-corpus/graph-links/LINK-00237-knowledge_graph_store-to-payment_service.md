---
id: LINK-00237
title: "Graph Link: knowledge_graph_store ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, knowledge_graph_store, payment_service]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-PAYMENT_SERVICE]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-PAYMENT_SERVICE]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Graph Link: knowledge_graph_store → payment_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `knowledge_graph_store` depends on `payment_service`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
