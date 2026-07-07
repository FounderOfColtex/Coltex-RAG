---
id: ROUTE-0008
title: "Domain Route: architecture → routing (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: architecture
cluster_target: routing
route_type: associative
tags: [domain-route, associative, architecture, routing]
related: [CLUSTER-ARCHITECTURE, CLUSTER-ROUTING]
see_also: [CLUSTER-ARCHITECTURE, CLUSTER-ROUTING]
synthesizes: [CLUSTER-ARCHITECTURE]
---

# Domain Route: architecture → routing

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `architecture` connect to cluster `routing` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-ARCHITECTURE` (architecture)
- Target: `CLUSTER-ROUTING` (routing)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
