---
id: LINK-00118
title: "Graph Link: embedding_service ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, embedding_service, security_operations]
related: [HUB-EMBEDDING_SERVICE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-EMBEDDING_SERVICE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Graph Link: embedding_service → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `embedding_service` depends on `security_operations`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
