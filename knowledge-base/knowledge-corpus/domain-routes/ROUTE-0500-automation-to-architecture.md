---
id: ROUTE-0500
title: "Domain Route: automation → architecture (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: automation
cluster_target: architecture
route_type: excitatory
tags: [domain-route, excitatory, automation, architecture]
related: [CLUSTER-AUTOMATION, CLUSTER-ARCHITECTURE]
see_also: [CLUSTER-AUTOMATION, CLUSTER-ARCHITECTURE]
synthesizes: [CLUSTER-AUTOMATION]
---

# Domain Route: automation → architecture

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `automation` connect to cluster `architecture` via this cross-cluster route.

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
- Target: `CLUSTER-ARCHITECTURE` (architecture)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
