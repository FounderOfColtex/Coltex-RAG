---
id: LINK-00085
title: "Graph Link: ci_cd_platform ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, ci_cd_platform, knowledge_graph_store]
related: [HUB-CI_CD_PLATFORM, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-CI_CD_PLATFORM, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Graph Link: ci_cd_platform → knowledge_graph_store

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `ci_cd_platform` is related to `knowledge_graph_store`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
