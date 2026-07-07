---
id: ROUTE-0607
title: "Domain Route: operations → retention (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: operations
cluster_target: retention
route_type: associative
tags: [domain-route, associative, operations, retention]
related: [CLUSTER-OPERATIONS, CLUSTER-RETENTION]
see_also: [CLUSTER-OPERATIONS, CLUSTER-RETENTION]
synthesizes: [CLUSTER-OPERATIONS]
---

# Domain Route: operations → retention

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `operations` connect to cluster `retention` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-OPERATIONS` (operations)
- Target: `CLUSTER-RETENTION` (retention)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
