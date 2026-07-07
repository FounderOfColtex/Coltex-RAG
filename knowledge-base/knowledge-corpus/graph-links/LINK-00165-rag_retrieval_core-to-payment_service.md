---
id: LINK-00165
title: "Graph Link: rag_retrieval_core ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, rag_retrieval_core, payment_service]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-PAYMENT_SERVICE]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-PAYMENT_SERVICE]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Graph Link: rag_retrieval_core → payment_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `rag_retrieval_core` depends on `payment_service`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
