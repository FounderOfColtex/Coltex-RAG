---
id: ROUTE-0703
title: "Domain Route: retention → observability (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retention
cluster_target: observability
route_type: excitatory
tags: [domain-route, excitatory, retention, observability]
related: [CLUSTER-RETENTION, CLUSTER-OBSERVABILITY]
see_also: [CLUSTER-RETENTION, CLUSTER-OBSERVABILITY]
synthesizes: [CLUSTER-RETENTION]
---

# Domain Route: retention → observability

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `retention` connect to cluster `observability` via this cross-cluster route.

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
- Target: `CLUSTER-OBSERVABILITY` (observability)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
