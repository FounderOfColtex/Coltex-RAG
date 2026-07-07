---
id: LINK-00018
title: "Graph Link: indexing_pipeline ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, auth_service]
related: [HUB-INDEXING_PIPELINE, HUB-AUTH_SERVICE]
see_also: [HUB-INDEXING_PIPELINE, HUB-AUTH_SERVICE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → auth_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `indexing_pipeline` is related to `auth_service`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
