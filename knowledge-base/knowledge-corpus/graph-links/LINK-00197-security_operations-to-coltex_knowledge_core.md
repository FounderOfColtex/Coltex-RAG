---
id: LINK-00197
title: "Graph Link: security_operations ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, security_operations, coltex_knowledge_core]
related: [HUB-SECURITY_OPERATIONS, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-SECURITY_OPERATIONS, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Graph Link: security_operations → coltex_knowledge_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `security_operations` documents `coltex_knowledge_core`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
