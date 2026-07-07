---
id: LINK-00259
title: "Graph Link: incident_command ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, agent_orchestrator]
related: [HUB-INCIDENT_COMMAND, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-INCIDENT_COMMAND, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → agent_orchestrator

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `incident_command` is related to `agent_orchestrator`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
