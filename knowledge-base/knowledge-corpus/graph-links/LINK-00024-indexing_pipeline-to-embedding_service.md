---
id: LINK-00024
title: "Graph Link: indexing_pipeline ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, embedding_service]
related: [HUB-INDEXING_PIPELINE, HUB-EMBEDDING_SERVICE]
see_also: [HUB-INDEXING_PIPELINE, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → embedding_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `indexing_pipeline` documents `embedding_service`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
