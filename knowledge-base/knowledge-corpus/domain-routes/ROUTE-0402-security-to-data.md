---
id: ROUTE-0402
title: "Domain Route: security → data (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: security
cluster_target: data
route_type: inhibitory
tags: [domain-route, inhibitory, security, data]
related: [CLUSTER-SECURITY, CLUSTER-DATA]
see_also: [CLUSTER-SECURITY, CLUSTER-DATA]
synthesizes: [CLUSTER-SECURITY]
---

# Domain Route: security → data

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `security` connect to cluster `data` via this cross-cluster route.

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
- Target: `CLUSTER-DATA` (data)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
