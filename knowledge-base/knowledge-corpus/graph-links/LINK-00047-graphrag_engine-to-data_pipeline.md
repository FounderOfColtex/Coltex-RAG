---
id: LINK-00047
title: "Graph Link: graphrag_engine ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, data_pipeline]
related: [HUB-GRAPHRAG_ENGINE, HUB-DATA_PIPELINE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-DATA_PIPELINE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → data_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `graphrag_engine` is related to `data_pipeline`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
