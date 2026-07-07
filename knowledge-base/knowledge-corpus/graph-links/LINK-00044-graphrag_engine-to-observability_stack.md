---
id: LINK-00044
title: "Graph Link: graphrag_engine ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, observability_stack]
related: [HUB-GRAPHRAG_ENGINE, HUB-OBSERVABILITY_STACK]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → observability_stack

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `graphrag_engine` calls into `observability_stack`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
