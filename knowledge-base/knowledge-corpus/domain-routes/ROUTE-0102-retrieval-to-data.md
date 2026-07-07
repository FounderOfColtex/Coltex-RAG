---
id: ROUTE-0102
title: "Domain Route: retrieval → data (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retrieval
cluster_target: data
route_type: associative
tags: [domain-route, associative, retrieval, data]
related: [CLUSTER-RETRIEVAL, CLUSTER-DATA]
see_also: [CLUSTER-RETRIEVAL, CLUSTER-DATA]
synthesizes: [CLUSTER-RETRIEVAL]
---

# Domain Route: retrieval → data

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `retrieval` connect to cluster `data` via this cross-cluster route.

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
- Target: `CLUSTER-DATA` (data)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
