---
id: ROUTE-0704
title: "Domain Route: retention → security (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retention
cluster_target: security
route_type: inhibitory
tags: [domain-route, inhibitory, retention, security]
related: [CLUSTER-RETENTION, CLUSTER-SECURITY]
see_also: [CLUSTER-RETENTION, CLUSTER-SECURITY]
synthesizes: [CLUSTER-RETENTION]
---

# Domain Route: retention → security

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `retention` connect to cluster `security` via this cross-cluster route.

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
- Target: `CLUSTER-SECURITY` (security)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
