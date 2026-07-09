#!/usr/bin/env python3
"""Build sellable marketplace pack catalog from Mega RAG catalog + marketplace.yaml."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

from common import ROOT, iter_jsonl, load_product_config, resolve_path


def load_marketplace() -> dict:
    path = ROOT / "config" / "marketplace.yaml"
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build marketplace pack catalog")
    parser.add_argument("--config", type=Path, default=Path("config/product_mega.yaml"))
    args = parser.parse_args()

    cfg = load_product_config(args.config)
    market_cfg = cfg.get("marketplace", {})
    if not market_cfg.get("enabled", True):
        print("Marketplace disabled in product config — skipping.")
        return

    marketplace = load_marketplace()
    packs_def = marketplace.get("packs", [])
    catalog_path = resolve_path(cfg["output"].get("catalog", "data/product/catalog.jsonl"))
    out_path = resolve_path(
        cfg["output"].get("marketplace_catalog", "data/product/marketplace/packs.json")
    )

    category_counts: Counter[str] = Counter()
    if catalog_path.exists():
        for rec in iter_jsonl(catalog_path):
            cat = rec.get("category") or "unknown"
            category_counts[cat] += 1

    pack_docs: dict[str, int] = {}
    pack_categories: dict[str, list[str]] = {}
    for pack in packs_def:
        cats = list(pack.get("categories", []))
        pack_categories[pack["id"]] = cats
        pack_docs[pack["id"]] = sum(category_counts.get(c, 0) for c in cats)

    # For capped smoke builds, estimate sellable capacity from generation stats
    gen_stats_path = resolve_path(cfg["output"].get("generation_stats", "data/product/generation_stats.json"))
    estimated_total = 0
    if gen_stats_path.exists():
        gen_stats = json.loads(gen_stats_path.read_text(encoding="utf-8"))
        estimated_total = int(gen_stats.get("estimated_total_documents") or 0)

    total_catalog = sum(category_counts.values())
    sellable_packs = []
    for pack in packs_def:
        pid = pack["id"]
        docs_in_build = pack_docs.get(pid, 0)
        # Proportionally project to full Mega scale when estimate is available
        projected = docs_in_build
        if estimated_total and total_catalog:
            projected = int(estimated_total * (docs_in_build / total_catalog))
        sellable_packs.append({
            "id": pid,
            "label": pack.get("label"),
            "price_usd": pack.get("price_usd"),
            "description": pack.get("description"),
            "categories": pack_categories[pid],
            "documents_in_build": docs_in_build,
            "projected_documents_at_mega_scale": projected,
            "sellable": projected >= int(market_cfg.get("min_pack_documents", marketplace.get("publishing", {}).get("min_documents_per_pack", 1000))),
        })

    payload = {
        "product": cfg.get("name", "Coltex Mega RAG"),
        "sku": cfg.get("sku", "MEGA-100M"),
        "version": cfg.get("version", "5.0.0"),
        "built_at": datetime.now(timezone.utc).isoformat(),
        "scale_target": marketplace.get("scale_target", 100_000_000),
        "catalog_documents": total_catalog,
        "estimated_total_documents": estimated_total,
        "meets_100m_floor": estimated_total >= 100_000_000,
        "category_counts": dict(category_counts),
        "packs": sellable_packs,
        "sku_bundles": marketplace.get("sku_bundles", {}),
        "license": cfg.get("license", "EULA"),
        "eula": "EULA.md",
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps({
        "marketplace_catalog": str(out_path),
        "packs": len(sellable_packs),
        "catalog_documents": total_catalog,
        "estimated_total_documents": estimated_total,
        "meets_100m_floor": payload["meets_100m_floor"],
    }, indent=2))


if __name__ == "__main__":
    main()
