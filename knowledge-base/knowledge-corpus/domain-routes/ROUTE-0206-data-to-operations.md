---
id: ROUTE-0206
title: "Domain Route: data → operations (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: data
cluster_target: operations
route_type: associative
tags: [domain-route, associative, data, operations]
related: [CLUSTER-DATA, CLUSTER-OPERATIONS]
see_also: [CLUSTER-DATA, CLUSTER-OPERATIONS]
synthesizes: [CLUSTER-DATA]
---

# Domain Route: data → operations

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `data` connect to cluster `operations` via this cross-cluster route.

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
- Target: `CLUSTER-OPERATIONS` (operations)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
