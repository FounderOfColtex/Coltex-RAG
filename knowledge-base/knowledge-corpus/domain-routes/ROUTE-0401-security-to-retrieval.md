---
id: ROUTE-0401
title: "Domain Route: security → retrieval (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: security
cluster_target: retrieval
route_type: excitatory
tags: [domain-route, excitatory, security, retrieval]
related: [CLUSTER-SECURITY, CLUSTER-RETRIEVAL]
see_also: [CLUSTER-SECURITY, CLUSTER-RETRIEVAL]
synthesizes: [CLUSTER-SECURITY]
---

# Domain Route: security → retrieval

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `security` connect to cluster `retrieval` via this cross-cluster route.

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
- Target: `CLUSTER-RETRIEVAL` (retrieval)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
