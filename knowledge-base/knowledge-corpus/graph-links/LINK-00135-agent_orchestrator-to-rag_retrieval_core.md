---
id: LINK-00135
title: "Graph Link: agent_orchestrator ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, agent_orchestrator, rag_retrieval_core]
related: [HUB-AGENT_ORCHESTRATOR, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Graph Link: agent_orchestrator → rag_retrieval_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `agent_orchestrator` depends on `rag_retrieval_core`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
