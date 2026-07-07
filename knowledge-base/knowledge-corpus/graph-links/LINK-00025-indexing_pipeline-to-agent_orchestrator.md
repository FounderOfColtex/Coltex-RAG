---
id: LINK-00025
title: "Graph Link: indexing_pipeline ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, agent_orchestrator]
related: [HUB-INDEXING_PIPELINE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-INDEXING_PIPELINE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → agent_orchestrator

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `indexing_pipeline` depends on `agent_orchestrator`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
