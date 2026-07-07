---
id: ROUTE-0205
title: "Domain Route: data → automation (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: data
cluster_target: automation
route_type: modulatory
tags: [domain-route, modulatory, data, automation]
related: [CLUSTER-DATA, CLUSTER-AUTOMATION]
see_also: [CLUSTER-DATA, CLUSTER-AUTOMATION]
synthesizes: [CLUSTER-DATA]
---

# Domain Route: data → automation

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `data` connect to cluster `automation` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-DATA` (data)
- Target: `CLUSTER-AUTOMATION` (automation)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
