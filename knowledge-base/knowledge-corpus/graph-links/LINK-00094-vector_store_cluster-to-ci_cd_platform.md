---
id: LINK-00094
title: "Graph Link: vector_store_cluster ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, vector_store_cluster, ci_cd_platform]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-CI_CD_PLATFORM]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-CI_CD_PLATFORM]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Graph Link: vector_store_cluster → ci_cd_platform

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `vector_store_cluster` is related to `ci_cd_platform`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
