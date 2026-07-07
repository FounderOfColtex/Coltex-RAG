---
id: LINK-00150
title: "Graph Link: observability_stack ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, embedding_service]
related: [HUB-OBSERVABILITY_STACK, HUB-EMBEDDING_SERVICE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → embedding_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `observability_stack` calls into `embedding_service`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
