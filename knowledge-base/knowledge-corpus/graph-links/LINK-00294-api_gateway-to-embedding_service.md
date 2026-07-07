---
id: LINK-00294
title: "Graph Link: api_gateway ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, api_gateway, embedding_service]
related: [HUB-API_GATEWAY, HUB-EMBEDDING_SERVICE]
see_also: [HUB-API_GATEWAY, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-API_GATEWAY]
---

# Graph Link: api_gateway → embedding_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `api_gateway` calls into `embedding_service`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
