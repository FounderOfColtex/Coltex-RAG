---
id: ROUTE-0100
title: "Domain Route: retrieval → architecture (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: retrieval
cluster_target: architecture
route_type: inhibitory
tags: [domain-route, inhibitory, retrieval, architecture]
related: [CLUSTER-RETRIEVAL, CLUSTER-ARCHITECTURE]
see_also: [CLUSTER-RETRIEVAL, CLUSTER-ARCHITECTURE]
synthesizes: [CLUSTER-RETRIEVAL]
---

# Domain Route: retrieval → architecture

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `retrieval` connect to cluster `architecture` via this cross-cluster route.

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
- Target: `CLUSTER-ARCHITECTURE` (architecture)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
