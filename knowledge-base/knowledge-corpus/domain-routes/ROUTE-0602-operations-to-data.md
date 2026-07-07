---
id: ROUTE-0602
title: "Domain Route: operations → data (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: operations
cluster_target: data
route_type: associative
tags: [domain-route, associative, operations, data]
related: [CLUSTER-OPERATIONS, CLUSTER-DATA]
see_also: [CLUSTER-OPERATIONS, CLUSTER-DATA]
synthesizes: [CLUSTER-OPERATIONS]
---

# Domain Route: operations → data

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `operations` connect to cluster `data` via this cross-cluster route.

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
- Target: `CLUSTER-DATA` (data)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
