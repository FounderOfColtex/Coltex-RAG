---
id: LINK-00223
title: "Graph Link: llm_inference_gateway ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, llm_inference_gateway, agent_orchestrator]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Graph Link: llm_inference_gateway → agent_orchestrator

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `llm_inference_gateway` documents `agent_orchestrator`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
