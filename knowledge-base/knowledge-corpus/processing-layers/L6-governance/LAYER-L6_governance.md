---
id: LAYER-6
title: "Processing Layer L6_governance"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [processing-layer, L6_governance, knowledge_architecture]
---

# Processing Layer: L6_governance

**Role:** Corpus identity, architecture docs, catalog orchestration

## Processing latency target
200ms

## Path
`processing-layers/L6-governance`

## Integration
Layer L6_governance feeds forward into the next processing layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during graph routing.
