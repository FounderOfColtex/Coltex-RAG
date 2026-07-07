---
id: ROUTE-0408
title: "Domain Route: security → routing (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: security
cluster_target: routing
route_type: modulatory
tags: [domain-route, modulatory, security, routing]
related: [CLUSTER-SECURITY, CLUSTER-ROUTING]
see_also: [CLUSTER-SECURITY, CLUSTER-ROUTING]
synthesizes: [CLUSTER-SECURITY]
---

# Domain Route: security → routing

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `security` connect to cluster `routing` via this cross-cluster route.

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
- Target: `CLUSTER-ROUTING` (routing)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
