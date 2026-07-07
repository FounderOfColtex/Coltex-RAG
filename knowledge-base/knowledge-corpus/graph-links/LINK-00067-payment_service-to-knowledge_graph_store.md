---
id: LINK-00067
title: "Graph Link: payment_service ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, knowledge_graph_store]
related: [HUB-PAYMENT_SERVICE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-PAYMENT_SERVICE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → knowledge_graph_store

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `payment_service` depends on `knowledge_graph_store`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
