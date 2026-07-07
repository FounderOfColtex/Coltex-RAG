---
id: ROUTE-0201
title: "Domain Route: data → retrieval (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: data
cluster_target: retrieval
route_type: associative
tags: [domain-route, associative, data, retrieval]
related: [CLUSTER-DATA, CLUSTER-RETRIEVAL]
see_also: [CLUSTER-DATA, CLUSTER-RETRIEVAL]
synthesizes: [CLUSTER-DATA]
---

# Domain Route: data → retrieval

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `data` connect to cluster `retrieval` via this cross-cluster route.

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
- Target: `CLUSTER-RETRIEVAL` (retrieval)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
