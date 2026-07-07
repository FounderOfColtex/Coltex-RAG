---
id: ROUTE-0407
title: "Domain Route: security → retention (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: security
cluster_target: retention
route_type: inhibitory
tags: [domain-route, inhibitory, security, retention]
related: [CLUSTER-SECURITY, CLUSTER-RETENTION]
see_also: [CLUSTER-SECURITY, CLUSTER-RETENTION]
synthesizes: [CLUSTER-SECURITY]
---

# Domain Route: security → retention

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `security` connect to cluster `retention` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-SECURITY` (security)
- Target: `CLUSTER-RETENTION` (retention)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
