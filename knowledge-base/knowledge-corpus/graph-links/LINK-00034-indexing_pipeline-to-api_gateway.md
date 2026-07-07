---
id: LINK-00034
title: "Graph Link: indexing_pipeline ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, api_gateway]
related: [HUB-INDEXING_PIPELINE, HUB-API_GATEWAY]
see_also: [HUB-INDEXING_PIPELINE, HUB-API_GATEWAY]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → api_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `indexing_pipeline` is related to `api_gateway`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
