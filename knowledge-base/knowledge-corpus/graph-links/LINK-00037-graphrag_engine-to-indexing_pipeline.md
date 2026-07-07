---
id: LINK-00037
title: "Graph Link: graphrag_engine ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, indexing_pipeline]
related: [HUB-GRAPHRAG_ENGINE, HUB-INDEXING_PIPELINE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-INDEXING_PIPELINE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → indexing_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `graphrag_engine` documents `indexing_pipeline`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
