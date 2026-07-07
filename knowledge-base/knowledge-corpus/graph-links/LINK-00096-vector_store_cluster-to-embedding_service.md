---
id: LINK-00096
title: "Graph Link: vector_store_cluster ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, vector_store_cluster, embedding_service]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-EMBEDDING_SERVICE]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Graph Link: vector_store_cluster → embedding_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `vector_store_cluster` documents `embedding_service`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
