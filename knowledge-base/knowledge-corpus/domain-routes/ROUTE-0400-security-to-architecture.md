---
id: ROUTE-0400
title: "Domain Route: security → architecture (commissural)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: security
cluster_target: architecture
route_type: commissural
tags: [domain-route, commissural, security, architecture]
related: [CLUSTER-SECURITY, CLUSTER-ARCHITECTURE]
see_also: [CLUSTER-SECURITY, CLUSTER-ARCHITECTURE]
synthesizes: [CLUSTER-SECURITY]
---

# Domain Route: security → architecture

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in cluster `security` connect to cluster `architecture` via this cross-cluster route.

## Traversal weight
| Route type | Graph boost |
|------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-cluster bridge |

## Anchors
- Source: `CLUSTER-SECURITY` (security)
- Target: `CLUSTER-ARCHITECTURE` (architecture)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
