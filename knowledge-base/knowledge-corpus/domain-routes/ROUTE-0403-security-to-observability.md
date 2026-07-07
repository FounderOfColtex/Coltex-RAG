---
id: ROUTE-0403
title: "Domain Route: security → observability (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: security
cluster_target: observability
route_type: modulatory
tags: [domain-route, modulatory, security, observability]
related: [CLUSTER-SECURITY, CLUSTER-OBSERVABILITY]
see_also: [CLUSTER-SECURITY, CLUSTER-OBSERVABILITY]
synthesizes: [CLUSTER-SECURITY]
---

# Domain Route: security → observability

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `security` connect to cluster `observability` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-SECURITY` (security)
- Target: `CLUSTER-OBSERVABILITY` (observability)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
