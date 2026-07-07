---
id: LINK-00027
title: "Graph Link: indexing_pipeline ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, rag_retrieval_core]
related: [HUB-INDEXING_PIPELINE, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-INDEXING_PIPELINE, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → rag_retrieval_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `indexing_pipeline` calls into `rag_retrieval_core`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
