"""_apply_verse_read_meaning.py — L2 VERSE-READ = MEANING pipeline (verse-complete, term-driven).

For each term (driver), read its verses; each verse is read ONCE (idempotent, verse-complete — all in-scope
terms in the verse are resolved together). The API (Sonnet 4.6, where CC cannot do the synthesis) fills the
verse-level extraction record (the read fields) per term-in-verse, then writes a MEANING PARAGRAPH that
collates the answered tier questions in the verse's context. Each tier element is a SEPARATELY IDENTIFIABLE
`finding`; the paragraph is its own VERSE-level finding (provenance 'l2_meaning'). After each paragraph a
SELF-AUDIT checks every element is represented; after each term a SELF-AUDIT checks all verses + findings are
present. Engine-logged: engine_run_log (run) + engine_stream_checkpoint (per term) with timestamps for
completion control, stall-visibility and clean resume. STATE-not-induce: NONE/SILENT/not-stated are
first-class, never guessed.

Spec: research/investigations/wa-verse-read-meaning-plan-v1-20260609.md ·
      wa-verse-level-extraction-spec-v1 · wa-catalogue-refit-two-layer-v1

Usage:
  python scripts/_apply_verse_read_meaning.py --terms 291 --dry-run --limit-verses 8   # smoke test, no writes
  python scripts/_apply_verse_read_meaning.py --cluster M01 --terms 269,829,305 --live  # pilot
  python scripts/_apply_verse_read_meaning.py --cluster M01 --live                      # full M01 (resumes)
"""
import argparse, os, re, sqlite3, sys, time
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 12000
BATCH = 6                       # verses per API call (verse-complete fans out to ~2.5 terms/verse)
PROV_TIER = "l2_api"            # provenance for read-field tier findings
PROV_MEAN = "l2_meaning"        # provenance for the meaning paragraph finding

# --- field -> catalogue obs_id (single-value fields) ---
FIELD_OBS = {
    "sense_applied": 395, "type": 239, "compound": 240, "mode": 245,
    "origin": 285, "attributed_to_God": 225, "purpose_equips": 227,
    "typology_direction": 234, "immediate_response": 248, "produces_effect": 251,
    "relational_implication": 238, "literary_setting": 404,
}
# multi-select fields -> {option: obs_id}
FACULTY_OBS = {"perception": 291, "cognition": 294, "memory": 297, "affect": 300,
               "creativity": 303, "volition": 306, "agency": 309, "moral-evaluation": 312,
               "conscience": 315, "relational": 321}
LOCATION_OBS = {"spirit": 260, "soul": 264, "heart": 267, "mind": 270, "body": 276}
NULLISH = {"none", "silent", "not-stated", "n/a", "na", ""}

FIELDS_ORDER = ["sense_applied", "type", "compound", "mode", "constitutional_location",
                "origin", "faculty", "attributed_to_God", "purpose_equips",
                "typology_direction", "immediate_response", "produces_effect",
                "relational_implication", "literary_setting"]


def load_key():
    if "ANTHROPIC_API_KEY" in os.environ:
        return
    for line in open(".env", encoding="utf-8"):
        if line.startswith("ANTHROPIC_API_KEY="):
            os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip()
            return


# ---------------------------------------------------------------- data assembly
def fetch_terms(conn, cluster, term_ids):
    c = conn.cursor()
    if term_ids:
        q = "SELECT id, strongs_number sn, transliteration tl, cluster_code cc FROM mti_terms WHERE id IN (%s)" % \
            ",".join("?" * len(term_ids))
        rows = c.execute(q, term_ids).fetchall()
    else:
        rows = c.execute("SELECT id, strongs_number sn, transliteration tl, cluster_code cc FROM mti_terms "
                         "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0 ORDER BY id", (cluster,)).fetchall()
    return rows


def fetch_term_refs(conn, mid):
    """Distinct verse references where this term has an active occurrence (drives iteration order)."""
    return [r[0] for r in conn.execute(
        """SELECT DISTINCT vr.reference FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
           WHERE vc.mti_term_id=? AND COALESCE(vc.delete_flagged,0)=0 ORDER BY vr.id""", (mid,))]


