---
id: LINK-00049
title: "Graph Link: graphrag_engine ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, knowledge_graph_store]
related: [HUB-GRAPHRAG_ENGINE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → knowledge_graph_store

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `graphrag_engine` documents `knowledge_graph_store`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
