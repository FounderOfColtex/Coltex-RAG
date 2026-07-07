---
id: LINK-00235
title: "Graph Link: knowledge_graph_store ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, knowledge_graph_store, indexing_pipeline]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-INDEXING_PIPELINE]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-INDEXING_PIPELINE]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Graph Link: knowledge_graph_store → indexing_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `knowledge_graph_store` calls into `indexing_pipeline`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
