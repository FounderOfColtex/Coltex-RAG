---
id: ROUTE-0901
title: "Domain Route: priority → retrieval (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: priority
cluster_target: retrieval
route_type: excitatory
tags: [domain-route, excitatory, priority, retrieval]
related: [CLUSTER-PRIORITY, CLUSTER-RETRIEVAL]
see_also: [CLUSTER-PRIORITY, CLUSTER-RETRIEVAL]
synthesizes: [CLUSTER-PRIORITY]
---

# Domain Route: priority → retrieval

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `priority` connect to cluster `retrieval` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-PRIORITY` (priority)
- Target: `CLUSTER-RETRIEVAL` (retrieval)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
