"""_cc_verse_read.py — CC-GENERATION mode of the verse-read = meaning layer. Same output as the API pipeline
(_apply_verse_read_meaning.py) but the *generation* is done by Claude Code (Opus, subscription) instead of the
Sonnet API — a saving, since the subscription is already paid. The API pipeline is left fully intact; this is
a parallel path (reverting = just use the API script). Reuses the API pipeline's shared helpers by import.

T2 rules baked in (feedback_t2_reference_flag_reclassify):
  - DRIVERS = M-clusters only (cluster_code LIKE 'M%'); WRITE terms = M-cluster terms lacking a meaning.
  - T2 terms at the reference are CONTEXT only — shown as qualifiers to embed in the characteristic's meaning,
    NEVER written as standalone records.
  - participation gate: only M-cluster terms get records.

Handshake (all in-session, no manual paste):
  1. python scripts/_cc_verse_read.py --cluster M47 --emit  --limit 12 --out outputs/cc/cc_packets.md
  2. (CC reads the packets and writes the @@@-format records to outputs/cc/cc_output.md)
  3. python scripts/_cc_verse_read.py --cluster M47 --ingest --in  outputs/cc/cc_output.md
Repeat 1-3 per batch. --status shows progress. Engine-logged like the API runs.
"""
import argparse, importlib.util, os, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")

# import shared helpers from the API pipeline (keep them single-sourced; API script untouched)
_spec = importlib.util.spec_from_file_location("vrm", os.path.join("scripts", "_apply_verse_read_meaning.py"))
vrm = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(vrm)
PROV_MEAN, PROV_TIER = vrm.PROV_MEAN, vrm.PROV_TIER


def fetch_cc_blocks(conn, cluster, limit):
    """Verse-complete blocks for a cluster: WRITE = M-cluster terms at the ref lacking a meaning; CONTEXT = T2
    qualifiers present at the ref (to embed, not write)."""
    c = conn.cursor(); c2 = conn.cursor()
    refs = [r[0] for r in c.execute(
        """SELECT DISTINCT vr.reference FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
           JOIN mti_terms m ON m.id=vc.mti_term_id
           WHERE m.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0 ORDER BY vr.id""", (cluster,))]
    blocks = []
    for ref in refs:
        vt = None; write = []
        for r in c2.execute(
            """SELECT vc.id vcid, vr.verse_text vt, vr.morph_code morph, vr.stem stem,
                      m.id mid, m.transliteration tl, m.strongs_number sn, m.cluster_code cc, ti.parsed_meaning_id pmid
               FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
               JOIN mti_terms m ON m.id=vc.mti_term_id
               LEFT JOIN wa_term_inventory ti ON ti.strongs_number=m.strongs_number AND COALESCE(ti.delete_flagged,0)=0
               WHERE vr.reference=? AND m.cluster_code LIKE 'M%' AND COALESCE(vc.delete_flagged,0)=0 GROUP BY vc.id""", (ref,)):
            if vt is None:
                vt = (r["vt"] or "").strip()
            if vrm.vcid_read(conn, r["vcid"]):
                continue
            senses = []
            if r["pmid"]:
                senses = [x[0] for x in conn.execute("SELECT sense_text FROM wa_meaning_sense WHERE parsed_meaning_id=? ORDER BY sort_order LIMIT 3", (r["pmid"],))]
            write.append({"vcid": r["vcid"], "mid": r["mid"], "cc": r["cc"], "tl": r["tl"], "sn": r["sn"],
                          "morph": r["morph"], "stem": r["stem"], "senses": senses})
        if not write:
            continue
        # T2 qualifiers present at this ref (context only)
        t2 = [(x["tl"], (x["gloss"] or "").strip()[:34]) for x in c2.execute(
            """SELECT DISTINCT m.transliteration tl, m.gloss FROM verse_context vc JOIN wa_verse_records vr ON vr.id=vc.verse_record_id
               JOIN mti_terms m ON m.id=vc.mti_term_id WHERE vr.reference=? AND m.cluster_code='T2' AND COALESCE(vc.delete_flagged,0)=0""", (ref,))]
        blocks.append({"ref": ref, "vt": vt, "write": write, "t2": t2})
        if len(blocks) >= limit:
            break
    return blocks


