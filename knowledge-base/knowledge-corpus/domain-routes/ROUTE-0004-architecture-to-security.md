---
id: ROUTE-0004
title: "Domain Route: architecture → security (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: architecture
cluster_target: security
route_type: commissural
tags: [domain-route, commissural, architecture, security]
related: [CLUSTER-ARCHITECTURE, CLUSTER-SECURITY]
see_also: [CLUSTER-ARCHITECTURE, CLUSTER-SECURITY]
synthesizes: [CLUSTER-ARCHITECTURE]
---

# Domain Route: architecture → security

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `architecture` connect to cluster `security` via this cross-cluster route.

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
- Target: `CLUSTER-SECURITY` (security)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
