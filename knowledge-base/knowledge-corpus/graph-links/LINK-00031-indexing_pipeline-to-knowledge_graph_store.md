---
id: LINK-00031
title: "Graph Link: indexing_pipeline ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, knowledge_graph_store]
related: [HUB-INDEXING_PIPELINE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-INDEXING_PIPELINE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → knowledge_graph_store

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `indexing_pipeline` calls into `knowledge_graph_store`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
