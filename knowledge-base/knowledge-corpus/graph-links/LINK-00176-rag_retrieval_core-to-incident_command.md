---
id: LINK-00176
title: "Graph Link: rag_retrieval_core ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, rag_retrieval_core, incident_command]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-INCIDENT_COMMAND]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Graph Link: rag_retrieval_core → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `rag_retrieval_core` documents `incident_command`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
