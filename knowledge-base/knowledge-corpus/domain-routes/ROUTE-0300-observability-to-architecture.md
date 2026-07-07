---
id: ROUTE-0300
title: "Domain Route: observability → architecture (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: observability
cluster_target: architecture
route_type: associative
tags: [domain-route, associative, observability, architecture]
related: [CLUSTER-OBSERVABILITY, CLUSTER-ARCHITECTURE]
see_also: [CLUSTER-OBSERVABILITY, CLUSTER-ARCHITECTURE]
synthesizes: [CLUSTER-OBSERVABILITY]
---

# Domain Route: observability → architecture

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `observability` connect to cluster `architecture` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-OBSERVABILITY` (observability)
- Target: `CLUSTER-ARCHITECTURE` (architecture)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
