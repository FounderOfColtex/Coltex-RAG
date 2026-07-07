---
id: LINK-00149
title: "Graph Link: observability_stack ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, vector_store_cluster]
related: [HUB-OBSERVABILITY_STACK, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-OBSERVABILITY_STACK, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `observability_stack` is related to `vector_store_cluster`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
