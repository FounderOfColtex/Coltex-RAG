---
id: ROUTE-0305
title: "Domain Route: observability → automation (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: observability
cluster_target: automation
route_type: associative
tags: [domain-route, associative, observability, automation]
related: [CLUSTER-OBSERVABILITY, CLUSTER-AUTOMATION]
see_also: [CLUSTER-OBSERVABILITY, CLUSTER-AUTOMATION]
synthesizes: [CLUSTER-OBSERVABILITY]
---

# Domain Route: observability → automation

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `observability` connect to cluster `automation` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-OBSERVABILITY` (observability)
- Target: `CLUSTER-AUTOMATION` (automation)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
