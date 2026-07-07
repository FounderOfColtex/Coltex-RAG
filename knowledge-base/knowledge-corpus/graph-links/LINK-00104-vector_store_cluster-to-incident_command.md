---
id: LINK-00104
title: "Graph Link: vector_store_cluster ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, vector_store_cluster, incident_command]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-INCIDENT_COMMAND]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-INCIDENT_COMMAND]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Graph Link: vector_store_cluster → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `vector_store_cluster` documents `incident_command`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
