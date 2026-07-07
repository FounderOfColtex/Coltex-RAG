---
id: LINK-00290
title: "Graph Link: api_gateway ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, api_gateway, graphrag_engine]
related: [HUB-API_GATEWAY, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-API_GATEWAY, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-API_GATEWAY]
---

# Graph Link: api_gateway → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `api_gateway` calls into `graphrag_engine`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
