---
id: ROUTE-0802
title: "Domain Route: routing → data (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: routing
cluster_target: data
route_type: excitatory
tags: [domain-route, excitatory, routing, data]
related: [CLUSTER-ROUTING, CLUSTER-DATA]
see_also: [CLUSTER-ROUTING, CLUSTER-DATA]
synthesizes: [CLUSTER-ROUTING]
---

# Domain Route: routing → data

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `routing` connect to cluster `data` via this cross-cluster route.

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
- Target: `CLUSTER-DATA` (data)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
