---
id: ROUTE-0805
title: "Domain Route: routing → automation (associative)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: routing
cluster_target: automation
route_type: associative
tags: [domain-route, associative, routing, automation]
related: [CLUSTER-ROUTING, CLUSTER-AUTOMATION]
see_also: [CLUSTER-ROUTING, CLUSTER-AUTOMATION]
synthesizes: [CLUSTER-ROUTING]
---

# Domain Route: routing → automation

**Type:** `associative` · **Tier:** association layer

## Route
Documents in cluster `routing` connect to cluster `automation` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-ROUTING` (routing)
- Target: `CLUSTER-AUTOMATION` (automation)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
