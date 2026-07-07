---
id: LINK-00056
title: "Graph Link: payment_service ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, graphrag_engine]
related: [HUB-PAYMENT_SERVICE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-PAYMENT_SERVICE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `payment_service` is related to `graphrag_engine`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
