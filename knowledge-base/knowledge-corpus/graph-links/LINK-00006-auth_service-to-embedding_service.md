---
id: LINK-00006
title: "Graph Link: auth_service ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, auth_service, embedding_service]
related: [HUB-AUTH_SERVICE, HUB-EMBEDDING_SERVICE]
see_also: [HUB-AUTH_SERVICE, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-AUTH_SERVICE]
---

# Graph Link: auth_service → embedding_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `auth_service` calls into `embedding_service`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
