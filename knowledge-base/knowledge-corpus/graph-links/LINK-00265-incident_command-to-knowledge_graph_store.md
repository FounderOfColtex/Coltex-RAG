---
id: LINK-00265
title: "Graph Link: incident_command ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, knowledge_graph_store]
related: [HUB-INCIDENT_COMMAND, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-INCIDENT_COMMAND, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → knowledge_graph_store

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `incident_command` documents `knowledge_graph_store`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
