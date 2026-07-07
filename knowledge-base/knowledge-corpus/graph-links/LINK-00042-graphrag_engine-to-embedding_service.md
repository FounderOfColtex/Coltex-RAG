---
id: LINK-00042
title: "Graph Link: graphrag_engine ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, embedding_service]
related: [HUB-GRAPHRAG_ENGINE, HUB-EMBEDDING_SERVICE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → embedding_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `graphrag_engine` depends on `embedding_service`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
