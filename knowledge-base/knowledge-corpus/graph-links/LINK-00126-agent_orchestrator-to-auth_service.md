---
id: LINK-00126
title: "Graph Link: agent_orchestrator ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, agent_orchestrator, auth_service]
related: [HUB-AGENT_ORCHESTRATOR, HUB-AUTH_SERVICE]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-AUTH_SERVICE]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Graph Link: agent_orchestrator → auth_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `agent_orchestrator` documents `auth_service`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
