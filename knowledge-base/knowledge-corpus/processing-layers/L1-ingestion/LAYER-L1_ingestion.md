---
id: LAYER-1
title: "Processing Layer L1_ingestion"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [processing-layer, L1_ingestion, knowledge_architecture]
---

# Processing Layer: L1_ingestion

**Role:** Raw document ingestion, chunk boundaries, embedding triggers

## Processing latency target
5ms

## Path
`processing-layers/L1-ingestion`

## Integration
Layer L1_ingestion feeds forward into the next processing layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during graph routing.
