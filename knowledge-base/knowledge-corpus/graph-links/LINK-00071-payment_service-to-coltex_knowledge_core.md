---
id: LINK-00071
title: "Graph Link: payment_service ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, coltex_knowledge_core]
related: [HUB-PAYMENT_SERVICE, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-PAYMENT_SERVICE, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → coltex_knowledge_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `payment_service` depends on `coltex_knowledge_core`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
