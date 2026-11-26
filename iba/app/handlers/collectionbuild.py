"""collectionbuild handlers -- work package `collection-build` (#2361, module 5 of 5 of the surface cycle), one step per Collection-Build.ps1 action.

Status says how the stored members of the collections stand against what the AI judgements decide (read-only). Links writes the difference
(-Check previews; a pair whose link was removed is not linked again): new links, links whose tier changed (the old row
set to deleted with superseded_by_id), the shared flags and the word states. Show prints one collection with its members by tier. Export writes a
CSV of the collections from the tables to the exports folder (a view, never an input). Set changes the status of a collection and Merge folds one
collection into another, both only on the researcher's instruction and each with a reason and a surface_event. Everything is read from tables; a
usage problem is the routed condition 'refused' and writes nothing. See lib/collectionbuild.py for the rule."""
from __future__ import annotations

import csv
import json
import pathlib
import re

from ..lib import collectionbuild as cb
from ..lib import reportkit
from .base import Ctx, Outcome, fail, ok


# ══ #2637 X8: every refusal or crash of a read or record command is kept in read_failure, for learning ═══════════════════════════
_RULE_KEY = re.compile(r"\b(?:B:\d+|[A-Z]{2}-\d{2}|RO\d+)\b")


def _log_failure(ctx: Ctx, kind: str, problems: str) -> None:
    """One read_failure row: the step, the collection and subgroup of the command or of its answer file, the file, the full message and the
    rule keys it names. Written on its own commit after a rollback of the command's work (a refusal wrote nothing; a crash keeps nothing). A
    failure of this log never replaces the command's own outcome."""
    conn = ctx.cfg.conn
    coll, sub = str(ctx.params.get("Collection", "") or "").strip() or None, str(ctx.params.get("Subgroup", "") or "").strip() or None
    file = str(ctx.params.get("File", "") or "").strip() or None
    if file and not coll:
        try:
            d = _answer_of(json.loads(pathlib.Path(file).read_text(encoding="utf-8")))
            coll, sub = (str(d.get("collection") or "").strip() or None), (str(d.get("subgroup") or "").strip() or None)
        except Exception:       # an unreadable file is itself the problem the message names
            pass
    keys = ",".join(sorted(set(_RULE_KEY.findall(problems or "")))) or None
    try:
        conn.rollback()
        conn.execute("INSERT INTO read_failure (run_id, step, collection, subgroup, kind, file, problems, rule_keys) VALUES (?,?,?,?,?,?,?,?)",
                     (ctx.run_id, ctx.step_id or "", coll, sub, kind, file, problems or "", keys))
        conn.commit()
    except Exception as exc:     # never mask the command's own outcome
        import sys
        print(f"[WARN] read_failure not written: {exc!r}", file=sys.stderr)


def _logged(fn):
    """A read or record handler whose refusals and crashes are kept in read_failure (#2637 X8). A refusal stays a usage outcome
    (cfg_on_fail refused, report-continue); a crash is logged and re-raised, so run.py still raises its escalation."""
    import functools
    import traceback

    @functools.wraps(fn)
    def wrapper(ctx: Ctx) -> Outcome:
        try:
            out = fn(ctx)
        except Exception as exc:
            _log_failure(ctx, "crash", f"{exc!r}\n{traceback.format_exc()}")
            raise
        if out.condition == "refused":
            from ..lib import refusalrules       # #2637 X4: each line of the refusal names the rule it applies (cfg_setting layer.refusals)
            out.message = refusalrules.annotate(ctx.cfg.conn, out.message)
            _log_failure(ctx, "refused", out.message)
        return out
    return wrapper


def _export_target(ctx: Ctx, view: str) -> tuple[pathlib.Path, pathlib.Path]:
    """(the new file's path, the base path of its stem) of one CSV export (#2413). The stem is cfg_setting collection.export_names[view], the folder
    surfaces.exports_root; the version is the next one over the live and archived files (reportkit.next_versioned_path). Raises ValueError, routed as
    'refused', on a missing setting; nothing is written."""
    root = ctx.cfg.setting("surfaces.exports_root")
    names = ctx.cfg.setting("collection.export_names")
    if not root:
        raise ValueError("cfg_setting surfaces.exports_root is missing")
    if not isinstance(names, dict) or not names.get(view):
        raise ValueError(f"cfg_setting collection.export_names has no stem for the view {view!r}")
    archive = ctx.cfg.required_setting("governance.oneoff_report_archive_dir")
    base = pathlib.Path(root) / f"{names[view]}.csv"
    return reportkit.next_versioned_path(base, archive), base


def _archive_prior(base: pathlib.Path, ctx: Ctx) -> None:
    """Move the live versions of this export to the archive folder, after the new rows are built and before the new file is written."""
    reportkit._archive_prior_versions(base, ctx.cfg.required_setting("governance.oneoff_report_archive_dir"))


def _flag(ctx, name):
    return str(ctx.params.get(name, "")).lower() in ("1", "true", "yes")


def _lines(pl: dict, conn) -> list[str]:
    tiers = conn.execute("SELECT tier, count(*), sum(shared) FROM collection_link WHERE deleted=0 GROUP BY 1 ORDER BY 2 DESC").fetchall()
    cols = conn.execute("SELECT status, count(*) FROM collection WHERE deleted=0 GROUP BY 1").fetchall()
    name = {r[0]: r[1] for r in conn.execute("SELECT t.id, t.surface FROM surface_term t")}
    lines = ["collections: " + ", ".join(f"{s} {n}" for s, n in cols) + f" ({pl['n_cols']} take part in the rule)",
             "stored links: " + "; ".join(f"{t} {n}" + (f" ({s} shared)" if s else "") for t, n, s in tiers),
             f"the judgements decide {len(pl['decided'])} pairs: {pl['same']} as stored; to add {len(pl['add'])}; tier changed {len(pl['change'])}; "
             f"shared flag {len(pl['reshare'])}; word state {len(pl['state_changes'])}",
             f"withheld, the link was removed earlier (the 18 pairs the prototype left out, or a later removal): {len(pl['proposed'])}"]
    if pl["proposed"]:
        lines.append("  " + ", ".join(sorted(f"{name[t]}" for (c, t), _ in pl["proposed"]))[:300])
    if pl["orphans"]:
        lines.append(f"stored links the judgements no longer produce (kept, never deleted by this step): {len(pl['orphans'])}")
    return lines


def status(ctx: Ctx) -> Outcome:
    pl = cb.plan(ctx.cfg.conn, ctx.cfg.setting('collection.score_threshold'))
    return ok("\n  ".join(_lines(pl, ctx.cfg.conn)), to_add=len(pl["add"]), to_change=len(pl["change"]), withheld=len(pl["proposed"]), unchanged=pl["same"])


def links(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    pl = cb.plan(conn, ctx.cfg.setting('collection.score_threshold'))
    lines = _lines(pl, conn)
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written)\n  " + "\n  ".join(lines), to_add=len(pl["add"]), to_change=len(pl["change"]))
    done = cb.write(conn, ctx.run_id, pl)
    conn.execute("UPDATE run SET counts=? WHERE run_id=?", (json.dumps(done), ctx.run_id))
    conn.commit()
    return ok("\n  ".join(lines) + f"\n  written: {done['added']} links added, {done['superseded']} superseded, {done['reshared']} shared flags, {done['states']} word states", **done)


def _collection(conn, name):
    name = (name or "").strip().lower()
    if not name:
        raise cb.CollectionError("-Collection is required: the name of a collection (its core word)")
    row = conn.execute("SELECT c.id, c.name, c.status, t.surface, c.pole_word, c.pole_of_pole, c.pole_reciprocal, c.merged_into_id FROM collection c "
                       "JOIN surface_term t ON t.id=c.core_term_id WHERE c.deleted=0 AND lower(c.name)=?", (name,)).fetchone()
    if row is None:
        raise cb.CollectionError(f"{name!r} is not a collection")
    return row


