---
id: LINK-00021
title: "Graph Link: indexing_pipeline ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, payment_service]
related: [HUB-INDEXING_PIPELINE, HUB-PAYMENT_SERVICE]
see_also: [HUB-INDEXING_PIPELINE, HUB-PAYMENT_SERVICE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → payment_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `indexing_pipeline` depends on `payment_service`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
