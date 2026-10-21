"""_audit_findings_v1_20260621.py — read-only findings audit (wa-findings-audit-spec-v1_0).

Runs Gate 1 (findings) + Gate 2 (essay) checks for a cluster and writes a PLAIN-LANGUAGE,
self-explanatory report (policy 8.3) to Sessions-v2/{CLUSTER}/findings/wa-findings-audit-{CLUSTER}-{date}.md.
Read-only: no DB writes. Returns non-zero if any unresolved STOP remains.

  python scripts/_audit_findings_v1_20260621.py --cluster M05 [--date YYYYMMDD]
"""
import argparse, glob, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

JARGON = [r"\bcluster\b", r"\bcharacteristic", r"\bvalence\b", r"\bfaculty\b", r"\bfinding\b",
          r"\bVCG\b", r"\bsub-group\b", r"\btier\b", r"\bT\d\.\d", r"\bM\d\d\b"]
# scope-qualified superlatives only — a primacy claim tied to the study/cluster/programme
# (so quoted scripture like "the greatest of these is love" and ordinary prose are not caught)
SUPERLATIVE = [
    r"\bthe (?:single )?(?:most|largest|broadest|greatest|strongest|deepest|widest|highest)\b[\w\-, ]{0,32}?\b(?:in|of|across|among)\b (?:the |this )?(?:study|research|programme|program|cluster|family|inner[\- ]life|inner[\- ]being|corpus|any \w+|all \w+|the whole \w+)\b",
    r"\bby far the\b", r"\bunprecedented\b",
    r"\bthe only \w+\b[\w\-, ]{0,24}?\b(?:in|of)\b (?:the|this) (?:cluster|study|family|programme)\b",
]
# silence detector + expected-cause map (from wa-silent-answers-why-expected-v1)
SILENT = re.compile(r"(?i)\bsilent\b|not evidenced|does not speak|\bnegative\b|does not (apply|engage|appear)|no (mind|memory|spirit|conscience|faculty|location|occurrence|evidence)|not (engaged|located|applicable|evidenced)")
HDR = re.compile(r"\*\*(T\d+(?:\.\d+)*(?:\s*[/·][^*]*?)?)\*\*")
QID = re.compile(r"T\d+\.\d+(?:\.\d+)?")
VERSE = re.compile(r"\(([1-3]?[A-Z][a-z]{1,4}\s+\d+:\d+)\)")


