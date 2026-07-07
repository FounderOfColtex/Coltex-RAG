---
id: LAYER-2
title: "Processing Layer L2_metadata"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [processing-layer, L2_metadata, knowledge_architecture]
---

# Processing Layer: L2_metadata

**Role:** Domain tagging, metadata extraction, initial graph edges

## Processing latency target
15ms

## Path
`processing-layers/L2-metadata`

## Integration
Layer L2_metadata feeds forward into the next processing layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during graph routing.
