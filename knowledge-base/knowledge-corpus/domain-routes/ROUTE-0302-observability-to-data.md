---
id: ROUTE-0302
title: "Domain Route: observability → data (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: observability
cluster_target: data
route_type: excitatory
tags: [domain-route, excitatory, observability, data]
related: [CLUSTER-OBSERVABILITY, CLUSTER-DATA]
see_also: [CLUSTER-OBSERVABILITY, CLUSTER-DATA]
synthesizes: [CLUSTER-OBSERVABILITY]
---

# Domain Route: observability → data

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `observability` connect to cluster `data` via this cross-cluster route.

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
- Target: `CLUSTER-DATA` (data)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
