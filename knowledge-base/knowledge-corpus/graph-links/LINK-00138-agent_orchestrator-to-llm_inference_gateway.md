---
id: LINK-00138
title: "Graph Link: agent_orchestrator ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, agent_orchestrator, llm_inference_gateway]
related: [HUB-AGENT_ORCHESTRATOR, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Graph Link: agent_orchestrator → llm_inference_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `agent_orchestrator` documents `llm_inference_gateway`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
