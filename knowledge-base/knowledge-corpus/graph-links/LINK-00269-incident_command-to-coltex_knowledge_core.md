---
id: LINK-00269
title: "Graph Link: incident_command ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, coltex_knowledge_core]
related: [HUB-INCIDENT_COMMAND, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-INCIDENT_COMMAND, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → coltex_knowledge_core

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `incident_command` documents `coltex_knowledge_core`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
