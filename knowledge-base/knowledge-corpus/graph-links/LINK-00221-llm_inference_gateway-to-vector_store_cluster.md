---
id: LINK-00221
title: "Graph Link: llm_inference_gateway ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, llm_inference_gateway, vector_store_cluster]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Graph Link: llm_inference_gateway → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `llm_inference_gateway` is related to `vector_store_cluster`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
