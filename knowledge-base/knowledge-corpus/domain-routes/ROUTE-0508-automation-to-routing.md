---
id: ROUTE-0508
title: "Domain Route: automation → routing (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: automation
cluster_target: routing
route_type: associative
tags: [domain-route, associative, automation, routing]
related: [CLUSTER-AUTOMATION, CLUSTER-ROUTING]
see_also: [CLUSTER-AUTOMATION, CLUSTER-ROUTING]
synthesizes: [CLUSTER-AUTOMATION]
---

# Domain Route: automation → routing

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `automation` connect to cluster `routing` via this cross-cluster route.

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
- Target: `CLUSTER-ROUTING` (routing)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
