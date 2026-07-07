---
id: LINK-00136
title: "Graph Link: agent_orchestrator ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, agent_orchestrator, security_operations]
related: [HUB-AGENT_ORCHESTRATOR, HUB-SECURITY_OPERATIONS]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Graph Link: agent_orchestrator → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `agent_orchestrator` is related to `security_operations`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
