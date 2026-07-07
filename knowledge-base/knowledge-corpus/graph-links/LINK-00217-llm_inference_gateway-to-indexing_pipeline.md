---
id: LINK-00217
title: "Graph Link: llm_inference_gateway ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, llm_inference_gateway, indexing_pipeline]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-INDEXING_PIPELINE]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-INDEXING_PIPELINE]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Graph Link: llm_inference_gateway → indexing_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `llm_inference_gateway` is related to `indexing_pipeline`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