def show(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    try:
        c = _collection(conn, ctx.params.get("Collection"))
    except cb.CollectionError as exc:
        return fail("refused", str(exc))
    lines = [f"{c[1]} ({c[2]}); core {c[3]}; pole {c[4]} (pole of the pole {c[5]}, reciprocal {c[6]})" + (f"; merged into collection {c[7]}" if c[7] else "")]
    for tier in ("core", "synonym", "opposite", "possible_opposite", "associated", "set_aside", "gathered"):
        ws = [r[0] + ("*" if r[1] else "") for r in conn.execute(
            "SELECT t.surface, l.shared FROM collection_link l JOIN surface_term t ON t.id=l.term_id WHERE l.collection_id=? AND l.tier=? AND l.deleted=0 "
            "ORDER BY t.surface", (c[0], tier))]
        lines.append(f"{tier} ({len(ws)}): " + ", ".join(ws))
    lines.append("* shared with another collection")
    return ok("\n  ".join(lines), collection=c[1])


def export(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    try:
        path, base = _export_target(ctx, "collections")
    except ValueError as exc:
        return fail("refused", str(exc))
    rows = conn.execute(
        "SELECT c.name, c.status, ct.surface, c.pole_word, c.pole_of_pole, c.pole_reciprocal, l.tier, t.surface, l.shared, t.surface_group, t.collection_state, l.reason "
        "FROM collection_link l JOIN collection c ON c.id=l.collection_id JOIN surface_term ct ON ct.id=c.core_term_id JOIN surface_term t ON t.id=l.term_id "
        "WHERE l.deleted=0 AND c.deleted=0 ORDER BY c.name, CASE l.tier WHEN 'core' THEN 0 WHEN 'synonym' THEN 1 WHEN 'opposite' THEN 2 WHEN 'possible_opposite' THEN 3 "
        "WHEN 'associated' THEN 4 ELSE 5 END, t.surface").fetchall()
    path.parent.mkdir(parents=True, exist_ok=True)
    _archive_prior(base, ctx)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["collection", "status", "core", "pole", "pole_of_pole", "reciprocal", "tier", "word", "shared", "group", "word_state", "reason"])
        w.writerows(rows)
    return ok(f"{len(rows)} links of {len({r[0] for r in rows})} collections written to {path.as_posix()} (a view of the tables, not an input); {_register(ctx, path)}", rows=len(rows))


def _export_view(ctx: Ctx, view: str) -> Outcome:
    """One of the two #2379 views (lib/collectionexport.py), written under surfaces.exports_root as <collection.export_names stem>-v<n>-<yyyymmdd>.csv (#2413):
    the name and version come from config and the filing rule, the previous live version is archived, and nothing is written when the build is refused."""
    from ..lib import collectionexport as ce
    try:
        vals = ce.read_settings(ctx.cfg)
        path, base = _export_target(ctx, view)
        head, rows = ce.build(ctx.cfg.conn, view, vals["tiers"], vals["groups"])
    except (ce.ExportError, ValueError) as exc:
        return fail("refused", str(exc))
    path.parent.mkdir(parents=True, exist_ok=True)
    _archive_prior(base, ctx)
    ce.write(path, head, rows)
    return ok(f"{len(rows)} rows of the {view} view written to {path.as_posix()} (a view of the tables, not an input); {_register(ctx, path)}", rows=len(rows))


def export_members(ctx: Ctx) -> Outcome:
    return _export_view(ctx, "members-verses")


def export_surfaces(ctx: Ctx) -> Outcome:
    return _export_view(ctx, "surfaces")


def evidence(ctx: Ctx) -> Outcome:
    """The evidence report (#2464, #2467, #2477; lib/collectionevidence.py builds the data, lib/collectionevidencereport.py the files) of one collection or a comma list
    (-Collection), or of a verse or list of verses (-Verse, items separated by a semicolon): the stored entries from the base data through the observations and the claims into the
    narrative, as a Markdown report (the reading) and an Excel workbook (every listing in full, one sheet each) under surfaces.exports_root, versioned by the filing rule (the
    previous live versions archived). Read-only on the tables; -Check builds the data and writes no file."""
    import datetime
    from ..lib import collectionevidence as ev
    from ..lib import collectionevidencereport as rep
    conn = ctx.cfg.conn
    names, verse = str(ctx.params.get("Collection", "")).strip(), str(ctx.params.get("Verse", "")).strip()
    try:
        if bool(names) == bool(verse):
            raise ev.EvidenceError("give either -Collection (one name or a comma list) or -Verse (" + ev.REF_FORM + "), not both and not neither")
        vals = ev.read_settings(ctx.cfg)
        order = ev.Order(conn)
        if verse:
            datas = [ev.build_verses(conn, ev.resolve_verses(conn, ctx.cfg, verse, order), order)]
        else:
            datas = [ev.build_collection(conn, c, vals["tiers"], order) for c in ev.resolve(conn, names.split(","))]
            for d_ in datas:
                d_["pairs"] = ev.build_pairs(conn, d_, vals, order)
        archive = ctx.cfg.required_setting("governance.oneoff_report_archive_dir")
    except (ev.EvidenceError, ValueError) as exc:
        return fail("refused", str(exc))
    if verse:
        slug = "-".join(re.sub(r"[^a-z0-9]+", "-", v["reference"].lower()).strip("-") for v in datas[0]["verses"][:3])
        stem = f"{vals['verse_name']}-{slug}" if len(datas[0]["verses"]) <= 3 else f"{vals['verse_name']}-{len(datas[0]['verses'])}-verses"
    else:
        slug = "-".join(re.sub(r"[^a-z0-9]+", "-", d["name"].lower()).strip("-") for d in datas)
        stem = f"{vals['name']}-{slug}" if len(slug) <= 60 else f"{vals['name']}-{len(datas)}-collections"
    summary = "; ".join(f"{d['name']}: {len(d['occurrences'])} occurrences, {len(d['observations'])} observations, {len(d['claims'])} claims, {len(d['sections'])} narrative sections, "
                        f"{sum(1 for f in d['faults'] if f['rows'])} fault rules with findings" for d in datas)
    if _flag(ctx, "Check"):
        return ok(f"PREVIEW (nothing written): {summary}; {len(rep.sheets(datas, vals))} workbook sheets")
    base = pathlib.Path(vals["path"]) / f"{stem}.md"
    md_path = reportkit.next_versioned_path(base, archive)
    xlsx_path = md_path.with_suffix(".xlsx")
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    text = rep.render(datas, vals, ctx.run_id, stamp, xlsx_path.name)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    live = {f for f in md_path.parent.glob(f"{stem}-v*") if f.is_file()}
    try:
        reportkit._archive_prior_versions(base, archive)
        reportkit._archive_prior_versions(base.with_suffix(".xlsx"), archive)
        reportkit._archive_prior_versions(base.with_suffix(".csv"), archive)    # the CSV of the reports before #2477
    except OSError as exc:     # a previous file is open in another program: put back what was moved, write nothing
        for f in live:
            moved = md_path.parent / archive / f.name
            if not f.exists() and moved.exists():
                moved.replace(f)
        return fail("refused", f"a previous version of this report is in use by another program ({exc}); close it and run again; nothing was written")
    md_path.write_text(text, encoding="utf-8")
    listed = rep.write_workbook(xlsx_path, datas, vals, ctx.run_id, stamp)
    return ok(f"{summary}\n  written: {md_path.as_posix()} ({len(text.splitlines())} lines) and {xlsx_path.as_posix()} ({len(listed)} sheets, "
              f"{sum(x['rows'] for x in listed)} rows; a view of the tables, not an input); run Manifest-Rebuild.ps1 to register them", rows=sum(x["rows"] for x in listed))


def _event(conn, run_id, cid, action, before, after, reason):
    conn.execute("INSERT INTO surface_event (subject_kind, subject_id, action, field, value_before, value_after, by, reason, run_id, created_by) "
                 "VALUES ('collection',?,?,'status',?,?,'collection-build',?,?,'collection-build')", (cid, action, before, after, reason, run_id))


def set_status(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    status_ = (ctx.params.get("Status") or "").strip()
    reason = (ctx.params.get("Reason") or "").strip()
    try:
        c = _collection(conn, ctx.params.get("Collection"))
    except cb.CollectionError as exc:
        return fail("refused", str(exc))
    if status_ not in ("indicative", "confirmed", "retired"):
        return fail("refused", f"-Status {status_!r} must be indicative, confirmed or retired (merged is made by Merge)")
    if not reason:
        return fail("refused", "-Reason is required: why the status changes (on your instruction)")
    if c[2] == "merged":
        return fail("refused", f"{c[1]!r} is merged into another collection: its status is not changed")
    if c[2] == status_:
        return ok(f"{c[1]} is already {status_}", changed=0)
    conn.execute("UPDATE collection SET status=?, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), run_id=? WHERE id=?", (status_, ctx.run_id, c[0]))
    _event(conn, ctx.run_id, c[0], "confirm" if status_ == "confirmed" else ("retire" if status_ == "retired" else "reopen"), c[2], status_, reason)
    conn.commit()
    return ok(f"{c[1]}: {c[2]} -> {status_} ({reason})", changed=1)


def gather(ctx: Ctx) -> Outcome:
    """One collection of a list of surfaces the researcher names, tier gathered, without the AI (escalation #2388). -Name, -Surface (comma list),
    -Reason (the instruction, quoted, with the escalation id); -Check previews."""
    conn = ctx.cfg.conn
    surfaces = (ctx.params.get("Surface") or "").split(",")
    try:
        r = cb.gather(conn, ctx.run_id, ctx.params.get("Name"), surfaces, ctx.params.get("Reason") or "", dry=_flag(ctx, "Check"))
    except cb.CollectionError as exc:
        return fail("refused", str(exc))
    if _flag(ctx, "Check"):
        return ok(f"PREVIEW (nothing written): collection {(ctx.params.get('Name') or '').strip().lower()} of {r['members']} surfaces, tier gathered", members=r["members"])
    conn.commit()
    return ok(f"collection {(ctx.params.get('Name') or '').strip().lower()} made (id {r['collection']}) of {r['members']} surfaces, tier gathered. Next: Engagement.ps1 -Action Pull -Collection {(ctx.params.get('Name') or '').strip().lower()}",
              collection=r["collection"], members=r["members"])


def index_fill(ctx: Ctx) -> Outcome:
    """Fill the index of the surfaces of the confirmed collections (#2503): one live row for each member surface, unplaced; a row whose surface left its collection is retired. -Check previews."""
    from ..lib import collectionindex as ci
    conn = ctx.cfg.conn
    try:
        r = ci.fill(conn, ctx.cfg, ctx.run_id, dry=_flag(ctx, "Check"))
    except ci.IndexError_ as exc:
        return fail("refused", str(exc))
    if _flag(ctx, "Check"):
        return ok(f"PREVIEW (nothing written): {r['expected']} member surfaces, {r['live']} live index rows; to add {r['add']}, to retire {r['retire']}", **r)
    conn.commit()
    return ok(f"index filled: {r['add']} rows added, {r['retire']} retired; {ci.counts(conn)}", **r)


def subgroup(ctx: Ctx) -> Outcome:
    """Make a subgroup of a collection (-Collection, -Name, -Reason) or place surfaces in it (-Surface a,b -Name -Reason [-Strong H4284]) or set aside surfaces whose meaning is not the collection's
    (-Surface a,b -Isolate -Reason), as the researcher's correction of the grouping by meaning (#2503, #2509). -Check previews."""
    from ..lib import collectionindex as ci
    conn = ctx.cfg.conn
    p = ctx.params
    coll = str(p.get("Collection", "")).strip()
    try:
        if _flag(ctx, "Isolate") or str(p.get("Surface", "")).strip():
            r = ci.place(conn, ctx.run_id, coll, (p.get("Name") or None), str(p.get("Surface", "")).split(","), (p.get("Strong") or None), p.get("Reason") or "",
                         isolate=_flag(ctx, "Isolate"), dry=_flag(ctx, "Check"))
            line = f"{r['placed']} surface(s) of {r['collection']} " + (f"placed in {r['group']}" if r["group"] else "isolated")
        else:
            r = ci.make_group(conn, ctx.run_id, coll, p.get("Name"), p.get("Reason") or "", dry=_flag(ctx, "Check"))
            line = f"subgroup {r['name']!r} of {r['collection']} made"
    except ci.IndexError_ as exc:
        return fail("refused", str(exc))
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written): " + line, **{k: v for k, v in r.items() if isinstance(v, (int, str))})
    conn.commit()
    return ok(line, **{k: v for k, v in r.items() if isinstance(v, (int, str))})


def index_check(ctx: Ctx) -> Outcome:
    """The checker of the index (#2503): member surfaces with no row, rows of surfaces that left, a surface in two collections, duplicates, the split rule, placements that do not agree, shared flags
    with no second link. Read-only on the tables; writes its findings as a versioned Markdown report under surfaces.exports_root (cfg_setting collection.index_check_name)."""
    import datetime

    from ..lib import collectionindex as ci
    conn = ctx.cfg.conn
    root, stem = ctx.cfg.setting("surfaces.exports_root"), ctx.cfg.setting("collection.index_check_name")
    if not root or not stem:
        return fail("refused", "cfg_setting surfaces.exports_root or collection.index_check_name is missing")
    try:
        found = ci.check(conn, ctx.cfg)
        archive = ctx.cfg.required_setting("governance.oneoff_report_archive_dir")
    except (ci.IndexError_, ValueError) as exc:
        return fail("refused", str(exc))
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    L = ["# Collection index check", "", f"Generated {stamp} by run {ctx.run_id} (`Collection-Build.ps1 -Action IndexCheck`, escalation #2503). Read-only on the tables. Counts: {ci.counts(conn)}.", ""]
    for f in found:
        L += [f"## {f['key']}: {len(f['rows'])}", "", f["how"] + ".", ""]
        if f["rows"]:
            L += ["| " + " | ".join(f["cols"]) + " |", "|" + "---|" * len(f["cols"])]
            L += ["| " + " | ".join(str(c).replace("|", "/") for c in r) + " |" for r in f["rows"][:200]]
            if len(f["rows"]) > 200:
                L += [f"_{len(f['rows']) - 200} more_"]
            L += [""]
    base = pathlib.Path(root) / f"{stem}.md"
    path = reportkit.next_versioned_path(base, archive)
    path.parent.mkdir(parents=True, exist_ok=True)
    reportkit._archive_prior_versions(base, archive)
    path.write_text("\n".join(L) + "\n", encoding="utf-8")
    n = sum(len(f["rows"]) for f in found)
    return ok("; ".join(f"{f['key']} {len(f['rows'])}" for f in found if f["rows"]) + (" -- " if n else "no findings -- ") + f"report {path.as_posix()} ({_register(ctx, path)})", findings=n)


# ══ the layered reading (#2505) ══════════════════════════════════════════════════════════════════
def _layer_args(ctx: Ctx):
    coll = str(ctx.params.get("Collection", "")).strip()
    step = str(ctx.params.get("Step", "")).strip()
    return coll, step


def layer_open(ctx: Ctx) -> Outcome:
    """Open a step of the layered reading for a collection: the gates (the grouping finished, the previous step closed; step 1.1 opens once the grouping is finished; -Subgroup opens it for one subgroup), then the ledger rows the data demands. -Check previews."""
    from ..lib import layerreading as lr
    conn = ctx.cfg.conn
    coll, step = _layer_args(ctx)
    try:
        r = lr.open_step(conn, ctx.cfg, ctx.run_id, coll, step, dry=_flag(ctx, "Check"), subgroup=str(ctx.params.get("Subgroup", "")).strip() or None)
    except lr.LayerError as exc:
        return fail("refused", str(exc))
    line = f"step {r['step']} of {r['collection']}: the data demands {r['demanded']} aspects; {r['add']} added to the ledger, {r['retire']} retired, {r['revive']} reopened"
    if r.get("legacy") or r.get("superseded"):
        line += f"; superseded by the subgroup's new reading: {r.get('legacy', 0)} whole-collection word rows retired, {r.get('superseded', 0)} rows of later steps read again (their observations withdrawn)"
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written): " + line, **{k: v for k, v in r.items() if isinstance(v, int)})
    conn.commit()
    return ok(line + ". Next: Collection-Build.ps1 -Action LayerPull", **{k: v for k, v in r.items() if isinstance(v, int)})


