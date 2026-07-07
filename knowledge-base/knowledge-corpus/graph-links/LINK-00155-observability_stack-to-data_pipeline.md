---
id: LINK-00155
title: "Graph Link: observability_stack ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, data_pipeline]
related: [HUB-OBSERVABILITY_STACK, HUB-DATA_PIPELINE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-DATA_PIPELINE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → data_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `observability_stack` documents `data_pipeline`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
