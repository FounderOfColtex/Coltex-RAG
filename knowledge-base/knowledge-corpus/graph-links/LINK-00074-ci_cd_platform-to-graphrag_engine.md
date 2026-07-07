---
id: LINK-00074
title: "Graph Link: ci_cd_platform ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ci_cd_platform, graphrag_engine]
related: [HUB-CI_CD_PLATFORM, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-CI_CD_PLATFORM, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Graph Link: ci_cd_platform → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `ci_cd_platform` calls into `graphrag_engine`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
