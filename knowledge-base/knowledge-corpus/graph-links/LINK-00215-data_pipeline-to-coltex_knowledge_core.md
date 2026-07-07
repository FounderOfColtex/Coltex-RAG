---
id: LINK-00215
title: "Graph Link: data_pipeline ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, data_pipeline, coltex_knowledge_core]
related: [HUB-DATA_PIPELINE, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-DATA_PIPELINE, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-DATA_PIPELINE]
---

# Graph Link: data_pipeline → coltex_knowledge_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `data_pipeline` depends on `coltex_knowledge_core`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
