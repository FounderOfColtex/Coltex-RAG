---
id: ROUTE-0708
title: "Domain Route: retention → routing (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retention
cluster_target: routing
route_type: excitatory
tags: [domain-route, excitatory, retention, routing]
related: [CLUSTER-RETENTION, CLUSTER-ROUTING]
see_also: [CLUSTER-RETENTION, CLUSTER-ROUTING]
synthesizes: [CLUSTER-RETENTION]
---

# Domain Route: retention → routing

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `retention` connect to cluster `routing` via this cross-cluster route.

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
- Target: `CLUSTER-ROUTING` (routing)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
