"""strandreading.py -- the reading process (escalation #2172; design
`outputs/escalation/2172-reading-process-design-v2-20261022.md`, build plan
`outputs/escalation/2172-process-build-plan-v1-20261022.md`).

Claude does the reading and the writing in the session; the app gives everything already known,
records the results as rows and checks facts. Where judgement is needed it shows the texts side by
side; it refuses only on a fact. One strand at a time:

  define    a strand: its word family (reading_strand, reading_strand_strong) and its escalation
  1 context every hit (a strand strong in a verse, reading_strand_hit) with its text and lexical
            data, every observation already on those strongs and verses, the open thread items that
            match, each verse's coverage status -> a context file
  2 record  the reading: observations (recordingpass, grounded through ib_node, quote-checked), a
            face or a stated reason for each hit read; read verses -> 'analysed'
  3 gather  every block of the narrative related to the strand, with its text and its tellings
  4 map     each related block's statements to the claims register; a statement with no claim
            becomes a new claim or an item on the strand's escalation (build decision 4)
  5 derive  new, adjusted and withdrawn claims, each resting on observations or verses; each
            observation's disposition (claim, held, silent, withdrawn)
  6 rewrite blocks written anew, whole (narrativeregister.rewrite, safeguard 3); cited verses ->
            'citated'
  7 account the strand from the tables, gaps as text; account_gaps() is also the close gate

Open items (#2219): Context records every open thread item that matches the strand (its words, the
clusters they sit in, its verses, its code; escalation.match_open_items) as an item to answer
(reading_strand_item 'matched'). Record, Map and Derive raise the new items they find on the strand's
own thread (reading_strand.thread_id, raised on first use; reading_strand_item 'raised'). A matched
item is answered by a thread response (Escalation.ps1 -Action Update -Id OT-nn -Item ...); the close
gate refuses while one has no response since it was matched.

Every write action validates first and raises Refused before writing; a refusal inside a write is
rolled back (narrativeregister._atomic). Writes go through narrativeregister.Writer (cfg_write_grant);
ib_observation/ib_node only through recordingpass; thread items only through escalation.
"""
from __future__ import annotations

import json
import pathlib

from . import escalation
from . import narrativeregister as nr
from . import quotecheck
from . import recordingpass
from . import versemeta
from .db import Db

Refused = nr.Refused
PARTS = recordingpass.STRAND_PARTS


# ══ lookups ═════════════════════════════════════════════════════════════════════════════════════
def strand(conn, code: str | None):
    if not (code or "").strip():
        raise Refused("-Strand (the strand's code) is required")
    r = conn.execute("SELECT * FROM reading_strand WHERE code=?", (code.strip(),)).fetchone()
    if r is None:
        raise Refused(f"strand {code!r} does not exist (Strand-Reading.ps1 -Step Define)")
    return r


def _open_strand(conn, code):
    s = strand(conn, code)
    if s["state"] != "open":
        raise Refused(f"strand {s['code']} is {s['state']}")
    return s


def _strongs(conn, sid: int) -> list[str]:
    return [r[0] for r in conn.execute("SELECT strong FROM reading_strand_strong WHERE strand_id=? ORDER BY strong",
                                       (sid,))]


def _load_json(p: dict) -> dict:
    f = pathlib.Path(p.get("File") or "")
    if not f.is_absolute():
        f = nr.PROJECT_ROOT / f
    if not f.is_file():
        raise Refused(f"-File {p.get('File')!r} not found")
    try:
        return json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise Refused(f"-File is not valid JSON: {exc}") from exc


def _verse(conn, vx, ref: str | None):
    """A verse named as osisId ('Gen.6.5') or as written in the narrative ('Gen 6:5')."""
    if not ref:
        raise Refused("a verse reference is required")
    r = conn.execute("SELECT id, osisId, reference FROM verse WHERE osisId=? AND deleted=0", (ref,)).fetchone()
    if r:
        return r
    refs = nr.parse_refs(ref, vx, follow_ons=False)
    if len(refs) != 1 or refs[0].verse_id is None:
        raise Refused(f"{ref!r} is not one verse")
    return conn.execute("SELECT id, osisId, reference FROM verse WHERE id=?", (refs[0].verse_id,)).fetchone()


def _cluster_name(conn, code: str) -> str:
    r = conn.execute("SELECT short_name FROM cluster WHERE cluster_code=?", (code,)).fetchone()
    return f"{code} {r[0]}" if r and r[0] else code


def _word(conn, strong: str) -> str:
    r = conn.execute("SELECT stepTransliteration, stepGloss FROM strong WHERE strongNumber=?", (strong,)).fetchone()
    return f"{strong} {r[0] or ''} ({r[1] or ''})".replace(" ()", "") if r else strong


def _cell(s) -> str:
    return nr._cell(None if s is None else str(s))


def _quote_check(conn, cfg, texts: list[str], where: str) -> list[str]:
    corpus = quotecheck.Corpus(conn)
    _, bad = quotecheck.check_lines(corpus, [t for x in texts if x for t in x.split("\n")],
                                    int(cfg.required_setting("narrative.quote_min_words")), quotecheck.titles(conn))
    return [f"{where}: \"{b}\"" for b in bad]


def strand_observations(conn, sid: int) -> list:
    """The strand's observations: every live strand-reading observation grounded on one of its hits."""
    return conn.execute(
        "SELECT DISTINCT o.* FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id JOIN verse v ON "
        "v.osisId=n.verse_reference JOIN reading_strand_hit h ON h.verse_id=v.id AND h.strong=n.strong "
        "WHERE h.strand_id=? AND o.stage=? ORDER BY o.id", (sid, recordingpass.STRAND_STAGE)).fetchall()


# ══ open items (#2219) ══════════════════════════════════════════════════════════════════════════
def strand_clusters(conn, s) -> list[str]:
    """The strand's home cluster and every cluster its words are assigned to."""
    return sorted({s["cluster_code"]} | {r[0] for r in conn.execute(
        "SELECT DISTINCT cs.cluster_code FROM cluster_strong cs JOIN reading_strand_strong ss ON ss.strong=cs.strong "
        "WHERE ss.strand_id=? AND COALESCE(cs.deleted, 0)=0", (s["id"],))})


