---
id: LINK-00032
title: "Graph Link: indexing_pipeline ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [graph-link, graph, indexing_pipeline, incident_command]
related: [HUB-INDEXING_PIPELINE, HUB-INCIDENT_COMMAND]
see_also: [HUB-INDEXING_PIPELINE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Graph Link: indexing_pipeline → incident_command

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**documents** — documents in `indexing_pipeline` documents `incident_command`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this graph link for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
