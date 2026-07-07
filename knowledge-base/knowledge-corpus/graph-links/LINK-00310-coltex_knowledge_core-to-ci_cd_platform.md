---
id: LINK-00310
title: "Graph Link: coltex_knowledge_core ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, ci_cd_platform]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-CI_CD_PLATFORM]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → ci_cd_platform

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `coltex_knowledge_core` is related to `ci_cd_platform`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
