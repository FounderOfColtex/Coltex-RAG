---
id: LINK-00036
title: "Graph Link: graphrag_engine ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, auth_service]
related: [HUB-GRAPHRAG_ENGINE, HUB-AUTH_SERVICE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-AUTH_SERVICE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → auth_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `graphrag_engine` calls into `auth_service`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
