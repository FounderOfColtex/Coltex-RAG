---
id: LINK-00257
title: "Graph Link: incident_command ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, vector_store_cluster]
related: [HUB-INCIDENT_COMMAND, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-INCIDENT_COMMAND, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → vector_store_cluster

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `incident_command` documents `vector_store_cluster`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