def match_items(cfg, w: nr.Writer, s) -> int:
    """Every open item matching the strand, not yet recorded against it, recorded as 'matched'."""
    conn = cfg.conn
    verses = [r[0] for r in conn.execute(
        "SELECT DISTINCT v.reference FROM reading_strand_hit h JOIN verse v ON v.id=h.verse_id WHERE h.strand_id=? "
        "AND v.reference IS NOT NULL", (s["id"],))]
    why: dict[int, set] = {}
    for _, it, q in escalation.match_open_items(Db(cfg), clusters=strand_clusters(conn, s), strongs=_strongs(
            conn, s["id"]), verses=verses, strands=[s["code"]]):
        why.setdefault(it["id"], set()).add(q)
    n = 0
    for iid, qs in why.items():
        if not conn.execute("SELECT 1 FROM reading_strand_item WHERE strand_id=? AND item_id=?", (s["id"], iid)).fetchone():
            on = ", ".join(sorted(qs))
            w.insert("reading_strand_item", {"strand_id": s["id"], "item_id": iid, "source": "matched",
                                             "matched_on": on if len(on) <= 300 else on[:297] + "..."})
            n += 1
    return n


def item_specs(cfg, specs, at: str, errors: list) -> list[tuple]:
    """'kind:value :: note' -> (kind, value, note), checked before anything is written."""
    kinds = cfg.enum("escalation_thread_item_kind")
    out = []
    for sp in specs or []:
        try:
            k, v, n = escalation.parse_item_spec(str(sp))
        except ValueError as exc:
            errors.append(f"{at}: {exc}")
            continue
        if k not in kinds or not v:
            errors.append(f"{at}: item {sp!r} needs kind:value, kind one of {kinds}")
            continue
        out.append((k, v, n))
    return out


def raise_items(cfg, w: nr.Writer, s, items: list[tuple], where: str) -> list[str]:
    """New open items on the strand's own thread (raised on first use, or again when the last one
    completed), each linked to the strand as 'raised'; an item already open there is reused.
    Returns 'OT-nn.n' for each. Runs inside the step's transaction."""
    if not items:
        return []
    conn, db = cfg.conn, Db(cfg)
    s = conn.execute("SELECT * FROM reading_strand WHERE id=?", (s["id"],)).fetchone()
    tid = s["thread_id"]
    if tid is not None and escalation._current(db, tid)["state"] not in escalation._THREAD_OPEN_STATES:
        tid = None
    try:
        if tid is None:
            tid = escalation.raise_new(
                cfg, db, f"Open items from strand {s['code']}"[:60], "strandreading", "thread",
                comment=f"Open items found while reading strand {s['code']} ({s['title']}, #{s['escalation_id']}); "
                        f"raised by Strand-Reading ({where}, #2219).",
                resolution_kind="self_correctable", originator=w.who,
                comes_back_when="a strand whose words, clusters or verses match an item (Strand-Reading Context)",
                items=items)
            w.update("reading_strand", {"id": s["id"]}, {"thread_id": tid})
        else:
            have = {(r["kind"], r["value"].lower()): r for r in escalation._thread_items(db, tid)}
            new = [i for i in items if (i[0], i[1].lower()) not in have]
            for k, v, _ in items:
                r = have.get((k, v.lower()))
                if r is not None and r["status"] != "open":
                    escalation.update(cfg, db, tid, item_refs=[str(r["item_no"])], response_kind="reopened",
                                      respond=f"found again reading strand {s['code']} ({where})", originator=w.who)
            if new:
                escalation.update(cfg, db, tid, add_items=new, originator=w.who)
    except ValueError as exc:
        raise Refused(f"the open item(s) could not be raised: {exc}") from exc
    alias = escalation._current(db, tid)["alias"]
    refs = []
    for k, v, _ in items:
        it = conn.execute("SELECT id, item_no FROM escalation_thread_item WHERE escalation_id=? AND kind=? AND "
                          "value=? COLLATE NOCASE", (tid, k, v)).fetchone()
        if not conn.execute("SELECT 1 FROM reading_strand_item WHERE strand_id=? AND item_id=?",
                            (s["id"], it["id"])).fetchone():
            w.insert("reading_strand_item", {"strand_id": s["id"], "item_id": it["id"], "source": "raised",
                                             "matched_on": where})
        refs.append(f"{alias}.{it['item_no']}")
    return refs


def strand_items(conn, sid: int) -> list:
    """The strand's items with their state: the latest response since each was recorded."""
    return conn.execute(
        "SELECT ri.source, ri.matched_on, ri.created_at, i.id item_id, i.item_no, i.kind, i.value, i.status, i.note, "
        "e.alias, (SELECT r.kind || ': ' || r.text FROM escalation_thread_item_response r WHERE r.item_id=i.id AND "
        "r.responded_at >= ri.created_at ORDER BY r.id DESC LIMIT 1) answer FROM reading_strand_item ri JOIN "
        "escalation_thread_item i ON i.id=ri.item_id JOIN escalation e ON e.id=i.escalation_id AND "
        "e.version=(SELECT MAX(version) FROM escalation x WHERE x.id=e.id) WHERE ri.strand_id=? "
        "ORDER BY ri.source, e.id, i.item_no", (sid,)).fetchall()


# ══ define ══════════════════════════════════════════════════════════════════════════════════════
def define(cfg, w: nr.Writer, p: dict) -> str:
    """A new strand (-Strand -Title -Cluster -Escalation -Strongs), or more words for an open one
    (-Strand -Strongs). A strong must be in live verse_lexical exactly as given (suffixed codes)."""
    conn = cfg.conn
    code = (p.get("Strand") or "").strip()
    if not code or code != code.lower() or " " in code:
        raise Refused("-Strand is the strand's code, lowercase-hyphenated (e.g. flesh-body)")
    strongs = [s.strip() for s in (p.get("Strongs") or "").split(",") if s.strip()]
    if not strongs:
        raise Refused("-Strongs (comma-separated Strong's codes, e.g. H1320,G4561) is required")
    bad = [s for s in strongs if not conn.execute("SELECT 1 FROM verse_lexical WHERE strong=? AND deleted=0 "
                                                  "LIMIT 1", (s,)).fetchone()]
    if bad:
        raise Refused(f"no live verse_lexical occurrence of {bad} (exact, zero-padded and suffixed codes: H0639G)")
    cur = conn.execute("SELECT * FROM reading_strand WHERE code=?", (code,)).fetchone()
    if cur is None:
        missing = [n for n in ("Title", "Cluster", "Escalation") if not p.get(n)]
        if missing:
            raise Refused(f"a new strand needs {', '.join('-' + m for m in missing)}")
        if not conn.execute("SELECT 1 FROM cluster WHERE cluster_code=?", (p["Cluster"],)).fetchone():
            raise Refused(f"cluster {p['Cluster']!r} does not exist")
        eid = int(str(p["Escalation"]).lstrip("#"))
        if not conn.execute("SELECT 1 FROM escalation WHERE id=? AND type IN ('task','issue')", (eid,)).fetchone():
            raise Refused(f"escalation #{eid} is not a task or issue")
    elif cur["state"] != "open":
        raise Refused(f"strand {code} is {cur['state']}")

    def go():
        sid = cur["id"] if cur else w.insert("reading_strand", {
            "code": code, "title": p["Title"], "cluster_code": p["Cluster"], "escalation_id": eid,
            "note": p.get("Note")})
        have = set(_strongs(conn, sid))
        added = [s for s in strongs if s not in have]
        for s in added:
            w.insert("reading_strand_strong", {"strand_id": sid, "strong": s, "note": p.get("Note")})
        return added
    added = nr._atomic(conn, go)
    return f"strand {code}: {'created' if cur is None else 'open'}; {len(added)} word(s) added ({', '.join(added) or '-'})"


