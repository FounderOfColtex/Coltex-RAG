# Coltex Mega RAG — Product Spec

**Tagline:** The largest commercial RAG corpus — 100,000,000+ sellable knowledge files.

**Goal:** Ship the most advanced, sellable RAG knowledge product: GraphRAG-native,
streaming-generated, audit-ready, and packaged as Personal → Professional → Enterprise → Mega SKUs.

---

## Primary build

```bash
make product-mega-smoke   # capped validation
make product-mega         # full 100M+ commercial build (cluster)
```

Config: `config/product_mega.yaml`

---

## Commercial docs

- [Product overview](../commercial/product-overview.md)
- [SKU matrix](../commercial/sku-matrix.md)
- [Datasheet](../commercial/datasheet.md)
- [EULA](../../EULA.md)

---

## Self-hosted Studio (bundled)

```bash
pip install -e .
coltex serve
coltex deploy
```

See [self-hosted deployment](../deployment/self-hosted.md)

---

## License

- Engine: MIT
- Commercial dataset: EULA + Mega license
