---
id: LINK-00041
title: "Graph Link: graphrag_engine ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, vector_store_cluster]
related: [HUB-GRAPHRAG_ENGINE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `graphrag_engine` documents `vector_store_cluster`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
