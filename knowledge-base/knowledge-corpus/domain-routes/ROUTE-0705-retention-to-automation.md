---
id: ROUTE-0705
title: "Domain Route: retention → automation (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retention
cluster_target: automation
route_type: modulatory
tags: [domain-route, modulatory, retention, automation]
related: [CLUSTER-RETENTION, CLUSTER-AUTOMATION]
see_also: [CLUSTER-RETENTION, CLUSTER-AUTOMATION]
synthesizes: [CLUSTER-RETENTION]
---

# Domain Route: retention → automation

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `retention` connect to cluster `automation` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-RETENTION` (retention)
- Target: `CLUSTER-AUTOMATION` (automation)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
