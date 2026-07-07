---
id: LINK-00048
title: "Graph Link: graphrag_engine ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, llm_inference_gateway]
related: [HUB-GRAPHRAG_ENGINE, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → llm_inference_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `graphrag_engine` calls into `llm_inference_gateway`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
