---
id: ROUTE-0005
title: "Domain Route: architecture → automation (excitatory)"
doc_type: domain_route
category: graphrag
hub: coltex_knowledge_core
cluster_source: architecture
cluster_target: automation
route_type: excitatory
tags: [domain-route, excitatory, architecture, automation]
related: [CLUSTER-ARCHITECTURE, CLUSTER-AUTOMATION]
see_also: [CLUSTER-ARCHITECTURE, CLUSTER-AUTOMATION]
synthesizes: [CLUSTER-ARCHITECTURE]
---

# Domain Route: architecture → automation

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in cluster `architecture` connect to cluster `automation` via this cross-cluster route.

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
- Target: `CLUSTER-AUTOMATION` (automation)

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/domain-routes/` during GraphRAG expansion.
