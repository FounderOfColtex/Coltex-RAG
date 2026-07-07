---
id: ROUTE-0907
title: "Domain Route: priority → retention (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: priority
cluster_target: retention
route_type: inhibitory
tags: [domain-route, inhibitory, priority, retention]
related: [CLUSTER-PRIORITY, CLUSTER-RETENTION]
see_also: [CLUSTER-PRIORITY, CLUSTER-RETENTION]
synthesizes: [CLUSTER-PRIORITY]
---

# Domain Route: priority → retention

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `priority` connect to cluster `retention` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-PRIORITY` (priority)
- Target: `CLUSTER-RETENTION` (retention)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
