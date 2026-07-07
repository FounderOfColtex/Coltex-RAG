---
id: LINK-00055
title: "Graph Link: payment_service ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, indexing_pipeline]
related: [HUB-PAYMENT_SERVICE, HUB-INDEXING_PIPELINE]
see_also: [HUB-PAYMENT_SERVICE, HUB-INDEXING_PIPELINE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → indexing_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `payment_service` depends on `indexing_pipeline`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
