---
id: LINK-00102
title: "Graph Link: vector_store_cluster ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, vector_store_cluster, llm_inference_gateway]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Graph Link: vector_store_cluster → llm_inference_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `vector_store_cluster` is related to `llm_inference_gateway`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
