"""surfacemap handler -- work package `cluster-surface-map` (escalation #2293, #2286 U3).

Steps cluster.surface_pairs (the pairs file, read-only), cluster.surface_apply (the session pass from the filled
file), cluster.surface_tail (the API pass: a preview unless -Live) and cluster.surface_check (the report, read-only).
The logic is in lib/surfacemap.py. A MapError is the routed condition 'refused' (cfg_on_fail: report-continue);
API failures are their own conditions."""
from __future__ import annotations

import json
import pathlib

from ..lib import filingkit
from ..lib import surfacemap as sm
from ..lib.lexicalenrichgenerate import ApiCallFailed, ApiKeyMissing, call_api, log_usage
from .base import Ctx, Outcome, fail, ok


def _may(ctx: Ctx, table: str) -> None:
    if table not in ctx.cfg.may_write(ctx.step_id):
        raise PermissionError(f"write-grant violation: {ctx.step_id!r} may not write {table!r}")


def _cluster(ctx: Ctx) -> str:
    """The cluster code as the cluster table spells it (M10c is lower-case at its end), matched without case."""
    c = (ctx.params.get("Cluster") or "").strip()
    if not c:
        raise sm.MapError("-Cluster is required (an M cluster code, e.g. M18)")
    row = ctx.db.conn.execute("SELECT cluster_code FROM cluster WHERE upper(cluster_code)=upper(?)", (c,)).fetchone()
    return row[0] if row else c


def _head(ctx: Ctx) -> float:
    return float(ctx.cfg.required_setting("cluster.surface_map.head_share"))


def _out(ctx: Ctx, topic: str, ext: str) -> pathlib.Path:
    path = filingkit.versioned_path(ctx.cfg, topic, out_dir=ctx.cfg.required_setting("cluster.surface_map.output_dir"),
                                    ext=ext)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def pairs(ctx: Ctx) -> Outcome:
    try:
        cluster = _cluster(ctx)
        data = sm.build_file(ctx.db.conn, cluster, _head(ctx))
    except sm.MapError as exc:
        return fail("refused", str(exc))
    path = _out(ctx, f"{cluster.lower()}-pairs", "json")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    c = data["counts"]
    return ok(f"-> {path.as_posix()}\n  {cluster} {data['cluster_name']}: {c['pairs']} pairs ({c['head']} head, "
              f"{c['tail']} tail), {c['hits']} hits; {c['allocated']} already allocated, {c['inherited']} with an "
              f"inherited subgroup. Fill the groups and the head, then -Step Apply -File <this file>.",
              path=str(path), **c)


def apply(ctx: Ctx) -> Outcome:
    _may(ctx, "cluster_subgroup")
    _may(ctx, "surface_subgroup")
    try:
        cluster = _cluster(ctx)
        f = pathlib.Path(ctx.params.get("File") or "")
        if not f.is_file():
            raise sm.MapError(f"-File is required and must exist: {f.as_posix()!r}")
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except ValueError as exc:
            raise sm.MapError(f"{f.as_posix()} is not JSON: {exc}")
        conn = ctx.db.conn
        counts = sm.apply_file(conn, cluster, data, _head(ctx), ctx.run_id)
        conn.commit()
    except sm.MapError as exc:
        ctx.db.conn.rollback()
        return fail("refused", str(exc))
    return ok(f"{cluster}: {counts['stale_retired']} stale pair(s) retired; {counts['groups_added']} group(s) added; "
              f"pairs {counts['inserted']} inserted, {counts['updated']} updated, {counts['unchanged']} unchanged. "
              f"Next: -Step Tail (a preview), then -Step Check.", **counts)


def tail(ctx: Ctx) -> Outcome:
    live = str(ctx.params.get("Live", "")).strip().lower() in ("1", "true", "yes")
    conn = ctx.db.conn
    try:
        cluster = _cluster(ctx)
        pkg = sm.assemble_tail(ctx.cfg, conn, cluster, _head(ctx))
    except sm.MapError as exc:
        return fail("refused", str(exc))
    n = len(pkg["pairs"])
    if n == 0:
        return ok(f"{cluster}: no unallocated pair left; nothing to send", pairs=0)
    cap = float(ctx.cfg.required_setting("lexical.llm_max_cost_per_batch"))
    head = (f"{cluster}: {n} tail pair(s), about {pkg['est_input_tokens']} input tokens, at most "
            f"{pkg['max_output_tokens']} output tokens, estimated ${pkg['est_cost_usd']:.4f} on {pkg['model']}")
    if pkg["est_cost_usd"] > cap:
        return fail("cost-cap-exceeded", f"{head}: over lexical.llm_max_cost_per_batch (${cap:.2f})")
    if not live:
        return ok(f"PREVIEW {head}. No call made, nothing written. Re-run with -Live to allocate.", pairs=n,
                  est_cost_usd=pkg["est_cost_usd"], preview=1)
    _may(ctx, "surface_subgroup")
    _may(ctx, "cluster_subgroup")
    try:
        result = call_api(ctx, pkg)
    except ApiKeyMissing as exc:
        return fail("api-key-missing", str(exc))
    except ApiCallFailed as exc:
        return fail("api-error", str(exc))
    rate_in = float(ctx.cfg.required_setting("lexical.llm_rate_input_per_million"))
    rate_out = float(ctx.cfg.required_setting("lexical.llm_rate_output_per_million"))
    cost = result["input_tokens"] / 1e6 * rate_in + result["output_tokens"] / 1e6 * rate_out
    log_usage(ctx.cfg, ctx.run_id, f"surface-tail {cluster}", pkg["model"], result["input_tokens"],
              result["output_tokens"], cost)
    codes = {g["code"] for g in sm.groups(conn, cluster)} | {sm.anomaly_code(cluster)}
    try:
        allocs = sm.parse_tail(result["text"], pkg["pairs"], codes)
        counts = sm.apply_tail(conn, cluster, allocs, ctx.run_id)
        conn.commit()
    except sm.MapError as exc:
        conn.rollback()
        return fail("bad-model-response", f"{cluster}: {exc}")
    anomaly = sum(1 for a in allocs if a["group"] == sm.anomaly_code(cluster))
    return ok(f"{cluster}: {n} tail pair(s) allocated by the API ({anomaly} to the anomaly group); "
              f"{counts['inserted']} inserted, {counts['updated']} updated; cost ${cost:.4f} "
              f"({result['input_tokens']} in, {result['output_tokens']} out). Next: -Step Check.",
              pairs=n, anomaly=anomaly, cost_usd=round(cost, 4), **counts)


def check(ctx: Ctx) -> Outcome:
    try:
        cluster = _cluster(ctx)
        r = sm.check(ctx.db.conn, cluster, _head(ctx),
                     float(ctx.cfg.required_setting("cluster.surface_map.max_group_share")))
    except sm.MapError as exc:
        return fail("refused", str(exc))
    path = _out(ctx, f"{cluster.lower()}-check", "md")
    path.write_text(sm.check_markdown(r), encoding="utf-8")
    over = [g["code"] for g in r["groups"] if g["over"]]
    return ok(f"-> {path.as_posix()}\n  {cluster}: {len(r['groups'])} group(s); {len(r['unallocated'])} pair(s) "
              f"unallocated; {len(r['stale'])} stale; {len(r['anomaly'])} in the anomaly group; "
              f"{len(r['two_sense'])} two-sense; "
              f"over {r['max_group_share'] * 100:.0f}%: {', '.join(over) or 'none'}",
              path=str(path), unallocated=len(r["unallocated"]), stale=len(r["stale"]), anomaly=len(r["anomaly"]),
              over=len(over))
