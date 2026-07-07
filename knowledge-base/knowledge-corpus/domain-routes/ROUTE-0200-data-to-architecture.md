---
id: ROUTE-0200
title: "Domain Route: data → architecture (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: data
cluster_target: architecture
route_type: modulatory
tags: [domain-route, modulatory, data, architecture]
related: [CLUSTER-DATA, CLUSTER-ARCHITECTURE]
see_also: [CLUSTER-DATA, CLUSTER-ARCHITECTURE]
synthesizes: [CLUSTER-DATA]
---

# Domain Route: data → architecture

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `data` connect to cluster `architecture` via this cross-cluster route.

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
- Target: `CLUSTER-ARCHITECTURE` (architecture)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
