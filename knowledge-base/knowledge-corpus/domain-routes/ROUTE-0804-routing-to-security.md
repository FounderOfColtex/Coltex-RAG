---
id: ROUTE-0804
title: "Domain Route: routing → security (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: routing
cluster_target: security
route_type: modulatory
tags: [domain-route, modulatory, routing, security]
related: [CLUSTER-ROUTING, CLUSTER-SECURITY]
see_also: [CLUSTER-ROUTING, CLUSTER-SECURITY]
synthesizes: [CLUSTER-ROUTING]
---

# Domain Route: routing → security

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `routing` connect to cluster `security` via this cross-cluster route.

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
- Target: `CLUSTER-SECURITY` (security)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
