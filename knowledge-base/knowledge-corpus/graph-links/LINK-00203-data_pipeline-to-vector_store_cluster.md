---
id: LINK-00203
title: "Graph Link: data_pipeline ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, data_pipeline, vector_store_cluster]
related: [HUB-DATA_PIPELINE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-DATA_PIPELINE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-DATA_PIPELINE]
---

# Graph Link: data_pipeline → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `data_pipeline` depends on `vector_store_cluster`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
