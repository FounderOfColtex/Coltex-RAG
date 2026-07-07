---
id: ROUTE-0806
title: "Domain Route: routing → operations (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: routing
cluster_target: operations
route_type: commissural
tags: [domain-route, commissural, routing, operations]
related: [CLUSTER-ROUTING, CLUSTER-OPERATIONS]
see_also: [CLUSTER-ROUTING, CLUSTER-OPERATIONS]
synthesizes: [CLUSTER-ROUTING]
---

# Domain Route: routing → operations

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `routing` connect to cluster `operations` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-ROUTING` (routing)
- Target: `CLUSTER-OPERATIONS` (operations)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
