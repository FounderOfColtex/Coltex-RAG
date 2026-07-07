---
id: LINK-00088
title: "Graph Link: ci_cd_platform ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ci_cd_platform, api_gateway]
related: [HUB-CI_CD_PLATFORM, HUB-API_GATEWAY]
see_also: [HUB-CI_CD_PLATFORM, HUB-API_GATEWAY]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Graph Link: ci_cd_platform → api_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `ci_cd_platform` depends on `api_gateway`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
