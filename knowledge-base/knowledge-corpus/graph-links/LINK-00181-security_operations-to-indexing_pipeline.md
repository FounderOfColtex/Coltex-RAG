---
id: LINK-00181
title: "Graph Link: security_operations ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, security_operations, indexing_pipeline]
related: [HUB-SECURITY_OPERATIONS, HUB-INDEXING_PIPELINE]
see_also: [HUB-SECURITY_OPERATIONS, HUB-INDEXING_PIPELINE]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Graph Link: security_operations → indexing_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `security_operations` documents `indexing_pipeline`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
