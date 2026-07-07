---
id: LINK-00251
title: "Graph Link: knowledge_graph_store ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, knowledge_graph_store, coltex_knowledge_core]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Graph Link: knowledge_graph_store → coltex_knowledge_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `knowledge_graph_store` calls into `coltex_knowledge_core`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
