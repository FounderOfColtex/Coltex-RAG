---
id: HUB-INCIDENT_COMMAND
title: "Knowledge Cluster: Incident Command System"
doc_type: architecture_decision
category: incidents
hub: incident_command
cluster: priority
tags: [hub, knowledge-cluster, incident_command]
see_also: [ARCH-00001]
---

# Incident Command System

Central knowledge cluster for the Coltex corpus.

## Components
- PagerDuty
- Postmortem
- SLA Tracking
- War Room

## Cluster assignment
**priority** cluster · tier `operations`

## Document types in this hub
runbook, incident_report, troubleshooting, best_practices, meeting_notes

## GraphRAG
All documents with `hub: incident_command` form a traversable cluster.
Graph links and domain routes connect this hub to other knowledge clusters.
