---
id: ROUTE-0701
title: "Domain Route: retention → retrieval (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retention
cluster_target: retrieval
route_type: associative
tags: [domain-route, associative, retention, retrieval]
related: [CLUSTER-RETENTION, CLUSTER-RETRIEVAL]
see_also: [CLUSTER-RETENTION, CLUSTER-RETRIEVAL]
synthesizes: [CLUSTER-RETENTION]
---

# Domain Route: retention → retrieval

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `retention` connect to cluster `retrieval` via this cross-cluster route.

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
- Target: `CLUSTER-RETRIEVAL` (retrieval)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
