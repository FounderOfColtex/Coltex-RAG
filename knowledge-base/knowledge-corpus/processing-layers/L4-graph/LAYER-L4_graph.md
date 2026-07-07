---
id: LAYER-4
title: "Processing Layer L4_graph"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [processing-layer, L4_graph, knowledge_architecture]
---

# Processing Layer: L4_graph

**Role:** Multi-hop GraphRAG, graph-link traversal, ADR chains

## Processing latency target
80ms

## Path
`processing-layers/L4-graph`

## Integration
Layer L4_graph feeds forward into the next processing layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during graph routing.
