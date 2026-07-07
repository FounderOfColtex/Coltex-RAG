---
id: LINK-00050
title: "Graph Link: graphrag_engine ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, graphrag_engine, incident_command]
related: [HUB-GRAPHRAG_ENGINE, HUB-INCIDENT_COMMAND]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Graph Link: graphrag_engine → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `graphrag_engine` depends on `incident_command`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
