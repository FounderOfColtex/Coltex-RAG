---
id: ROUTE-0603
title: "Domain Route: operations → observability (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: operations
cluster_target: observability
route_type: commissural
tags: [domain-route, commissural, operations, observability]
related: [CLUSTER-OPERATIONS, CLUSTER-OBSERVABILITY]
see_also: [CLUSTER-OPERATIONS, CLUSTER-OBSERVABILITY]
synthesizes: [CLUSTER-OPERATIONS]
---

# Domain Route: operations → observability

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `operations` connect to cluster `observability` via this cross-cluster route.

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
- Target: `CLUSTER-OBSERVABILITY` (observability)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