# ══ 1 context ═══════════════════════════════════════════════════════════════════════════════════
def refresh_hits(conn, w: nr.Writer, s) -> int:
    """A hit row for every live occurrence of the strand's words not yet a hit (one per verse and strong)."""
    n = 0
    for r in conn.execute(
            "SELECT vl.verse_id, vl.strong, MIN(vl.surface) surface FROM verse_lexical vl JOIN reading_strand_strong "
            "ss ON ss.strong=vl.strong WHERE ss.strand_id=? AND vl.deleted=0 AND NOT EXISTS (SELECT 1 FROM "
            "reading_strand_hit h WHERE h.strand_id=ss.strand_id AND h.verse_id=vl.verse_id AND h.strong=vl.strong) "
            "GROUP BY vl.verse_id, vl.strong", (s["id"],)).fetchall():
        w.insert("reading_strand_hit", {"strand_id": s["id"], "verse_id": r["verse_id"], "strong": r["strong"],
                                        "surface": r["surface"]})
        n += 1
    return n


def context(cfg, w: nr.Writer, p: dict) -> tuple[list[str], str]:
    """(report lines, console line). Writes the strand's new hits first."""
    conn = cfg.conn
    s = _open_strand(conn, p.get("Strand"))
    added, matched = nr._atomic(conn, lambda: (refresh_hits(conn, w, s), match_items(cfg, w, s)))
    words = _strongs(conn, s["id"])
    hits = conn.execute(
        "SELECT h.*, v.osisId, v.reference, v.text, vm.status AS vstatus, (SELECT GROUP_CONCAT(DISTINCT vl.morph_code) "
        "FROM verse_lexical vl WHERE vl.verse_id=h.verse_id AND vl.strong=h.strong AND vl.deleted=0) AS morph "
        "FROM reading_strand_hit h JOIN verse v ON v.id=h.verse_id LEFT JOIN verse_meta vm ON vm.verse_id=v.id "
        "WHERE h.strand_id=? ORDER BY h.strong, v.id", (s["id"],)).fetchall()
    read = sum(1 for h in hits if h["face"] or h["reason"])
    L = [f"# Strand context: {s['code']} — {s['title']}", "",
         f"Cluster {_cluster_name(conn, s['cluster_code'])} · escalation #{s['escalation_id']} · "
         f"{len(words)} word(s) · {len(hits)} hit(s) in {len({h['verse_id'] for h in hits})} verse(s) · "
         f"{read} read, {len(hits) - read} unread · {added} hit(s) new this run", ""]
    L += ["## The words", "", "| Strong | Word | Gloss | Hits | Read |", "|---|---|---|---|---|"]
    for st in words:
        r = conn.execute("SELECT stepTransliteration, stepGloss FROM strong WHERE strongNumber=?", (st,)).fetchone()
        sh = [h for h in hits if h["strong"] == st]
        L.append(f"| {st} | {_cell(r[0] if r else '')} | {_cell(r[1] if r else '')} | {len(sh)} | "
                 f"{sum(1 for h in sh if h['face'] or h['reason'])} |")
    # what is already known
    obs = conn.execute(
        "SELECT DISTINCT o.* FROM ib_observation o JOIN ib_node n ON n.observation_id=o.id WHERE o.status<>'withdrawn' "
        "AND (n.strong IN (SELECT strong FROM reading_strand_strong WHERE strand_id=?) OR n.verse_reference IN "
        "(SELECT v.osisId FROM reading_strand_hit h JOIN verse v ON v.id=h.verse_id WHERE h.strand_id=?)) "
        "ORDER BY o.id", (s["id"], s["id"])).fetchall()
    L += ["", f"## Observations already recorded on these words and verses ({len(obs)})", "",
          "September's drafts are offered here to be confirmed, corrected or withdrawn in the reading "
          "(a corrected one is recorded with `supersedes`).", ""]
    if obs:
        L += ["| Obs | Stage | Status | Observation | Verses |", "|---|---|---|---|---|"]
        for o in obs:
            vs = [r[0] for r in conn.execute("SELECT DISTINCT verse_reference FROM ib_node WHERE observation_id=? AND "
                                             "verse_reference IS NOT NULL ORDER BY seq", (o["id"],))]
            text = o["obs_text"] + "".join(f" · {k}: {o[k]}" for k in ("meaning", "implication", "chain") if o[k])
            L.append(f"| {o['id']} | {o['stage']} | {o['status']} | {_cell(text)} | {', '.join(vs[:8])}"
                     f"{' …' if len(vs) > 8 else ''} |")
    items = [r for r in strand_items(conn, s["id"]) if r["source"] == "matched"]
    todo = sum(1 for r in items if not r["answer"])
    L += ["", f"## Open items to answer ({len(items)}; {todo} not yet answered; {matched} new this run)", "",
          f"Matched on the strand's words, the clusters they sit in ({', '.join(strand_clusters(conn, s))}), its "
          f"verses and its code. Each must be answered before the strand's escalation can close: "
          f"`Escalation.ps1 -Action Update -Id OT-nn -Item OT-nn.n -ResponseKind touched|narrowed|forward|ruling|"
          f"note|closed -Respond \"...\" -Via {s['escalation_id']} -AnsweredBy Claude`.", ""]
    if items:
        L += ["| Item | Matched on | Item text | Answered since matched |", "|---|---|---|---|"]
        L += [f"| {r['alias']}.{r['item_no']} {r['kind']}:{_cell(r['value'])} | {_cell(r['matched_on'])} | "
              f"{_cell(r['note'])} | {_cell(r['answer']) or '**not yet**'} |" for r in items]
    L += ["", "## The hits", "", "Each hit needs a face, or a stated reason it has none (Record).", ""]
    for st in words:
        L += [f"### {_word(conn, st)}", "", "| Verse | Surface | Morph | Coverage | Face / reason | Text |",
              "|---|---|---|---|---|---|"]
        for h in (h for h in hits if h["strong"] == st):
            fr = h["face"] or (f"(no face) {h['reason']}" if h["reason"] else "")
            L.append(f"| {h['reference'] or h['osisId']} | {_cell(h['surface'])} | {_cell(h['morph'])} | "
                     f"{h['vstatus'] or '—'} | {_cell(fr)} | {_cell(h['text'])} |")
        L.append("")
    return L, (f"{s['code']}: {len(hits)} hit(s), {read} read; {len(obs)} observation(s) already; {len(items)} open "
               f"item(s) to answer ({matched} new, {todo} not yet answered)")


