---
id: LINK-00063
title: "Graph Link: payment_service ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, rag_retrieval_core]
related: [HUB-PAYMENT_SERVICE, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-PAYMENT_SERVICE, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → rag_retrieval_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `payment_service` depends on `rag_retrieval_core`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
