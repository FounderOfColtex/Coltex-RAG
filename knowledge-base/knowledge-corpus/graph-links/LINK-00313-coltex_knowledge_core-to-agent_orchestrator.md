---
id: LINK-00313
title: "Graph Link: coltex_knowledge_core ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, agent_orchestrator]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → agent_orchestrator

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `coltex_knowledge_core` depends on `agent_orchestrator`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
