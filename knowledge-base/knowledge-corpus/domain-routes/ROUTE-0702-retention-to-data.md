---
id: ROUTE-0702
title: "Domain Route: retention → data (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retention
cluster_target: data
route_type: commissural
tags: [domain-route, commissural, retention, data]
related: [CLUSTER-RETENTION, CLUSTER-DATA]
see_also: [CLUSTER-RETENTION, CLUSTER-DATA]
synthesizes: [CLUSTER-RETENTION]
---

# Domain Route: retention → data

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `retention` connect to cluster `data` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-RETENTION` (retention)
- Target: `CLUSTER-DATA` (data)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
