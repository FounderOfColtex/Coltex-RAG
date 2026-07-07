---
id: ROUTE-0006
title: "Domain Route: architecture → operations (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: architecture
cluster_target: operations
route_type: inhibitory
tags: [domain-route, inhibitory, architecture, operations]
related: [CLUSTER-ARCHITECTURE, CLUSTER-OPERATIONS]
see_also: [CLUSTER-ARCHITECTURE, CLUSTER-OPERATIONS]
synthesizes: [CLUSTER-ARCHITECTURE]
---

# Domain Route: architecture → operations

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `architecture` connect to cluster `operations` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-ARCHITECTURE` (architecture)
- Target: `CLUSTER-OPERATIONS` (operations)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