def vcid_read(conn, vcid):
    return conn.execute("SELECT 1 FROM finding WHERE verse_context_id=? AND provenance=? LIMIT 1",
                        (vcid, PROV_MEAN)).fetchone() is not None


def fetch_verse_block(conn, ref):
    """Verse-complete: the verse text + EVERY in-scope (clustered) term occurrence at this reference that does
    NOT yet have a meaning finding. Each term carries its own vcid, mti_term_id, cluster, sense options, morph."""
    c = conn.cursor(); c2 = conn.cursor()
    vt = None; terms = []
    for r in c.execute("""SELECT vc.id vcid, vr.verse_text vt, vr.morph_code morph, vr.stem stem,
                                 m.id mid, m.transliteration tl, m.strongs_number sn, m.cluster_code cc,
                                 ti.parsed_meaning_id pmid
                          FROM verse_context vc
                          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
                          JOIN mti_terms m ON m.id = vc.mti_term_id
                          LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number AND COALESCE(ti.delete_flagged,0)=0
                          WHERE vr.reference=? AND m.cluster_code IS NOT NULL AND COALESCE(vc.delete_flagged,0)=0
                          GROUP BY vc.id""", (ref,)):
        if vt is None:
            vt = (r["vt"] or "").strip()
        if vcid_read(conn, r["vcid"]):
            continue
        senses = []
        if r["pmid"]:
            senses = [x[0] for x in c2.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=? ORDER BY sort_order LIMIT 4", (r["pmid"],))]
        terms.append({"vcid": r["vcid"], "mid": r["mid"], "cc": r["cc"], "tl": r["tl"], "sn": r["sn"],
                      "morph": r["morph"], "stem": r["stem"], "senses": senses})
    if not terms:
        return None
    # co-occurring labels (all clustered terms at the ref, for context)
    cooc = [(x["tl"], x["sn"], x["cc"]) for x in c2.execute(
        """SELECT DISTINCT m.transliteration tl, m.strongs_number sn, m.cluster_code cc
           FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id JOIN mti_terms m ON m.id=vc.mti_term_id
           WHERE vr.reference=? AND m.cluster_code IS NOT NULL AND COALESCE(vc.delete_flagged,0)=0""", (ref,))]
    for t in terms:
        t["cooc"] = [x for x in cooc if x[1] != t["sn"]]
    return {"ref": ref, "vt": vt, "terms": terms}


SYSTEM_PROMPT = """You are doing VERSE-LEVEL MEANING extraction for an academic study of Scripture's vocabulary for the inner life of mankind. You read one verse at a time and, for each in-scope inner-life TERM in that verse, you extract a structured record and then write a short MEANING PARAGRAPH.

CORE DISCIPLINE
- "Characteristic" = the typed term-in-verse you are examining (e.g. THIS ya.re here), NOT a cluster label.
- STATE, NEVER INDUCE. If the verse does not resolve a field, output the null token (NONE / SILENT / not-stated). Silence is a first-class, significant finding. Do NOT guess, infer beyond the verse, or import doctrine.
- Read the verse in its own context; use the term's sense options only to disambiguate, not to override the verse.
- Option-list fields MUST use one of the listed values exactly.

FIELDS (per term-in-verse)
- sense_applied: the verse-specific sense of the term (short phrase).
- type: one of action | status | quality
- compound: simple  OR  compound:<parts>
- mode: the operative mode/stem nuance in this verse (short), or NONE
- constitutional_location: multi, comma-sep from {spirit, soul, heart, mind, body} or NONE  (only if the verse locates it there)
- origin: one of within-person | received-from-outside | bestowed-by-God | carried-generationally | from-other-spirits | not-stated
- faculty: multi, comma-sep from {perception, cognition, memory, affect, creativity, volition, agency, moral-evaluation, conscience, relational} or NONE  (which inner faculty the term engages here, from its meaning)
- attributed_to_God: yes | no   (is the term predicated of / related to God in THIS verse)
- purpose_equips: what the verse says it equips the person to be/do/become, or not-stated
- typology_direction: human->divine | divine->human | none
- immediate_response: the first inner response shown in the verse, or SILENT
- produces_effect: what it produces in the inner being here, or not-stated
- relational_implication: directional/relational force the term carries here, or not-stated
- literary_setting: the literary form of the verse (narrative | poetry | law | prophecy | wisdom | epistle | ...)

OUTPUT FORMAT — for EACH (verse, term) pair, emit exactly:
@@@ <reference> | <term_translit> | vcid=<vcid>
sense_applied: ...
type: ...
compound: ...
mode: ...
constitutional_location: ...
origin: ...
faculty: ...
attributed_to_God: ...
purpose_equips: ...
typology_direction: ...
immediate_response: ...
produces_effect: ...
relational_implication: ...
literary_setting: ...
MEANING: <2-4 sentence paragraph that collates the fields above into the meaning of this term in THIS verse's context. Every non-null field above must be reflected in the paragraph.>
SELFAUDIT: <comma-list of any field name NOT represented in MEANING, or "OK">
@@@END

Process every (verse, term) pair given. Use the exact vcid supplied. No preamble, no other text."""


def build_user_message(batch):
    parts = ["Read these verses. For EACH verse, process the listed in-scope term(s). Emit one block per (verse, term) pair.\n"]
    for v in batch:
        parts.append(f"=== VERSE {v['ref']} ===")
        parts.append(f"text: {v['vt']}")
        for t in v["terms"]:
            so = " | ".join(t["senses"][:3]) if t["senses"] else "(none)"
            cooc = ", ".join(f"{x[0]}({x[2]})" for x in t["cooc"][:8]) or "none"
            parts.append(f"  TERM {t['tl']} ({t['sn']}) vcid={t['vcid']}  morph={t['morph'] or '-'} stem={t['stem'] or '-'}")
            parts.append(f"    sense_options: {so}")
            parts.append(f"    co-occurring_inscope_terms: {cooc}")
        parts.append("")
    return "\n".join(parts)


def call_api(user_msg):
    import anthropic
    client = anthropic.Anthropic()
    chunks = []
    with client.messages.stream(model=MODEL, max_tokens=MAX_TOKENS,
                                system=[{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}],
                                messages=[{"role": "user", "content": user_msg}]) as stream:
        for tc in stream.text_stream:
            chunks.append(tc)
        final = stream.get_final_message()
    u = final.usage
    return "".join(chunks).strip(), {"in": u.input_tokens, "out": u.output_tokens,
                                     "cr": getattr(u, "cache_read_input_tokens", 0)}


# ---------------------------------------------------------------- parse
def parse_response(text):
    blocks = re.split(r"@@@END\s*", text)
    recs = []
    for b in blocks:
        m = re.search(r"@@@\s*(.+?)\s*\|\s*(.+?)\s*\|\s*vcid=(\d+)", b)
        if not m:
            continue
        rec = {"ref": m.group(1).strip(), "tl": m.group(2).strip(), "vcid": int(m.group(3)), "fields": {}, "meaning": "", "selfaudit": ""}
        for fm in re.finditer(r"^(\w[\w_]*?):[ \t]*(.*)$", b, re.MULTILINE):
            k, val = fm.group(1), fm.group(2).strip()
            if k == "MEANING":
                rec["meaning"] = val
            elif k == "SELFAUDIT":
                rec["selfaudit"] = val
            elif k in (set(FIELD_OBS) | {"constitutional_location", "faculty"}):
                rec["fields"][k] = val
        # MEANING/SELFAUDIT may span multiple lines — capture remainder
        mm = re.search(r"MEANING:\s*(.+?)\s*SELFAUDIT:", b, re.DOTALL)
        if mm:
            rec["meaning"] = mm.group(1).strip()
        sm = re.search(r"SELFAUDIT:\s*(.+)$", b, re.DOTALL)
        if sm:
            rec["selfaudit"] = sm.group(1).strip().splitlines()[0].strip()
        recs.append(rec)
    return recs


# ---------------------------------------------------------------- write
def _now(conn):
    return conn.execute("SELECT strftime('%Y-%m-%dT%H:%M:%fZ','now')").fetchone()[0]


def upsert_finding(conn, level, vcid, mid, cc, value, status, prov, obs_id, now):
    """Idempotent: one finding per (vcid, mid, prov, obs_id)."""
    cur = conn.cursor()
    row = cur.execute("""SELECT f.id FROM finding f LEFT JOIN finding_question_link l ON l.finding_id=f.id
                         WHERE f.verse_context_id=? AND f.mti_term_id=? AND f.provenance=?
                         AND IFNULL(l.question_id,-1)=? LIMIT 1""", (vcid, mid, prov, obs_id if obs_id else -1)).fetchone()
    if row:
        cur.execute("UPDATE finding SET finding_value=?, finding_status=?, last_updated_date=? WHERE id=?",
                    (value, status, now, row[0]))
        return row[0]
    cur.execute("""INSERT INTO finding(level, verse_context_id, mti_term_id, cluster_code, finding_value,
                   finding_status, provenance, created_at, last_updated_date)
                   VALUES(?,?,?,?,?,?,?,?,?)""", (level, vcid, mid, cc, value, status, prov, now, now))
    fid = cur.lastrowid
    if obs_id:
        cur.execute("INSERT INTO finding_question_link(finding_id, question_id, coverage, created_at) VALUES(?,?,?,?)",
                    (fid, obs_id, "direct", now))
    return fid


def write_record(conn, rec, term_lookup, now):
    """Write all separately-identifiable tier findings + the meaning paragraph for one (verse, term)."""
    vcid = rec["vcid"]; f = rec["fields"]
    info = term_lookup.get(vcid)
    if not info:
        return 0, "no-vcid"
    mid, cc = info
    n = 0
    # single-value fields
    for field, obs in FIELD_OBS.items():
        val = (f.get(field) or "").strip()
        low = val.lower()
        if field == "sense_applied" and field not in f:
            continue
        status = "STATED_SILENT" if low in NULLISH else "ANSWERED"
        upsert_finding(conn, "VERSE", vcid, mid, cc, val or "NONE", status, PROV_TIER, obs, now); n += 1
    # multi: faculty
    fac = [x.strip().lower() for x in (f.get("faculty") or "").split(",") if x.strip()]
    fac = [x for x in fac if x not in NULLISH]
    for opt, obs in FACULTY_OBS.items():
        present = opt in fac
        upsert_finding(conn, "VERSE", vcid, mid, cc, opt if present else "NONE",
                       "ANSWERED" if present else "STATED_SILENT", PROV_TIER, obs, now); n += 1 if present else 0
    # multi: location
    loc = [x.strip().lower() for x in (f.get("constitutional_location") or "").split(",") if x.strip()]
    loc = [x for x in loc if x not in NULLISH]
    for opt, obs in LOCATION_OBS.items():
        present = opt in loc
        if present:
            upsert_finding(conn, "VERSE", vcid, mid, cc, opt, "ANSWERED", PROV_TIER, obs, now); n += 1
    # meaning paragraph (own finding, no question link)
    upsert_finding(conn, "VERSE", vcid, mid, cc, rec["meaning"] or "NONE",
                   "ANSWERED" if rec["meaning"] else "STATED_UNRESOLVED", PROV_MEAN, None, now)
    return n, "ok"


# CC backstop checks only CONTENT fields (abstract option-fields like type/compound/mode are conceptual,
# rarely echoed verbatim — the API's semantic SELFAUDIT covers those). Flag only an EGREGIOUS omission:
# a content field whose value shares NO significant word with the paragraph.
# Only FREE-TEXT content fields — option-list fields (origin/location/faculty/type/mode…) are conceptual and
# need not appear verbatim; the API's semantic SELFAUDIT covers them.
AUDIT_CONTENT = {"immediate_response", "produces_effect", "relational_implication", "purpose_equips"}
_STOP = {"the", "and", "that", "with", "from", "this", "into", "upon", "have", "been", "which", "their", "person"}


def audit_paragraph(rec):
    """CC structural backstop: a content field with a real value must share >=1 significant word with the paragraph."""
    para = set(re.findall(r"[a-z]{4,}", (rec["meaning"] or "").lower()))
    missing = []
    for k in AUDIT_CONTENT:
        low = (rec["fields"].get(k) or "").lower().strip()
        if low in NULLISH or not low:
            continue
        words = {w for w in re.findall(r"[a-z]{4,}", low) if w not in _STOP}
        if words and not (words & para):
            missing.append(k)
    return missing


# ---------------------------------------------------------------- run
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", default="M01")
    ap.add_argument("--terms", default="", help="comma-sep mti_term ids; default = whole cluster")
    ap.add_argument("--dry-run", action="store_true", help="one batch, print, NO writes/log")
    ap.add_argument("--live", action="store_true")
    ap.add_argument("--limit-verses", type=int, default=0)
    args = ap.parse_args()
    if not (args.dry_run or args.live):
        print("specify --dry-run or --live"); sys.exit(1)
    load_key()
    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ERROR: ANTHROPIC_API_KEY not set"); sys.exit(1)
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    term_ids = [int(x) for x in args.terms.split(",") if x.strip()]
    terms = fetch_terms(conn, args.cluster, term_ids)
    print(f"Terms: {len(terms)} | mode={'DRY' if args.dry_run else 'LIVE'}")

    run_id = None
    if args.live:
        now = _now(conn)
        conn.execute("INSERT INTO engine_run_log(run_id, mode, target_registry_ids, started_at) VALUES(?,?,?,?)",
                     (f"vrm_{now}", "verse_read_meaning", args.cluster, now))
        run_id = f"vrm_{now}"; conn.commit()

    tot = {"in": 0, "out": 0, "cr": 0, "verses": 0, "findings": 0, "audit_flags": 0}
    for term in terms:
        mid = term["id"]
        refs = fetch_term_refs(conn, mid)
        # verse-complete: build a block per ref of its in-scope terms still missing a meaning finding
        blocks = []
        for ref in refs:
            blk = fetch_verse_block(conn, ref)
            if blk:
                blocks.append(blk)
        if args.limit_verses:
            blocks = blocks[:args.limit_verses]
        nterms = sum(len(b["terms"]) for b in blocks)
        print(f"\n=== TERM {term['tl']} ({term['sn']}, id={mid}) — {len(refs)} refs, "
              f"{len(blocks)} verse-blocks / {nterms} term-slots pending ===")
        if args.live:
            now = _now(conn)
            conn.execute("INSERT INTO engine_stream_checkpoint(run_id, stream_name, status, last_strong, started_at) "
                         "VALUES(?,?,?,?,?)", (run_id, f"term:{term['sn']}", "in_progress", term["sn"], now))
            conn.commit()
        written = 0; flags = 0
        for i in range(0, len(blocks), BATCH):
            batch = blocks[i:i + BATCH]                       # each block already carries ref/vt/terms[]
            term_lookup = {t["vcid"]: (t["mid"], t["cc"]) for b in batch for t in b["terms"]}
            user_msg = build_user_message(batch)
            t0 = time.time()
            try:
                text, usage = call_api(user_msg)
            except Exception as e:
                print(f"  batch {i//BATCH}: API ERROR {e}")
                if args.live:
                    conn.execute("UPDATE engine_stream_checkpoint SET status='error', error_detail=? "
                                 "WHERE run_id=? AND stream_name=?", (str(e)[:300], run_id, f"term:{term['sn']}"))
                    conn.commit()
                continue
            for k in usage: tot[k] += usage[k]
            recs = parse_response(text)
            bterms = sum(len(b["terms"]) for b in batch)
            print(f"  batch {i//BATCH} [{time.time()-t0:.1f}s] {len(batch)} verses / {bterms} terms -> {len(recs)} recs | in={usage['in']} out={usage['out']} cr={usage['cr']}")
            if args.dry_run:
                print("\n----- RAW (first 1800 chars) -----\n" + text[:1800])
                for rec in recs[:3]:
                    miss = audit_paragraph(rec)
                    print(f"\n  PARSED {rec['ref']} {rec['tl']} vcid={rec['vcid']}: {len(rec['fields'])} fields; "
                          f"meaning={len(rec['meaning'])}c; routed_cluster={term_lookup.get(rec['vcid'])}; "
                          f"API-selfaudit={rec['selfaudit']!r}; CC-missing={miss}")
                print("\n[DRY RUN — no writes] stopping after first batch."); conn.close(); return
            for rec in recs:
                n, st = write_record(conn, rec, term_lookup, _now(conn))
                if st != "ok":
                    continue
                written += n
                miss = audit_paragraph(rec)
                api_flag = bool(rec["selfaudit"]) and not rec["selfaudit"].lower().rstrip(". ").endswith("ok")
                if miss or api_flag:
                    flags += 1
                    rmid = term_lookup.get(rec["vcid"], (None,))[0]
                    conn.execute("UPDATE finding SET flagged_for_review=1 WHERE verse_context_id=? AND mti_term_id=? AND provenance=?",
                                 (rec["vcid"], rmid, PROV_MEAN))
            tot["verses"] += len(batch)
            conn.execute("UPDATE engine_stream_checkpoint SET rows_written=COALESCE(rows_written,0)+?, last_strong=? "
                         "WHERE run_id=? AND stream_name=?", (written, term["sn"], run_id, f"term:{term['sn']}"))
            conn.commit()
        # per-term self-audit: all of THIS term's own occurrences have a meaning finding
        own = conn.execute("SELECT COUNT(*) FROM verse_context WHERE mti_term_id=? AND COALESCE(delete_flagged,0)=0", (mid,)).fetchone()[0]
        rd = conn.execute("""SELECT COUNT(*) FROM verse_context vc WHERE vc.mti_term_id=? AND COALESCE(vc.delete_flagged,0)=0
                             AND EXISTS(SELECT 1 FROM finding f WHERE f.verse_context_id=vc.id AND f.provenance=?)""", (mid, PROV_MEAN)).fetchone()[0]
        status = "complete" if rd >= own else "review"
        detail = f"own_verses={own} read={rd} findings_written={written} audit_flags={flags}"
        if args.live:
            conn.execute("UPDATE engine_stream_checkpoint SET status=?, completed_at=?, rows_written=?, error_detail=? "
                         "WHERE run_id=? AND stream_name=?", (status, _now(conn), written, detail, run_id, f"term:{term['sn']}"))
            conn.commit()
        tot["findings"] += written; tot["audit_flags"] += flags
        print(f"  TERM self-audit: {detail} -> {status}")

    if args.live:
        # supersede old l2_mechanical findings for every verse the verse-read has now covered (reversible)
        sup = conn.execute("""UPDATE finding SET delete_flagged=1 WHERE provenance='l2_mechanical'
                              AND COALESCE(delete_flagged,0)=0
                              AND verse_context_id IN (SELECT DISTINCT verse_context_id FROM finding WHERE provenance='l2_meaning')""").rowcount
        conn.execute("UPDATE engine_run_log SET completed_at=?, outcome=?, total_verses_inserted=? WHERE run_id=?",
                     (_now(conn), "PASS", tot["verses"], run_id))
        conn.commit()
        print(f"superseded {sup} old l2_mechanical findings (verse-read-covered verses)")
    print(f"\n=== TOTAL: verses={tot['verses']} findings={tot['findings']} audit_flags={tot['audit_flags']} | "
          f"tokens in={tot['in']:,} out={tot['out']:,} cache_read={tot['cr']:,} ===")
    conn.close()


if __name__ == "__main__":
    main()
