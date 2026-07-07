---
id: ROUTE-0700
title: "Domain Route: retention → architecture (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retention
cluster_target: architecture
route_type: modulatory
tags: [domain-route, modulatory, retention, architecture]
related: [CLUSTER-RETENTION, CLUSTER-ARCHITECTURE]
see_also: [CLUSTER-RETENTION, CLUSTER-ARCHITECTURE]
synthesizes: [CLUSTER-RETENTION]
---

# Domain Route: retention → architecture

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `retention` connect to cluster `architecture` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-RETENTION` (retention)
- Target: `CLUSTER-ARCHITECTURE` (architecture)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
