---
id: LINK-00146
title: "Graph Link: observability_stack ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, graphrag_engine]
related: [HUB-OBSERVABILITY_STACK, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `observability_stack` calls into `graphrag_engine`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
