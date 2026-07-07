---
id: ROUTE-0605
title: "Domain Route: operations → automation (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: operations
cluster_target: automation
route_type: inhibitory
tags: [domain-route, inhibitory, operations, automation]
related: [CLUSTER-OPERATIONS, CLUSTER-AUTOMATION]
see_also: [CLUSTER-OPERATIONS, CLUSTER-AUTOMATION]
synthesizes: [CLUSTER-OPERATIONS]
---

# Domain Route: operations → automation

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `operations` connect to cluster `automation` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-OPERATIONS` (operations)
- Target: `CLUSTER-AUTOMATION` (automation)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
