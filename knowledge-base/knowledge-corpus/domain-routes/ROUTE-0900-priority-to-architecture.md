---
id: ROUTE-0900
title: "Domain Route: priority → architecture (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: priority
cluster_target: architecture
route_type: commissural
tags: [domain-route, commissural, priority, architecture]
related: [CLUSTER-PRIORITY, CLUSTER-ARCHITECTURE]
see_also: [CLUSTER-PRIORITY, CLUSTER-ARCHITECTURE]
synthesizes: [CLUSTER-PRIORITY]
---

# Domain Route: priority → architecture

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `priority` connect to cluster `architecture` via this cross-cluster route.

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
- Target: `CLUSTER-ARCHITECTURE` (architecture)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
