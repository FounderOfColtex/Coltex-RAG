---
id: LINK-00172
title: "Graph Link: rag_retrieval_core ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, rag_retrieval_core, security_operations]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Graph Link: rag_retrieval_core → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `rag_retrieval_core` documents `security_operations`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
