---
id: LINK-00225
title: "Graph Link: llm_inference_gateway ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, llm_inference_gateway, rag_retrieval_core]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Graph Link: llm_inference_gateway → rag_retrieval_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `llm_inference_gateway` is related to `rag_retrieval_core`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
