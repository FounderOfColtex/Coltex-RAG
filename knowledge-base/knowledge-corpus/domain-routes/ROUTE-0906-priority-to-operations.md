---
id: ROUTE-0906
title: "Domain Route: priority → operations (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: priority
cluster_target: operations
route_type: excitatory
tags: [domain-route, excitatory, priority, operations]
related: [CLUSTER-PRIORITY, CLUSTER-OPERATIONS]
see_also: [CLUSTER-PRIORITY, CLUSTER-OPERATIONS]
synthesizes: [CLUSTER-PRIORITY]
---

# Domain Route: priority → operations

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `priority` connect to cluster `operations` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-PRIORITY` (priority)
- Target: `CLUSTER-OPERATIONS` (operations)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
