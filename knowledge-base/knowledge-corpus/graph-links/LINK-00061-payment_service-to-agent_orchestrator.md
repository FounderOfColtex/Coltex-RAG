---
id: LINK-00061
title: "Graph Link: payment_service ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, agent_orchestrator]
related: [HUB-PAYMENT_SERVICE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-PAYMENT_SERVICE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → agent_orchestrator

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `payment_service` calls into `agent_orchestrator`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
