---
id: LINK-00151
title: "Graph Link: observability_stack ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, agent_orchestrator]
related: [HUB-OBSERVABILITY_STACK, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-OBSERVABILITY_STACK, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → agent_orchestrator

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `observability_stack` documents `agent_orchestrator`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
