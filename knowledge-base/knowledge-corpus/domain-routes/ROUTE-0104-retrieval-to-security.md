---
id: ROUTE-0104
title: "Domain Route: retrieval → security (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retrieval
cluster_target: security
route_type: excitatory
tags: [domain-route, excitatory, retrieval, security]
related: [CLUSTER-RETRIEVAL, CLUSTER-SECURITY]
see_also: [CLUSTER-RETRIEVAL, CLUSTER-SECURITY]
synthesizes: [CLUSTER-RETRIEVAL]
---

# Domain Route: retrieval → security

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `retrieval` connect to cluster `security` via this cross-cluster route.

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
- Target: `CLUSTER-SECURITY` (security)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
