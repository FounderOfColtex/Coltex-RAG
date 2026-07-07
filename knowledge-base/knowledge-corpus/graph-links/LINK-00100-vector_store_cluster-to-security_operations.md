---
id: LINK-00100
title: "Graph Link: vector_store_cluster ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, vector_store_cluster, security_operations]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-SECURITY_OPERATIONS]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Graph Link: vector_store_cluster → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `vector_store_cluster` documents `security_operations`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
