---
id: ROUTE-0904
title: "Domain Route: priority → security (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: priority
cluster_target: security
route_type: associative
tags: [domain-route, associative, priority, security]
related: [CLUSTER-PRIORITY, CLUSTER-SECURITY]
see_also: [CLUSTER-PRIORITY, CLUSTER-SECURITY]
synthesizes: [CLUSTER-PRIORITY]
---

# Domain Route: priority → security

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `priority` connect to cluster `security` via this cross-cluster route.

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
- Target: `CLUSTER-SECURITY` (security)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
