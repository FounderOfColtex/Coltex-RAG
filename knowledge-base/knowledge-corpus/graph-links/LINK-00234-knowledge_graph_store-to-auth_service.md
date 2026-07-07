---
id: LINK-00234
title: "Graph Link: knowledge_graph_store ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, knowledge_graph_store, auth_service]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-AUTH_SERVICE]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-AUTH_SERVICE]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Graph Link: knowledge_graph_store → auth_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `knowledge_graph_store` is related to `auth_service`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
