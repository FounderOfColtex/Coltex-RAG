---
id: ROUTE-0908
title: "Domain Route: priority → routing (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: priority
cluster_target: routing
route_type: modulatory
tags: [domain-route, modulatory, priority, routing]
related: [CLUSTER-PRIORITY, CLUSTER-ROUTING]
see_also: [CLUSTER-PRIORITY, CLUSTER-ROUTING]
synthesizes: [CLUSTER-PRIORITY]
---

# Domain Route: priority → routing

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `priority` connect to cluster `routing` via this cross-cluster route.

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
- Target: `CLUSTER-ROUTING` (routing)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
