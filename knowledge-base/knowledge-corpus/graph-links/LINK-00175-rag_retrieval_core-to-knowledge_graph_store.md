---
id: LINK-00175
title: "Graph Link: rag_retrieval_core ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, rag_retrieval_core, knowledge_graph_store]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Graph Link: rag_retrieval_core → knowledge_graph_store

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `rag_retrieval_core` calls into `knowledge_graph_store`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
