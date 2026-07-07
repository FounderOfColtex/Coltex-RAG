---
id: LINK-00179
title: "Graph Link: rag_retrieval_core ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, rag_retrieval_core, coltex_knowledge_core]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Graph Link: rag_retrieval_core → coltex_knowledge_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `rag_retrieval_core` calls into `coltex_knowledge_core`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