# ══ 2 record ════════════════════════════════════════════════════════════════════════════════════
def record(cfg, w: nr.Writer, p: dict, run_id: str) -> str:
    """-File: {"observations": [{"key", "text", "setting", "meaning", "implication", "chain",
    "basis": "stated|read", "parties", "verses": [{"verse": "Gen 6:5", "strong": "H3820"}],
    "supersedes": <observation id>, "stable_key": "<strand>:<source row id>", "note": "<revisit note>"}],
    "hits": [{"verse", "strong", "face", "parties", "observation": "<key>|<id>"} |
             {"verse", "strong", "reason"}],
    "items": ["verse:Rom 7:15 :: what is open", ...]}  (new open items found in the reading).
    Refused, with nothing written, on: a hit not in the strand, or with neither (or both) a face and
    a reason; an observation with no text, meaning or basis, or a verse in which its strong does not
    occur; a quotation not in its verse; an item that is not kind:value."""
    conn = cfg.conn
    s = _open_strand(conn, p.get("Strand"))
    data = _load_json(p)
    vx = nr.VerseIndex(cfg)
    bases = cfg.enum("ib_observation.basis")
    obs, keys, errors, quotes = [], set(), [], []
    for i, o in enumerate(data.get("observations") or []):
        where = f"observations[{i}] ({o.get('key')})"
        if not o.get("key") or o["key"] in keys:
            errors.append(f"{where}: a unique key is required")
        keys.add(o.get("key"))
        for f in ("text", "meaning"):
            if not (o.get(f) or "").strip():
                errors.append(f"{where}: {f} is required")
        if o.get("basis") not in bases:
            errors.append(f"{where}: basis must be one of {bases}")
        occs = []
        for v in o.get("verses") or []:
            try:
                vr = _verse(conn, vx, v.get("verse"))
                occs.append(recordingpass.resolve_occurrence(conn, v.get("strong"), vr["osisId"], None, None)
                            | {"strong": v.get("strong")})
            except (Refused, recordingpass.UnresolvedOccurrence) as exc:
                errors.append(f"{where}: {exc}")
        if not occs:
            errors.append(f"{where}: at least one verse (with its strong) is required")
        if o.get("supersedes") is not None and not conn.execute(
                "SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'", (o["supersedes"],)).fetchone():
            errors.append(f"{where}: supersedes {o['supersedes']} is not a live observation")
        quotes += _quote_check(conn, cfg, [o.get(k) for k in ("text", "setting", "meaning", "implication", "chain")], where)
        obs.append({**{k: o.get(k) for k in ("key", "text", "supersedes", "stable_key", "note") + PARTS},
                    "occurrences": occs})
    hits = []
    for i, h in enumerate(data.get("hits") or []):
        where = f"hits[{i}]"
        try:
            vr = _verse(conn, vx, h.get("verse"))
        except Refused as exc:
            errors.append(f"{where}: {exc}")
            continue
        row = conn.execute("SELECT * FROM reading_strand_hit WHERE strand_id=? AND verse_id=? AND strong=?",
                           (s["id"], vr["id"], h.get("strong"))).fetchone()
        if row is None:
            errors.append(f"{where}: {h.get('strong')} at {h.get('verse')} is not a hit of {s['code']} (run Context)")
            continue
        if bool((h.get("face") or "").strip()) == bool((h.get("reason") or "").strip()):
            errors.append(f"{where} ({h.get('verse')} {h.get('strong')}): give a face or a reason, one of them")
        ob = h.get("observation")
        if ob is not None and ob not in keys and not conn.execute(
                "SELECT 1 FROM ib_observation WHERE id=? AND status<>'withdrawn'", (ob,)).fetchone():
            errors.append(f"{where}: observation {ob!r} is neither a key in this file nor a live observation")
        hits.append((row, h))
    new_items = item_specs(cfg, data.get("items"), "items", errors)
    if not data.get("observations") and not data.get("hits") and not data.get("items"):
        errors.append("the file has no observations, no hits and no items")
    if errors or quotes:
        raise Refused("\n  ".join(["the reading is not recorded:"] + errors + (
            ["quotation(s) not found in the ESV text:"] + quotes if quotes else [])))

    def go():
        w._grant("ib_observation")
        w._grant("ib_node")
        ids = recordingpass.record_strand_observations(conn, s["cluster_code"], run_id, obs)
        for row, h in hits:
            ob = h.get("observation")
            w.update("reading_strand_hit", {"id": row["id"]}, {
                "face": h.get("face"), "reason": h.get("reason"), "parties": h.get("parties"),
                "observation_id": ids.get(ob, ob if isinstance(ob, int) else None), "run_id": run_id})
        w._grant("verse_meta")
        vids = {row["verse_id"] for row, _ in hits} | {
            conn.execute("SELECT id FROM verse WHERE osisId=?", (occ["verse_reference"],)).fetchone()[0]
            for o in obs for occ in o["occurrences"]}
        return ids, versemeta.mark(conn, vids, "analysed"), raise_items(cfg, w, s, new_items, f"Record {run_id}")
    ids, marked, raised = nr._atomic(conn, go)
    left = conn.execute("SELECT COUNT(*) FROM reading_strand_hit WHERE strand_id=? AND face IS NULL AND reason IS NULL",
                        (s["id"],)).fetchone()[0]
    return (f"{s['code']}: {len(ids)} observation(s) recorded ({', '.join(f'{k}={v}' for k, v in ids.items()) or '-'}); "
            f"{len(hits)} hit(s) read; {marked} verse(s) marked analysed; {left} hit(s) still unread; "
            f"{len(raised)} open item(s) raised ({', '.join(raised) or '-'})")


