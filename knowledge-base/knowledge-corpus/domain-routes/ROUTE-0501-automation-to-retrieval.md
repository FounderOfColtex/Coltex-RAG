---
id: ROUTE-0501
title: "Domain Route: automation → retrieval (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: automation
cluster_target: retrieval
route_type: inhibitory
tags: [domain-route, inhibitory, automation, retrieval]
related: [CLUSTER-AUTOMATION, CLUSTER-RETRIEVAL]
see_also: [CLUSTER-AUTOMATION, CLUSTER-RETRIEVAL]
synthesizes: [CLUSTER-AUTOMATION]
---

# Domain Route: automation → retrieval

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `automation` connect to cluster `retrieval` via this cross-cluster route.

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
- Target: `CLUSTER-RETRIEVAL` (retrieval)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
