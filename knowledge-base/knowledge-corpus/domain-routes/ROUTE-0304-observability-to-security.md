---
id: ROUTE-0304
title: "Domain Route: observability → security (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: observability
cluster_target: security
route_type: modulatory
tags: [domain-route, modulatory, observability, security]
related: [CLUSTER-OBSERVABILITY, CLUSTER-SECURITY]
see_also: [CLUSTER-OBSERVABILITY, CLUSTER-SECURITY]
synthesizes: [CLUSTER-OBSERVABILITY]
---

# Domain Route: observability → security

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `observability` connect to cluster `security` via this cross-cluster route.

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
- Target: `CLUSTER-SECURITY` (security)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
