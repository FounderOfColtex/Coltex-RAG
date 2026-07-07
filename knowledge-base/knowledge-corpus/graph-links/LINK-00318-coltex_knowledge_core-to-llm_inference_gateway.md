---
id: LINK-00318
title: "Graph Link: coltex_knowledge_core ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, llm_inference_gateway]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → llm_inference_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `coltex_knowledge_core` is related to `llm_inference_gateway`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
