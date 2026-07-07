---
id: LINK-00129
title: "Graph Link: agent_orchestrator ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, agent_orchestrator, payment_service]
related: [HUB-AGENT_ORCHESTRATOR, HUB-PAYMENT_SERVICE]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-PAYMENT_SERVICE]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Graph Link: agent_orchestrator → payment_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `agent_orchestrator` calls into `payment_service`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
