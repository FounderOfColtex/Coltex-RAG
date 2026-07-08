# Excluded from Product Build

These files are excluded from the default product build (`make product`).

## Why excluded

These documents are procedural placeholder stubs generated from templates.
They contain a single boilerplate paragraph and do not meet product quality standards.

Example marker:

> "This document provides detailed information on … as it relates to the
> Coltex Enterprise AI Coding Chatbot …"

## Subdirectories

| Directory | Contents | Count |
|-----------|----------|-------|
| `boilerplate-stubs/` | Single-paragraph placeholder "supporting documents" | 50 |
| `thin-stubs/` | Title-only incident reports and support tickets | 4 |

Release scripts and tarballs must exclude:

- `knowledge-base/_excluded_from_distribution/`
- `knowledge-base/generated/`
- `knowledge-base/_seed/`
