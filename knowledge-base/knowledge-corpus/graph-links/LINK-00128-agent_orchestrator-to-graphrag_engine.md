---
id: LINK-00128
title: "Graph Link: agent_orchestrator ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, agent_orchestrator, graphrag_engine]
related: [HUB-AGENT_ORCHESTRATOR, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Graph Link: agent_orchestrator → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `agent_orchestrator` is related to `graphrag_engine`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
