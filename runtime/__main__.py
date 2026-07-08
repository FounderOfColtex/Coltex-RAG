"""Coltex Runtime CLI."""

from __future__ import annotations

import argparse
import json


def _rt(config: str):
    from runtime.runtime import ColtexRuntime
    return ColtexRuntime(config_path=config)


def cmd_status(args: argparse.Namespace) -> None:
    print(json.dumps(_rt(args.config).status(), indent=2))


def cmd_health(args: argparse.Namespace) -> None:
    print(json.dumps(_rt(args.config).analytics.health(), indent=2))


def cmd_dashboard(args: argparse.Namespace) -> None:
    print(json.dumps(_rt(args.config).v1.snapshot(), indent=2))


def cmd_curator(args: argparse.Namespace) -> None:
    rt = _rt(args.config)
    result = rt.curator.proactive_scan(save=not args.no_save)
    print(json.dumps(result, indent=2))


def cmd_monitor(args: argparse.Namespace) -> None:
    print(json.dumps(_rt(args.config).monitor.snapshot(), indent=2))


def cmd_explain(args: argparse.Namespace) -> None:
    rt = _rt(args.config)
    rt.brain.index(force=False)
    print(json.dumps(rt.explain.explain(args.query), indent=2))


def cmd_ingest(args: argparse.Namespace) -> None:
    print(json.dumps(_rt(args.config).ingest(args.document_id, source=args.source), indent=2))


def cmd_search(args: argparse.Namespace) -> None:
    rt = _rt(args.config)
    print(json.dumps(rt.universal_search(args.query), indent=2))


def cmd_ask(args: argparse.Namespace) -> None:
    rt = _rt(args.config)
    print(json.dumps(rt.ask.ask(args.question), indent=2))


def cmd_upload(args: argparse.Namespace) -> None:
    print(json.dumps(_rt(args.config).upload_and_process(args.path), indent=2))


def cmd_sources(args: argparse.Namespace) -> None:
    rt = _rt(args.config)
    print(json.dumps({
        "sources": rt.sources.list_sources(),
        "count": rt.sources.count(),
        "supported": [".pdf", ".docx", ".md", ".txt", ".html", ".json"],
    }, indent=2))


def cmd_settings(args: argparse.Namespace) -> None:
    rt = _rt(args.config)
    if args.set:
        key, _, value = args.set.partition("=")
        if not key:
            print(json.dumps({"error": "use --set key=value"}, indent=2))
            return
        current = rt.settings.load()
        current[key.strip()] = value.strip()
        print(json.dumps(rt.settings.save(current), indent=2))
    else:
        print(json.dumps(rt.settings.load(), indent=2))


def cmd_events(args: argparse.Namespace) -> None:
    rt = _rt(args.config)
    if args.simulate:
        rt.ingest(args.document_id or "SIM-DOC-001", source="simulation")
    print(json.dumps({"events": rt.event_bus.recent, "stats": rt.event_bus.stats()}, indent=2))


def cmd_knowledge(args: argparse.Namespace) -> None:
    rt = _rt(args.config)
    if args.document_id:
        print(json.dumps(rt.knowledge_dna(args.document_id), indent=2))
    else:
        print(json.dumps(rt.studio.explorer(limit=args.limit), indent=2))


def cmd_connector(args: argparse.Namespace) -> None:
    print(json.dumps(_rt(args.config).sync_connector(args.connector_id), indent=2))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="coltex",
        description="Coltex V1 — local CLI for AI-ready knowledge",
    )
    parser.add_argument("--config", default="config/runtime.yaml")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="Runtime and engine status").set_defaults(func=cmd_status)
    sub.add_parser("dashboard", help="Dashboard metrics").set_defaults(func=cmd_dashboard)
    sub.add_parser("health", help="Knowledge Health scores").set_defaults(func=cmd_health)

    p_curator = sub.add_parser("curator", help="Proactive knowledge alerts")
    p_curator.add_argument("--no-save", action="store_true")
    p_curator.set_defaults(func=cmd_curator)

    sub.add_parser("monitor", help="Runtime monitoring data").set_defaults(func=cmd_monitor)

    p_explain = sub.add_parser("explain", help="Why did Coltex retrieve this?")
    p_explain.add_argument("query")
    p_explain.set_defaults(func=cmd_explain)

    p_ingest = sub.add_parser("ingest", help="Event-driven ingest pipeline")
    p_ingest.add_argument("document_id")
    p_ingest.add_argument("--source", default="upload")
    p_ingest.set_defaults(func=cmd_ingest)

    p_search = sub.add_parser("search", help="Universal search")
    p_search.add_argument("query")
    p_search.set_defaults(func=cmd_search)

    p_ask = sub.add_parser("ask", help="Ask Knowledge")
    p_ask.add_argument("question")
    p_ask.set_defaults(func=cmd_ask)

    p_upload = sub.add_parser("upload", help="Upload and process a source file")
    p_upload.add_argument("path")
    p_upload.set_defaults(func=cmd_upload)

    sub.add_parser("sources", help="List uploaded sources").set_defaults(func=cmd_sources)

    p_settings = sub.add_parser("settings", help="View or update workspace settings")
    p_settings.add_argument("--set", default="", help="Set a value, e.g. chunk_size=1500")
    p_settings.set_defaults(func=cmd_settings)

    p_events = sub.add_parser("events", help="Recent event bus activity")
    p_events.add_argument("--simulate", action="store_true")
    p_events.add_argument("--document-id", default="")
    p_events.set_defaults(func=cmd_events)

    p_knowledge = sub.add_parser("knowledge", help="Browse knowledge objects")
    p_knowledge.add_argument("--document-id", default="")
    p_knowledge.add_argument("--limit", type=int, default=20)
    p_knowledge.set_defaults(func=cmd_knowledge)

    p_conn = sub.add_parser("connector", help="Sync a connector")
    p_conn.add_argument("connector_id", choices=["filesystem", "github"])
    p_conn.set_defaults(func=cmd_connector)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
