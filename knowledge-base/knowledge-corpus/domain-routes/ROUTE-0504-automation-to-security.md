---
id: ROUTE-0504
title: "Domain Route: automation → security (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: automation
cluster_target: security
route_type: commissural
tags: [domain-route, commissural, automation, security]
related: [CLUSTER-AUTOMATION, CLUSTER-SECURITY]
see_also: [CLUSTER-AUTOMATION, CLUSTER-SECURITY]
synthesizes: [CLUSTER-AUTOMATION]
---

# Domain Route: automation → security

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `automation` connect to cluster `security` via this cross-cluster route.

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
- Target: `CLUSTER-SECURITY` (security)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
