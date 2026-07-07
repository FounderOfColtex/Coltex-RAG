---
id: HUB-KNOWLEDGE_GRAPH_STORE
title: "Knowledge Cluster: Knowledge Graph Store"
doc_type: architecture_decision
category: graphrag
hub: knowledge_graph_store
cluster: routing
tags: [hub, knowledge-cluster, knowledge_graph_store]
see_also: [ARCH-00001]
---

# Knowledge Graph Store

Central knowledge cluster for the Coltex corpus.

## Components
- Neo4j
- Edge Types
- PageRank
- Community Detection

## Cluster assignment
**routing** cluster · tier `association`

## Document types in this hub
deep_dive, architecture_decision, benchmark, code_walkthrough, evaluation

## GraphRAG
All documents with `hub: knowledge_graph_store` form a traversable cluster.
Graph links and domain routes connect this hub to other knowledge clusters.
