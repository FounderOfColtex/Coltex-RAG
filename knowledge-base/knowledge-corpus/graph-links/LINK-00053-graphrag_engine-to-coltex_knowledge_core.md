---
id: LINK-00053
title: "Graph Link: graphrag_engine ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, coltex_knowledge_core]
related: [HUB-GRAPHRAG_ENGINE, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → coltex_knowledge_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `graphrag_engine` documents `coltex_knowledge_core`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
