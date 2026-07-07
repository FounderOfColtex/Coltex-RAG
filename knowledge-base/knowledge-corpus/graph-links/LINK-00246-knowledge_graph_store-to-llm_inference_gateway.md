---
id: LINK-00246
title: "Graph Link: knowledge_graph_store ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, knowledge_graph_store, llm_inference_gateway]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Graph Link: knowledge_graph_store → llm_inference_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `knowledge_graph_store` is related to `llm_inference_gateway`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
