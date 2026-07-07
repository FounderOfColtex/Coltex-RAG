---
id: LINK-00043
title: "Graph Link: graphrag_engine ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, agent_orchestrator]
related: [HUB-GRAPHRAG_ENGINE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → agent_orchestrator

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `graphrag_engine` is related to `agent_orchestrator`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
