---
id: ROUTE-0406
title: "Domain Route: security → operations (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: security
cluster_target: operations
route_type: excitatory
tags: [domain-route, excitatory, security, operations]
related: [CLUSTER-SECURITY, CLUSTER-OPERATIONS]
see_also: [CLUSTER-SECURITY, CLUSTER-OPERATIONS]
synthesizes: [CLUSTER-SECURITY]
---

# Domain Route: security → operations

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `security` connect to cluster `operations` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-SECURITY` (security)
- Target: `CLUSTER-OPERATIONS` (operations)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
