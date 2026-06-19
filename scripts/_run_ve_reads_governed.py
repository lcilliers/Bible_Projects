"""_run_ve_reads_governed.py (2026-06-17) — governed corpus API read for ONE VE field.
Honours the 01c API governance: BATCHED BY VERSE (token-min: verse text sent once), ORDERED
(book/chapter/verse), SELF-VERIFIED (submitted = applied + NONE + missing), PROCESSING MONITOR
(per-round time/tokens/cost) with a CIRCUIT-BREAKER (round out of range -> STOP) and a COST CAP.
RESIDUE-ONLY (never re-reads a resolved item) · T2 EXCLUDED · RESUMABLE (re-run continues).
Reads ANTHROPIC_API_KEY from .env. Applies inline (provenance=<field>_read_api, reversible), commits per batch.

  python scripts/_run_ve_reads_governed.py --field cause --live [--max-cost 30] [--limit-verses N]
"""
import argparse, json, os, re, sys, time, sqlite3
sys.stdout.reconfigure(encoding="utf-8")
if not os.getenv("ANTHROPIC_API_KEY") and os.path.exists(".env"):
    for line in open(".env", encoding="utf-8"):
        if line.strip().startswith("ANTHROPIC_API_KEY="):
            os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip().strip('"').strip("'")
import anthropic
DB = os.path.join("database", "bible_research.db")
RATES = {"claude-sonnet-4-6": (3.0, 15.0), "claude-haiku-4-5-20251001": (1.0, 5.0)}
STAMP = "2026-06-18T00:00:00Z"

