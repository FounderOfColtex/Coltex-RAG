---
id: ROUTE-0502
title: "Domain Route: automation → data (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: automation
cluster_target: data
route_type: modulatory
tags: [domain-route, modulatory, automation, data]
related: [CLUSTER-AUTOMATION, CLUSTER-DATA]
see_also: [CLUSTER-AUTOMATION, CLUSTER-DATA]
synthesizes: [CLUSTER-AUTOMATION]
---

# Domain Route: automation → data

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `automation` connect to cluster `data` via this cross-cluster route.

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
- Target: `CLUSTER-DATA` (data)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
