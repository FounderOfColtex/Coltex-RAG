---
id: LINK-00306
title: "Graph Link: coltex_knowledge_core ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, coltex_knowledge_core, auth_service]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-AUTH_SERVICE]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-AUTH_SERVICE]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Graph Link: coltex_knowledge_core → auth_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `coltex_knowledge_core` is related to `auth_service`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
