---
id: LINK-00065
title: "Graph Link: payment_service ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, data_pipeline]
related: [HUB-PAYMENT_SERVICE, HUB-DATA_PIPELINE]
see_also: [HUB-PAYMENT_SERVICE, HUB-DATA_PIPELINE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → data_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `payment_service` calls into `data_pipeline`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
