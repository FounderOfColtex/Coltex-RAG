---
id: LINK-00308
title: "Graph Link: coltex_knowledge_core ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, graphrag_engine]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `coltex_knowledge_core` documents `graphrag_engine`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
