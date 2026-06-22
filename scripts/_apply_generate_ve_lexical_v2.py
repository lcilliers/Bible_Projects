"""_apply_generate_ve_lexical_v2.py (2026-06-16) — generate the v2 verse-lexical for ALL analysed
term-in-verse units and write to `ve_lexical`, replacing the interim mechanical_v1.

Reuses the engine (`_ve_engine_v2.py`) derivation over the persisted measure layer (verse_morphology +
lexicon). Whole-verse reset (01b P6): each unit's existing ve_lexical rows are deleted, then the v2 rows
written. Per-verse timing + circuit-breaker (VE_MAX_SEC). Pre-run DB snapshot for safety.

ITERATION-1 seed lists (faculty/location-seat/intensifier/divine/origin are seeds) — the run is fully
reproducible, so re-run after expanding any list. source_provenance='v2_engine_iter1'.

  python scripts/_apply_generate_ve_lexical_v2.py --dry-run [--limit 50]
  python scripts/_apply_generate_ve_lexical_v2.py --live [--limit N]
"""
import argparse, os, sqlite3, sys, time, shutil
sys.path.insert(0, os.path.dirname(__file__))
import _ve_engine_v2 as eng
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
SNAP = os.path.join("backups", "bible_research_pre-ve_lexical-v2_20260616.db")
PROV = "v2_engine_iter1"
STAMP = "2026-06-16T00:00:00Z"

# engine item label -> (ve_nr, related_tier).  'mode' is skipped (it is a column); lexical_note handled separately.
VE_MAP = {
    "sense": (1, "T7.1.3"), "type": (2, "T1.2.1"), "compound": (3, "T6.1.1"),
    "location": (5, "T2"), "origin": (6, "T2.9.1"), "faculty": (7, "T3"),
    "divine-involvement": (8, "T0.1.2"), "immediate-response": (11, "T1.5.1"),
    "relational": (13, "T1.1.3"), "object": (16, "T1.1.4"), "object-type": (16, "T1.1.4"),
    "cause": (17, "T2.9.2"), "how": (18, "T1.4.1"), "intensity": (19, "T1.6.1"),
    "experiencer": (20, "T2.8.1"), "valence": (21, "T0.3.1"), "cause_clause": (22, "T2.9.3"),
}


