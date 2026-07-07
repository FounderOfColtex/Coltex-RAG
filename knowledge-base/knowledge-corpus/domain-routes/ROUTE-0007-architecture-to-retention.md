---
id: ROUTE-0007
title: "Domain Route: architecture → retention (modulatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: architecture
cluster_target: retention
route_type: modulatory
tags: [domain-route, modulatory, architecture, retention]
related: [CLUSTER-ARCHITECTURE, CLUSTER-RETENTION]
see_also: [CLUSTER-ARCHITECTURE, CLUSTER-RETENTION]
synthesizes: [CLUSTER-ARCHITECTURE]
---

# Domain Route: architecture → retention

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in cluster `architecture` connect to cluster `retention` via this cross-cluster route.

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
- Target: `CLUSTER-RETENTION` (retention)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
