---
id: HUB-LLM_INFERENCE_GATEWAY
title: "Knowledge Cluster: LLM Inference Gateway"
doc_type: architecture_decision
category: rag
hub: llm_inference_gateway
cluster: retrieval
tags: [hub, knowledge-cluster, llm_inference_gateway]
see_also: [ARCH-00001]
---

# LLM Inference Gateway

Central knowledge cluster for the Coltex corpus.

## Components
- OpenAI API
- Streaming
- Rate Limiting
- Token Budget

## Cluster assignment
**retrieval** cluster · tier `executive`

## Document types in this hub
api_reference, architecture_decision, runbook, benchmark, troubleshooting

## GraphRAG
All documents with `hub: llm_inference_gateway` form a traversable cluster.
Graph links and domain routes connect this hub to other knowledge clusters.
