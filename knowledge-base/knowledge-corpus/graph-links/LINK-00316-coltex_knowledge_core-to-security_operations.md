---
id: LINK-00316
title: "Graph Link: coltex_knowledge_core ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, security_operations]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → security_operations

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `coltex_knowledge_core` documents `security_operations`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