# ══ 3 gather ════════════════════════════════════════════════════════════════════════════════════
def related_blocks(conn, sid: int) -> dict[int, list[str]]:
    """{block id: why it is related}: it cites a strand verse; it tells a claim resting on a strand
    verse; it tells a claim resting on one of the strand's observations."""
    why: dict[int, list[str]] = {}
    for r in conn.execute(
            "SELECT ci.section_id, COUNT(DISTINCT ci.verse_id) n FROM narrative_citation ci JOIN narrative_section s ON "
            "s.id=ci.section_id WHERE ci.last_version IS NULL AND s.last_version IS NULL AND ci.verse_id IN (SELECT "
            "verse_id FROM reading_strand_hit WHERE strand_id=?) GROUP BY ci.section_id", (sid,)):
        why.setdefault(r[0], []).append(f"cites {r[1]} strand verse(s)")
    obs_ids = [o["id"] for o in strand_observations(conn, sid)]
    for r in conn.execute(
            "SELECT t.section_id, GROUP_CONCAT(DISTINCT c.claim_ref) refs FROM narrative_claim_telling t JOIN "
            "narrative_claim c ON c.id=t.claim_id JOIN narrative_claim_source cs ON cs.claim_id=c.id JOIN "
            "narrative_section s ON s.id=t.section_id WHERE t.status='current' AND s.last_version IS NULL AND "
            f"(cs.verse_id IN (SELECT verse_id FROM reading_strand_hit WHERE strand_id=?) OR cs.observation_id IN "
            f"({','.join('?' * len(obs_ids)) or 'NULL'})) GROUP BY t.section_id", (sid, *obs_ids)):
        why.setdefault(r[0], []).append(f"tells {r[1]}, resting on the strand's verses or observations")
    return why


def gather(cfg, p: dict) -> tuple[list[str], str]:
    conn = cfg.conn
    s = strand(conn, p.get("Strand"))
    why = related_blocks(conn, s["id"])
    rows = conn.execute(
        f"SELECT s.*, ch.chapter_no, ch.title, ch.reading_order, ps.heading AS parent FROM narrative_section s JOIN "
        f"narrative_chapter ch ON ch.id=s.chapter_id LEFT JOIN narrative_section ps ON ps.id=s.parent_section_id "
        f"WHERE s.id IN ({','.join('?' * len(why)) or 'NULL'}) ORDER BY ch.reading_order, s.ordinal",
        tuple(why)).fetchall()
    L = [f"# Strand gather: {s['code']} — {s['title']}", "",
         f"{len(rows)} block(s) related to the strand. Map each block's statements to the claims register "
         f"(Strand-Reading.ps1 -Step Map); every block below must be mapped.", ""]
    for b in rows:
        name = f"{b['parent']} > {b['heading']}" if b["parent"] else b["heading"]
        L += [f"## Ch {b['chapter_no']} {b['title']} — {name}", "", f"*Related: {'; '.join(why[b['id']])}*", ""]
        told = conn.execute("SELECT c.claim_ref, c.claim_text, c.status, t.kind, t.part_told FROM narrative_claim_telling t "
                            "JOIN narrative_claim c ON c.id=t.claim_id WHERE t.section_id=? AND t.status='current' "
                            "ORDER BY c.id", (b["id"],)).fetchall()
        L += [f"**Tells now ({len(told)}):**", ""] + [
            f"- {t['claim_ref']} ({t['kind']}{': ' + t['part_told'] if t['part_told'] else ''}) {t['claim_text']}"
            for t in told] + ["", "**The block:**", "", "````markdown", b["block_text"] or "", "````", ""]
    untold = conn.execute(
        "SELECT DISTINCT c.claim_ref, c.claim_text FROM narrative_claim c JOIN narrative_claim_source cs ON "
        "cs.claim_id=c.id WHERE c.status='current' AND c.in_narrative=0 AND cs.verse_id IN (SELECT verse_id FROM "
        "reading_strand_hit WHERE strand_id=?) ORDER BY c.id", (s["id"],)).fetchall()
    L += [f"## Claims resting on the strand's verses that no block tells ({len(untold)})", ""]
    L += [f"- {c['claim_ref']} {c['claim_text']}" for c in untold]
    return L, f"{s['code']}: {len(rows)} related block(s); {len(untold)} claim(s) on its verses told nowhere"


