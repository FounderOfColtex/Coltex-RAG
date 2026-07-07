---
id: LINK-00300
title: "Graph Link: api_gateway ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, api_gateway, llm_inference_gateway]
related: [HUB-API_GATEWAY, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-API_GATEWAY, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-API_GATEWAY]
---

# Graph Link: api_gateway → llm_inference_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `api_gateway` depends on `llm_inference_gateway`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
