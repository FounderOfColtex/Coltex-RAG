---
id: LINK-00020
title: "Graph Link: indexing_pipeline ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, graphrag_engine]
related: [HUB-INDEXING_PIPELINE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-INDEXING_PIPELINE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `indexing_pipeline` documents `graphrag_engine`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
