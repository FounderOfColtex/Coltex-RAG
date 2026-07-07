---
id: LINK-00030
title: "Graph Link: indexing_pipeline ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, llm_inference_gateway]
related: [HUB-INDEXING_PIPELINE, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-INDEXING_PIPELINE, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → llm_inference_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `indexing_pipeline` is related to `llm_inference_gateway`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
