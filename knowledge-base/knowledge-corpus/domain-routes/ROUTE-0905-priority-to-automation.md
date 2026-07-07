---
id: ROUTE-0905
title: "Domain Route: priority → automation (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: priority
cluster_target: automation
route_type: commissural
tags: [domain-route, commissural, priority, automation]
related: [CLUSTER-PRIORITY, CLUSTER-AUTOMATION]
see_also: [CLUSTER-PRIORITY, CLUSTER-AUTOMATION]
synthesizes: [CLUSTER-PRIORITY]
---

# Domain Route: priority → automation

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `priority` connect to cluster `automation` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-PRIORITY` (priority)
- Target: `CLUSTER-AUTOMATION` (automation)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
