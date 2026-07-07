---
id: LINK-00046
title: "Graph Link: graphrag_engine ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, security_operations]
related: [HUB-GRAPHRAG_ENGINE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `graphrag_engine` depends on `security_operations`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
