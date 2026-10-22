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

Every write action validates first and raises Refused before writing; a refusal inside a write is
rolled back (narrativeregister._atomic). Writes go through narrativeregister.Writer (cfg_write_grant);
ib_observation/ib_node only through recordingpass.
"""
from __future__ import annotations

import json
import pathlib

from . import narrativeregister as nr
from . import quotecheck
from . import recordingpass
from . import versemeta

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
    added = nr._atomic(conn, lambda: refresh_hits(conn, w, s))
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
    refs = {h["reference"] for h in hits if h["reference"]}
    items = conn.execute(
        "SELECT e.alias, i.item_no, i.kind, i.value, i.note FROM escalation_thread_item i JOIN escalation e ON "
        "e.id=i.escalation_id AND e.version=(SELECT MAX(version) FROM escalation x WHERE x.id=e.id) WHERE "
        "i.status='open' AND ((i.kind='strong' AND i.value IN (SELECT strong FROM reading_strand_strong WHERE "
        "strand_id=?)) OR (i.kind='cluster' AND i.value=?) OR (i.kind='strand' AND i.value=?)) ORDER BY e.id, i.item_no",
        (s["id"], s["cluster_code"], s["code"])).fetchall()
    items += [r for r in conn.execute(
        "SELECT e.alias, i.item_no, i.kind, i.value, i.note FROM escalation_thread_item i JOIN escalation e ON "
        "e.id=i.escalation_id AND e.version=(SELECT MAX(version) FROM escalation x WHERE x.id=e.id) WHERE "
        "i.status='open' AND i.kind='verse' ORDER BY e.id, i.item_no") if r["value"] in refs]
    L += ["", f"## Open thread items that match ({len(items)})", ""]
    L += [f"- {r['alias']}.{r['item_no']} {r['kind']}:{r['value']}{' — ' + r['note'] if r['note'] else ''}" for r in items]
    L += ["", "## The hits", "", "Each hit needs a face, or a stated reason it has none (Record).", ""]
    for st in words:
        L += [f"### {_word(conn, st)}", "", "| Verse | Surface | Morph | Coverage | Face / reason | Text |",
              "|---|---|---|---|---|---|"]
        for h in (h for h in hits if h["strong"] == st):
            fr = h["face"] or (f"(no face) {h['reason']}" if h["reason"] else "")
            L.append(f"| {h['reference'] or h['osisId']} | {_cell(h['surface'])} | {_cell(h['morph'])} | "
                     f"{h['vstatus'] or '—'} | {_cell(fr)} | {_cell(h['text'])} |")
        L.append("")
    return L, f"{s['code']}: {len(hits)} hit(s), {read} read; {len(obs)} observation(s) already; {len(items)} open item(s)"


# ══ 2 record ════════════════════════════════════════════════════════════════════════════════════
def record(cfg, w: nr.Writer, p: dict, run_id: str) -> str:
    """-File: {"observations": [{"key", "text", "setting", "meaning", "implication", "chain",
    "basis": "stated|read", "parties", "verses": [{"verse": "Gen 6:5", "strong": "H3820"}],
    "supersedes": <observation id>}],
    "hits": [{"verse", "strong", "face", "parties", "observation": "<key>|<id>"} |
             {"verse", "strong", "reason"}]}.
    Refused, with nothing written, on: a hit not in the strand, or with neither (or both) a face and
    a reason; an observation with no text, meaning or basis, or a verse in which its strong does not
    occur; a quotation not in its verse."""
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
        obs.append({**{k: o.get(k) for k in ("key", "text", "supersedes") + PARTS}, "occurrences": occs})
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
    if not data.get("observations") and not data.get("hits"):
        errors.append("the file has no observations and no hits")
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
        return ids, versemeta.mark(conn, vids, "analysed")
    ids, marked = nr._atomic(conn, go)
    left = conn.execute("SELECT COUNT(*) FROM reading_strand_hit WHERE strand_id=? AND face IS NULL AND reason IS NULL",
                        (s["id"],)).fetchone()[0]
    return (f"{s['code']}: {len(ids)} observation(s) recorded ({', '.join(f'{k}={v}' for k, v in ids.items()) or '-'}); "
            f"{len(hits)} hit(s) read; {marked} verse(s) marked analysed; {left} hit(s) still unread")


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
def map_blocks(cfg, w: nr.Writer, p: dict) -> tuple[str, list[str]]:
    """-File: {"blocks": [{"chapter", "section", "statements": [
        {"text": "<the statement>", "claims": [{"claim": "C-12", "kind": "in full|in part|pointer", "part"}]} |
        {"text", "new_claim": {"text", "beyond_text", "sources": ["Rom 7:22", ...], "kind", "part"}} |
        {"text", "item": "<why it is held>"}]}]}
    Every related block (Gather) must be mapped, and every statement must name its claim(s), a new
    claim, or an item. Told claims become the block's tellings; a new claim is added and told; an item
    is returned for the strand's escalation. Returns (message, items)."""
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
                plan.append(("item", sec, f"{where}: \"{st['text']}\" -- {st['item']}"))
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
        return told, new
    told, new = nr._atomic(conn, go)
    items = [x[2] for x in plan if x[0] == "item"]
    return (f"{s['code']}: {len(seen)} block(s) mapped; {told} telling(s) recorded; {len(new)} new claim(s) "
            f"({', '.join(new) or '-'}); {len(items)} statement(s) held on #{s['escalation_id']}"), items


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
            kind = "escalation" if item.startswith("#") else "thread item" if "." in item else "thread"
            if not item or not nr._escalation_exists(conn, kind, item):
                errors.append(f"{at}: held needs an existing item (OT-nn.n, OT-nn or #nnnn)")
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
    """The facts the close gate stands on (safeguards 1 and 2): unread hits and undisposed observations."""
    unread = [f"{r[0]} {r[1]}" for r in conn.execute(
        "SELECT COALESCE(v.reference, v.osisId), h.strong FROM reading_strand_hit h JOIN verse v ON v.id=h.verse_id "
        "WHERE h.strand_id=? AND h.face IS NULL AND h.reason IS NULL ORDER BY v.id", (sid,))]
    undisposed = [f"observation {o['id']}" for o in strand_observations(conn, sid) if o["status"] == "draft"]
    return {"hits with no face or reason": unread, "observations with no disposition": undisposed}


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
    L += ["", f"## Hits ({len(hits)})", "", "| Verse | Strong | Face / reason | Observation | Coverage |",
          "|---|---|---|---|---|"]
    for h in hits:
        fr = h["face"] or (f"(no face) {h['reason']}" if h["reason"] else "**unread**")
        L.append(f"| {h['reference'] or h['osisId']} | {h['strong']} | {_cell(fr)} | {h['observation_id'] or '—'} | "
                 f"{h['vstatus'] or '—'} |")
    gate = "the strand's escalation can close" if not open_gaps else "the strand's escalation cannot close (gaps above)"
    return L, f"{s['code']}: {open_gaps} gated gap(s); {len(untold)} claim(s) told nowhere -- {gate}"