# field -> (residue value to target, prompt)
SPECS = {
    "cause": ("pending-read",
        "For EACH term, state what AROUSES / elicits the inner-being state it names in THIS verse (the cause). "
        "A short phrase. If the verse states no cause, value=\"NONE\"."),
    "location": ("UNRESOLVED",
        "Each verse contains an inner-being seat word whose sense is ambiguous (usually qereb 'inward part / midst', "
        "sometimes ruach/pneuma 'spirit/wind/breath'). For EACH term decide whether that word denotes the human inner "
        "being as a CONSTITUTIONAL SEAT in THIS verse: answer \"inward-parts\" (qereb = a person's innermost being, "
        "e.g. 'within me', 'my heart within me') or \"spirit\" (ruach/pneuma = the human spirit-seat). If instead it is "
        "a LOCATIVE 'in the midst of / among' a place/people/group, or the divine Spirit, a disposition, wind, or "
        "breath (NOT a seat of the person) -> \"NONE\"."),
    "divine-involvement": ("UNRESOLVED",
        "For EACH term, state GOD's role toward the inner-being term in THIS verse — EXACTLY one of: "
        "agent | possessor | giver | object | addressee | none."),
    "object-type": ("thing/abstract",
        "For EACH term, the inner-being term is directed at an object. Classify that object in THIS verse — EXACTLY one of: "
        "threat | person | God | spiritual-being | situation | abstract | thing."),
    # valence: residue=None -> UNITS mode (read every M-cluster unit not yet valence-read; upsert, not residue-update)
    "valence": (None,
        "For EACH term, does the inner-being state it names carry a MORAL valence in THIS verse — EXACTLY one of: "
        "righteous | sinful | commanded | forbidden | neutral | NONE. Use NONE if the verse gives no moral framing."),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--field", required=True, choices=list(SPECS))
    ap.add_argument("--model", default="claude-sonnet-4-6")
    ap.add_argument("--verses-per-batch", type=int, default=60)
    ap.add_argument("--max-cost", type=float, default=30.0, help="USD cost cap — STOP before exceeding")
    ap.add_argument("--max-round-sec", type=float, default=150.0, help="circuit-breaker: STOP if a round exceeds this")
    ap.add_argument("--limit-verses", type=int, default=0)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    residue, prompt = SPECS[a.field]
    prov = a.field.replace("-", "_") + "_read_api"
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    if residue is None:   # UNITS mode (valence): every M-cluster non-T2 unit not yet read for this field
        rows = cur.execute("""
            SELECT vc.id vcid, vr.reference ref, vr.verse_text vt, m.transliteration tr, m.gloss gloss
            FROM verse_context vc
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
            JOIN mti_terms m ON m.id = vc.mti_term_id
            WHERE COALESCE(vc.delete_flagged,0)=0 AND m.cluster_code IS NOT NULL AND m.cluster_code<>'T2'
              AND NOT EXISTS (SELECT 1 FROM ve_lexical y WHERE y.verse_context_id=vc.id
                              AND y.ve_label=? AND y.source_provenance=?)
            ORDER BY vr.book_id, vr.chapter, vr.verse_num, vc.id""", (a.field, prov)).fetchall()
    else:                 # RESIDUE mode: rows still carrying the residue token
        rows = cur.execute("""
            SELECT x.verse_context_id vcid, vr.reference ref, vr.verse_text vt, m.transliteration tr, m.gloss gloss
            FROM ve_lexical x
            JOIN verse_context vc ON vc.id = x.verse_context_id
            JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
            JOIN mti_terms m ON m.id = vc.mti_term_id
            WHERE x.ve_label=? AND x.value=? AND COALESCE(x.delete_flagged,0)=0
              AND m.cluster_code IS NOT NULL AND m.cluster_code<>'T2'
            ORDER BY vr.book_id, vr.chapter, vr.verse_num, x.verse_context_id""", (a.field, residue)).fetchall()

    # group by verse (token-min)
    verses = {}
    for r in rows:
        v = verses.setdefault(r["ref"], {"reference": r["ref"], "verse_text": r["vt"], "terms": []})
        v["terms"].append({"vcid": r["vcid"], "term": r["tr"], "gloss": r["gloss"]})
    vlist = list(verses.values())
    if a.limit_verses:
        vlist = vlist[:a.limit_verses]
    nitems = sum(len(v["terms"]) for v in vlist)
    print(f"[{a.field}] residue: {nitems} items across {len(vlist)} verses · cap ${a.max_cost} · model {a.model}"
          f"{' (DRY-RUN)' if a.dry_run else ''}")
    if a.dry_run:
        print("  sample verse-unit:", json.dumps(vlist[0], ensure_ascii=False)[:300] if vlist else "(none)")
        return

    client = anthropic.Anthropic()
    ri, ro = RATES.get(a.model, (3.0, 15.0))
    instr = (prompt + " OUTPUT JSON ONLY: a flat array [{\"vcid\":int,\"value\":\"...\"}]. Return EXACTLY ONE object "
             "per term — the array length MUST equal the total number of terms across all verses below; do NOT omit "
             "any vcid. Use the vcid given verbatim.")
    it = ot = applied = none = 0
    times = []
    cost = 0.0
    nb = (len(vlist) + a.verses_per_batch - 1) // a.verses_per_batch
    for bi in range(nb):
        chunk = vlist[bi * a.verses_per_batch:(bi + 1) * a.verses_per_batch]
        content = instr + "\n\nVERSES:\n" + json.dumps(chunk, ensure_ascii=False)
        t0 = time.time()
        resp = client.messages.create(model=a.model, max_tokens=8000,
                                      messages=[{"role": "user", "content": content}])
        dt = time.time() - t0
        times.append(dt)
        text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
        it += resp.usage.input_tokens; ot += resp.usage.output_tokens
        cost = it / 1e6 * ri + ot / 1e6 * ro
        # apply this batch
        m = re.search(r"\[.*\]", text, re.S)
        ba = bn = 0
        if m:
            try:
                for d in json.loads(m.group(0)):
                    vcid = d.get("vcid"); val = (d.get("value") or "").strip()
                    if vcid is None:
                        continue
                    is_none = (not val) or val.upper() == "NONE"
                    if residue is None:   # UNITS mode (valence) — UPSERT: update any existing valence row, else insert
                        if is_none:
                            u = cur.execute("UPDATE ve_lexical SET delete_flagged=1, notes='read pass: NONE', source_provenance=? "
                                            "WHERE verse_context_id=? AND ve_label=? AND COALESCE(delete_flagged,0)=0", (prov, vcid, a.field)).rowcount
                            if not u:
                                cur.execute("INSERT INTO ve_lexical (verse_context_id, ve_nr, ve_label, related_tier, value, notes, source_provenance, delete_flagged, created_at) "
                                            "VALUES (?,21,?, 'T0.3.1','NONE','read pass: NONE',?,1,?)", (vcid, a.field, prov, STAMP))
                            bn += 1
                        else:
                            u = cur.execute("UPDATE ve_lexical SET value=?, source_provenance=?, notes='resolved by read pass' "
                                            "WHERE verse_context_id=? AND ve_label=? AND COALESCE(delete_flagged,0)=0", (val[:140], prov, vcid, a.field)).rowcount
                            if not u:
                                cur.execute("INSERT INTO ve_lexical (verse_context_id, ve_nr, ve_label, related_tier, value, notes, source_provenance, delete_flagged, created_at) "
                                            "VALUES (?,21,?, 'T0.3.1',?,'resolved by read pass',?,0,?)", (vcid, a.field, val[:140], prov, STAMP))
                            ba += 1
                    elif is_none:
                        cur.execute("UPDATE ve_lexical SET delete_flagged=1, notes='read pass: NONE', source_provenance=? "
                                    "WHERE verse_context_id=? AND ve_label=? AND value=? AND COALESCE(delete_flagged,0)=0",
                                    (prov, vcid, a.field, residue)); bn += cur.rowcount
                    else:
                        cur.execute("UPDATE ve_lexical SET value=?, source_provenance=?, notes='resolved by read pass' "
                                    "WHERE verse_context_id=? AND ve_label=? AND value=? AND COALESCE(delete_flagged,0)=0",
                                    (val[:140], prov, vcid, a.field, residue)); ba += cur.rowcount
            except Exception as e:
                print(f"  WARN batch {bi+1}: parse/apply error {e}")
        conn.commit()
        applied += ba; none += bn
        mean = sum(times) / len(times)
        print(f"  round {bi+1}/{nb}: {dt:.1f}s · {len(chunk)} verses · set {ba} NONE {bn} · "
              f"tok {resp.usage.input_tokens}/{resp.usage.output_tokens} · cum ${cost:.3f} · mean {mean:.1f}s")
        # circuit-breaker
        if dt > a.max_round_sec or (len(times) >= 3 and dt > 3 * mean):
            print(f"  ⛔ CIRCUIT-BREAKER: round {dt:.1f}s out of range (cap {a.max_round_sec}s / 3×mean) — STOP. Resumable.")
            break
        if cost > a.max_cost:
            print(f"  ⛔ COST CAP: ${cost:.2f} > ${a.max_cost} — STOP before next round. Resumable.")
            break

    # self-verify
    remaining = cur.execute("""SELECT COUNT(*) FROM ve_lexical x JOIN verse_context vc ON vc.id=x.verse_context_id
        JOIN mti_terms m ON m.id=vc.mti_term_id WHERE x.ve_label=? AND x.value=? AND COALESCE(x.delete_flagged,0)=0
        AND m.cluster_code<>'T2'""", (a.field, residue)).fetchone()[0]
    print(f"\n[{a.field}] DONE this run: set {applied} · NONE {none} · resolved {applied+none} · "
          f"residue remaining {remaining} · tokens {it:,}/{ot:,} · cost ${cost:.3f}")
    print(f"  self-verify: started {nitems} · resolved {applied+none} · still-residue {remaining} "
          f"({'OK' if remaining == nitems - (applied+none) else 'CHECK'})")


if __name__ == "__main__":
    main()
