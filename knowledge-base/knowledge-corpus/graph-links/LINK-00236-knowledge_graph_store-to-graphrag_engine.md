---
id: LINK-00236
title: "Graph Link: knowledge_graph_store ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, knowledge_graph_store, graphrag_engine]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Graph Link: knowledge_graph_store → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `knowledge_graph_store` documents `graphrag_engine`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
