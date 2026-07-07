---
id: LINK-00164
title: "Graph Link: rag_retrieval_core ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, rag_retrieval_core, graphrag_engine]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Graph Link: rag_retrieval_core → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `rag_retrieval_core` documents `graphrag_engine`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
