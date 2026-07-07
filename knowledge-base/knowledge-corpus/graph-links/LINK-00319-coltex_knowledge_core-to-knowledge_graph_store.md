---
id: LINK-00319
title: "Graph Link: coltex_knowledge_core ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, knowledge_graph_store]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → knowledge_graph_store

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `coltex_knowledge_core` calls into `knowledge_graph_store`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
