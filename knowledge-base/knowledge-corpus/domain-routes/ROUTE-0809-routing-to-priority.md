---
id: ROUTE-0809
title: "Domain Route: routing → priority (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: routing
cluster_target: priority
route_type: modulatory
tags: [domain-route, modulatory, routing, priority]
related: [CLUSTER-ROUTING, CLUSTER-PRIORITY]
see_also: [CLUSTER-ROUTING, CLUSTER-PRIORITY]
synthesizes: [CLUSTER-ROUTING]
---

# Domain Route: routing → priority

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `routing` connect to cluster `priority` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-ROUTING` (routing)
- Target: `CLUSTER-PRIORITY` (priority)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