def to_rows(vcid, items):
    rows = []
    for (it, value, cite) in items:
        if it == "mode":
            continue
        if it == "lexical_note":
            rows.append((vcid, 0, "lexical_note", None, value, cite, "audit", 0, STAMP)); continue
        nr, tier = VE_MAP.get(it, (None, None))
        rows.append((vcid, nr, it, tier, value, cite, PROV, 0, STAMP))
    return rows


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--vcids", default="", help="restrict to these verse_context ids (comma-list or @file) — targeted top-up")
    a = ap.parse_args()
    only_vcids = set()
    if a.vcids:
        raw = open(a.vcids[1:], encoding="utf-8").read() if a.vcids.startswith("@") else a.vcids
        only_vcids = {int(x) for x in raw.replace("\n", ",").split(",") if x.strip()}
    MAX_SEC = float(os.environ.get("VE_MAX_SEC", "30"))
    conn = sqlite3.connect(DB, timeout=600); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    lex = eng.LexDB(cur)

    units = cur.execute("""
        SELECT vc.id vcid, vc.mti_term_id mti, vr.transliteration translit, m.gloss gloss,
               m.strongs_number strong, m.cluster_code cluster, vr.reference ref, vr.target_word tw, v.id verse_id
        FROM verse_context vc
        JOIN wa_verse_records vr ON vr.id = vc.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
        JOIN mti_terms m ON m.id = vc.mti_term_id
        JOIN verse v ON v.reference = vr.reference
        WHERE COALESCE(vc.delete_flagged,0)=0 AND m.cluster_code IS NOT NULL
        ORDER BY v.id, vc.id""").fetchall()
    if only_vcids:
        units = [u for u in units if u["vcid"] in only_vcids]
        print(f"scoped to --vcids: {len(units)} of {len(only_vcids)} requested units")
    if a.limit:
        units = units[:a.limit]
    print(f"units to generate: {len(units):,}{' (DRY-RUN)' if a.dry_run else ''}")

    if a.live:
        cur.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        os.makedirs("backups", exist_ok=True)
        if not os.path.exists(SNAP):
            shutil.copy2(DB, SNAP); print(f"snapshot: {SNAP}")

    wordcache = {}
    timings = []
    nrows = nunits = nnarr = nskip_t2 = 0
    t_verse = time.time(); cur_verse = None
    for u in units:
        if u["verse_id"] not in wordcache:
            wordcache[u["verse_id"]] = eng.load_words(cur, u["verse_id"])
        words = wordcache[u["verse_id"]]
        # 01c §A3/A4: T2-grammatical units (function words: prep/pronoun/particle/adverb/conj/…) are
        # NOT inner-being terms — generate no lexical for them. T2-content (noun/verb/adjective) is kept as context.
        if u["cluster"] == "T2":
            _tw = eng.find_term(words, u["strong"])
            if _tw is None or _tw["pos"] not in ("noun", "verb", "adjective"):
                if a.live:   # dispose any stale rows for this now-excluded unit (no rewrite)
                    cur.execute("DELETE FROM ve_lexical WHERE verse_context_id=? AND source_provenance IN ('v2_engine_iter1','audit')", (u["vcid"],))
                nskip_t2 += 1
                continue
        coterms = cur.execute("""SELECT DISTINCT vr.transliteration tr, m.gloss gl, m.cluster_code cc, m.strongs_number st
            FROM verse_context vc2 JOIN wa_verse_records vr ON vr.id=vc2.verse_record_id AND COALESCE(vr.delete_flagged,0)=0
            JOIN mti_terms m ON m.id=vc2.mti_term_id
            WHERE vr.reference=? AND m.strongs_number<>? AND COALESCE(vc2.delete_flagged,0)=0""", (u["ref"], u["strong"])).fetchall()
        unit = {"ref": u["ref"], "translit": u["translit"], "gloss": u["gloss"], "strong": u["strong"],
                "cluster": u["cluster"], "tw": u["tw"], "coterms": [(c["tr"], c["gl"], c["cc"], c["st"]) for c in coterms]}
        items = eng.derive(unit, words, lex)
        rows = to_rows(u["vcid"], items)
        nrows += len(rows); nunits += 1
        if a.live:
            # ve_lexical: hard-replace the MECHANICAL rows, but PRESERVE read-resolved values across the rebuild
            # (a read-resolved or read-NONE'd cause must NOT be reverted to the mechanical 'pending-read').
            read_fields = set(r[0] for r in cur.execute("""SELECT DISTINCT ve_label FROM ve_lexical
                WHERE verse_context_id=? AND (source_provenance LIKE '%_read_api' OR notes LIKE 'read pass:%')""", (u["vcid"],)))
            wr = [r for r in rows if r[2] not in read_fields]          # skip the mechanical version of any read-decided field
            cur.execute("DELETE FROM ve_lexical WHERE verse_context_id=? AND source_provenance IN ('v2_engine_iter1','audit')", (u["vcid"],))
            cur.executemany("""INSERT INTO ve_lexical
                (verse_context_id, ve_nr, ve_label, related_tier, value, notes, source_provenance, delete_flagged, created_at)
                VALUES (?,?,?,?,?,?,?,?,?)""", wr)
            # narration = the single l2_meaning FINDING (M-cluster only): SOFT-delete the superseded one, insert new
            if u["cluster"] != "T2":
                narr = eng.narrate(unit, items)
                cur.execute("DELETE FROM finding WHERE verse_context_id=? AND provenance='l2_meaning' "
                            "AND delete_flagged=1 AND source_legacy_ref=?", (u["vcid"], "ve-narration-v2-20260616"))
                cur.execute("UPDATE finding SET delete_flagged=1, last_updated_date=? WHERE verse_context_id=? "
                            "AND provenance='l2_meaning' AND COALESCE(delete_flagged,0)=0", (STAMP, u["vcid"]))
                cur.execute("INSERT INTO finding (level, verse_context_id, mti_term_id, cluster_code, finding_value, "
                            "finding_status, provenance, source_legacy_ref, created_at, last_updated_date, delete_flagged) "
                            "VALUES ('VERSE', ?, ?, ?, ?, 'ANSWERED', 'l2_meaning', 've-narration-v2-20260616', ?, ?, 0)",
                            (u["vcid"], u["mti"], u["cluster"], narr, STAMP, STAMP))
                nnarr += 1
        # per-verse timing (circuit-breaker)
        if cur_verse is None: cur_verse = u["verse_id"]
        if u["verse_id"] != cur_verse:
            dt = time.time() - t_verse; timings.append(dt)
            if dt > MAX_SEC:
                if a.live: conn.commit()
                print(f"\n⛔ CIRCUIT-BREAKER: a verse took {dt:.1f}s > {MAX_SEC}s — aborting."); break
            cur_verse = u["verse_id"]; t_verse = time.time()
        if a.live and nunits % 2000 == 0:
            conn.commit(); print(f"  …{nunits:,} units, {nrows:,} rows")
    if a.live:
        conn.commit()

    tot = cur.execute("SELECT COUNT(*) FROM ve_lexical WHERE source_provenance=?", (PROV,)).fetchone()[0] if a.live else 0
    print(f"\n{'LIVE' if a.live else 'DRY-RUN'}: {nunits:,} units · {nrows:,} ve_lexical rows"
          f"{' written ('+format(tot, ',')+' active v2 in table)' if a.live else ' (not written)'} · {nnarr:,} narration findings"
          f" · {nskip_t2:,} T2-grammatical units skipped (01c §A3)")
    if timings:
        import statistics
        print(f"per-verse: mean {statistics.mean(timings)*1000:.1f}ms · max {max(timings)*1000:.0f}ms · circuit-breaker {MAX_SEC}s")


if __name__ == "__main__":
    main()
