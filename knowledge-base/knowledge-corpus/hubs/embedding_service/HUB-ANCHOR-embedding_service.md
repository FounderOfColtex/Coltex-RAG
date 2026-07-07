---
id: HUB-EMBEDDING_SERVICE
title: "Knowledge Cluster: Embedding Service"
doc_type: architecture_decision
category: embeddings
hub: embedding_service
cluster: retrieval
tags: [hub, knowledge-cluster, embedding_service]
see_also: [ARCH-00001]
---

# Embedding Service

Central knowledge cluster for the Coltex corpus.

## Components
- MiniLM
- Batch Encoding
- GPU Pipeline
- Model Registry

## Cluster assignment
**retrieval** cluster · tier `ingestion`

## Document types in this hub
api_reference, architecture_decision, benchmark, code_walkthrough, best_practices

## GraphRAG
All documents with `hub: embedding_service` form a traversable cluster.
Graph links and domain routes connect this hub to other knowledge clusters.
