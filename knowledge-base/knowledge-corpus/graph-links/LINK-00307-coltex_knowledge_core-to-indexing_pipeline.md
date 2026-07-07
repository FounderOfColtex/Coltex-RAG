---
id: LINK-00307
title: "Graph Link: coltex_knowledge_core ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, indexing_pipeline]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-INDEXING_PIPELINE]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-INDEXING_PIPELINE]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → indexing_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `coltex_knowledge_core` calls into `indexing_pipeline`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
