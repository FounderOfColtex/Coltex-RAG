---
id: LINK-00158
title: "Graph Link: observability_stack ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, observability_stack, incident_command]
related: [HUB-OBSERVABILITY_STACK, HUB-INCIDENT_COMMAND]
see_also: [HUB-OBSERVABILITY_STACK, HUB-INCIDENT_COMMAND]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Graph Link: observability_stack → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**calls** — documents in `observability_stack` calls into `incident_command`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
