---
id: ROUTE-0709
title: "Domain Route: retention → priority (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retention
cluster_target: priority
route_type: inhibitory
tags: [domain-route, inhibitory, retention, priority]
related: [CLUSTER-RETENTION, CLUSTER-PRIORITY]
see_also: [CLUSTER-RETENTION, CLUSTER-PRIORITY]
synthesizes: [CLUSTER-RETENTION]
---

# Domain Route: retention → priority

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `retention` connect to cluster `priority` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-RETENTION` (retention)
- Target: `CLUSTER-PRIORITY` (priority)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
