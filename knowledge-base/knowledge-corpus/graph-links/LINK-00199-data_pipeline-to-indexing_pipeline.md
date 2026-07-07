---
id: LINK-00199
title: "Graph Link: data_pipeline ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, data_pipeline, indexing_pipeline]
related: [HUB-DATA_PIPELINE, HUB-INDEXING_PIPELINE]
see_also: [HUB-DATA_PIPELINE, HUB-INDEXING_PIPELINE]
depends_on: [HUB-DATA_PIPELINE]
---

# Graph Link: data_pipeline → indexing_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `data_pipeline` depends on `indexing_pipeline`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
