---
id: LINK-00167
title: "Graph Link: rag_retrieval_core ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, rag_retrieval_core, vector_store_cluster]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Graph Link: rag_retrieval_core → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `rag_retrieval_core` calls into `vector_store_cluster`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
