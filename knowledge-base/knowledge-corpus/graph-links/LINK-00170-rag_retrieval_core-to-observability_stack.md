---
id: LINK-00170
title: "Graph Link: rag_retrieval_core ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, rag_retrieval_core, observability_stack]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-OBSERVABILITY_STACK]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Graph Link: rag_retrieval_core → observability_stack

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `rag_retrieval_core` is related to `observability_stack`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
