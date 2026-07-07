---
id: LINK-00226
title: "Graph Link: llm_inference_gateway ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, llm_inference_gateway, security_operations]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-SECURITY_OPERATIONS]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Graph Link: llm_inference_gateway → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `llm_inference_gateway` calls into `security_operations`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
