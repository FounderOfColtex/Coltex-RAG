---
id: ROUTE-0706
title: "Domain Route: retention → operations (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retention
cluster_target: operations
route_type: associative
tags: [domain-route, associative, retention, operations]
related: [CLUSTER-RETENTION, CLUSTER-OPERATIONS]
see_also: [CLUSTER-RETENTION, CLUSTER-OPERATIONS]
synthesizes: [CLUSTER-RETENTION]
---

# Domain Route: retention → operations

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `retention` connect to cluster `operations` via this cross-cluster route.

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
- Target: `CLUSTER-OPERATIONS` (operations)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
