---
id: LINK-00169
title: "Graph Link: rag_retrieval_core ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, rag_retrieval_core, agent_orchestrator]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Graph Link: rag_retrieval_core → agent_orchestrator

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `rag_retrieval_core` depends on `agent_orchestrator`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
