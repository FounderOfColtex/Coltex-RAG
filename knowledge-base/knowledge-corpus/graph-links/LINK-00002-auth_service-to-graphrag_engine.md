---
id: LINK-00002
title: "Graph Link: auth_service ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, auth_service, graphrag_engine]
related: [HUB-AUTH_SERVICE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-AUTH_SERVICE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-AUTH_SERVICE]
---

# Graph Link: auth_service → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `auth_service` calls into `graphrag_engine`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