def layer_pull(ctx: Ctx) -> Outcome:
    """Write the working file of the open rows of a step with the evidence to read; the file is filled in the session and recorded with LayerRecord."""
    from ..lib import layerreading as lr
    conn = ctx.cfg.conn
    coll, step = _layer_args(ctx)
    root = ctx.cfg.setting("layer.working_dir")
    if not root:
        return fail("refused", "cfg_setting layer.working_dir is missing")
    try:
        path, n = lr.pull(conn, ctx.cfg, coll, step, pathlib.Path(root), subgroup=str(ctx.params.get("Subgroup", "")).strip() or None)
    except lr.LayerError as exc:
        return fail("refused", str(exc))
    conn.commit()
    return ok(f"working file with {n} rows: {path.as_posix()}. Fill each row (disposition, obs_text, basis; route where asked), then Collection-Build.ps1 -Action LayerRecord -File <file> -Check", rows=n)


def layer_record(ctx: Ctx) -> Outcome:
    """Check a filled working file whole and write its observations, nodes and ledger answers in one transaction. -Check previews (everything is checked, nothing kept)."""
    from ..lib import layerreading as lr
    conn = ctx.cfg.conn
    file = str(ctx.params.get("File", "")).strip()
    if not file:
        return fail("refused", "-File is required: the filled working file from LayerPull")
    try:
        data = json.loads(pathlib.Path(file).read_text(encoding="utf-8"))
        r = lr.record(conn, ctx.cfg, ctx.run_id, data, keep=not _flag(ctx, "Check"))
    except (OSError, ValueError) as exc:
        return fail("refused", f"cannot read {file}: {exc}")
    except lr.LayerError as exc:
        return fail("refused", str(exc))
    line = f"{r['observed']} observations written with {r['nodes']} nodes, {r['none']} recorded as none, {r['withdrawn']} earlier observations withdrawn"
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written): " + line, **r)
    conn.commit()
    return ok(line + ". Next: Collection-Build.ps1 -Action LayerCheck", **r)


@_logged
def layer_next(ctx: Ctx) -> Outcome:
    """Say what to do next in the layered reading of a collection, from the ledger alone: the subgroup in flight, the step, its state and the verbs (lib/layerloop.py; escalation #2538)."""
    from ..lib import layerloop as ll
    from ..lib import layerreading as lr
    coll = str(ctx.params.get("Collection", "")).strip()
    if not coll:
        return fail("refused", "-Collection is required")
    try:
        r = ll.next_action(ctx.cfg.conn, ctx.cfg, coll)
    except (lr.LayerError, ValueError) as exc:
        return fail("refused", str(exc))
    lines = ["progress (closed means every live row answered and validated):"] + ["  " + x for x in r["progress"]]
    lines.append("collection steps: " + ", ".join(f"{k}={v}" for k, v in r["collection_steps"].items()))
    if r.get("step"):
        who = f"subgroup {r['subgroup']!r}" if r.get("subgroup") else "the collection"
        lines.append(f"NEXT: {who}, step {r['step']} ({r['state']}): {r['what']}")
        lines += ["  " + c for c in r["commands"]]
        if r.get("others_waiting"):
            lines.append("waiting (their loop starts or continues only after this one is finished): " + ", ".join(r["others_waiting"]))
    else:
        lines.append(r["what"])
        lines += ["  " + c for c in r["commands"]]
    return ok(chr(10).join(lines), **{k: r[k] for k in ("subgroup", "step", "state") if k in r})


