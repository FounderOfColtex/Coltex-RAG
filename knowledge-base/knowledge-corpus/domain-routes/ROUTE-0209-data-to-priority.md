---
id: ROUTE-0209
title: "Domain Route: data → priority (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: data
cluster_target: priority
route_type: inhibitory
tags: [domain-route, inhibitory, data, priority]
related: [CLUSTER-DATA, CLUSTER-PRIORITY]
see_also: [CLUSTER-DATA, CLUSTER-PRIORITY]
synthesizes: [CLUSTER-DATA]
---

# Domain Route: data → priority

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `data` connect to cluster `priority` via this cross-cluster route.

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
- Target: `CLUSTER-PRIORITY` (priority)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
