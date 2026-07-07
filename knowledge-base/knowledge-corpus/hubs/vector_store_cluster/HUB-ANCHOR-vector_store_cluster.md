---
id: HUB-VECTOR_STORE_CLUSTER
title: "Knowledge Cluster: Vector Store Cluster"
doc_type: architecture_decision
category: vector_stores
hub: vector_store_cluster
cluster: data
tags: [hub, knowledge-cluster, vector_store_cluster]
see_also: [ARCH-00001]
---

# Vector Store Cluster

Central knowledge cluster for the Coltex corpus.

## Components
- ChromaDB
- HNSW
- pgvector
- Sharding
- Replication

## Cluster assignment
**data** cluster · tier `association`

## Document types in this hub
architecture_decision, benchmark, runbook, api_reference, deep_dive, troubleshooting

## GraphRAG
All documents with `hub: vector_store_cluster` form a traversable cluster.
Graph links and domain routes connect this hub to other knowledge clusters.
