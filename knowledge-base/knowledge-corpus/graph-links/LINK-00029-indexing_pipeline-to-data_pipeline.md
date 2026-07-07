---
id: LINK-00029
title: "Graph Link: indexing_pipeline ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, data_pipeline]
related: [HUB-INDEXING_PIPELINE, HUB-DATA_PIPELINE]
see_also: [HUB-INDEXING_PIPELINE, HUB-DATA_PIPELINE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → data_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `indexing_pipeline` depends on `data_pipeline`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