@_logged
def read_words(ctx: Ctx) -> Outcome:
    """ReadWords: the package of the next words of one subgroup to read (step S1): the instruction of this read, only these words' occurrences, verses and lexicon, and the answer
    template (lib/readcommands.py; escalation #2538). Opens S1 for the subgroup if it is not open; the order and grouping gates apply."""
    from ..lib import layerreading as lr
    from ..lib import readcommands as rc
    from ..lib import scanguard as sg
    coll, sub = str(ctx.params.get("Collection", "")).strip(), str(ctx.params.get("Subgroup", "")).strip()
    if not coll or not sub:
        return fail("refused", "-Collection and -Subgroup are required (the words are read one subgroup at a time)")
    root = ctx.cfg.setting("layer.working_dir")
    if not root:
        return fail("refused", "cfg_setting layer.working_dir is missing")
    try:
        r = rc.read_words(ctx.cfg.conn, ctx.cfg, ctx.run_id, coll, sub, pathlib.Path(root))
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except (rc.ReadError, lr.LayerError, sg.ScanBudgetExceeded) as exc:
        return fail("refused", str(exc))
    ctx.cfg.conn.commit()
    head = f"step S1 opened for the subgroup ({r['opened']['add']} rows added). " if r.get("opened") else ""
    return ok(head + f"package of {r['words']} word(s), {r['left']} left after it ({r['chars']} characters, {r['seconds']} s): {r['path'].as_posix()}. "
              f"Read it (its view beside it: the same name, .md, or -part-<n>.md) and fill its `answer`, then: Collection-Build.ps1 -Action CheckAnswer -File <answer file> until it finds no problem, and -Action RecordWords -File <answer file>", words=r["words"], left=r["left"])


@_logged
def record_words(ctx: Ctx) -> Outcome:
    """RecordWords: check a filled ReadWords answer whole, write it through the recorder of the layered reading, validate the subgroup's rows and name the next command. -Check previews."""
    from ..lib import readcommands as rc
    file = str(ctx.params.get("File", "")).strip()
    if not file:
        return fail("refused", "-File is required: the filled answer of a ReadWords package")
    conn = ctx.cfg.conn
    try:
        data = _answer_of(json.loads(pathlib.Path(file).read_text(encoding="utf-8")))
        r = rc.record_words(conn, ctx.cfg, ctx.run_id, data, keep=not _flag(ctx, "Check"))
    except (OSError, ValueError) as exc:
        return fail("refused", f"cannot read {file}: {exc}")
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except rc.ReadError as exc:
        return fail("refused", str(exc))
    line = f"{r['observed']} observations written with {r['nodes']} nodes for {r['rows']} word(s)"
    if r.get("preview"):
        return ok("PREVIEW (nothing written): " + line, observed=r["observed"], nodes=r["nodes"])
    conn.commit()
    tail = f"; check: {r['validated']} validated" + (f", FAILED: {', '.join(r['failed'])}" if r["failed"] else "") + f"; {r['words_open']} word(s) still open. Next: {r['next']}"
    return ok(line + tail, observed=r["observed"], nodes=r["nodes"], validated=r["validated"])


@_logged
def check_answer(ctx: Ctx) -> Outcome:
    """CheckAnswer (#2637 X3): every check the Record command of the answer's read makes, run on the filled answer at once, without stopping
    between the answer's own checks, the recorder's rules, the write and the check of the written rows; every problem is listed in one refusal,
    each line with the rule it applies. Nothing is written: the write is tried in savepoints that are rolled back. The read is the one the
    answer names in `command` (lib/readcommands.py CHECKS)."""
    from ..lib import readcommands as rc
    file = str(ctx.params.get("File", "")).strip()
    if not file:
        return fail("refused", "-File is required: the filled answer of a read package")
    conn = ctx.cfg.conn
    try:
        data = _answer_of(json.loads(pathlib.Path(file).read_text(encoding="utf-8")))
    except (OSError, ValueError) as exc:
        return fail("refused", f"cannot read {file}: {exc}")
    cmd = data.get("command") if isinstance(data, dict) else None
    if cmd == "GroupPull":      # a grouping file: every check of GroupRecord, previewed (#2637 v20 K3)
        from ..lib import collectiongroup as cg
        try:
            cg.record(conn, ctx.cfg, ctx.run_id, data, keep=False, file_name=pathlib.Path(file).name)
        except (cg.GroupError, ci_error()) as exc:
            conn.rollback()
            return fail("refused", str(exc))
        conn.rollback()
        return ok(f"no problem found: every check of GroupRecord passes on {file}; nothing written. Next: Collection-Build.ps1 -Action GroupRecord -File {file}")
    if cmd not in rc.CHECKS:
        return fail("refused", f"this is not the answer of a read: its `command` is {cmd!r}, one of {sorted(rc.CHECKS)} (fill the `answer` part of the package)")
    record = "Record" + cmd[len("Read"):]
    try:
        getattr(rc, rc.CHECKS[cmd])(conn, ctx.cfg, ctx.run_id, data, keep=False, collect=True)
    except rc.ReadNext as exc:
        conn.rollback()
        return ok(str(exc))
    except rc.ReadError as exc:
        conn.rollback()
        return fail("refused", str(exc))
    finally:
        conn.rollback()
    return ok(f"no problem found: every check of {record} passes on {file}; nothing written. Next: Collection-Build.ps1 -Action {record} -File {file}")


@_logged
def cycle(ctx: Ctx) -> Outcome:
    """Cycle (#2637 X6, X7): the reading cycle of a collection or one subgroup -- steps, ledger, packages, refusals and crashes -- and the audit of
    a run under B:138 (every refusal line names its rule, no crash, no file the package commands do not write), from -Since (ISO-8601 UTC) or
    all time. Writes the report (cfg_setting layer.cycle report_name, under surfaces.exports_root, versioned); reads nothing else."""
    import datetime
    from ..lib import cycleview, reportkit
    name = str(ctx.params.get("Collection", "")).strip()
    if not name:
        return fail("refused", "-Collection is required (-Subgroup and -Since are optional)")
    sub = str(ctx.params.get("Subgroup", "")).strip() or None
    since = str(ctx.params.get("Since", "")).strip() or None
    try:
        if since:
            datetime.datetime.fromisoformat(since.replace("Z", "+00:00"))
        r = cycleview.build(ctx.cfg.conn, ctx.cfg, name, sub, since)
    except ValueError as exc:
        return fail("refused", f"cannot read the cycle: {exc}")
    stem = json.loads(ctx.cfg.conn.execute("SELECT value FROM cfg_setting WHERE key='layer.cycle'").fetchone()[0])["report_name"]
    archive = ctx.cfg.required_setting("governance.oneoff_report_archive_dir")
    base = pathlib.Path(ctx.cfg.required_setting("surfaces.exports_root")) / f"{stem}-{cycleview._slug(name)}{'-' + cycleview._slug(sub) if sub else ''}.md"
    path = reportkit.next_versioned_path(base, archive)
    path.parent.mkdir(parents=True, exist_ok=True)
    reportkit._archive_prior_versions(base, archive)
    path.write_text("\n".join(r["lines"] + ["", f"_Generated by run {ctx.run_id} (Collection-Build.ps1 -Action Cycle)._"]) + "\n", encoding="utf-8")
    return ok(f"audit {r['verdict'].upper()}: {len(r['unstated'])} unstated refusal line(s), {len(r['crashes'])} crash(es), {len(r['other_files'])} other file(s); "
              f"report {path.as_posix()}")


def _register(ctx: Ctx, path) -> str:
    """Register a report just written, and the earlier versions of it moved to the archive, in file_manifest (#2637 v20 K4)."""
    from ..lib import manifest
    path = pathlib.Path(path)
    archive = pathlib.Path(ctx.cfg.required_setting("governance.oneoff_report_archive_dir"))
    stem = re.sub(r"-v\d+-\d{8}$", "", path.stem)
    older = [q for q in archive.rglob(f"{stem}-v*.md")] if archive.exists() else []
    n = manifest.register_files(ctx.cfg, [path] + older)
    ctx.cfg.conn.commit()
    return f"registered in the file manifest ({n} file(s))"


def _answer_of(data):
    """The answer of a read command: the file is the answer itself, or the whole package with its `answer` filled."""
    return data["answer"] if isinstance(data, dict) and isinstance(data.get("answer"), dict) and "instruction" in data else data


@_logged
def read_senses(ctx: Ctx) -> Outcome:
    """ReadSenses: the package of the senses of one subgroup (step 1.1): the instruction of this read, every B1 observation of the subgroup with the occurrences it holds, the sense head
    and meaning range of each code, the older observations to answer, and the answer template (lib/readcommands.py; escalation #2538). Opens 1.1 for the subgroup if it is not open."""
    from ..lib import layerreading as lr
    from ..lib import readcommands as rc
    from ..lib import scanguard as sg
    coll, sub = str(ctx.params.get("Collection", "")).strip(), str(ctx.params.get("Subgroup", "")).strip()
    if not coll or not sub:
        return fail("refused", "-Collection and -Subgroup are required (the senses are read one subgroup at a time)")
    root = ctx.cfg.setting("layer.working_dir")
    if not root:
        return fail("refused", "cfg_setting layer.working_dir is missing")
    try:
        r = rc.read_senses(ctx.cfg.conn, ctx.cfg, ctx.run_id, coll, sub, pathlib.Path(root))
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except (rc.ReadError, lr.LayerError, sg.ScanBudgetExceeded) as exc:
        return fail("refused", str(exc))
    ctx.cfg.conn.commit()
    head = f"step 1.1 opened for the subgroup ({r['opened']['add']} rows added). " if r.get("opened") else ""
    return ok(head + f"package of {r['readings']} B1 observation(s) on {r['occurrences']} occurrence(s), {r['older']} older observation(s) ({r['chars']} characters, {r['seconds']} s): "
              f"{r['path'].as_posix()}. Read it (its view beside it: the same name, .md, or -part-<n>.md) and fill its `answer`, then: Collection-Build.ps1 -Action CheckAnswer -File <answer file> until it finds no problem, and -Action RecordSenses -File <answer file>", readings=r["readings"])


