---
id: ROUTE-0609
title: "Domain Route: operations → priority (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: operations
cluster_target: priority
route_type: excitatory
tags: [domain-route, excitatory, operations, priority]
related: [CLUSTER-OPERATIONS, CLUSTER-PRIORITY]
see_also: [CLUSTER-OPERATIONS, CLUSTER-PRIORITY]
synthesizes: [CLUSTER-OPERATIONS]
---

# Domain Route: operations → priority

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `operations` connect to cluster `priority` via this cross-cluster route.

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
- Target: `CLUSTER-PRIORITY` (priority)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
