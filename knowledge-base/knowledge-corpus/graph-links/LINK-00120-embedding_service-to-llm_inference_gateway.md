---
id: LINK-00120
title: "Graph Link: embedding_service ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, embedding_service, llm_inference_gateway]
related: [HUB-EMBEDDING_SERVICE, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-EMBEDDING_SERVICE, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Graph Link: embedding_service → llm_inference_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `embedding_service` calls into `llm_inference_gateway`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