@_logged
def record_senses(ctx: Ctx) -> Outcome:
    """RecordSenses: check a filled ReadSenses answer whole, write it through the recorder of the layered reading, validate the subgroup's 1.1 row and name the next command. -Check previews."""
    from ..lib import readcommands as rc
    file = str(ctx.params.get("File", "")).strip()
    if not file:
        return fail("refused", "-File is required: the filled answer of a ReadSenses package")
    conn = ctx.cfg.conn
    try:
        data = _answer_of(json.loads(pathlib.Path(file).read_text(encoding="utf-8")))
        r = rc.record_senses(conn, ctx.cfg, ctx.run_id, data, keep=not _flag(ctx, "Check"))
    except (OSError, ValueError) as exc:
        return fail("refused", f"cannot read {file}: {exc}")
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except rc.ReadError as exc:
        return fail("refused", str(exc))
    line = f"{r['observed']} observations written with {r['nodes']} nodes for {r['senses']} sense(s)"
    if r.get("preview"):
        return ok("PREVIEW (nothing written): " + line, observed=r["observed"], nodes=r["nodes"])
    conn.commit()
    tail = "; check: validated" if r["validated"] else f"; check: NOT validated ({r['reason']})"
    return ok(line + tail + f". Next: {r['next']}", observed=r["observed"], nodes=r["nodes"], validated=r["validated"])


@_logged
def read_enrichment(ctx: Ctx) -> Outcome:
    """ReadEnrichment: the package of the enrichment of one subgroup (step 1.2): the instruction of this read, every 1.1 sense of the subgroup with its codes and occurrences, the lexicon
    of every code, the older observations to answer, and the answer template (lib/readcommands.py; escalation #2538). Opens 1.2 for the subgroup if it is not open."""
    from ..lib import layerreading as lr
    from ..lib import readcommands as rc
    from ..lib import scanguard as sg
    coll, sub = str(ctx.params.get("Collection", "")).strip(), str(ctx.params.get("Subgroup", "")).strip()
    if not coll or not sub:
        return fail("refused", "-Collection and -Subgroup are required (the enrichment is read one subgroup at a time)")
    root = ctx.cfg.setting("layer.working_dir")
    if not root:
        return fail("refused", "cfg_setting layer.working_dir is missing")
    try:
        r = rc.read_enrichment(ctx.cfg.conn, ctx.cfg, ctx.run_id, coll, sub, pathlib.Path(root))
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except (rc.ReadError, lr.LayerError, sg.ScanBudgetExceeded) as exc:
        return fail("refused", str(exc))
    ctx.cfg.conn.commit()
    head = f"step 1.2 opened for the subgroup ({r['opened']['add']} rows added). " if r.get("opened") else ""
    return ok(head + f"package of {r['senses']} sense(s) and {r['codes']} code(s), {r['older']} older observation(s) ({r['chars']} characters, {r['seconds']} s): "
              f"{r['path'].as_posix()}. Read it (its view beside it: the same name, .md, or -part-<n>.md) and fill its `answer`, then: Collection-Build.ps1 -Action CheckAnswer -File <answer file> until it finds no problem, and -Action RecordEnrichment -File <answer file>", senses=r["senses"])


@_logged
def record_enrichment(ctx: Ctx) -> Outcome:
    """RecordEnrichment: check a filled ReadEnrichment answer whole, write it through the recorder of the layered reading, validate the subgroup's 1.2 row and name the next command. -Check previews."""
    from ..lib import readcommands as rc
    file = str(ctx.params.get("File", "")).strip()
    if not file:
        return fail("refused", "-File is required: the filled answer of a ReadEnrichment package")
    conn = ctx.cfg.conn
    try:
        data = _answer_of(json.loads(pathlib.Path(file).read_text(encoding="utf-8")))
        r = rc.record_enrichment(conn, ctx.cfg, ctx.run_id, data, keep=not _flag(ctx, "Check"))
    except (OSError, ValueError) as exc:
        return fail("refused", f"cannot read {file}: {exc}")
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except rc.ReadError as exc:
        return fail("refused", str(exc))
    line = f"{r['observed']} observations written with {r['nodes']} nodes for {r['enrichments']} enrichment(s)"
    if r.get("preview"):
        return ok("PREVIEW (nothing written): " + line, observed=r["observed"], nodes=r["nodes"])
    conn.commit()
    tail = "; check: validated" if r["validated"] else f"; check: NOT validated ({r['reason']})"
    return ok(line + tail + f". Next: {r['next']}", observed=r["observed"], nodes=r["nodes"], validated=r["validated"])

@_logged
def read_structure(ctx: Ctx) -> Outcome:
    """ReadStructure: the package of the next rows of step 2.1 of one subgroup, one item at a time (-Item to choose): what each row asks, its occurrences, the WordNet control of a
    pairing, the older observations, the verses with their stored structure, the subgroup's 1.1 senses, and the answer template (lib/readcommands.py; escalation #2538). Opens 2.1 for
    the subgroup if it is not open."""
    from ..lib import layerreading as lr
    from ..lib import readcommands as rc
    from ..lib import scanguard as sg
    coll, sub = str(ctx.params.get("Collection", "")).strip(), str(ctx.params.get("Subgroup", "")).strip()
    item = str(ctx.params.get("Item", "") or "").strip() or None
    if not coll or not sub:
        return fail("refused", "-Collection and -Subgroup are required (the structure is read one subgroup at a time)")
    root = ctx.cfg.setting("layer.working_dir")
    if not root:
        return fail("refused", "cfg_setting layer.working_dir is missing")
    try:
        r = rc.read_structure(ctx.cfg.conn, ctx.cfg, ctx.run_id, coll, sub, pathlib.Path(root), item)
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except (rc.ReadError, lr.LayerError, sg.ScanBudgetExceeded) as exc:
        return fail("refused", str(exc))
    ctx.cfg.conn.commit()
    head = f"step 2.1 opened for the subgroup ({r['opened']['add']} rows added). " if r.get("opened") else ""
    return ok(head + f"package of {r['rows']} {r['item']} row(s), {r['left']} row(s) left after it, {r['verses']} verse(s) ({r['chars']} characters, {r['seconds']} s): "
              f"{r['path'].as_posix()}. Read it (its view beside it: the same name, .md, or -part-<n>.md) and fill its `answer`, then: Collection-Build.ps1 -Action CheckAnswer -File <answer file> until it finds no problem, and -Action RecordStructure -File <answer file>", rows=r["rows"], left=r["left"])


@_logged
def record_structure(ctx: Ctx) -> Outcome:
    """RecordStructure: check a filled ReadStructure answer whole, write it through the recorder of the layered reading, validate the subgroup's rows and name the next command. -Check previews."""
    from ..lib import readcommands as rc
    file = str(ctx.params.get("File", "")).strip()
    if not file:
        return fail("refused", "-File is required: the filled answer of a ReadStructure package")
    conn = ctx.cfg.conn
    try:
        data = _answer_of(json.loads(pathlib.Path(file).read_text(encoding="utf-8")))
        r = rc.record_structure(conn, ctx.cfg, ctx.run_id, data, keep=not _flag(ctx, "Check"))
    except (OSError, ValueError) as exc:
        return fail("refused", f"cannot read {file}: {exc}")
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except rc.ReadError as exc:
        return fail("refused", str(exc))
    line = f"{r['observed']} observations written with {r['nodes']} nodes for {r['rows']} row(s)"
    if r.get("preview"):
        return ok("PREVIEW (nothing written): " + line, observed=r["observed"], nodes=r["nodes"])
    conn.commit()
    tail = f"; check: {r['validated']} validated" + (f", FAILED: {'; '.join(r['failed'])}" if r["failed"] else "") + f"; {r['rows_open']} row(s) still open. Next: {r['next']}"
    return ok(line + tail, observed=r["observed"], nodes=r["nodes"], validated=r["validated"])

def _read_gate(ctx: Ctx, fn_name: str, what: str) -> Outcome:
    from ..lib import layerreading as lr
    from ..lib import readcommands as rc
    from ..lib import scanguard as sg
    coll, sub = str(ctx.params.get("Collection", "")).strip(), str(ctx.params.get("Subgroup", "")).strip()
    if not coll or not sub:
        return fail("refused", f"-Collection and -Subgroup are required ({what} is read one subgroup at a time)")
    root = ctx.cfg.setting("layer.working_dir")
    if not root:
        return fail("refused", "cfg_setting layer.working_dir is missing")
    try:
        r = getattr(rc, fn_name)(ctx.cfg.conn, ctx.cfg, ctx.run_id, coll, sub, pathlib.Path(root))
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except rc.ReadError as exc:
        ctx.cfg.conn.commit()       # a gate answered from the tables (nothing left to sweep or to read) is kept; the message names the next command
        return fail("refused", str(exc))
    except (lr.LayerError, sg.ScanBudgetExceeded) as exc:
        return fail("refused", str(exc))
    ctx.cfg.conn.commit()
    return ok(", ".join(f"{k} {v}" for k, v in r.items() if k != "path") + f": {r['path'].as_posix()}. Read it (its view beside it: the same name, .md, or -part-<n>.md) and fill its `answer`, then CheckAnswer -File <answer> until it finds no problem, and the Record command")


