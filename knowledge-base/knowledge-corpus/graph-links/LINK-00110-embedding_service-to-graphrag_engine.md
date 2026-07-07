---
id: LINK-00110
title: "Graph Link: embedding_service ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, embedding_service, graphrag_engine]
related: [HUB-EMBEDDING_SERVICE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-EMBEDDING_SERVICE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Graph Link: embedding_service → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `embedding_service` depends on `graphrag_engine`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
