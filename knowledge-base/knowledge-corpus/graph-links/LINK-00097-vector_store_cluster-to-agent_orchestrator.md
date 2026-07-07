---
id: LINK-00097
title: "Graph Link: vector_store_cluster ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, vector_store_cluster, agent_orchestrator]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Graph Link: vector_store_cluster → agent_orchestrator

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `vector_store_cluster` depends on `agent_orchestrator`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
