---
id: LINK-00208
title: "Graph Link: data_pipeline ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, data_pipeline, security_operations]
related: [HUB-DATA_PIPELINE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-DATA_PIPELINE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-DATA_PIPELINE]
---

# Graph Link: data_pipeline → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `data_pipeline` is related to `security_operations`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
