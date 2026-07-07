---
id: ROUTE-0503
title: "Domain Route: automation → observability (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: automation
cluster_target: observability
route_type: associative
tags: [domain-route, associative, automation, observability]
related: [CLUSTER-AUTOMATION, CLUSTER-OBSERVABILITY]
see_also: [CLUSTER-AUTOMATION, CLUSTER-OBSERVABILITY]
synthesizes: [CLUSTER-AUTOMATION]
---

# Domain Route: automation → observability

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `automation` connect to cluster `observability` via this cross-cluster route.

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
- Target: `CLUSTER-OBSERVABILITY` (observability)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
