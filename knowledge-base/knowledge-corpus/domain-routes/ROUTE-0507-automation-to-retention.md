---
id: ROUTE-0507
title: "Domain Route: automation → retention (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: automation
cluster_target: retention
route_type: modulatory
tags: [domain-route, modulatory, automation, retention]
related: [CLUSTER-AUTOMATION, CLUSTER-RETENTION]
see_also: [CLUSTER-AUTOMATION, CLUSTER-RETENTION]
synthesizes: [CLUSTER-AUTOMATION]
---

# Domain Route: automation → retention

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `automation` connect to cluster `retention` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-AUTOMATION` (automation)
- Target: `CLUSTER-RETENTION` (retention)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
