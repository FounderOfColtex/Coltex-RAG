---
id: LINK-00185
title: "Graph Link: security_operations ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, security_operations, vector_store_cluster]
related: [HUB-SECURITY_OPERATIONS, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-SECURITY_OPERATIONS, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Graph Link: security_operations → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `security_operations` documents `vector_store_cluster`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
