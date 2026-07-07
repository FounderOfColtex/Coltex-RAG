---
id: LINK-00039
title: "Graph Link: graphrag_engine ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, payment_service]
related: [HUB-GRAPHRAG_ENGINE, HUB-PAYMENT_SERVICE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-PAYMENT_SERVICE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → payment_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `graphrag_engine` is related to `payment_service`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
