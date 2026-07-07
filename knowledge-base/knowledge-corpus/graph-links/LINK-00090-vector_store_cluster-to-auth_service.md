---
id: LINK-00090
title: "Graph Link: vector_store_cluster ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, vector_store_cluster, auth_service]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-AUTH_SERVICE]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-AUTH_SERVICE]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Graph Link: vector_store_cluster → auth_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `vector_store_cluster` is related to `auth_service`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
