---
id: LINK-00089
title: "Graph Link: ci_cd_platform ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ci_cd_platform, coltex_knowledge_core]
related: [HUB-CI_CD_PLATFORM, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-CI_CD_PLATFORM, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Graph Link: ci_cd_platform → coltex_knowledge_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `ci_cd_platform` is related to `coltex_knowledge_core`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
