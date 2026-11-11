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
    return ok(f"{len(rows)} links of {len({r[0] for r in rows})} collections written to {path.as_posix()} (a view of the tables, not an input); run Manifest-Rebuild.ps1 to register it", rows=len(rows))


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
    return ok(f"{len(rows)} rows of the {view} view written to {path.as_posix()} (a view of the tables, not an input); run Manifest-Rebuild.ps1 to register it", rows=len(rows))


def export_members(ctx: Ctx) -> Outcome:
    return _export_view(ctx, "members-verses")


def export_surfaces(ctx: Ctx) -> Outcome:
    return _export_view(ctx, "surfaces")


def evidence(ctx: Ctx) -> Outcome:
    """The evidence report (#2464, #2467, lib/collectionevidence.py) of one collection or a comma list (-Collection), or of a verse or list of verses (-Verse, items
    separated by a semicolon): the stored entries from the base data through the observations and the claims into the narrative, as a Markdown file and a CSV under
    surfaces.exports_root (the folder of the collection exports and of the results of surface analysis, #2361), versioned by the filing rule (the previous live versions archived). The layout is by word (or verse) then by type; -ByType gives one
    section for each type. Read-only on the tables; -Check builds the report and writes no file."""
    import datetime
    from ..lib import collectionevidence as ev
    conn = ctx.cfg.conn
    by_type = _flag(ctx, "ByType")
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
        archive = ctx.cfg.required_setting("governance.oneoff_report_archive_dir")
    except (ev.EvidenceError, ValueError) as exc:
        return fail("refused", str(exc))
    if verse:
        slug = "-".join(re.sub(r"[^a-z0-9]+", "-", v["reference"].lower()).strip("-") for v in datas[0]["verses"][:3])
        stem = f"{vals['verse_name']}-{slug}" if len(datas[0]["verses"]) <= 3 else f"{vals['verse_name']}-{len(datas[0]['verses'])}-verses"
    else:
        slug = "-".join(re.sub(r"[^a-z0-9]+", "-", d["name"].lower()).strip("-") for d in datas)
        stem = f"{vals['name']}-{slug}" if len(slug) <= 60 else f"{vals['name']}-{len(datas)}-collections"
    if by_type:
        stem += "-by-type"
    rows = ev.csv_rows(datas)
    summary = "; ".join(f"{d['name']}: {len(d['occurrences'])} occurrences, {len(d['observations'])} observations, {len(d['claims'])} claims, {len(d['sections'])} narrative sections, "
                        f"{sum(1 for f in d['faults'] if f['rows'])} fault rules with findings" for d in datas)
    if _flag(ctx, "Check"):
        return ok(f"PREVIEW (nothing written): {summary}; {len(rows)} CSV rows", rows=len(rows))
    base = pathlib.Path(vals["path"]) / f"{stem}.md"
    md_path = reportkit.next_versioned_path(base, archive)
    csv_path = md_path.with_suffix(".csv")
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    text = ev.render(datas, ctx.run_id, stamp, by_type)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    live = {f for f in md_path.parent.glob(f"{stem}-v*") if f.is_file()}
    try:
        reportkit._archive_prior_versions(base, archive)
        reportkit._archive_prior_versions(base.with_suffix(".csv"), archive)
    except OSError as exc:     # a previous file is open in another program: put back what was moved, write nothing
        for f in live:
            moved = md_path.parent / archive / f.name
            if not f.exists() and moved.exists():
                moved.replace(f)
        return fail("refused", f"a previous version of this report is in use by another program ({exc}); close it and run again; nothing was written")
    md_path.write_text(text, encoding="utf-8")
    ev.write_csv(csv_path, datas[0]["kind"], rows)
    return ok(f"{summary}\n  written: {md_path.as_posix()} and {csv_path.as_posix()} ({len(rows)} CSV rows; a view of the tables, not an input); run Manifest-Rebuild.ps1 to register them",
              rows=len(rows))


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


def attach_phrases(ctx: Ctx) -> Outcome:
    """Connect the phrases of collection a to collections by their words, then by their own Strong's codes; the phrases neither reaches are flagged
    phrase_no_match (escalation #2437). -Reason (the instruction, quoted, with the escalation id); -Check previews."""
    conn = ctx.cfg.conn
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
