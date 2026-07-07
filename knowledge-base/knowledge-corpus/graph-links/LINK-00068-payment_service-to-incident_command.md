---
id: LINK-00068
title: "Graph Link: payment_service ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, payment_service, incident_command]
related: [HUB-PAYMENT_SERVICE, HUB-INCIDENT_COMMAND]
see_also: [HUB-PAYMENT_SERVICE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Graph Link: payment_service → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**see_also** — documents in `payment_service` is related to `incident_command`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
