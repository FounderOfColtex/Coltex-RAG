---
id: ROUTE-0002
title: "Domain Route: architecture → data (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: architecture
cluster_target: data
route_type: modulatory
tags: [domain-route, modulatory, architecture, data]
related: [CLUSTER-ARCHITECTURE, CLUSTER-DATA]
see_also: [CLUSTER-ARCHITECTURE, CLUSTER-DATA]
synthesizes: [CLUSTER-ARCHITECTURE]
---

# Domain Route: architecture → data

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `architecture` connect to cluster `data` via this cross-cluster route.

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
- Target: `CLUSTER-DATA` (data)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
