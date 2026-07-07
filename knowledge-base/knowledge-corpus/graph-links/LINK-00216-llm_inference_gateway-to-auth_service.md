---
id: LINK-00216
title: "Graph Link: llm_inference_gateway ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, llm_inference_gateway, auth_service]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-AUTH_SERVICE]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-AUTH_SERVICE]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Graph Link: llm_inference_gateway → auth_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `llm_inference_gateway` depends on `auth_service`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
