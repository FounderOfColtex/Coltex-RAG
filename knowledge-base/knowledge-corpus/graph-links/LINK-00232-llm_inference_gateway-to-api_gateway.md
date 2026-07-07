---
id: LINK-00232
title: "Graph Link: llm_inference_gateway ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, llm_inference_gateway, api_gateway]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-API_GATEWAY]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-API_GATEWAY]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Graph Link: llm_inference_gateway → api_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `llm_inference_gateway` depends on `api_gateway`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
