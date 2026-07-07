---
id: LINK-00075
title: "Graph Link: ci_cd_platform ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ci_cd_platform, payment_service]
related: [HUB-CI_CD_PLATFORM, HUB-PAYMENT_SERVICE]
see_also: [HUB-CI_CD_PLATFORM, HUB-PAYMENT_SERVICE]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Graph Link: ci_cd_platform → payment_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `ci_cd_platform` documents `payment_service`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
