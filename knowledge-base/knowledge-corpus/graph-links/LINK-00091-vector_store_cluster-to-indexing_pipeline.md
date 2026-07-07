---
id: LINK-00091
title: "Graph Link: vector_store_cluster ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, vector_store_cluster, indexing_pipeline]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-INDEXING_PIPELINE]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-INDEXING_PIPELINE]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Graph Link: vector_store_cluster → indexing_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `vector_store_cluster` calls into `indexing_pipeline`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
