---
id: ROUTE-0009
title: "Domain Route: architecture → priority (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: architecture
cluster_target: priority
route_type: commissural
tags: [domain-route, commissural, architecture, priority]
related: [CLUSTER-ARCHITECTURE, CLUSTER-PRIORITY]
see_also: [CLUSTER-ARCHITECTURE, CLUSTER-PRIORITY]
synthesizes: [CLUSTER-ARCHITECTURE]
---

# Domain Route: architecture → priority

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `architecture` connect to cluster `priority` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-ARCHITECTURE` (architecture)
- Target: `CLUSTER-PRIORITY` (priority)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
