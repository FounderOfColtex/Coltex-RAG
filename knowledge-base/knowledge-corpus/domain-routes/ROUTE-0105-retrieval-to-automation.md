---
id: ROUTE-0105
title: "Domain Route: retrieval → automation (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retrieval
cluster_target: automation
route_type: inhibitory
tags: [domain-route, inhibitory, retrieval, automation]
related: [CLUSTER-RETRIEVAL, CLUSTER-AUTOMATION]
see_also: [CLUSTER-RETRIEVAL, CLUSTER-AUTOMATION]
synthesizes: [CLUSTER-RETRIEVAL]
---

# Domain Route: retrieval → automation

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `retrieval` connect to cluster `automation` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-RETRIEVAL` (retrieval)
- Target: `CLUSTER-AUTOMATION` (automation)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