def expected_cause(qid, why):
    w = (why or "").lower()
    if re.match(r"T5\.", qid): return "data-shape (formative/developmental)"
    if qid == "T0.2.3": return "data-shape (eschatology)"
    if re.match(r"T4\.6", qid) or ("spirit" in w or "adversar" in w): return "register (no spiritual-being interface)"
    if re.match(r"T3\.5", qid): return "defining (creativity not engaged)"
    if re.match(r"T3\.3", qid): return "faculty not engaged (memory)"
    if re.match(r"T3\.4", qid): return "defining (affect not engaged)"
    if re.match(r"T0\.(1|3|4)", qid): return "defining (no divine instance)"
    if qid in ("T1.7.1", "T1.7.3", "T4.3.3", "T4.4.2", "T4.4.3", "T1.6.1", "T4.5.1", "T4.5.2", "T6.3.3"): return "data-shape (over-time / relational / uptake)"
    if re.match(r"T7\.1", qid): return "lexical-fit (term-type absent)"
    if re.match(r"T2\.", qid): return "register (unseated / outward)"
    if re.match(r"T3\.", qid): return "faculty not engaged"
    return "UNEXPLAINED"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--date", default=__import__("datetime").date.today().strftime("%Y%m%d"))
    a = ap.parse_args()
    cc = a.cluster
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cdir = glob.glob(f"Sessions-v2/{cc}-*/")
    if not cdir:
        print(f"no folder for {cc}"); return 2
    cdir = cdir[0]
    fdir = os.path.join(cdir, "findings")

    g1, g2 = [], []  # (code, status, plain, action)

    # ---- gather DB content ----
    chars = cur.execute("SELECT id, short_name, char_seq, definition FROM characteristic WHERE cluster_code=? AND char_seq>=100 AND COALESCE(delete_flagged,0)=0 ORDER BY char_seq", (cc,)).fetchall()
    def prose(layer):
        return cur.execute("""SELECT ps.characteristic_id cid, ch.short_name sn, ps.body, ps.source_file sf
            FROM prose_section ps JOIN prose_section_type t ON t.id=ps.section_type_id
            LEFT JOIN characteristic ch ON ch.id=ps.characteristic_id
            WHERE ps.cluster_code=? AND ps.metadata_json LIKE ? AND COALESCE(ps.delete_flagged,0)=0""", (cc, f'%{layer}%')).fetchall()
    tiers = prose("tier_findings"); profiles = prose("evidence_profile")
    synth = cur.execute("SELECT body, source_file FROM prose_section ps JOIN prose_section_type t ON t.id=ps.section_type_id WHERE ps.cluster_code=? AND t.code='cf_cluster_synth' AND COALESCE(ps.delete_flagged,0)=0", (cc,)).fetchone()
    essay = cur.execute("SELECT body, source_file, status FROM prose_section ps JOIN prose_section_type t ON t.id=ps.section_type_id WHERE ps.cluster_code=? AND t.code='cluster_essay' AND ps.status='approved' AND COALESCE(ps.delete_flagged,0)=0 ORDER BY ps.id DESC", (cc,)).fetchone()

    # ===================== GATE 1 =====================
    # FA-01 presence
    miss = []
    if not chars: miss.append("characteristics")
    if len(tiers) < len(chars): miss.append(f"tier-answers ({len(tiers)}/{len(chars)})")
    if len(profiles) < len(chars): miss.append(f"profiles ({len(profiles)}/{len(chars)})")
    if not synth: miss.append("cluster synthesis")
    if miss:
        g1.append(("FA-01", "STOP", f"Required findings are missing: {', '.join(miss)}. Capture cannot proceed without them.", "CA-3"))
    else:
        g1.append(("FA-01", "PASS", f"All findings present: {len(chars)} characteristics, {len(tiers)} tier-answer sets, {len(profiles)} profiles, cluster synthesis.", ""))

    # FA-05 characteristic set consistent
    nt = len({t["cid"] for t in tiers}); npf = len({p["cid"] for p in profiles})
    if not (len(chars) == nt == npf):
        g1.append(("FA-05", "STOP", f"Characteristic set disagrees across sources: {len(chars)} defined, {nt} with tier-answers, {npf} with profiles. A characteristic may be missing a file.", "CA-3"))
    else:
        g1.append(("FA-05", "PASS", f"Characteristic set is consistent across definitions, tier-answers and profiles ({len(chars)} each).", ""))

    # FA-06 unique
    dup = cur.execute("SELECT COUNT(*) n FROM (SELECT char_seq FROM characteristic WHERE cluster_code=? AND char_seq>=100 AND COALESCE(delete_flagged,0)=0 GROUP BY char_seq HAVING COUNT(*)>1)", (cc,)).fetchone()["n"]
    g1.append(("FA-06", "STOP" if dup else "PASS", "Characteristic sequence/name collision in the DB." if dup else "No characteristic key collisions in the DB.", "CA-3" if dup else ""))

    # FA-07 definitions
    nodef = [c["short_name"] for c in chars if not (c["definition"] or "").strip()]
    g1.append(("FA-07", "WARN" if nodef else "PASS", f"{len(nodef)} characteristic(s) have no definition: {nodef}" if nodef else "Every characteristic carries a definition.", "CA-2" if nodef else ""))

    # FA-08 coverage + FA-10 silences explained
    cov_lines = []; unexplained = []
    conv = "Silent" if any("**Silent" in t["body"] or "Silent." in t["body"] for t in tiers) else ("SILENT" if any("SILENT" in t["body"] for t in tiers) else ("not-evidenced" if any("not evidenced" in t["body"] for t in tiers) else "prose"))
    for t in tiers:
        body = re.split(r"(?im)^#{0,4}\s*(?:coverage summary|answer coverage)", t["body"])[0]
        hdrs = [(m.start(), m.group(1)) for m in HDR.finditer(body)]
        sil = []
        for i, (p, h) in enumerate(hdrs):
            seg = body[p:(hdrs[i+1][0] if i+1 < len(hdrs) else len(body))]
            if SILENT.search(seg):
                for q in QID.findall(h):
                    cause = expected_cause(q, seg)
                    sil.append((q, cause))
                    if cause == "UNEXPLAINED": unexplained.append((t["sn"], q))
        cov_lines.append((t["sn"], len(set(q for q, _ in sil))))
    cov_summary = "; ".join(f"{sn.split('—')[0].strip()}:{n}" for sn, n in cov_lines)
    g1.append(("FA-08", "WARN" if conv == "prose" else "PASS",
               f"Silent-answer counts per characteristic — {cov_summary}." + (" Marker is prose-style, so counts are approximate." if conv == "prose" else ""),
               "" ))
    # FA-09 convention
    std = conv in ("SILENT",)  # M06-style is the recommended; others flagged
    g1.append(("FA-09", "WARN" if not std else "PASS",
               f"Silence is marked with the '{conv}' convention. The recommended standard is the M06-style 'X of Y per tier' coverage line; this cluster differs, so silence isn't a clean queryable field." if not std else "Uses the recommended silence-marking convention.",
               "CA-1"))
    g1.append(("FA-10", "REVIEW" if unexplained else "PASS",
               (f"{len(unexplained)} silent answer(s) are NOT explained by an expected cause and may be real gaps: " + ", ".join(f"{s.split('—')[0].strip()} {q}" for s, q in unexplained[:8]) + (" …" if len(unexplained) > 8 else "")) if unexplained else "Every silent answer maps to an expected cause (faculty-not-engaged / data-shape / register / defining / lexical-fit / thin-evidence) — no surprising gaps.",
               "CA-1" if unexplained else ""))

    # FA-11 verse reconciliation
    db_in = cur.execute("""SELECT COUNT(DISTINCT CASE WHEN vc.set_aside_reason IS NULL THEN vr.reference END) n
        FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id
        JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
        WHERE m.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0""", (cc,)).fetchone()["n"]
    ext = sorted([f for f in glob.glob(f"{cdir}Data/wa-ve-lexical-extract-{cc}-*.json") if "-narr" not in f])
    if ext:
        refs = set()
        edate = re.search(r"-(\d{8})-b", ext[0]); edate = edate.group(1) if edate else "?"
        for f in ext:
            for v in json.load(open(f, encoding="utf-8"))["data"]: refs.add(v["verse"]["reference"])
        diff = len(refs) - db_in
        if diff != 0:
            g1.append(("FA-11", "REVIEW", f"The extract (generated {edate}) holds {len(refs)} verses but the current in-scope corpus is {db_in} ({'+' if diff>0 else ''}{diff}). The extract is stale — verses were set aside or re-clustered after it was built. Regenerate before re-using it as a Chat input.", "CA-2"))
        else:
            g1.append(("FA-11", "PASS", f"Extract verse count ({len(refs)}) matches the current in-scope corpus ({db_in}) exactly.", ""))
    else:
        g1.append(("FA-11", "WARN", f"No lexical extract found on disk to reconcile against (DB in-scope = {db_in}).", ""))

    # FA-12 set-asides documented
    sa = cur.execute("SELECT COUNT(*) n FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id WHERE m.cluster_code=? AND vc.set_aside_reason IS NOT NULL AND COALESCE(vc.delete_flagged,0)=0", (cc,)).fetchone()["n"]
    g1.append(("FA-12", "PASS", f"{sa} out-of-scope occurrences are documented with a set-aside reason." if sa else "No occurrences set aside (nothing excluded, or rework not yet applied).", ""))

    # FA-13 no-faculty bands
    nofac = cur.execute("""SELECT m.transliteration tr, m.gloss, COUNT(DISTINCT vc.id) occ
        FROM mti_terms m JOIN verse_context vc ON vc.mti_term_id=m.id AND COALESCE(vc.delete_flagged,0)=0
        WHERE m.cluster_code=? GROUP BY m.strongs_number
        HAVING occ>=8 AND SUM(CASE WHEN EXISTS(SELECT 1 FROM ve_lexical x WHERE x.verse_context_id=vc.id AND x.ve_label='faculty' AND x.value<>'NONE') THEN 1 ELSE 0 END)=0
        ORDER BY occ DESC LIMIT 8""", (cc,)).fetchall()
    if nofac:
        g1.append(("FA-13", "REVIEW", "Terms with NO inner-being faculty across all occurrences (candidate set-aside / co-term, your call): " + ", ".join(f"{r['tr']} ({r['gloss']}, {r['occ']})" for r in nofac), "CA-1"))
    else:
        g1.append(("FA-13", "PASS", "No high-frequency term is wholly without an inner-being faculty.", ""))

    # FA-14 gloss vs sense — flag only when the gloss word appears NOWHERE in the top senses
    artifacts = []
    hf = cur.execute("""SELECT m.strongs_number sn, m.transliteration tr, m.gloss, COUNT(*) occ
        FROM mti_terms m JOIN verse_context vc ON vc.mti_term_id=m.id AND COALESCE(vc.delete_flagged,0)=0
        WHERE m.cluster_code=? GROUP BY m.strongs_number HAVING occ>=30""", (cc,)).fetchall()
    for r in hf:  # iterate a fetched list (avoid cursor reuse)
        senses = cur.execute("""SELECT LOWER(vr.target_word) w, COUNT(*) n FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id
            JOIN wa_verse_records vr ON vr.id=vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
            WHERE m.strongs_number=? AND COALESCE(vc.delete_flagged,0)=0 GROUP BY LOWER(vr.target_word) ORDER BY n DESC LIMIT 8""", (r["sn"],)).fetchall()
        if not senses or not r["gloss"]:
            continue
        gloss_words = [w for w in re.findall(r"[a-z]{3,}", r["gloss"].lower())]
        sense_words = re.findall(r"[a-z]{3,}", " ".join(s["w"] for s in senses))
        cov = lambda gw: any(gw in sw or sw in gw or gw[:4] == sw[:4] for sw in sense_words)
        if gloss_words and not any(cov(gw) for gw in gloss_words):
            top, topn = senses[0]["w"], senses[0]["n"]
            if topn > r["occ"]*0.4:
                artifacts.append(f"{r['tr']} {r['sn']} is glossed '{r['gloss']}' but its occurrences read '{top}' ({topn}/{r['occ']}) and never '{gloss_words[0]}' — likely a disambiguation artifact")
    g1.append(("FA-14", "REVIEW" if artifacts else "PASS", ("Possible gloss/sense mismatch (disambiguation artifact?): " + "; ".join(artifacts)) if artifacts else "High-frequency term glosses are consistent with their per-occurrence senses.", "CA-3" if artifacts else ""))

    # FA-16 open forks
    forks = []
    for src, label in [(synth["body"] if synth else "", "synthesis")] + ([(open(f, encoding="utf-8").read(), "ib-characteristics") for f in glob.glob(f"{fdir}/wa-{cc.lower()}-*characteristics*.md")]):
        for m in re.finditer(r"(?im)^#{1,4}.*?(interpretive choice|open question|open item|for you to decide|carried for researcher|flag \d|decision required).*$", src):
            forks.append(m.group(0).strip()[:80])
    forks = list(dict.fromkeys(forks))
    g1.append(("FA-16", "REVIEW" if forks else "PASS", (f"{len(forks)} open interpretive fork(s)/flag(s) to acknowledge before capture: " + " | ".join(forks[:5])) if forks else "No unresolved interpretive forks flagged in the findings.", "CA-1" if forks else ""))

    # FA-17 provenance
    if ext:
        meta = json.load(open(ext[0], encoding="utf-8"))["meta"]
        ok = ("extract_version" in meta) and ("2026-06-18" not in meta.get("source", ""))
        g1.append(("FA-17", "PASS" if ok else "WARN", f"Extract provenance is current (version {meta.get('extract_version','?')}, generated {meta.get('generated','?')})." if ok else "Extract carries a stale/missing provenance string.", "" if ok else "CA-2"))

    # FA-23 superlatives (findings prose)
    sup = []
    for t in tiers + ([synth] if synth else []):
        for pat in SUPERLATIVE:
            for m in re.finditer(pat, t["body"], re.I):
                sup.append(m.group(0))
    sup = list(dict.fromkeys(sup))
    g1.append(("FA-23", "REVIEW" if sup else "PASS", (f"{len(sup)} possibly-unsubstantiated superlative(s) in the findings: " + "; ".join(f'\"{s}\"' for s in sup[:6])) if sup else "No unsubstantiated programme-wide superlatives detected in the findings.", "CA-2" if sup else ""))

    # ===================== GATE 2 (essay) =====================
    if not essay:
        g2.append(("FA-18", "WARN", "No approved cluster essay in the DB yet — Gate 2 not applicable.", ""))
    else:
        eb = essay["body"]
        # verse existence by book_id — the DB stores some books under >1 prefix (e.g. Php AND Phili),
        # and essays may use shorter codes (2Co), so match on (book_id, chapter:verse), not the literal string.
        variants = {r["code"]: r["book_id"] for r in cur.execute("SELECT code, book_id FROM book_code_variants WHERE book_id IS NOT NULL")}
        def book_id_of(tok):
            if tok in variants: return variants[tok]
            bids = {variants[cp] for cp in variants if cp.startswith(tok) or tok.startswith(cp)}
            return next(iter(bids)) if len(bids) == 1 else None
        existing = set()
        for (rf,) in cur.execute("SELECT DISTINCT reference FROM wa_verse_records WHERE COALESCE(delete_flagged,0)=0 AND reference LIKE '% %'"):
            tk, _, rs = rf.partition(" ")
            existing.add((book_id_of(tk) or tk, rs))
        def verse_exists(ref):
            tok, _, rest = ref.partition(" ")
            return ((book_id_of(tok), rest) in existing) or ((tok, rest) in existing)
        # FA-18 cited verses exist
        cited = sorted(set(VERSE.findall(eb)))
        absent = [r for r in cited if not verse_exists(r)]
        g2.append(("FA-18", "STOP" if absent else "PASS", (f"The essay cites {len(absent)} verse(s) not in the corpus: {absent}. Remove or replace them.") if absent else f"All {len(cited)} cited verses exist in the corpus.", "CA-2" if absent else ""))
        # FA-20 jargon
        body_noheader = "\n".join(eb.splitlines()[5:])
        jl = sorted({m.group(0) for pat in JARGON for m in re.finditer(pat, body_noheader)})
        g2.append(("FA-20", "WARN" if jl else "PASS", (f"Project jargon leaked into the reader-facing essay: {jl}") if jl else "No project jargon in the essay.", "CA-2" if jl else ""))
        # FA-21 coverage + grounding: (a) every characteristic represented; (b) statements without a citation
        covered = []; missing = []
        for c in chars:
            words = [w for w in re.findall(r"[A-Za-z]{4,}", re.sub(r"^[A-Z]\s*—\s*", "", c["short_name"])) if w.lower() not in ("felt", "settled", "interior", "state", "affect")]
            if any(re.search(r"\b" + re.escape(w) + r"\b", eb, re.I) for w in words[:3]): covered.append(c["short_name"].split("—")[0].strip())
            else: missing.append(c["short_name"].split("—")[1].strip() if "—" in c["short_name"] else c["short_name"])
        # grounding test — an analytical claim should rest on a quoted verse (essay style §6)
        REF = re.compile(r"\b[1-3]?[A-Z][a-z]{1,4}\s+\d+:\d+")  # matches parenthesised or inline references
        prose = " ".join(l for l in eb.splitlines() if l.strip() and l[0] not in "#-*" and not l.startswith("> "))
        sents = re.split(r"(?<=[.!?])\s+(?=[\"A-Z])", prose)
        sub_idx = [i for i, s in enumerate(sents) if len(s.split()) >= 12 and not s.strip().endswith("?")]
        uncited = [sents[i] for i in sub_idx if not REF.search(sents[i]) and not (i+1 < len(sents) and REF.search(sents[i+1]))]
        ex = " | ".join('"' + re.sub(r"\s+", " ", u.strip())[:95] + '…"' for u in uncited[:3])
        status = "REVIEW" if (missing or uncited) else "PASS"
        cov_txt = (f"Essay covers {len(covered)}/{len(chars)} characteristics" + (f" (not visibly: {missing})" if missing else "")
                   + f". Grounding: {len(uncited)} of {len(sub_idx)} substantive statements carry NO verse citation (in the statement or the next sentence).")
        g2.append(("FA-21", status, cov_txt + " Each uncited statement is either an ungrounded analytical claim (fix) or acceptable framing/synthesis (accept) — review. " + (f"Examples: {ex}" if ex else ""), "CA-1" if status == "REVIEW" else ""))
        # FA-22 derive
        g2.append(("FA-22", "REVIEW", "Researcher check: confirm the essay asserts nothing the captured findings don't carry (cannot be verified mechanically).", "CA-1"))
        # FA-23 superlatives in essay
        es = list(dict.fromkeys([m.group(0) for pat in SUPERLATIVE for m in re.finditer(pat, eb, re.I)]))
        g2.append(("FA-23", "REVIEW" if es else "PASS", (f"Possibly-unsubstantiated superlative(s) in the essay: " + "; ".join(f'\"{s}\"' for s in es[:6])) if es else "No unsubstantiated superlatives in the essay.", "CA-2" if es else ""))

    # ===================== REPORT =====================
    def tally(items):
        from collections import Counter; return Counter(s for _, s, _, _ in items)
    t1, t2 = tally(g1), tally(g2)
    L = [f"# Findings audit — {cc}", "",
         f"_Run: {a.date} · read-only · spec wa-findings-audit-spec-v1_0_  ", "",
         f"**GATE 1 (findings → DB):** PASS {t1['PASS']} · REVIEW {t1['REVIEW']} · WARN {t1['WARN']} · STOP {t1['STOP']}",
         f"**GATE 2 (essay):** PASS {t2['PASS']} · REVIEW {t2['REVIEW']} · WARN {t2['WARN']} · STOP {t2['STOP']}", "",
         "> Each item below is written to be read on its own. The bracket shows the check id and severity; "
         "*STOP* = blocks unless you release it · *REVIEW* = needs your sign-off · *WARN* = hygiene · *PASS* = clear. "
         "Suggested action: CA-1 accept · CA-2 CC fixes the file · CA-3 you direct a file/DB fix · CA-4 set aside & redo in Chat.", ""]
    for title, items in [("Gate 1 — findings", g1), ("Gate 2 — essay", g2)]:
        L.append(f"## {title}")
        L.append("")
        order = {"STOP": 0, "REVIEW": 1, "WARN": 2, "PASS": 3}
        for code, st, plain, act in sorted(items, key=lambda x: order.get(x[1], 9)):
            tag = f"[{code} · {st}" + (f" → {act}" if act else "") + "]"
            L.append(f"- **{st}** — {plain}  `{tag}`")
        L.append("")
    open_stop = [i for i in g1+g2 if i[1] == "STOP"]
    L.append("## To resolve")
    L.append("")
    if open_stop:
        L.append(f"**{len(open_stop)} STOP(s) open** — release (with CA-1/3/4) or let CC fix (CA-2):")
        for code, st, plain, act in open_stop: L.append(f"- {code}: {plain}")
    else:
        L.append("No STOPs. ")
    review = [i for i in g1+g2 if i[1] == "REVIEW"]
    L.append("")
    L.append(f"**{len(review)} REVIEW item(s)** need your decision (record the corrective action against each).")
    L.append("")
    out = os.path.join(fdir, f"wa-findings-audit-{cc}-{a.date}.md")
    os.makedirs(fdir, exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(L))
    print(f"WROTE {out}  ·  G1 STOP {t1['STOP']} REVIEW {t1['REVIEW']} | G2 STOP {t2['STOP']} REVIEW {t2['REVIEW']}")
    return 1 if open_stop else 0


if __name__ == "__main__":
    sys.exit(main())