# ══ 4 map ═══════════════════════════════════════════════════════════════════════════════════════
def map_blocks(cfg, w: nr.Writer, p: dict) -> str:
    """-File: {"blocks": [{"chapter", "section", "statements": [
        {"text": "<the statement>", "claims": [{"claim": "C-12", "kind": "in full|in part|pointer", "part"}]} |
        {"text", "new_claim": {"text", "beyond_text", "sources": ["Rom 7:22", ...], "kind", "part"}} |
        {"text", "item": "<why it is held>" | "kind:value :: note"}]}]}
    Every related block (Gather) must be mapped, and every statement must name its claim(s), a new
    claim, or an item. Told claims become the block's tellings; a new claim is added and told; an item
    is raised as an open item on the strand's thread: as given when it is kind:value, else
    chapter:'Ch n heading: "statement"' with the reason as its note."""
    conn = cfg.conn
    s = _open_strand(conn, p.get("Strand"))
    data = _load_json(p)
    vx = nr.VerseIndex(cfg)
    kinds = cfg.enum("narrative_telling_kind")
    plan, errors, seen = [], [], set()
    for i, b in enumerate(data.get("blocks") or []):
        try:
            ch = nr._chapter(conn, b.get("chapter"))
            sec = nr._block(conn, ch, b.get("section"))
        except Refused as exc:
            errors.append(f"blocks[{i}]: {exc}")
            continue
        seen.add(sec["id"])
        where = f"Ch {ch['chapter_no']} *{sec['heading']}*"
        if not b.get("statements"):
            errors.append(f"{where}: no statements mapped")
        for j, st in enumerate(b.get("statements") or []):
            at = f"{where} statement {j + 1}"
            ways = [k for k in ("claims", "new_claim", "item") if st.get(k)]
            if not (st.get("text") or "").strip() or len(ways) != 1:
                errors.append(f"{at}: give the statement's text and one of claims, new_claim or item")
                continue
            if ways[0] == "claims":
                for c in st["claims"]:
                    try:
                        cr = nr._claim(conn, c.get("claim"))
                        kind = c.get("kind") or "in full"
                        nr._check_enum(kinds, kind, f"{at} kind")
                        if kind == "in part" and not (c.get("part") or "").strip():
                            raise Refused(f"{cr['claim_ref']} told 'in part' with no part")
                        if cr["status"] == "withdrawn":
                            raise Refused(f"{cr['claim_ref']} is withdrawn")
                        plan.append(("tell", sec, cr["id"], kind, c.get("part")))
                    except Refused as exc:
                        errors.append(f"{at}: {exc}")
            elif ways[0] == "new_claim":
                nc = st["new_claim"]
                try:
                    if not (nc.get("text") and nc.get("beyond_text")):
                        raise Refused("new_claim needs text and beyond_text")
                    srcs = nr._parse_sources(cfg, vx, "; ".join(nc.get("sources") or []))
                    if not srcs:
                        raise Refused("new_claim needs at least one source")
                    plan.append(("new", sec, nc, srcs))
                except Refused as exc:
                    errors.append(f"{at}: {exc}")
            else:
                spec = str(st["item"])
                if spec.split(":", 1)[0].strip().lower() not in cfg.enum("escalation_thread_item_kind"):
                    spec = f"chapter:Ch {ch['chapter_no']} {sec['heading']}: \"{st['text'].strip()}\" :: {spec}"
                plan += [("item", sec, i) for i in item_specs(cfg, [spec], at, errors)]
    unmapped = set(related_blocks(conn, s["id"])) - seen
    for sid in sorted(unmapped):
        r = conn.execute("SELECT s.heading, ch.chapter_no FROM narrative_section s JOIN narrative_chapter ch ON "
                         "ch.id=s.chapter_id WHERE s.id=?", (sid,)).fetchone()
        errors.append(f"Ch {r['chapter_no']} *{r['heading']}* is related to the strand and not mapped")
    if errors:
        raise Refused("\n  ".join(["the mapping is not recorded:"] + errors))

    def go():
        since = nr._max_change_id(conn)
        told, new = 0, []
        for x in plan:
            if x[0] == "tell":
                _, sec, cid, kind, part = x
                t = nr._block_telling(conn, cid, sec["id"])
                if not (t and t["status"] == "current" and t["kind"] == kind and t["part_told"] == part):
                    nr.tell_block(w, cid, sec["id"], kind, part)
                    told += 1
            elif x[0] == "new":
                _, sec, nc, srcs = x
                cid = w.insert("narrative_claim", {"origin": "narrative", "claim_text": nc["text"],
                                                   "beyond_text": nc["beyond_text"], "verdict": "New",
                                                   "status": "current", "main_chapter_id": sec["chapter_id"],
                                                   "main_section_id": sec["id"]})
                for src in srcs:
                    w.insert("narrative_claim_source", {"claim_id": cid, **src})
                    w.note_unresolved(vx, src, "new claim source")
                nr.tell_block(w, cid, sec["id"], nc.get("kind") or "in full", nc.get("part"))
                new.append(conn.execute("SELECT claim_ref FROM narrative_claim WHERE id=?", (cid,)).fetchone()[0])
        w.mark_changes(since, f"Strand-Reading.ps1 -Step Map -Strand {s['code']}")
        return told, new, raise_items(cfg, w, s, [x[2] for x in plan if x[0] == "item"], "Map")
    told, new, raised = nr._atomic(conn, go)
    return (f"{s['code']}: {len(seen)} block(s) mapped; {told} telling(s) recorded; {len(new)} new claim(s) "
            f"({', '.join(new) or '-'}); {len(raised)} statement(s) held as open item(s) ({', '.join(raised) or '-'})")


# ══ 5 derive ════════════════════════════════════════════════════════════════════════════════════
def _obs_source(conn, oid: int) -> dict:
    o = conn.execute("SELECT obs_text FROM ib_observation WHERE id=?", (oid,)).fetchone()
    return {"source_kind": "observation", "observation_id": oid, "source_text": f"observation {oid}: {o[0][:200]}"}


