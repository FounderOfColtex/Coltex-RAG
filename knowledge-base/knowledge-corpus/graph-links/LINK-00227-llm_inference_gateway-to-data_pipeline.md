---
id: LINK-00227
title: "Graph Link: llm_inference_gateway ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, llm_inference_gateway, data_pipeline]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-DATA_PIPELINE]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-DATA_PIPELINE]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Graph Link: llm_inference_gateway → data_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `llm_inference_gateway` documents `data_pipeline`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
