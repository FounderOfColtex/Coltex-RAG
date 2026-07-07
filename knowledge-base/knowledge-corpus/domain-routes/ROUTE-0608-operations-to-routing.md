---
id: ROUTE-0608
title: "Domain Route: operations → routing (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: operations
cluster_target: routing
route_type: commissural
tags: [domain-route, commissural, operations, routing]
related: [CLUSTER-OPERATIONS, CLUSTER-ROUTING]
see_also: [CLUSTER-OPERATIONS, CLUSTER-ROUTING]
synthesizes: [CLUSTER-OPERATIONS]
---

# Domain Route: operations → routing

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `operations` connect to cluster `routing` via this cross-cluster route.

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
- Target: `CLUSTER-ROUTING` (routing)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
