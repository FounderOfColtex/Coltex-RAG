---
id: LINK-00007
title: "Graph Link: auth_service ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, auth_service, agent_orchestrator]
related: [HUB-AUTH_SERVICE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-AUTH_SERVICE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-AUTH_SERVICE]
---

# Graph Link: auth_service → agent_orchestrator

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `auth_service` documents `agent_orchestrator`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
