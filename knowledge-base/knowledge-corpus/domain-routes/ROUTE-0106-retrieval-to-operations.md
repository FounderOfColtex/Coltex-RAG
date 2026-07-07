---
id: ROUTE-0106
title: "Domain Route: retrieval → operations (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retrieval
cluster_target: operations
route_type: modulatory
tags: [domain-route, modulatory, retrieval, operations]
related: [CLUSTER-RETRIEVAL, CLUSTER-OPERATIONS]
see_also: [CLUSTER-RETRIEVAL, CLUSTER-OPERATIONS]
synthesizes: [CLUSTER-RETRIEVAL]
---

# Domain Route: retrieval → operations

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `retrieval` connect to cluster `operations` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-RETRIEVAL` (retrieval)
- Target: `CLUSTER-OPERATIONS` (operations)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
