---
id: LAYER-5
title: "Processing Layer L5_assembly"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [processing-layer, L5_assembly, knowledge_architecture]
---

# Processing Layer: L5_assembly

**Role:** Context assembly, reranking, faithfulness checks

## Processing latency target
120ms

## Path
`processing-layers/L5-assembly`

## Integration
Layer L5_assembly feeds forward into the next processing layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during graph routing.
