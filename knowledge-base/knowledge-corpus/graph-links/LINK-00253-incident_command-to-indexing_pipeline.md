---
id: LINK-00253
title: "Graph Link: incident_command ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, incident_command, indexing_pipeline]
related: [HUB-INCIDENT_COMMAND, HUB-INDEXING_PIPELINE]
see_also: [HUB-INCIDENT_COMMAND, HUB-INDEXING_PIPELINE]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Graph Link: incident_command → indexing_pipeline

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `incident_command` documents `indexing_pipeline`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
