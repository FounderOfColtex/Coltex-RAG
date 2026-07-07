---
id: LINK-00086
title: "Graph Link: ci_cd_platform ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ci_cd_platform, incident_command]
related: [HUB-CI_CD_PLATFORM, HUB-INCIDENT_COMMAND]
see_also: [HUB-CI_CD_PLATFORM, HUB-INCIDENT_COMMAND]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Graph Link: ci_cd_platform → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `ci_cd_platform` calls into `incident_command`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
