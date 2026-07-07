---
id: LINK-00309
title: "Graph Link: coltex_knowledge_core ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, payment_service]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-PAYMENT_SERVICE]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-PAYMENT_SERVICE]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → payment_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `coltex_knowledge_core` depends on `payment_service`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