def emit(conn, cluster, limit, out):
    blocks = fetch_cc_blocks(conn, cluster, limit)
    L = [f"# CC verse-read packets — {cluster} — {len(blocks)} verses", "",
         "INSTRUCTIONS — produce one @@@…@@@END record per WRITE-term, in this exact format and field discipline:", "",
         vrm.SYSTEM_PROMPT, "",
         "Embed the QUALIFIERS-PRESENT (T2) force into the relevant WRITE-term meaning; do NOT emit records for them.",
         "=" * 60, ""]
    for b in blocks:
        L.append(f"@@@VERSE {b['ref']}")
        L.append(f"TEXT: {b['vt']}")
        L.append("WRITE:")
        for w in b["write"]:
            so = " | ".join(w["senses"][:3]) if w["senses"] else "(none)"
            L.append(f"  - {w['tl']} ({w['sn']}) cluster={w['cc']} vcid={w['vcid']} morph={w['morph'] or '-'} stem={w['stem'] or '-'}")
            L.append(f"      senses: {so}")
        if b["t2"]:
            L.append("QUALIFIERS-PRESENT (T2 — embed, do NOT write): " + ", ".join(f"{t[0]}({t[1]})" for t in b["t2"]))
        L.append("")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(L))
    nterms = sum(len(b["write"]) for b in blocks)
    # vcid -> (mid, cc) sidecar so ingest can route without re-deriving
    side = out + ".map"
    with open(side, "w", encoding="utf-8") as f:
        for b in blocks:
            for w in b["write"]:
                f.write(f"{w['vcid']}\t{w['mid']}\t{w['cc']}\n")
    print(f"emitted {len(blocks)} verses / {nterms} WRITE-terms (M-clusters only; T2 as context) -> {out}")


def _find_or_open_run(conn, cluster):
    r = conn.execute("SELECT run_id FROM engine_run_log WHERE mode='cc_verse_read' AND target_registry_ids=? AND completed_at IS NULL ORDER BY id DESC LIMIT 1", (cluster,)).fetchone()
    if r:
        return r["run_id"]
    now = vrm._now(conn)
    rid = f"ccvrm_{cluster}_{now}"
    conn.execute("INSERT INTO engine_run_log(run_id, mode, target_registry_ids, started_at) VALUES(?,?,?,?)", (rid, "cc_verse_read", cluster, now))
    conn.commit()
    return rid


