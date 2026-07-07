---
id: LINK-00244
title: "Graph Link: knowledge_graph_store ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, knowledge_graph_store, security_operations]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Graph Link: knowledge_graph_store → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `knowledge_graph_store` documents `security_operations`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
