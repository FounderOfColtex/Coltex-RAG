---
id: ROUTE-0001
title: "Domain Route: architecture → retrieval (inhibitory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: architecture
cluster_target: retrieval
route_type: inhibitory
tags: [domain-route, inhibitory, architecture, retrieval]
related: [CLUSTER-ARCHITECTURE, CLUSTER-RETRIEVAL]
see_also: [CLUSTER-ARCHITECTURE, CLUSTER-RETRIEVAL]
synthesizes: [CLUSTER-ARCHITECTURE]
---

# Domain Route: architecture → retrieval

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in cluster `architecture` connect to cluster `retrieval` via this cross-cluster route.

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
- Target: `CLUSTER-RETRIEVAL` (retrieval)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
