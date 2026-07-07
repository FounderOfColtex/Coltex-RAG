---
id: LINK-00026
title: "Graph Link: indexing_pipeline ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, observability_stack]
related: [HUB-INDEXING_PIPELINE, HUB-OBSERVABILITY_STACK]
see_also: [HUB-INDEXING_PIPELINE, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → observability_stack

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `indexing_pipeline` is related to `observability_stack`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
