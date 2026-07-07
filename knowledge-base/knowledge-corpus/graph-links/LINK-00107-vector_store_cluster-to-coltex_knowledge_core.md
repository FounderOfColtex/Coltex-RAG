---
id: LINK-00107
title: "Graph Link: vector_store_cluster ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, vector_store_cluster, coltex_knowledge_core]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Graph Link: vector_store_cluster → coltex_knowledge_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `vector_store_cluster` calls into `coltex_knowledge_core`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