def ingest(conn, cluster, infile, run_id):
    t0 = vrm._now(conn)
    text = open(infile, encoding="utf-8").read()
    recs = vrm.parse_response(text)
    # routing map from the emit sidecar (authoritative; only these vcids are writable)
    mp = {}
    side = None
    for cand in (infile + ".map", os.path.join(os.path.dirname(infile), "cc_packets.md.map")):
        if os.path.exists(cand):
            side = cand; break
    if side:
        for line in open(side, encoding="utf-8"):
            v, m, cc = line.strip().split("\t"); mp[int(v)] = (int(m), cc)
    expected = len(mp)
    seen_vcids = set()
    written = skipped = flags = 0
    for rec in recs:
        if rec["vcid"] not in mp:
            skipped += 1; continue   # T2 / out-of-scope vcid — never write
        seen_vcids.add(rec["vcid"])
        n, st = vrm.write_record(conn, rec, mp, vrm._now(conn))
        if st != "ok":
            skipped += 1; continue
        written += n
        miss = vrm.audit_paragraph(rec)
        api_flag = bool(rec["selfaudit"]) and not rec["selfaudit"].lower().rstrip(". ").endswith("ok")
        if miss or api_flag:
            flags += 1
            conn.execute("UPDATE finding SET flagged_for_review=1 WHERE verse_context_id=? AND provenance=?", (rec["vcid"], PROV_MEAN))
    # FAULT-LINE CHECK: did CC cover every emitted WRITE-term?
    missing_vcids = [v for v in mp if v not in seen_vcids]
    shortfall = len(missing_vcids)
    # engine logging: one checkpoint per cycle under the open run
    rid = _find_or_open_run(conn, cluster)
    done = vrm._now(conn)
    ncyc = conn.execute("SELECT COUNT(*) FROM engine_stream_checkpoint WHERE run_id=?", (rid,)).fetchone()[0] + 1
    detail = f"records={len(recs)} expected_terms={expected} covered={len(seen_vcids)} shortfall={shortfall} findings={written} flagged={flags} skipped={skipped}"
    if missing_vcids:
        detail += " | MISSING_vcids=" + ",".join(str(v) for v in missing_vcids[:30])
    conn.execute("""INSERT INTO engine_stream_checkpoint(run_id, stream_name, status, rows_written, rows_filtered, error_detail, started_at, completed_at)
                    VALUES(?,?,?,?,?,?,?,?)""", (rid, f"cc:{cluster}:cycle{ncyc:03d}", "review" if shortfall else "complete", written, skipped, detail, t0, done))
    conn.execute("UPDATE engine_run_log SET total_meanings_parsed=COALESCE(total_meanings_parsed,0)+?, total_verses_inserted=COALESCE(total_verses_inserted,0)+? WHERE run_id=?",
                 (len(recs), len(seen_vcids), rid))
    conn.commit()
    print(f"[cycle {ncyc}] ingested {len(recs)} records -> wrote {written} findings, skipped {skipped}, {flags} flagged "
          f"| covered {len(seen_vcids)}/{expected}" + (f"  ⚠ SHORTFALL {shortfall}: {missing_vcids[:30]}" if shortfall else ""))


def status(conn, cluster):
    own = conn.execute("SELECT COUNT(*) FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id WHERE m.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0", (cluster,)).fetchone()[0]
    rd = conn.execute("""SELECT COUNT(*) FROM verse_context vc JOIN mti_terms m ON m.id=vc.mti_term_id WHERE m.cluster_code=? AND COALESCE(vc.delete_flagged,0)=0
                         AND EXISTS(SELECT 1 FROM finding f WHERE f.verse_context_id=vc.id AND f.provenance=?)""", (cluster, PROV_MEAN)).fetchone()[0]
    print(f"{cluster}: {rd}/{own} own term-in-verses have a meaning ({100*rd/own:.0f}%)" if own else f"{cluster}: no terms")
    run = conn.execute("SELECT run_id, started_at FROM engine_run_log WHERE mode='cc_verse_read' AND target_registry_ids=? AND completed_at IS NULL ORDER BY id DESC LIMIT 1", (cluster,)).fetchone()
    if run:
        ck = conn.execute("SELECT COUNT(*) n, COALESCE(SUM(rows_written),0) f, SUM(status='review') sh FROM engine_stream_checkpoint WHERE run_id=?", (run["run_id"],)).fetchone()
        print(f"  CC run {run['run_id']} (open since {run['started_at'][:19]}): {ck['n']} cycles, {ck['f']} findings, {ck['sh'] or 0} cycles with shortfall")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cluster", required=True)
    ap.add_argument("--emit", action="store_true"); ap.add_argument("--ingest", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--limit", type=int, default=12); ap.add_argument("--out", default="outputs/cc/cc_packets.md")
    ap.add_argument("--in", dest="infile", default="outputs/cc/cc_output.md")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    if a.status:
        status(conn, a.cluster)
    elif a.emit:
        emit(conn, a.cluster, a.limit, a.out)
    elif a.ingest:
        ingest(conn, a.cluster, a.infile, None)
        status(conn, a.cluster)
    else:
        print("specify --emit | --ingest | --status")
    conn.close()


if __name__ == "__main__":
    main()
