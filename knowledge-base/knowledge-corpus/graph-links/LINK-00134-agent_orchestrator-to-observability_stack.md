---
id: LINK-00134
title: "Graph Link: agent_orchestrator ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, agent_orchestrator, observability_stack]
related: [HUB-AGENT_ORCHESTRATOR, HUB-OBSERVABILITY_STACK]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Graph Link: agent_orchestrator → observability_stack

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `agent_orchestrator` documents `observability_stack`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
