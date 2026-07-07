---
id: LINK-00224
title: "Graph Link: llm_inference_gateway ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, llm_inference_gateway, observability_stack]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-OBSERVABILITY_STACK]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Graph Link: llm_inference_gateway → observability_stack

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `llm_inference_gateway` depends on `observability_stack`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
