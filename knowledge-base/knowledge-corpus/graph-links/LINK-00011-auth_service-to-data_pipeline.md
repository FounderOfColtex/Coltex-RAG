---
id: LINK-00011
title: "Graph Link: auth_service ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, auth_service, data_pipeline]
related: [HUB-AUTH_SERVICE, HUB-DATA_PIPELINE]
see_also: [HUB-AUTH_SERVICE, HUB-DATA_PIPELINE]
depends_on: [HUB-AUTH_SERVICE]
---

# Graph Link: auth_service → data_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `auth_service` documents `data_pipeline`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
