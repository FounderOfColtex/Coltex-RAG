---
id: LINK-00238
title: "Graph Link: knowledge_graph_store ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, knowledge_graph_store, ci_cd_platform]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-CI_CD_PLATFORM]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Graph Link: knowledge_graph_store → ci_cd_platform

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `knowledge_graph_store` is related to `ci_cd_platform`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
