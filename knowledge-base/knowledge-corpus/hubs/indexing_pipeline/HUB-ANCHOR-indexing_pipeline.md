---
id: HUB-INDEXING_PIPELINE
title: "Knowledge Cluster: Document Indexing Pipeline"
doc_type: architecture_decision
category: indexing
hub: indexing_pipeline
cluster: data
tags: [hub, knowledge-cluster, indexing_pipeline]
see_also: [ARCH-00001]
---

# Document Indexing Pipeline

Central knowledge cluster for the Coltex corpus.

## Components
- Embeddings
- Vector Store
- Chunking
- HNSW
- Kafka

## Cluster assignment
**data** cluster · tier `association`

## Document types in this hub
api_reference, runbook, architecture_decision, code_walkthrough, troubleshooting, benchmark, design_document

## GraphRAG
All documents with `hub: indexing_pipeline` form a traversable cluster.
Graph links and domain routes connect this hub to other knowledge clusters.
