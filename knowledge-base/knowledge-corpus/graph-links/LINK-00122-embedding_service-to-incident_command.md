---
id: LINK-00122
title: "Graph Link: embedding_service ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, embedding_service, incident_command]
related: [HUB-EMBEDDING_SERVICE, HUB-INCIDENT_COMMAND]
see_also: [HUB-EMBEDDING_SERVICE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Graph Link: embedding_service → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `embedding_service` depends on `incident_command`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
