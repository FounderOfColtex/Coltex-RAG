---
id: ROUTE-0308
title: "Domain Route: observability → routing (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: observability
cluster_target: routing
route_type: inhibitory
tags: [domain-route, inhibitory, observability, routing]
related: [CLUSTER-OBSERVABILITY, CLUSTER-ROUTING]
see_also: [CLUSTER-OBSERVABILITY, CLUSTER-ROUTING]
synthesizes: [CLUSTER-OBSERVABILITY]
---

# Domain Route: observability → routing

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `observability` connect to cluster `routing` via this cross-cluster route.

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
- Target: `CLUSTER-ROUTING` (routing)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
