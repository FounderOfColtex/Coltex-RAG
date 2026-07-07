---
id: ROUTE-0604
title: "Domain Route: operations → security (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: operations
cluster_target: security
route_type: excitatory
tags: [domain-route, excitatory, operations, security]
related: [CLUSTER-OPERATIONS, CLUSTER-SECURITY]
see_also: [CLUSTER-OPERATIONS, CLUSTER-SECURITY]
synthesizes: [CLUSTER-OPERATIONS]
---

# Domain Route: operations → security

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `operations` connect to cluster `security` via this cross-cluster route.

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
- Target: `CLUSTER-SECURITY` (security)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
