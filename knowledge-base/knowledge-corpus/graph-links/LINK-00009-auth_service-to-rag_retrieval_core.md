---
id: LINK-00009
title: "Graph Link: auth_service ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, auth_service, rag_retrieval_core]
related: [HUB-AUTH_SERVICE, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-AUTH_SERVICE, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-AUTH_SERVICE]
---

# Graph Link: auth_service → rag_retrieval_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `auth_service` is related to `rag_retrieval_core`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
