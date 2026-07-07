---
id: LINK-00264
title: "Graph Link: incident_command ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, llm_inference_gateway]
related: [HUB-INCIDENT_COMMAND, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-INCIDENT_COMMAND, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → llm_inference_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `incident_command` calls into `llm_inference_gateway`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
