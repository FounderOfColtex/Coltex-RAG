---
id: LINK-00258
title: "Graph Link: incident_command ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, embedding_service]
related: [HUB-INCIDENT_COMMAND, HUB-EMBEDDING_SERVICE]
see_also: [HUB-INCIDENT_COMMAND, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → embedding_service

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `incident_command` depends on `embedding_service`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
