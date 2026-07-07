---
id: ROUTE-0800
title: "Domain Route: routing → architecture (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: routing
cluster_target: architecture
route_type: associative
tags: [domain-route, associative, routing, architecture]
related: [CLUSTER-ROUTING, CLUSTER-ARCHITECTURE]
see_also: [CLUSTER-ROUTING, CLUSTER-ARCHITECTURE]
synthesizes: [CLUSTER-ROUTING]
---

# Domain Route: routing → architecture

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `routing` connect to cluster `architecture` via this cross-cluster route.

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
- Target: `CLUSTER-ARCHITECTURE` (architecture)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