def derive(cfg, w: nr.Writer, p: dict, run_id: str) -> str:
    """-File: {"claims": [
        {"key": "n1", "new": {"text", "beyond_text", "verdict", "sources": ["Rom 7:22"], "observations": [12]}},
        {"claim": "C-12", "edit": {"text", "beyond_text", "verdict", "sources": [...], "observations": [...]}},
        {"claim": "C-13", "withdraw": "<why>"}],
     "dispositions": [{"observation": 12, "as": "claim", "claim": "C-12|n1"} |
                      {"observation": 13, "as": "held", "item": "OT-29.4|#2172"} |
                      {"observation": 13, "as": "held", "new_item": "verse:Rom 7:15 :: what is open"} |
                      {"observation": 14, "as": "silent|withdrawn", "reason": "..."}]}
    A new or adjusted claim rests on at least one observation or verse. A disposition 'claim' names
    a claim that has the observation as a source after this step (added if it is not)."""
    conn = cfg.conn
    s = _open_strand(conn, p.get("Strand"))
    data = _load_json(p)
    vx = nr.VerseIndex(cfg)
    mine = {o["id"] for o in strand_observations(conn, s["id"])}
    verdicts = cfg.enum("narrative_claim_verdict")
    errors, plan, keys = [], [], {}

    def obs_ids(lst, at):
        out = []
        for oid in lst or []:
            if oid not in mine:
                errors.append(f"{at}: observation {oid} is not one of the strand's observations")
            out.append(oid)
        return out
    for i, c in enumerate(data.get("claims") or []):
        at = f"claims[{i}]"
        try:
            if "new" in c:
                n = c["new"]
                if not c.get("key") or not n.get("text") or not n.get("beyond_text"):
                    raise Refused("a new claim needs key, text and beyond_text")
                if n.get("verdict") and n["verdict"] not in verdicts:
                    raise Refused(f"verdict must be one of {verdicts}")
                srcs = nr._parse_sources(cfg, vx, "; ".join(n.get("sources") or []))
                ob = obs_ids(n.get("observations"), at)
                if not srcs and not ob:
                    raise Refused("a new claim rests on at least one observation or verse")
                keys[c["key"]] = None
                plan.append(("new", c["key"], n, srcs, ob))
            elif c.get("withdraw"):
                cr = nr._claim(conn, c.get("claim"))
                plan.append(("withdraw", cr, c["withdraw"]))
            else:
                cr = nr._claim(conn, c.get("claim"))
                e = c.get("edit") or {}
                if e.get("verdict") and e["verdict"] not in verdicts:
                    raise Refused(f"verdict must be one of {verdicts}")
                srcs = nr._parse_sources(cfg, vx, "; ".join(e.get("sources") or []))
                ob = obs_ids(e.get("observations"), at)
                if not srcs and not ob:
                    raise Refused("an adjusted claim names the observation(s) or verse(s) it now rests on")
                plan.append(("edit", cr, e, srcs, ob))
        except Refused as exc:
            errors.append(f"{at}: {exc}")
    disp = []
    for i, d in enumerate(data.get("dispositions") or []):
        at = f"dispositions[{i}] (observation {d.get('observation')})"
        obs_ids([d.get("observation")], at)
        how = d.get("as")
        if how == "claim":
            if d.get("claim") not in keys:
                try:
                    nr._claim(conn, d.get("claim"))
                except Refused as exc:
                    errors.append(f"{at}: {exc}")
        elif how == "held":
            item = str(d.get("item") or "")
            if bool(item) == bool(d.get("new_item")):
                errors.append(f"{at}: held needs an existing item (OT-nn.n, OT-nn or #nnnn) or a new_item, one of them")
            elif d.get("new_item"):
                d = {**d, "spec": (item_specs(cfg, [d["new_item"]], at, errors) or [None])[0]}
            else:
                kind = "escalation" if item.startswith("#") else "thread item" if "." in item else "thread"
                if not nr._escalation_exists(conn, kind, item):
                    errors.append(f"{at}: held item {item} does not exist")
        elif how in ("silent", "withdrawn"):
            if not (d.get("reason") or "").strip():
                errors.append(f"{at}: {how} needs a reason")
        else:
            errors.append(f"{at}: 'as' must be claim, held, silent or withdrawn")
        disp.append(d)
    if not data.get("claims") and not data.get("dispositions"):
        errors.append("the file has no claims and no dispositions")
    if errors:
        raise Refused("\n  ".join(["the derivation is not recorded:"] + errors))
    status_of = {"claim": "resolved", "held": "open", "silent": "silent", "withdrawn": "withdrawn"}

    def go():
        since = nr._max_change_id(conn)
        made = []
        for x in plan:
            if x[0] == "new":
                _, key, n, srcs, ob = x
                cid = w.insert("narrative_claim", {"origin": "narrative", "claim_text": n["text"],
                                                   "beyond_text": n["beyond_text"], "verdict": n.get("verdict") or "New",
                                                   "status": "current"})
                keys[key] = cid
                made.append(conn.execute("SELECT claim_ref FROM narrative_claim WHERE id=?", (cid,)).fetchone()[0])
                for src in srcs + [_obs_source(conn, o) for o in ob]:
                    w.insert("narrative_claim_source", {"claim_id": cid, **src})
                    w.note_unresolved(vx, src, f"claim {made[-1]} source")
            elif x[0] == "edit":
                _, cr, e, srcs, ob = x
                sets = {k2: e[k1] for k1, k2 in (("text", "claim_text"), ("beyond_text", "beyond_text"),
                                                 ("verdict", "verdict")) if e.get(k1)}
                if sets:
                    w.update("narrative_claim", {"id": cr["id"]}, sets)
                have = {r[0] for r in conn.execute("SELECT observation_id FROM narrative_claim_source WHERE claim_id=? "
                                                   "AND observation_id IS NOT NULL", (cr["id"],))}
                for src in srcs + [_obs_source(conn, o) for o in ob if o not in have]:
                    w.insert("narrative_claim_source", {"claim_id": cr["id"], **src})
                    w.note_unresolved(vx, src, f"claim {cr['claim_ref']} source")
            else:
                _, cr, why = x
                w.update("narrative_claim", {"id": cr["id"]}, {"status": "withdrawn"})
        w._grant("ib_observation")
        for d in disp:
            if d.get("spec"):
                d["item"] = raise_items(cfg, w, s, [d["spec"]], f"Derive, observation {d['observation']}")[0]
            note = d.get("reason") or (f"held: {d['item']}" if d["as"] == "held" else None)
            if d["as"] == "claim":
                cid = keys.get(d["claim"]) or nr._claim(conn, d["claim"])["id"]
                if not conn.execute("SELECT 1 FROM narrative_claim_source WHERE claim_id=? AND observation_id=?",
                                    (cid, d["observation"])).fetchone():
                    w.insert("narrative_claim_source", {"claim_id": cid, **_obs_source(conn, d["observation"])})
                note = "carried by " + conn.execute("SELECT claim_ref FROM narrative_claim WHERE id=?", (cid,)).fetchone()[0]
            recordingpass.set_disposition(conn, d["observation"], status_of[d["as"]], note, run_id)
        conn.execute("UPDATE narrative_claim_change SET change_kind='claim restated' WHERE id > ? AND "
                     "change_kind='edited' AND claim_before IS NOT claim_after AND note IS NULL", (since,))
        w.mark_changes(since, f"Strand-Reading.ps1 -Step Derive -Strand {s['code']}")
        return made
    made = nr._atomic(conn, go)
    n_new = sum(1 for x in plan if x[0] == "new")
    n_edit = sum(1 for x in plan if x[0] == "edit")
    n_wd = sum(1 for x in plan if x[0] == "withdraw")
    return (f"{s['code']}: {n_new} new claim(s) ({', '.join(made) or '-'}), {n_edit} adjusted, {n_wd} withdrawn; "
            f"{len(disp)} observation(s) disposed")


# ══ 6 rewrite ═══════════════════════════════════════════════════════════════════════════════════
def rewrite(cfg, w: nr.Writer, p: dict) -> str:
    """-File: the narrativeregister.rewrite() shape; the update names the strand and its escalation.
    The verses the rewritten blocks cite are marked 'citated'."""
    conn = cfg.conn
    s = _open_strand(conn, p.get("Strand"))
    data = _load_json(p)
    data.setdefault("update", {}).setdefault("strand", s["code"])
    refs = data.setdefault("refs", [])
    if not any(r.get("kind") == "escalation" and str(r.get("value")).lstrip("#") == str(s["escalation_id"]) for r in refs):
        refs.append({"kind": "escalation", "value": str(s["escalation_id"])})
    out = nr.rewrite(cfg, w, data, f"Strand-Reading.ps1 -Step Rewrite -Strand {s['code']}")
    w._grant("verse_meta")
    marked = versemeta.mark(conn, out["cited_verse_ids"], "citated")
    return (f"{s['code']}: update {out['update_id']}; published {', '.join(out['chapters'].values())}; "
            f"{out['quote_parts']} quoted part(s) checked; {marked} verse(s) marked citated")


