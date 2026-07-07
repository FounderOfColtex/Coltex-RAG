---
id: ROUTE-0509
title: "Domain Route: automation → priority (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: automation
cluster_target: priority
route_type: commissural
tags: [domain-route, commissural, automation, priority]
related: [CLUSTER-AUTOMATION, CLUSTER-PRIORITY]
see_also: [CLUSTER-AUTOMATION, CLUSTER-PRIORITY]
synthesizes: [CLUSTER-AUTOMATION]
---

# Domain Route: automation → priority

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `automation` connect to cluster `priority` via this cross-cluster route.

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
- Target: `CLUSTER-PRIORITY` (priority)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
