---
id: LINK-00084
title: "Graph Link: ci_cd_platform ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ci_cd_platform, llm_inference_gateway]
related: [HUB-CI_CD_PLATFORM, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-CI_CD_PLATFORM, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Graph Link: ci_cd_platform → llm_inference_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `ci_cd_platform` depends on `llm_inference_gateway`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
