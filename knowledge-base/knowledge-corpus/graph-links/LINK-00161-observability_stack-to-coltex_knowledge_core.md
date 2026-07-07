---
id: LINK-00161
title: "Graph Link: observability_stack ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, coltex_knowledge_core]
related: [HUB-OBSERVABILITY_STACK, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → coltex_knowledge_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `observability_stack` is related to `coltex_knowledge_core`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
