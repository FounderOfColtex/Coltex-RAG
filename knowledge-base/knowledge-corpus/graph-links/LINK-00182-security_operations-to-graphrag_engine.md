---
id: LINK-00182
title: "Graph Link: security_operations ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, security_operations, graphrag_engine]
related: [HUB-SECURITY_OPERATIONS, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-SECURITY_OPERATIONS, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Graph Link: security_operations → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `security_operations` depends on `graphrag_engine`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
