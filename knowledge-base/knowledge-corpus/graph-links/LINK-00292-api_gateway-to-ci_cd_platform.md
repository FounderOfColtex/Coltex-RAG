---
id: LINK-00292
title: "Graph Link: api_gateway ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, api_gateway, ci_cd_platform]
related: [HUB-API_GATEWAY, HUB-CI_CD_PLATFORM]
see_also: [HUB-API_GATEWAY, HUB-CI_CD_PLATFORM]
depends_on: [HUB-API_GATEWAY]
---

# Graph Link: api_gateway → ci_cd_platform

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `api_gateway` depends on `ci_cd_platform`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
