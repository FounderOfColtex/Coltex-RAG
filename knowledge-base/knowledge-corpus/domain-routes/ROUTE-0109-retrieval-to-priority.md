---
id: ROUTE-0109
title: "Domain Route: retrieval → priority (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retrieval
cluster_target: priority
route_type: excitatory
tags: [domain-route, excitatory, retrieval, priority]
related: [CLUSTER-RETRIEVAL, CLUSTER-PRIORITY]
see_also: [CLUSTER-RETRIEVAL, CLUSTER-PRIORITY]
synthesizes: [CLUSTER-RETRIEVAL]
---

# Domain Route: retrieval → priority

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `retrieval` connect to cluster `priority` via this cross-cluster route.

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
- Target: `CLUSTER-PRIORITY` (priority)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
