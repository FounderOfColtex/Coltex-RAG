---
id: ROUTE-0204
title: "Domain Route: data → security (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: data
cluster_target: security
route_type: inhibitory
tags: [domain-route, inhibitory, data, security]
related: [CLUSTER-DATA, CLUSTER-SECURITY]
see_also: [CLUSTER-DATA, CLUSTER-SECURITY]
synthesizes: [CLUSTER-DATA]
---

# Domain Route: data → security

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `data` connect to cluster `security` via this cross-cluster route.

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
- Target: `CLUSTER-SECURITY` (security)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
