---
id: ROUTE-0801
title: "Domain Route: routing → retrieval (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: routing
cluster_target: retrieval
route_type: commissural
tags: [domain-route, commissural, routing, retrieval]
related: [CLUSTER-ROUTING, CLUSTER-RETRIEVAL]
see_also: [CLUSTER-ROUTING, CLUSTER-RETRIEVAL]
synthesizes: [CLUSTER-ROUTING]
---

# Domain Route: routing → retrieval

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `routing` connect to cluster `retrieval` via this cross-cluster route.

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
- Target: `CLUSTER-RETRIEVAL` (retrieval)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