@_logged
def read_sweep(ctx: Ctx) -> Outcome:
    """ReadSweep: the sweep (B4) of one subgroup after its 2.1 rows: the package of its older observations still unmarked, to judge by content (lib/readcommands.py; escalation #2538).
    With nothing left to sweep, the sweep row is answered as such and the next command is named."""
    return _read_gate(ctx, "read_sweep", "the sweep")


@_logged
def read_evidence(ctx: Ctx) -> Outcome:
    """ReadEvidence: the evidence validation (B5) of one subgroup after its sweep: the code checks and the package of the next evidence observations not yet read, to judge for truth and
    coherence (lib/readcommands.py; escalation #2538). With every observation read and the checks passing, the row is answered and the next command is named."""
    return _read_gate(ctx, "read_evidence", "the evidence validation")


def _record_gate(ctx: Ctx, fn_name: str, what: str) -> Outcome:
    from ..lib import readcommands as rc
    file = str(ctx.params.get("File", "")).strip()
    if not file:
        return fail("refused", f"-File is required: the filled answer of a {what} package")
    conn = ctx.cfg.conn
    try:
        data = _answer_of(json.loads(pathlib.Path(file).read_text(encoding="utf-8")))
        r = getattr(rc, fn_name)(conn, ctx.cfg, ctx.run_id, data, keep=not _flag(ctx, "Check"))
    except (OSError, ValueError) as exc:
        return fail("refused", f"cannot read {file}: {exc}")
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except rc.ReadError as exc:
        return fail("refused", str(exc))
    line = ", ".join(f"{k} {v}" for k, v in r.items() if k not in ("preview", "next"))
    if r.get("preview"):
        return ok("PREVIEW (nothing written): " + line)
    conn.commit()
    return ok(line + f". Next: {r['next']}")


@_logged
def release_dead_traces(ctx: Ctx) -> Outcome:
    """ReleaseDeadTraces: every live trace node that points at a deleted observation, across the database, dropped with its reason, logged on its
    holder (lib/validationactions.release_dead_traces; #2618). The deletes made since #2618 release their traces themselves and ReadEvidence
    releases those in its scope; this repairs what is left from before, or from a path that deleted without it. -Check counts and writes nothing."""
    from ..lib import validationactions as va
    from ..lib import dbsnapshot
    conn = ctx.cfg.conn
    check = _flag(ctx, "Check")
    r = va.release_dead_traces(conn, ctx.run_id, "Claude", None, check=True)
    line = f"{r['nodes']} dead trace node(s) on {r['observations']} live observation(s), by marker {r['by_nature']}"
    if check or not r["nodes"]:
        return ok(("PREVIEW (nothing written): " if check else "nothing to release: ") + line)
    snap = dbsnapshot.snapshot("pre-release-dead-traces", named=True)
    r = va.release_dead_traces(conn, ctx.run_id, "Claude", None)
    conn.commit()
    return ok(f"released: {line}; named snapshot {snap}", nodes=r["nodes"], observations=r["observations"])


@_logged
def record_sweep(ctx: Ctx) -> Outcome:
    """RecordSweep: check a filled ReadSweep answer whole and write it; validate the sweep row; name the next command. -Check previews."""
    return _record_gate(ctx, "record_sweep", "ReadSweep")


@_logged
def record_evidence(ctx: Ctx) -> Outcome:
    """RecordEvidence: check a filled ReadEvidence answer whole, write its repairs and log each observation read; validate the evidence-validation row when all is read; name the next
    command. -Check previews."""
    return _record_gate(ctx, "record_evidence", "ReadEvidence")


@_logged
def read_elements(ctx: Ctx) -> Outcome:
    """ReadElements: the package of step 3.1 of one subgroup (C1): the evidence observations to take up and those it may rest on, the older inner-being observations to answer, the
    definition, the meaning by code, every verse, and the answer (lib/readcommands.py; escalation #2538). Opens 3.1 for the subgroup if it is not open."""
    return _read_gate(ctx, "read_elements", "the elements")


@_logged
def record_elements(ctx: Ctx) -> Outcome:
    """RecordElements: check a filled ReadElements answer whole and write it through the recorder of stage 4; validate the 3.1 row; name the next command. -Check previews."""
    return _record_gate(ctx, "record_elements", "ReadElements")

@_logged
def sweep_superseded(ctx: Ctx) -> Outcome:
    """SweepSuperseded: the sweep that closes 3.1 for a collection: every live ledger row of a deleted subgroup retired and the observations written under it removed (nodes
    deleted, traces released, each change kept with its reason; lib/layerreading.sweep_superseded; researcher 2026-11-26, #2538). Refused while a current subgroup is not through
    3.1. A named snapshot first; -Check counts and writes nothing."""
    from ..lib import dbsnapshot
    from ..lib import layerreading as lr
    coll = str(ctx.params.get("Collection", "")).strip()
    if not coll:
        return fail("refused", "-Collection is required")
    conn = ctx.cfg.conn
    try:
        r = lr.sweep_superseded(conn, ctx.cfg, ctx.run_id, coll, check=True)
        line = (f"{r['collection']}: {r['rows']} live ledger row(s) of deleted subgroups ({', '.join(r['subgroups']) or 'none'}; by step {r['rows_by_step']}) holding "
                f"{r['observations']} observation(s)")
        if _flag(ctx, "Check") or not r["rows"]:
            return ok(("PREVIEW (nothing written): " if _flag(ctx, "Check") else "nothing to sweep: ") + line)
        snap = dbsnapshot.snapshot("pre-sweep-superseded", named=True)
        lr.sweep_superseded(conn, ctx.cfg, ctx.run_id, coll)
    except lr.LayerError as exc:
        return fail("refused", str(exc))
    conn.commit()
    return ok(f"swept: {line}; rows retired, observations removed; named snapshot {snap}. Next: Collection-Build.ps1 -Action LayerNext -Collection {coll}",
              rows=r["rows"], observations=r["observations"])


@_logged
def read_behaviours(ctx: Ctx) -> Outcome:
    """ReadBehaviours: the package of step 3.2 of a collection (C2): every inner-being observation of the collection to take up, each with its subgroups and occurrences, the subgroups
    with their definitions, and the answer (lib/readcommands.py; escalation #2538). Opens 3.2 if it is not open. -Collection only: 3.2 is the collection's own step."""
    from ..lib import layerreading as lr
    from ..lib import readcommands as rc
    from ..lib import scanguard as sg
    coll = str(ctx.params.get("Collection", "")).strip()
    if not coll:
        return fail("refused", "-Collection is required (3.2 reads the whole collection; it takes no -Subgroup)")
    root = ctx.cfg.setting("layer.working_dir")
    if not root:
        return fail("refused", "cfg_setting layer.working_dir is missing")
    try:
        r = rc.read_behaviours(ctx.cfg.conn, ctx.cfg, ctx.run_id, coll, pathlib.Path(root))
    except rc.ReadNext as exc:
        ctx.cfg.conn.commit()       # not a fault: the unit is read or has nothing to read; the message names the next command (#2637 X5)
        return ok(str(exc))
    except rc.ReadError as exc:
        return fail("refused", str(exc))
    except (lr.LayerError, sg.ScanBudgetExceeded) as exc:
        return fail("refused", str(exc))
    ctx.cfg.conn.commit()
    return ok(", ".join(f"{k} {v}" for k, v in r.items() if k != "path") + f": {r['path'].as_posix()}. Read it (its view beside it: the same name, .md, or -part-<n>.md) and fill its `answer`, then CheckAnswer -File <answer> until it finds no problem, and RecordBehaviours -File <answer>")


@_logged
def record_behaviours(ctx: Ctx) -> Outcome:
    """RecordBehaviours: check a filled ReadBehaviours answer whole and write it through the recorder of stage 4; validate the 3.2 row; name the next command. -Check previews."""
    return _record_gate(ctx, "record_behaviours", "ReadBehaviours")


def layer_check(ctx: Ctx) -> Outcome:
    """Validate every answered row of a collection against the tables, set `validated`, and write the findings as a versioned Markdown report (cfg_setting layer.check_name)."""
    import datetime

    from ..lib import layerreading as lr
    conn = ctx.cfg.conn
    coll = str(ctx.params.get("Collection", "")).strip()
    root, stem = ctx.cfg.setting("surfaces.exports_root"), ctx.cfg.setting("layer.check_name")
    if not root or not stem:
        return fail("refused", "cfg_setting surfaces.exports_root or layer.check_name is missing")
    try:
        rep = lr.check(conn, ctx.cfg, ctx.run_id, coll, subgroup=str(ctx.params.get("Subgroup", "")).strip() or None)
        archive = ctx.cfg.required_setting("governance.oneoff_report_archive_dir")
    except (lr.LayerError, ValueError) as exc:
        return fail("refused", str(exc))
    conn.commit()
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    L = [f"# Layered reading check: {rep['collection']}", "",
         f"Generated {stamp} by run {ctx.run_id} (`Collection-Build.ps1 -Action LayerCheck`, escalation #2505). Sets `validated` on the ledger rows it passes; nothing else is written.", "",
         "## Gates", "",
         f"- stage 1 (the lexical analysis of the words, step S1): {rep['lexical']['rows']} rows" + (" (closed)" if rep["lexical"]["closed"] else " (not closed)")]
    L += [f"- grouping: {g}" for g in rep["grouping"]]
    if not rep["grouping"]:
        L += ["- grouping: finished (every surface placed or isolated)"]
    for step, r in rep["steps"].items():
        L += ["", f"## Step {step}: {'closed' if r['closed'] else 'not closed'}", "",
              f"{r['rows']} rows; {r['validated']} validated; {r['open']} open; {len(r['failed'])} failed; {len(r['not_in_ledger'])} demanded by the data and not in the ledger (LayerOpen)."]
        L += [f"- failed: {x}" for x in r["failed"][:100]] + [f"- {x}" for x in r["not_in_ledger"][:100]]
    base = pathlib.Path(root) / f"{stem}.md"
    path = reportkit.next_versioned_path(base, archive)
    path.parent.mkdir(parents=True, exist_ok=True)
    reportkit._archive_prior_versions(base, archive)
    path.write_text("\n".join(L) + "\n", encoding="utf-8")
    closed = [k for k, r in rep["steps"].items() if r["closed"]]
    gate = "closed" if rep["lexical"]["closed"] else "not closed"
    return ok(f"{rep['collection']}: stage 1 (lexical analysis) {gate}; grouping {'unfinished' if rep['grouping'] else 'finished'}; "
              f"steps closed: {', '.join(closed) or 'none'} -- report {path.as_posix()} ({_register(ctx, path)})", closed=len(closed))


