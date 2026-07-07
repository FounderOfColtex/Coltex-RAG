---
id: LINK-00157
title: "Graph Link: observability_stack ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, knowledge_graph_store]
related: [HUB-OBSERVABILITY_STACK, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → knowledge_graph_store

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `observability_stack` is related to `knowledge_graph_store`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
