from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

RELATIONSHIP_FIELDS = (
    "related",
    "depends_on",
    "uses",
    "implements",
    "calls",
    "owned_by",
    "documents",
    "fixes",
    "replaces",
    "see_also",
)


@dataclass
class Document:
    doc_id: str
    title: str
    path: str
    content: str
    category: str = ""
    doc_type: str = ""
    hub: str = ""
    tags: list[str] | None = None
    related: list[str] | None = None
    relationships: dict[str, list[str]] = field(default_factory=dict)


def _parse_relationships(meta: dict) -> dict[str, list[str]]:
    rels: dict[str, list[str]] = {}
    for key in RELATIONSHIP_FIELDS:
        raw = meta.get(key)
        if raw:
            rels[key] = [str(r) for r in raw]
    return rels


def _merge_meta(outer: dict, inner: dict) -> dict:
    """Merge seed double-frontmatter: outer graph links + inner content metadata."""
    meta = {**outer, **inner}
    for key in RELATIONSHIP_FIELDS:
        outer_vals = outer.get(key) or []
        inner_vals = inner.get(key) or []
        combined = list(dict.fromkeys([str(v) for v in outer_vals + inner_vals]))
        if combined:
            meta[key] = combined
    if outer.get("title") and inner.get("title"):
        meta["title"] = inner["title"]
    if inner.get("tags"):
        meta["tags"] = inner["tags"]
    return meta


def _parse_md(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    meta: dict = {}
    body = text

    m = FRONTMATTER_RE.match(text)
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            meta = {}
        body = text[m.end() :].strip()
    elif text.count("---") >= 2:
        parts = text.split("---")
        outer: dict = {}
        inner: dict = {}
        if parts[0].strip():
            try:
                outer = yaml.safe_load(parts[0].strip()) or {}
            except yaml.YAMLError:
                outer = {}
        if len(parts) > 2 and parts[2].strip():
            try:
                inner = yaml.safe_load(parts[2].strip()) or {}
            except yaml.YAMLError:
                inner = {}
        meta = _merge_meta(outer, inner)
        body = "---".join(parts[3:]).strip() if len(parts) > 3 else ""

    relationships = _parse_relationships(meta)
    related = list(meta.get("related") or [])
    if not related:
        for key in ("see_also", "depends_on", "uses", "implements"):
            related.extend(relationships.get(key, []))
        related = list(dict.fromkeys(related))

    title = meta.get("title") or path.stem
    doc_id = str(meta.get("id", path.stem))

    return Document(
        doc_id=doc_id,
        title=str(title),
        path=str(path),
        content=body,
        category=str(meta.get("category", "")),
        doc_type=str(meta.get("doc_type", "")),
        hub=str(meta.get("hub", "")),
        tags=list(meta.get("tags") or []),
        related=related,
        relationships=relationships,
    )


    """Load and index markdown knowledge-base documents."""

    def __init__(self, paths: list[str], glob_pattern: str = "**/*.md", exclude: list[str] | None = None):
        self.documents: list[Document] = []
        self.by_id: dict[str, Document] = {}
        exclude = exclude or []
        for base in paths:
            root = Path(base)
            if not root.exists():
                continue
            for path in sorted(root.glob(glob_pattern)):
                if any(path.match(pat) for pat in exclude):
                    continue
                if not path.is_file():
                    continue
                doc = _parse_md(path)
                self.documents.append(doc)
                self.by_id[doc.doc_id] = doc
                if doc.doc_id.startswith("CHUNK-"):
                    parts = doc.doc_id.split("-")
                    if len(parts) >= 2:
                        self.by_id.setdefault(f"CHUNK-{parts[1]}", doc)

    def __len__(self) -> int:
        return len(self.documents)

    def get_related(
        self,
        doc: Document,
        max_chunks: int = 4,
        edge_types: list[str] | None = None,
    ) -> list[Document]:
        found: list[Document] = []
        seen: set[str] = {doc.doc_id}

        types = edge_types or list(RELATIONSHIP_FIELDS)
        for edge_type in types:
            for rel_id in doc.relationships.get(edge_type, []):
                if rel_id in self.by_id and rel_id not in seen:
                    found.append(self.by_id[rel_id])
                    seen.add(rel_id)
                if len(found) >= max_chunks:
                    return found

        for rel_id in doc.related or []:
            if rel_id in self.by_id and rel_id not in seen:
                found.append(self.by_id[rel_id])
                seen.add(rel_id)
            if len(found) >= max_chunks:
                break
        return found
