---
id: ROUTE-0107
title: "Domain Route: retrieval → retention (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retrieval
cluster_target: retention
route_type: associative
tags: [domain-route, associative, retrieval, retention]
related: [CLUSTER-RETRIEVAL, CLUSTER-RETENTION]
see_also: [CLUSTER-RETRIEVAL, CLUSTER-RETENTION]
synthesizes: [CLUSTER-RETRIEVAL]
---

# Domain Route: retrieval → retention

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `retrieval` connect to cluster `retention` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-RETRIEVAL` (retrieval)
- Target: `CLUSTER-RETENTION` (retention)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
