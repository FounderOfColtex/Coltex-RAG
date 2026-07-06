from __future__ import annotations

from collections import deque

from zypher.knowledge_base import Document, KnowledgeBase


class GraphRAG:
    """Expand vector hits with multi-hop typed graph traversal."""

    def __init__(self, kb: KnowledgeBase, max_hops: int = 2, max_extra_chunks: int = 8):
        self.kb = kb
        self.max_hops = max_hops
        self.max_extra_chunks = max_extra_chunks

    def expand(
        self,
        seed_docs: list[Document],
        edge_types: list[str] | None = None,
    ) -> list[Document]:
        seen = {d.doc_id for d in seed_docs}
        merged = list(seed_docs)
        queue: deque[tuple[Document, int]] = deque((doc, 0) for doc in seed_docs)

        while queue and len(merged) < len(seed_docs) + self.max_extra_chunks:
            current, depth = queue.popleft()
            if depth >= self.max_hops:
                continue
            for related in self.kb.get_related(
                current,
                max_chunks=self.max_extra_chunks,
                edge_types=edge_types,
            ):
                if related.doc_id not in seen:
                    seen.add(related.doc_id)
                    merged.append(related)
                    queue.append((related, depth + 1))
                if len(merged) >= len(seed_docs) + self.max_extra_chunks:
                    break
        return merged

    def retrieve(self, vector_store, query: str, top_k: int = 6) -> list[Document]:
        seeds = vector_store.search(query, top_k=top_k)
        return self.expand(seeds)
