---
id: LINK-00058
title: "Graph Link: payment_service ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, ci_cd_platform]
related: [HUB-PAYMENT_SERVICE, HUB-CI_CD_PLATFORM]
see_also: [HUB-PAYMENT_SERVICE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → ci_cd_platform

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `payment_service` documents `ci_cd_platform`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
