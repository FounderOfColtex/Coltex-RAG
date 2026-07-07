---
id: LINK-00141
title: "Graph Link: agent_orchestrator ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, agent_orchestrator, ml_training_pipeline]
related: [HUB-AGENT_ORCHESTRATOR, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Graph Link: agent_orchestrator → ml_training_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `agent_orchestrator` calls into `ml_training_pipeline`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
