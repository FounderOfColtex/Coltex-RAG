---
id: ROUTE-0306
title: "Domain Route: observability → operations (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: observability
cluster_target: operations
route_type: commissural
tags: [domain-route, commissural, observability, operations]
related: [CLUSTER-OBSERVABILITY, CLUSTER-OPERATIONS]
see_also: [CLUSTER-OBSERVABILITY, CLUSTER-OPERATIONS]
synthesizes: [CLUSTER-OBSERVABILITY]
---

# Domain Route: observability → operations

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `observability` connect to cluster `operations` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-OBSERVABILITY` (observability)
- Target: `CLUSTER-OPERATIONS` (operations)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
