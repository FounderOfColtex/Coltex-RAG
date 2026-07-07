---
id: LINK-00160
title: "Graph Link: observability_stack ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, api_gateway]
related: [HUB-OBSERVABILITY_STACK, HUB-API_GATEWAY]
see_also: [HUB-OBSERVABILITY_STACK, HUB-API_GATEWAY]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → api_gateway

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `observability_stack` depends on `api_gateway`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
