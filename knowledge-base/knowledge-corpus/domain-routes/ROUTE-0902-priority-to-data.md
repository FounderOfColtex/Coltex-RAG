---
id: ROUTE-0902
title: "Domain Route: priority → data (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: priority
cluster_target: data
route_type: inhibitory
tags: [domain-route, inhibitory, priority, data]
related: [CLUSTER-PRIORITY, CLUSTER-DATA]
see_also: [CLUSTER-PRIORITY, CLUSTER-DATA]
synthesizes: [CLUSTER-PRIORITY]
---

# Domain Route: priority → data

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `priority` connect to cluster `data` via this cross-cluster route.

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
- Target: `CLUSTER-DATA` (data)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
