"""v3_2_l1.py  — V3_2 Level 1 (verse establishment) command.

The sanctioned V3_2 L1 runner: mechanical STEP-sense application for a cluster's verses. WRITES to the live
DB, then reports (rollup design §3 L1; rollup instruction v3_2). Per discipline 2, L1 assigns ONLY where the
sense is unambiguous (single-sense terms); ALL multi-sense terms are flagged residue for the L2 deep read —
L1 never force-resolves a double meaning.

Per relevant span it writes: sense_multiplicity · pole · pole_is_metaphor · keywords (STEP-capture) ·
step_envelope_note · residue_flag · and (single-sense only) step_meaning_applied + sense_id.
analysis_note (the AI/L3 layer) is PRESERVED. Cluster status → 'In Progress'.

Usage:  python scripts/v3_2_l1.py --cluster M01 --report Sessions-v2/M01-Fear/<file>.md
"""
import argparse, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

# ---- tokenisation / sense parsing (consolidated from the prototypes) ----
STOP = set("""a an and or the of to be is are was were in on at as by for with from into onto upon that this
these those it its he she his her him they them their have has had not no any some all such which who whom
whose when where while because so then than also more most very own same other another each every both few
many much s t qal niphal piel pual hiphil hophal hithpael peal pael aphel haphel ithpeal twot bdb means also
spelled cause caused make made get got thing things state condition manner way feeling expression aramaic
equivalent used always act active absolute context cor col eph mt mk lk heb part""".split())
SUF = ("ingly","ing","edly","ed","ied","ies","ness","ment","ful","less","ity","ly","es","s")
WORD = re.compile(r"[a-zA-Z]+"); PAREN = re.compile(r"\([^)]*\)"); SREF = re.compile(r"\b[A-Z][a-z]{1,2}\.?\s*\d")
STEMS = re.compile(r"\((Qal|Niphal|Piel|Pual|Hiphil|Hophal|Hithpael)\)", re.I)
NUMSENSE = re.compile(r"(?<![a-z])(\d)\)")
HOMONYM = re.compile(r"TWOT|to shoot|to pour", re.I)   # non-biblical homonym markers (e.g. ya.re TWOT 'shoot/pour')

PHYS_LIT = {"wave","waves","breaker","shatter","shattered","broken","break"}
METAPHOR = {"burn","burning","heat","scorch","scorching","melt","melted","tremble","trembling","quake",
            "shudder","kindle","kindled"}
EXT = {"punish","punishment","penalty","vengeance","judgment","judgement","recompense","retribution"}

def stem(w):
    w=w.lower()
    for s in SUF:
        if len(w)>len(s)+2 and w.endswith(s): return w[:-len(s)]
    return w
def toks(t):
    if not t: return set()
    t=PAREN.sub(" ", t)
    out=set()
    for m in WORD.findall(t):
        if len(m)<3: continue
        sm=stem(m)
        if sm in STOP or len(sm)<3: continue
        out.add(sm)
    return out

