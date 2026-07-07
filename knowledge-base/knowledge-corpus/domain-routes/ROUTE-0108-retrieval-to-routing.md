---
id: ROUTE-0108
title: "Domain Route: retrieval → routing (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retrieval
cluster_target: routing
route_type: commissural
tags: [domain-route, commissural, retrieval, routing]
related: [CLUSTER-RETRIEVAL, CLUSTER-ROUTING]
see_also: [CLUSTER-RETRIEVAL, CLUSTER-ROUTING]
synthesizes: [CLUSTER-RETRIEVAL]
---

# Domain Route: retrieval → routing

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `retrieval` connect to cluster `routing` via this cross-cluster route.

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
- Target: `CLUSTER-ROUTING` (routing)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
