---
id: ROUTE-0409
title: "Domain Route: security → priority (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: security
cluster_target: priority
route_type: associative
tags: [domain-route, associative, security, priority]
related: [CLUSTER-SECURITY, CLUSTER-PRIORITY]
see_also: [CLUSTER-SECURITY, CLUSTER-PRIORITY]
synthesizes: [CLUSTER-SECURITY]
---

# Domain Route: security → priority

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `security` connect to cluster `priority` via this cross-cluster route.

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
- Target: `CLUSTER-PRIORITY` (priority)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
