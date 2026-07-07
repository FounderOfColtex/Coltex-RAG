---
id: ROUTE-0307
title: "Domain Route: observability → retention (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: observability
cluster_target: retention
route_type: excitatory
tags: [domain-route, excitatory, observability, retention]
related: [CLUSTER-OBSERVABILITY, CLUSTER-RETENTION]
see_also: [CLUSTER-OBSERVABILITY, CLUSTER-RETENTION]
synthesizes: [CLUSTER-OBSERVABILITY]
---

# Domain Route: observability → retention

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `observability` connect to cluster `retention` via this cross-cluster route.

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
- Target: `CLUSTER-RETENTION` (retention)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
