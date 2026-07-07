---
id: LINK-00218
title: "Graph Link: llm_inference_gateway ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, llm_inference_gateway, graphrag_engine]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Graph Link: llm_inference_gateway → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `llm_inference_gateway` calls into `graphrag_engine`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