def node_groups(ctx: Ctx) -> Outcome:
    """Set ib_node.subgroup_id of the live nodes from the collection index; -Check previews. Every change is kept with its reason."""
    from ..lib import layerreading as lr
    conn = ctx.cfg.conn
    r = lr.node_groups(conn, ctx.run_id, dry=_flag(ctx, "Check"))
    line = f"{r['changed']} nodes differ from the index ({r['set']} to set, {r['cleared']} to clear); {r['unchanged']} agree"
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written): " + line, **r)
    conn.commit()
    return ok(line + " -- changed", **r)


def group_pull(ctx: Ctx) -> Outcome:
    """Write the working file for the grouping of a collection's surfaces by their meaning in context (stage 2, #2509, #2526): one row for each surface, with its verses, codes and stage 1 results."""
    from ..lib import collectiongroup as cg
    conn = ctx.cfg.conn
    coll = str(ctx.params.get("Collection", "")).strip()
    root = ctx.cfg.setting("layer.working_dir")
    if not root:
        return fail("refused", "cfg_setting layer.working_dir is missing")
    try:
        path, n = cg.pull(conn, ctx.cfg, coll, pathlib.Path(root))
    except (cg.GroupError, ValueError) as exc:
        return fail("refused", str(exc))
    return ok(f"working file with {n} rows (one for each surface): {path.as_posix()}. The file holds each surface with what WordNet says of it and a seed grouping (a surface with no WordNet entry is a subgroup on its own); no verse is read here. Place each surface whole in the subgroup of its meaning, or set_aside with the reason where it is plainly not a member; define each subgroup in a sentence; then "
              f"Collection-Build.ps1 -Action GroupRecord -File <file> -Check", rows=n)


def group_record(ctx: Ctx) -> Outcome:
    """Check a filled grouping file whole and write the groups and placements in one transaction (-Check previews); the scrutiny report is written after a real record."""
    import datetime

    from ..lib import collectiongroup as cg
    conn = ctx.cfg.conn
    file = str(ctx.params.get("File", "")).strip()
    if not file:
        return fail("refused", "-File is required: the filled working file from GroupPull")
    try:
        data = json.loads(pathlib.Path(file).read_text(encoding="utf-8"))
        r = cg.record(conn, ctx.cfg, ctx.run_id, data, keep=not _flag(ctx, "Check"), file_name=pathlib.Path(file).name)
    except (OSError, ValueError) as exc:
        return fail("refused", f"cannot read {file}: {exc}")
    except (cg.GroupError, ci_error()) as exc:
        return fail("refused", str(exc))
    line = (f"{r['groups_made']} groups made, {r['groups_redefined']} redefined, {r['groups_retired']} retired; {r['placed']} surfaces placed, {r['set_aside']} set aside, {r['unchanged']} unchanged")
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written): " + line, **r)
    conn.commit()
    path_note = ""
    root, stem = ctx.cfg.setting("surfaces.exports_root"), ctx.cfg.setting("group.report_name")
    if root and stem:
        archive = ctx.cfg.required_setting("governance.oneoff_report_archive_dir")
        base = pathlib.Path(root) / f"{stem}-{data['collection']}.md"
        path = reportkit.next_versioned_path(base, archive)
        path.parent.mkdir(parents=True, exist_ok=True)
        reportkit._archive_prior_versions(base, archive)
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        path.write_text(chr(10).join(cg.report_lines(conn, data["collection"]) + [f"_Generated {stamp} by run {ctx.run_id} (`Collection-Build.ps1 -Action GroupRecord`, escalation #2509)._"]) + chr(10), encoding="utf-8")
        path_note = f" -- scrutiny report {path.as_posix()} ({_register(ctx, path)})"
    return ok(line + path_note, **r)


def ci_error():
    from ..lib import collectionindex as ci
    return ci.IndexError_


# ══ the validation after stage 4 (#2538) ═════════════════════════════════════════════════════════════
def _versioned_report(ctx: Ctx, stem_key: str, collection: str, lines: list[str]) -> pathlib.Path:
    root, stem = ctx.cfg.setting("surfaces.exports_root"), ctx.cfg.setting(stem_key)
    if not root or not stem:
        raise ValueError(f"cfg_setting surfaces.exports_root or {stem_key} is missing")
    archive = ctx.cfg.required_setting("governance.oneoff_report_archive_dir")
    base = pathlib.Path(root) / f"{stem}-{collection}.md"
    path = reportkit.next_versioned_path(base, archive)
    path.parent.mkdir(parents=True, exist_ok=True)
    reportkit._archive_prior_versions(base, archive)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def validate_pull(ctx: Ctx) -> Outcome:
    """The scope of a collection with the structural tests: a Markdown report, and the working file of every in-scope observation to read (read-only on the tables)."""
    import datetime

    from ..lib import collectionvalidate as cv
    conn = ctx.cfg.conn
    name = str(ctx.params.get("Collection", "")).strip()
    wd = ctx.cfg.setting("layer.working_dir")
    if not wd:
        return fail("refused", "cfg_setting layer.working_dir is missing")
    try:
        cid = cv.collection_id(conn, name)
        res = cv.pull(conn, ctx.cfg, cid)
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        lines = cv.report_lines(conn, ctx.cfg, name, res) + ["", f"_Generated {stamp} by run {ctx.run_id} (`Collection-Build.ps1 -Action ValidatePull`, escalation #2538). Nothing was written to a table._"]
        path = _versioned_report(ctx, "validate.pull_name", name, lines)
        wpath = pathlib.Path(wd) / f"validate-{name}.json"
        wpath.parent.mkdir(parents=True, exist_ok=True)
        wpath.write_text(json.dumps(cv.worksheet(conn, res, name), ensure_ascii=False, indent=1), encoding="utf-8")
    except (cv.ValidateError, ValueError, OSError) as exc:
        return fail("refused", str(exc))
    f = res["findings"]
    return ok(f"{name}: {res['scope']['union']} observations in scope to judge ({res['scope'].get('built', 0)} validated by the build and not judged again); {len(f.get('unmarked', []))} not marked; {len(f.get('word_missing', []))} word nodes missing a required column; "
              f"{len(f.get('no_node', []))} without a node; {len(f.get('traced_dead', []))} traces to a deleted observation -- report {path.as_posix()} ({_register(ctx, path)}), "
              f"working file {wpath.as_posix()}. Read each observation, then write the sheet of actions and Collection-Build.ps1 -Action ValidateRecord -File <sheet> -Check",
              observations=res["scope"]["union"])


def validate_record(ctx: Ctx) -> Outcome:
    """Check a sheet of actions whole and write it in one transaction (-Check runs every action and rolls back). Any problem refuses the whole sheet."""
    from ..lib import collectionvalidate as cv
    conn = ctx.cfg.conn
    file = str(ctx.params.get("File", "")).strip()
    if not file:
        return fail("refused", "-File is required: the sheet of actions")
    try:
        data = json.loads(pathlib.Path(file).read_text(encoding="utf-8"))
        r = cv.record(conn, ctx.cfg, ctx.run_id, data, keep=not _flag(ctx, "Check"))
    except (OSError, ValueError) as exc:
        return fail("refused", f"cannot read {file}: {exc}")
    except cv.ValidateError as exc:
        return fail("refused", str(exc))
    line = f"{r['actions']} actions ({', '.join(f'{k} {v}' for k, v in sorted(r['by_action'].items()))}); observations created: {r['created']}"
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written): " + line, actions=r["actions"])
    conn.commit()
    return ok(line + ". Next: Collection-Build.ps1 -Action ValidateCheck", actions=r["actions"])


def validate_check(ctx: Ctx) -> Outcome:
    """The completeness check of a collection's validation in two layers (evidence first); writes the findings as a versioned Markdown report. Writes nothing to a table."""
    import datetime

    from ..lib import collectionvalidate as cv
    conn = ctx.cfg.conn
    name = str(ctx.params.get("Collection", "")).strip()
    try:
        cid = cv.collection_id(conn, name)
        g = cv.check(conn, ctx.cfg, cid)
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        lines = cv.report_lines(conn, ctx.cfg, name, g["result"], gates=g) + ["", f"_Generated {stamp} by run {ctx.run_id} (`Collection-Build.ps1 -Action ValidateCheck`, escalation #2538)._"]
        path = _versioned_report(ctx, "validate.check_name", name, lines)
    except (cv.ValidateError, ValueError, OSError) as exc:
        return fail("refused", str(exc))
    return ok(f"{name}: evidence layer {'passes' if g['evidence_passes'] else 'does not pass'}; inner-being layer "
              f"{'passes' if g['inner_being_passes'] else ('does not pass' if g['evidence_passes'] else 'not judged')} -- report {path.as_posix()} ({_register(ctx, path)})",
              evidence=int(g["evidence_passes"]), inner_being=int(g["inner_being_passes"]))


