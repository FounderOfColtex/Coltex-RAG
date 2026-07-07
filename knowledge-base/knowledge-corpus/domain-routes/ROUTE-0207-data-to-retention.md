---
id: ROUTE-0207
title: "Domain Route: data → retention (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: data
cluster_target: retention
route_type: commissural
tags: [domain-route, commissural, data, retention]
related: [CLUSTER-DATA, CLUSTER-RETENTION]
see_also: [CLUSTER-DATA, CLUSTER-RETENTION]
synthesizes: [CLUSTER-DATA]
---

# Domain Route: data → retention

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `data` connect to cluster `retention` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-DATA` (data)
- Target: `CLUSTER-RETENTION` (retention)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
