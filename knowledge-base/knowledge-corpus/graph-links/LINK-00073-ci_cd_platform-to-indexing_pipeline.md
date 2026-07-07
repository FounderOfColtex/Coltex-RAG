---
id: LINK-00073
title: "Graph Link: ci_cd_platform ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ci_cd_platform, indexing_pipeline]
related: [HUB-CI_CD_PLATFORM, HUB-INDEXING_PIPELINE]
see_also: [HUB-CI_CD_PLATFORM, HUB-INDEXING_PIPELINE]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Graph Link: ci_cd_platform → indexing_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `ci_cd_platform` is related to `indexing_pipeline`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