# ══ 7 account ═══════════════════════════════════════════════════════════════════════════════════
def account_gaps(conn, sid: int) -> dict[str, list[str]]:
    """The facts the close gate stands on (safeguards 1 and 2, and #2219): unread hits, undisposed
    observations, and matched open items with no response since they were matched."""
    unread = [f"{r[0]} {r[1]}" for r in conn.execute(
        "SELECT COALESCE(v.reference, v.osisId), h.strong FROM reading_strand_hit h JOIN verse v ON v.id=h.verse_id "
        "WHERE h.strand_id=? AND h.face IS NULL AND h.reason IS NULL ORDER BY v.id", (sid,))]
    undisposed = [f"observation {o['id']}" for o in strand_observations(conn, sid) if o["status"] == "draft"]
    unanswered = [f"{r['alias']}.{r['item_no']}" for r in strand_items(conn, sid)
                  if r["source"] == "matched" and not r["answer"]]
    return {"hits with no face or reason": unread, "observations with no disposition": undisposed,
            "open items matched and not answered": unanswered}


def gate_message(conn, escalation_id: int) -> str | None:
    """None when every open strand recorded on this escalation has a clean account; else why not."""
    out = []
    for s in conn.execute("SELECT * FROM reading_strand WHERE escalation_id=? AND state='open'", (escalation_id,)):
        for what, gaps in account_gaps(conn, s["id"]).items():
            if gaps:
                out.append(f"strand {s['code']}: {len(gaps)} {what}")
    return "; ".join(out) or None


def account(cfg, p: dict) -> tuple[list[str], str]:
    conn = cfg.conn
    s = strand(conn, p.get("Strand"))
    gaps = account_gaps(conn, s["id"])
    hits = conn.execute("SELECT h.*, v.reference, v.osisId, vm.status vstatus FROM reading_strand_hit h JOIN verse v ON "
                        "v.id=h.verse_id LEFT JOIN verse_meta vm ON vm.verse_id=v.id WHERE h.strand_id=? ORDER BY "
                        "h.strong, v.id", (s["id"],)).fetchall()
    obs = strand_observations(conn, s["id"])
    L = [f"# Strand account: {s['code']} — {s['title']}", "",
         f"Cluster {_cluster_name(conn, s['cluster_code'])} · escalation #{s['escalation_id']} · state {s['state']}", "",
         "## Gaps", ""]
    open_gaps = 0
    for what, g in gaps.items():
        open_gaps += len(g)
        L.append(f"- **{len(g)} {what}**" + (f": {', '.join(g[:40])}{' …' if len(g) > 40 else ''}" if g else ""))
    # shown for judgement, not gated
    claims_on = conn.execute(
        f"SELECT DISTINCT c.* FROM narrative_claim c JOIN narrative_claim_source cs ON cs.claim_id=c.id WHERE "
        f"c.status='current' AND (cs.observation_id IN ({','.join('?' * len(obs)) or 'NULL'}) OR cs.verse_id IN "
        f"(SELECT verse_id FROM reading_strand_hit WHERE strand_id=?)) ORDER BY c.id",
        (*[o["id"] for o in obs], s["id"])).fetchall()
    untold = [c for c in claims_on if not c["in_narrative"]]
    resolved_no_claim = [o for o in obs if o["status"] == "resolved" and not conn.execute(
        "SELECT 1 FROM narrative_claim_source cs JOIN narrative_claim c ON c.id=cs.claim_id WHERE cs.observation_id=? "
        "AND c.status='current'", (o["id"],)).fetchone()]
    no_obs = [c for c in claims_on if not conn.execute(
        "SELECT 1 FROM narrative_claim_source WHERE claim_id=? AND observation_id IS NOT NULL", (c["id"],)).fetchone()]
    L += [f"- {len(untold)} claim(s) on the strand's verses or observations that no block tells (for judgement)",
          f"- {len(resolved_no_claim)} observation(s) marked carried whose claim is no longer current (for judgement)",
          f"- {len(no_obs)} claim(s) on the strand's verses that name no observation (for judgement)", ""]
    L += [f"## Observations ({len(obs)})", "", "| Obs | Status | Observation | Claim(s) | Note |", "|---|---|---|---|---|"]
    for o in obs:
        cl = [r[0] for r in conn.execute("SELECT c.claim_ref FROM narrative_claim_source cs JOIN narrative_claim c ON "
                                         "c.id=cs.claim_id WHERE cs.observation_id=?", (o["id"],))]
        L.append(f"| {o['id']} | {o['status']} | {_cell(o['obs_text'])} | {', '.join(cl) or '—'} | {_cell(o['revisit_note'])} |")
    L += ["", f"## Claims ({len(claims_on)})", "", "| Claim | Told in | Rests on observations |", "|---|---|---|"]
    for c in claims_on:
        ob = [str(r[0]) for r in conn.execute("SELECT observation_id FROM narrative_claim_source WHERE claim_id=? AND "
                                              "observation_id IS NOT NULL", (c["id"],))]
        L.append(f"| {c['claim_ref']} {_cell(c['claim_text'])} | {'; '.join(nr._told_in(conn, c['id'])) or '— (told nowhere)'} | "
                 f"{', '.join(ob) or '—'} |")
    its = strand_items(conn, s["id"])
    L += ["", f"## Open items ({len(its)})", "",
          "Matched: found by Context, answered by a thread response. Raised: found in this strand's reading.", "",
          "| Item | Source | Matched on / raised in | Item text | Item status | Latest response since |",
          "|---|---|---|---|---|---|"]
    L += [f"| {r['alias']}.{r['item_no']} {r['kind']}:{_cell(r['value'])} | {r['source']} | {_cell(r['matched_on'])} | "
          f"{_cell(r['note'])} | {r['status']} | "
          f"{_cell(r['answer']) or ('**not yet**' if r['source'] == 'matched' else '—')} |" for r in its]
    L += ["", f"## Hits ({len(hits)})", "", "| Verse | Strong | Face / reason | Observation | Coverage |",
          "|---|---|---|---|---|"]
    for h in hits:
        fr = h["face"] or (f"(no face) {h['reason']}" if h["reason"] else "**unread**")
        L.append(f"| {h['reference'] or h['osisId']} | {h['strong']} | {_cell(fr)} | {h['observation_id'] or '—'} | "
                 f"{h['vstatus'] or '—'} |")
    gate = "the strand's escalation can close" if not open_gaps else "the strand's escalation cannot close (gaps above)"
    return L, f"{s['code']}: {open_gaps} gated gap(s); {len(untold)} claim(s) told nowhere -- {gate}"
