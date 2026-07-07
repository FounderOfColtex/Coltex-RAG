---
id: ROUTE-0600
title: "Domain Route: operations → architecture (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: operations
cluster_target: architecture
route_type: inhibitory
tags: [domain-route, inhibitory, operations, architecture]
related: [CLUSTER-OPERATIONS, CLUSTER-ARCHITECTURE]
see_also: [CLUSTER-OPERATIONS, CLUSTER-ARCHITECTURE]
synthesizes: [CLUSTER-OPERATIONS]
---

# Domain Route: operations → architecture

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `operations` connect to cluster `architecture` via this cross-cluster route.

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
- Target: `CLUSTER-ARCHITECTURE` (architecture)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
