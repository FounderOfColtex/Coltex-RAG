---
id: ROUTE-0405
title: "Domain Route: security → automation (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: security
cluster_target: automation
route_type: commissural
tags: [domain-route, commissural, security, automation]
related: [CLUSTER-SECURITY, CLUSTER-AUTOMATION]
see_also: [CLUSTER-SECURITY, CLUSTER-AUTOMATION]
synthesizes: [CLUSTER-SECURITY]
---

# Domain Route: security → automation

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `security` connect to cluster `automation` via this cross-cluster route.

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
- Target: `CLUSTER-AUTOMATION` (automation)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
