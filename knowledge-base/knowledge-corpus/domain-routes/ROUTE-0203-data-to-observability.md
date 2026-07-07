---
id: ROUTE-0203
title: "Domain Route: data → observability (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: data
cluster_target: observability
route_type: excitatory
tags: [domain-route, excitatory, data, observability]
related: [CLUSTER-DATA, CLUSTER-OBSERVABILITY]
see_also: [CLUSTER-DATA, CLUSTER-OBSERVABILITY]
synthesizes: [CLUSTER-DATA]
---

# Domain Route: data → observability

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `data` connect to cluster `observability` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-DATA` (data)
- Target: `CLUSTER-OBSERVABILITY` (observability)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
