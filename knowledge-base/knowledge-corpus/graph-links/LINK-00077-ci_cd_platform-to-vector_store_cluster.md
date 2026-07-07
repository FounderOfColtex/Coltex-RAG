---
id: LINK-00077
title: "Graph Link: ci_cd_platform ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ci_cd_platform, vector_store_cluster]
related: [HUB-CI_CD_PLATFORM, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-CI_CD_PLATFORM, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Graph Link: ci_cd_platform → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `ci_cd_platform` is related to `vector_store_cluster`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
