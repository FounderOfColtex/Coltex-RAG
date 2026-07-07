---
id: LINK-00311
title: "Graph Link: coltex_knowledge_core ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, vector_store_cluster]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `coltex_knowledge_core` calls into `vector_store_cluster`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
