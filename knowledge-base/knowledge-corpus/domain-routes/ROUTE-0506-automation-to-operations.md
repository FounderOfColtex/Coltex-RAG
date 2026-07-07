---
id: ROUTE-0506
title: "Domain Route: automation → operations (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: automation
cluster_target: operations
route_type: inhibitory
tags: [domain-route, inhibitory, automation, operations]
related: [CLUSTER-AUTOMATION, CLUSTER-OPERATIONS]
see_also: [CLUSTER-AUTOMATION, CLUSTER-OPERATIONS]
synthesizes: [CLUSTER-AUTOMATION]
---

# Domain Route: automation → operations

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `automation` connect to cluster `operations` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-AUTOMATION` (automation)
- Target: `CLUSTER-OPERATIONS` (operations)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