def term_profile(c, strongs, gloss):
    """Return dict: sense-set tokens, single/multi, pole, metaphor flag, keywords, envelope, sense_id."""
    inv = c.execute("SELECT id, step_search_gloss, short_def_mounce, meaning, parsed_meaning_id "
                    "FROM wa_term_inventory WHERE strongs_number=? AND COALESCE(delete_flagged,0)=0", (strongs,)).fetchone()
    sense_text=""; sense_id=None
    if inv and inv["parsed_meaning_id"]:
        rows=c.execute("SELECT id, sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=? ORDER BY sort_order",
                       (inv["parsed_meaning_id"],)).fetchall()
        if rows: sense_id=rows[0]["id"]
        sense_text=" ".join(r["sense_text"] or "" for r in rows)
    homonym = bool(HOMONYM.search(sense_text or ""))
    # sense-set tokens, homonym-filtered (drop the non-biblical homonym tail words)
    full = " ".join(filter(None, [gloss, inv["step_search_gloss"] if inv else "",
                                   inv["short_def_mounce"] if inv else "", inv["meaning"] if inv else "", sense_text]))
    tk = toks(full)
    if homonym:
        tk -= {"shoot","pour"}                              # drop the flagged homonym sense
    # single/multi
    stems = set(m.group(1).title() for m in STEMS.finditer(sense_text or ""))
    nums  = set(NUMSENSE.findall(sense_text or ""))
    poles = set()
    if tk & EXT: poles.add("external")
    if tk & PHYS_LIT: poles.add("physical")
    if tk - EXT - PHYS_LIT - METAPHOR: poles.add("inner")
    multi = len(stems) >= 2 or len(nums) >= 2 or len(poles) >= 2
    # pole (term-level first pass): default inner; external/physical via lexicon; metaphor flagged not auto-physical
    metaphor = bool(tk & METAPHOR)
    if "external" in poles: pole = "external"
    elif "physical" in poles: pole = "physical"
    else: pole = "inner"
    # keywords = STEP-capture: gloss head + sense tokens, noise/ref/homonym filtered
    kw = [w for w in sorted(tk) if not SREF.match(w)][:10]
    # terse step meaning (single-sense use)
    terse = " / ".join(dict.fromkeys(filter(None, [
        gloss, inv["step_search_gloss"] if inv else "", inv["short_def_mounce"] if inv else ""])))[:160]
    envelope = (sense_text or full)[:400].replace("\n", " ").strip()
    # why single/multi (for the residue listing — lets the researcher assess the L1/L2 split)
    rp = []
    if len(stems) >= 2: rp.append(f"{len(stems)} stems ({'/'.join(sorted(stems))})")
    if len(nums) >= 2:  rp.append(f"{len(nums)} numbered senses")
    if len(poles) >= 2: rp.append("pole-span:" + "/".join(sorted(poles)))
    reason = "; ".join(rp) if multi else "single sense"
    return dict(multi=multi, pole=pole, metaphor=metaphor, keywords=kw, sense_id=sense_id,
                terse=terse, envelope=envelope, homonym=homonym, reason=reason)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--cluster", required=True); ap.add_argument("--report", required=True)
    a=ap.parse_args()
    conn=sqlite3.connect(DB); conn.row_factory=sqlite3.Row; c=conn.cursor()
    cc=a.cluster

    # 1) status -> In Progress
    conn.execute("UPDATE cluster SET status='In Progress', last_updated_date=? WHERE cluster_code=?",
                 (_now(), cc)); conn.commit()

    import collections
    terms=c.execute("SELECT id, strongs_number, transliteration, gloss, language FROM mti_terms "
                    "WHERE cluster_code=? AND COALESCE(delete_flagged,0)=0", (cc,)).fetchall()
    stats=dict(terms=len(terms), single=0, multi=0, assigned=0, residue=0, setaside=0,
               pole={}, metaphor=0, homonym=0, touched=0)
    assigned_terms=[]   # (translit, gloss, meaning, keywords, [(ref, text)])
    residue_terms=[]    # (translit, gloss, reason, [(ref, text)])
    kw_freq=collections.Counter()

    def clean(txt, ref):
        if not txt: return ""
        txt=re.sub(r"\s+", " ", txt).strip()
        if ref and txt.startswith(ref): txt=txt[len(ref):].strip()  # drop leading ref dup
        return txt[:160]

    for t in terms:
        p=term_profile(c, t["strongs_number"], t["gloss"])
        if p["multi"]: stats["multi"]+=1
        else: stats["single"]+=1
        if p["metaphor"]: stats["metaphor"]+=1
        if p["homonym"]: stats["homonym"]+=1
        kw_json=json.dumps(p["keywords"])
        rows=c.execute("""SELECT vc.id, vc.is_relevant, vr.reference, vr.verse_text
            FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
            WHERE vc.mti_term_id=? AND COALESCE(vc.delete_flagged,0)=0
            ORDER BY vr.book_id, vr.chapter, vr.verse_num""", (t["id"],)).fetchall()
        a_verses=[]; r_verses=[]
        for r in rows:
            if not r["is_relevant"]:
                stats["setaside"]+=1; continue
            stats["touched"]+=1
            stats["pole"][p["pole"]]=stats["pole"].get(p["pole"],0)+1
            vtxt=clean(r["verse_text"], r["reference"])
            if p["multi"]:
                conn.execute("""UPDATE verse_context SET sense_multiplicity='multi', residue_flag=1,
                    pole=?, pole_is_metaphor=?, keywords=?, step_envelope_note=?,
                    step_meaning_applied=NULL, sense_id=NULL WHERE id=?""",
                    (p["pole"], 1 if p["metaphor"] else 0, kw_json, p["envelope"], r["id"]))
                stats["residue"]+=1; r_verses.append((r["reference"], vtxt))
            else:
                conn.execute("""UPDATE verse_context SET sense_multiplicity='single', residue_flag=0,
                    pole=?, pole_is_metaphor=?, keywords=?, step_envelope_note=?,
                    step_meaning_applied=?, sense_id=? WHERE id=?""",
                    (p["pole"], 1 if p["metaphor"] else 0, kw_json, p["envelope"], p["terse"], p["sense_id"], r["id"]))
                stats["assigned"]+=1; a_verses.append((r["reference"], vtxt))
                for w in p["keywords"]: kw_freq[w]+=1
        if a_verses: assigned_terms.append((t["transliteration"], t["gloss"], p["terse"], p["keywords"], p["pole"], p["metaphor"], a_verses))
        if r_verses: residue_terms.append((t["transliteration"], t["gloss"], p["reason"], r_verses))
    conn.commit()

    # ---- report ----
    L=[f"# {cc} — V3_2 L1 run report", ""]
    L.append(f"> **WRITE-then-report · {os.path.basename(a.report)} · CC.** V3_2 L1 (verse establishment) "
             f"executed on the live DB (`scripts/v3_2_l1.py`). Cluster status → **In Progress**. "
             f"Per discipline 2, L1 assigned only single-sense terms; all multi-sense → **residue for L2**.")
    L.append("")
    L.append("## Result")
    L.append("")
    L.append(f"- Terms: **{stats['terms']}** — single-sense **{stats['single']}**, multi-sense **{stats['multi']}**")
    L.append(f"- Relevant verses touched: **{stats['touched']}**")
    L.append(f"  - **assigned a STEP meaning (single-sense): {stats['assigned']}**")
    L.append(f"  - **residue → L2 (multi-sense): {stats['residue']}** ({100*stats['residue']//max(stats['touched'],1)}% of touched)")
    L.append(f"- Set-aside verses (left as-is): {stats['setaside']}")
    L.append(f"- Pole distribution (verses): " + ", ".join(f"{k} {v}" for k,v in sorted(stats['pole'].items(), key=lambda x:-x[1])))
    L.append(f"- Terms flagged `pole_is_metaphor` (heat/tremble/melt): {stats['metaphor']} · homonym-filtered terms: {stats['homonym']}")
    L.append("")
    L.append("## What L1 wrote (per relevant verse_context row)")
    L.append("")
    L.append("- single-sense → `step_meaning_applied` (terse STEP sense) + `sense_id` + `sense_multiplicity='single'` + `residue_flag=0`")
    L.append("- multi-sense → `sense_multiplicity='multi'` + `residue_flag=1` (no meaning assigned — deferred to L2)")
    L.append("- all → `pole`, `pole_is_metaphor`, `keywords` (STEP-capture JSON), `step_envelope_note`")
    L.append("- `analysis_note` (existing AI/L3 layer) **preserved, untouched**")
    L.append("")

    def esc(s): return (s or "").replace("|", "\\|")

    # a) keyword analysis
    L.append("## a · Keyword analysis — STEP-capture keywords across assigned verses")
    L.append("")
    L.append(f"Distinct keywords on assigned verses: **{len(kw_freq)}**. Top 40 by verse-frequency:")
    L.append("")
    L.append("| keyword | verses | keyword | verses | keyword | verses | keyword | verses |")
    L.append("|---|---|---|---|---|---|---|---|")
    top = kw_freq.most_common(40)
    for i in range(0, len(top), 4):
        cells = []
        for w, n in top[i:i+4]:
            cells += [f"`{w}`", str(n)]
        while len(cells) < 8: cells += ["", ""]
        L.append("| " + " | ".join(cells) + " |")
    L.append("")

    # b) assigned verses
    L.append("## b · Assigned verses (single-sense) — reference · text · STEP-applied meaning")
    L.append("")
    L.append(f"{stats['assigned']} verses across {len(assigned_terms)} single-sense terms. "
             "The **STEP-applied meaning** is the per-term head (the same for each of a term's verses at L1; "
             "the per-verse contextual reading is L2 work).")
    L.append("")
    for translit, gloss, terse, kw, pole, met, verses in sorted(assigned_terms):
        L.append(f"### {translit} ({gloss}) → **{esc(terse)}**")
        L.append(f"*pole `{pole}`{' · metaphor-flagged' if met else ''} · keywords {kw[:8]} · {len(verses)} verses*")
        L.append("")
        L.append("| ref | verse text |")
        L.append("|---|---|")
        for ref, txt in verses: L.append(f"| {ref} | {esc(txt)} |")
        L.append("")

    # c) residue verses
    L.append("## c · Postponed to L2 (multi-sense residue) — assess why each is not L1")
    L.append("")
    L.append(f"{stats['residue']} verses across {len(residue_terms)} multi-sense terms. Each term shows **why "
             "it was classified multi-sense** (the signal that triggered the L1→L2 deferral, per discipline 2). "
             "Read the verses to judge whether the deferral is right.")
    L.append("")
    for translit, gloss, reason, verses in sorted(residue_terms):
        L.append(f"### {translit} ({gloss}) — **multi-sense: {esc(reason)}** · {len(verses)} verses")
        L.append("")
        L.append("| ref | verse text |")
        L.append("|---|---|")
        for ref, txt in verses: L.append(f"| {ref} | {esc(txt)} |")
        L.append("")

    L.append("## Notes for the L1→L2 gate")
    L.append("")
    L.append("- **Morphology capture deferred to L2.** Since L1 assigns only single-sense (multi → L2), the "
             "per-verse stem (which *helps resolve* multi-sense) is an L2 input — captured there, not forced "
             "into L1. Flagged for your confirmation.")
    L.append("- **`sense_id` is coarse** (points to the term's parsed sense row, not a split sub-sense — the "
             "BDB tree is not yet split into stem-branch rows). Precise sub-sense pointing is a refinement.")
    L.append("- **Pole is term-level first-pass** (per-verse pole refines at L2); literal-physical vs metaphor "
             "is flagged (`pole_is_metaphor`) not auto-assigned (R6).")
    L.append("- **Next:** run the L1 audit, then the **L1→L2 gate** (researcher review).")
    os.makedirs(os.path.dirname(a.report), exist_ok=True)
    open(a.report,"w",encoding="utf-8").write("\n".join(L))
    print(f"{cc} L1: {stats['assigned']} assigned, {stats['residue']} residue, {stats['setaside']} set-aside. Wrote {a.report}")

def _now():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

if __name__=="__main__":
    main()
