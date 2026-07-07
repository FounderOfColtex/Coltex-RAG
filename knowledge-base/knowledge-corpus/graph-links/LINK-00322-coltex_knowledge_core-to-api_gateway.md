---
id: LINK-00322
title: "Graph Link: coltex_knowledge_core ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, api_gateway]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-API_GATEWAY]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-API_GATEWAY]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → api_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `coltex_knowledge_core` is related to `api_gateway`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
