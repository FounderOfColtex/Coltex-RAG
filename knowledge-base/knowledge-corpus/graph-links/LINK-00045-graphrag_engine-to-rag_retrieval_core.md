---
id: LINK-00045
title: "Graph Link: graphrag_engine ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, rag_retrieval_core]
related: [HUB-GRAPHRAG_ENGINE, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → rag_retrieval_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `graphrag_engine` documents `rag_retrieval_core`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
