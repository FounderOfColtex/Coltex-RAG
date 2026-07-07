---
id: LAYER-3
title: "Processing Layer L3_integration"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [processing-layer, L3_integration, knowledge_architecture]
---

# Processing Layer: L3_integration

**Role:** Cross-domain pattern matching, hub assignment

## Processing latency target
30ms

## Path
`processing-layers/L3-integration`

## Integration
Layer L3_integration feeds forward into the next processing layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during graph routing.
