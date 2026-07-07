---
id: LINK-00154
title: "Graph Link: observability_stack ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, security_operations]
related: [HUB-OBSERVABILITY_STACK, HUB-SECURITY_OPERATIONS]
see_also: [HUB-OBSERVABILITY_STACK, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `observability_stack` calls into `security_operations`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
