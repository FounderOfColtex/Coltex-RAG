---
id: LINK-00254
title: "Graph Link: incident_command ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, graphrag_engine]
related: [HUB-INCIDENT_COMMAND, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-INCIDENT_COMMAND, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → graphrag_engine

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `incident_command` depends on `graphrag_engine`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
