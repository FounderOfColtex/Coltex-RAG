---
id: ROUTE-0803
title: "Domain Route: routing → observability (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: routing
cluster_target: observability
route_type: inhibitory
tags: [domain-route, inhibitory, routing, observability]
related: [CLUSTER-ROUTING, CLUSTER-OBSERVABILITY]
see_also: [CLUSTER-ROUTING, CLUSTER-OBSERVABILITY]
synthesizes: [CLUSTER-ROUTING]
---

# Domain Route: routing → observability

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `routing` connect to cluster `observability` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-ROUTING` (routing)
- Target: `CLUSTER-OBSERVABILITY` (observability)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