def attach_phrases(ctx: Ctx) -> Outcome:
    """Connect the phrases of collection a to collections by their words, then by their own Strong's codes; the phrases neither reaches are flagged
    phrase_no_match (escalation #2437). -Reason (the instruction, quoted, with the escalation id); -Check previews."""
    conn = ctx.cfg.conn
    if not _flag(ctx, "Check"):
        return fail("refused", "the phrase rule is retired (escalation #2491 step 4, BUILD 502): a phrase is one concept placed in one collection by meaning, "
                    "not attached to the collections of each of its words. A preview (-Check) still runs.")
    scope = ctx.cfg.setting("surfaces.scope_groups")
    tiers = ctx.cfg.setting("collection.export_tiers")
    if not scope or "a" not in scope or not tiers:
        return fail("refused", "cfg_setting surfaces.scope_groups (collection a) or collection.export_tiers is missing")
    try:
        r = cb.attach_phrases(conn, ctx.run_id, scope["a"], tiers, ctx.params.get("Reason") or "", dry=_flag(ctx, "Check"))
    except cb.CollectionError as exc:
        return fail("refused", str(exc))
    line = (f"{r['phrases']} phrases: {r['english']} reached by an English word, {r['strong']} by an own Strong's code, {r['unmatched']} reached by neither; "
            f"links to add {r['links_to_add']}, flags to add {r['flags_to_add']}")
    if _flag(ctx, "Check"):
        return ok("PREVIEW (nothing written): " + line, **r)
    conn.commit()
    return ok("written: " + line, **r)


def merge(ctx: Ctx) -> Outcome:
    conn = ctx.cfg.conn
    reason = (ctx.params.get("Reason") or "").strip()
    try:
        src = _collection(conn, ctx.params.get("From"))
        dst = _collection(conn, ctx.params.get("Into"))
    except cb.CollectionError as exc:
        return fail("refused", str(exc))
    if src[0] == dst[0]:
        return fail("refused", "-From and -Into are the same collection")
    if not reason:
        return fail("refused", "-Reason is required: why the collections are merged (on your instruction)")
    if "merged" in (src[2], dst[2]) or "retired" in (src[2], dst[2]):
        return fail("refused", "both collections must be indicative or confirmed")
    moved = 0
    for lid, term, tier, shared in conn.execute("SELECT id, term_id, tier, shared FROM collection_link WHERE collection_id=? AND deleted=0", (src[0],)).fetchall():
        has = conn.execute("SELECT 1 FROM collection_link WHERE collection_id=? AND term_id=? AND deleted=0", (dst[0], term)).fetchone()
        conn.execute("UPDATE collection_link SET deleted=1, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), run_id=? WHERE id=?", (ctx.run_id, lid))
        if not has and tier != "core":
            new = conn.execute("INSERT INTO collection_link (collection_id, term_id, tier, shared, reason, run_id, created_by) VALUES (?,?,?,?,?,?,'collection-build')",
                               (dst[0], term, tier, shared, f"merged from {src[1]}", ctx.run_id)).lastrowid
            conn.execute("UPDATE collection_link SET superseded_by_id=? WHERE id=?", (new, lid))
            moved += 1
    conn.execute("UPDATE collection SET status='merged', merged_into_id=?, updated_at=strftime('%Y-%m-%dT%H:%M:%SZ','now'), run_id=? WHERE id=?", (dst[0], ctx.run_id, src[0]))
    _event(conn, ctx.run_id, src[0], "merge", src[2], f"merged into {dst[1]}", reason)
    conn.commit()
    return ok(f"{src[1]} merged into {dst[1]}: {moved} links moved, the rest were already there or the core word; reason: {reason}. The words of the merged collection's "
              "judgements no longer map to the target, so Status will list them as stored links the judgements do not produce (kept)", moved=moved)


def _client_batch(ctx, step, label, work):
    """Common shell of the two AI steps: a run_batch row, the server session, halting and refusals. work(client, conn) -> (message, counts)."""
    import sys
    import time

    from ..lib import aiclient as ai
    from ..lib import batchcontrol as bc
    from ..lib import collectionask as ca
    from ..lib import surfacejudge as sj
    conn = ctx.cfg.conn
    try:
        vals = ca.read_settings(ctx.cfg)
        client = ai.AiClient(ctx.cfg, "collection", step, ctx.run_id)
        for key in ("collection.pole", "collection.real_word", "collection.list", "collection.synonym", "collection.score", "collection.associated"):
            client.prompt(key)
        client.model("judge"), client.model(vals["collection.embed_role"])
        plan_ = work(None, vals, client, True)       # a dry pass: validates the arguments and returns the number of calls to make
    except (ca.AskError, ai.AiError) as exc:
        return fail("refused", str(exc))
    bid = bc.start_batch(conn, ctx.run_id, "collection-build", step, f"{label}:{ctx.run_id}", 1, bc.content_key([str(plan_)]))
    client.batch_id = bid
    t0 = time.time()
    try:
        with client.session(["judge", vals["collection.embed_role"]]):
            msg, counts = work(conn, vals, client, False)
    except ai.AiHalted as exc:
        conn.execute("UPDATE run_batch SET model_role='judge', model=?, secs=? WHERE id=?", (client.model("judge")[1], round(time.time() - t0, 1), bid))
        bc.fail_batch(conn, bid, str(exc))
        return fail("halted", f"halted: {exc}")
    except (ca.AskError, ai.AiError, sj.JudgeError) as exc:
        bc.fail_batch(conn, bid, str(exc))
        return fail("refused", str(exc))
    n = conn.execute("SELECT count(*) FROM ai_call WHERE batch_id=?", (bid,)).fetchone()[0]
    conn.execute("UPDATE run_batch SET model_role='judge', model=?, calls=?, secs=? WHERE id=?", (client.model("judge")[1], n, round(time.time() - t0, 1), bid))
    bc.commit_batch(conn, bid)
    print(msg, file=sys.stderr, flush=True)
    return ok(f"{msg}; batch {bid}, {n} calls. Next: Collection-Build.ps1 -Action Links", **counts)


def seed(ctx: Ctx) -> Outcome:
    """Make a collection of a core word: its pole (and whether it is a real word and reciprocal) and the model's own list of synonyms and opposites, through
    the AI client. -Word is the core word (a single word of collection a)."""
    from ..lib import collectionask as ca
    word = (ctx.params.get("Word") or "").strip()
    if not word:
        return fail("refused", "-Word is required: the core word of the new collection")

    def work(conn, vals, client, dry):
        c = ctx.cfg.conn
        pool = ca.pool_words(c, vals)
        if word.lower() not in pool:
            raise ca.AskError(f"{word!r} is not a single word of collection a")
        if c.execute("SELECT 1 FROM collection WHERE core_term_id=? AND deleted=0 AND status!='retired'", (pool[word.lower()],)).fetchone():
            raise ca.AskError(f"{word!r} already has a collection")
        if dry:
            return word.lower(), {}
        r = ca.seed_collection(c, client, vals, word, ctx.run_id)
        return (f"collection {word.lower()} made (id {r['collection']}): pole {r['pole']}, pole of the pole {r['pole_of_pole']}, real word {r['real']}, "
                f"{r['listed']} words listed by the model"), {"collection": r["collection"], "listed": r["listed"]}

    return _client_batch(ctx, "collection.seed", "seed", work)


def ask(ctx: Ctx) -> Outcome:
    """Judge the candidates of a collection through the AI client (the shortlist by embedding plus the listed words), -Limit n at most."""
    from ..lib import collectionask as ca
    limit = ctx.params.get("Limit")
    if limit not in (None, "") and not str(limit).isdigit():
        return fail("refused", f"-Limit is a whole number, not {limit!r}")
    limit = int(limit) if limit not in (None, "") and int(limit) > 0 else None
    try:
        c = _collection(ctx.cfg.conn, ctx.params.get("Collection"))
    except cb.CollectionError as exc:
        return fail("refused", str(exc))
    if c[2] not in ("indicative", "confirmed"):
        return fail("refused", f"{c[1]!r} is {c[2]}: only an indicative or confirmed collection is asked")

    def work(conn, vals, client, dry):
        if dry:
            return c[1], {}
        cands = ca.candidates(ctx.cfg.conn, client, vals, c[0], limit)
        done = {"synonym": 0, "opposite": 0, "distinct": 0, "not_usable": 0}
        for w, tid in cands:
            r = ca.judge_candidate(ctx.cfg.conn, client, vals, c[0], c[3], c[4], w, tid)
            done[r["relation"] or "not_usable"] += 1
        return (f"{c[1]}: judged {len(cands)} words: {done['synonym']} synonym, {done['opposite']} opposite, {done['distinct']} distinct, "
                f"{done['not_usable']} not usable"), {"judged": len(cands)}

    return _client_batch(ctx, "collection.ask", "ask", work)
