---
id: LINK-00194
title: "Graph Link: security_operations ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, security_operations, incident_command]
related: [HUB-SECURITY_OPERATIONS, HUB-INCIDENT_COMMAND]
see_also: [HUB-SECURITY_OPERATIONS, HUB-INCIDENT_COMMAND]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Graph Link: security_operations → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**depends_on** — documents in `security_operations` depends on `incident_command`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
