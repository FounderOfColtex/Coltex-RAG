---
id: LINK-00119
title: "Graph Link: embedding_service ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, embedding_service, data_pipeline]
related: [HUB-EMBEDDING_SERVICE, HUB-DATA_PIPELINE]
see_also: [HUB-EMBEDDING_SERVICE, HUB-DATA_PIPELINE]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Graph Link: embedding_service → data_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `embedding_service` is related to `data_pipeline`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
