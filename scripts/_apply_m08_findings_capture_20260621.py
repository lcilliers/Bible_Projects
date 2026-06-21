"""_apply_m08_findings_capture_20260621.py — capture M08 (Pride, Arrogance and Boasting) characteristics A-F.

Per researcher decision (2026-06-21, prov-char-list v1_1): 7 characteristics kept distinct —
A, B, C1, C2, D, E, F. NO set-aside applied here: the M08 set-aside file (archo, ro.hav, akrates,
height-nouns) is an inclusion-by-default PROPOSAL pending researcher confirmation, so every term stays
in-scope until confirmed. Set-aside candidates are surfaced by the findings audit (FA-13) for decision.

File-as-finding · additive · idempotent (dedup on source_file + characteristic_id). NO Stage C.
char_seq = 100+n (avoids the legacy char_seq 1-5 rows + their UNIQUE keys, as for M07).

  python scripts/_apply_m08_findings_capture_20260621.py --dry-run | --live
"""
import argparse, glob, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-21T00:00:00Z"
D = "Sessions-v2/M08-Pride/findings"
SRCDOC = "wa-m08-prov-char-list-v1_1-20260621.md"
# (letter, short_name, profile-slug, tier-slug, definition)
CHARS = [
    ("A", "Self-exaltation", "a-self-exaltation", "a-tier-answers",
     "Self-exaltation — the active lifting of the self up above its place (heart 'lifted up', lofty eyes, ascending above one's station)"),
    ("B", "Settled pride", "b-settled-pride", "b-tier-answers",
     "Settled pride — the entrenched, often corporate, state of haughtiness / loftiness ('the proud', 'a haughty spirit')"),
    ("C1", "Presumption / defiance toward God and authority", "c1-presumption", "c1-tier-answers",
     "Presumption / defiance — acting above one's station against God's command or appointed authority (overreach, self-will)"),
    ("C2", "Insolence / contempt toward others", "c2-insolence", "c2-tier-answers",
     "Insolence / contempt — insolent derision and oppression directed at other people (the haughty turned against neighbour, elder, the lowly)"),
    ("D", "Boasting and glorying (two poles)", "d-boasting", "d-tier-answers",
     "Boasting and glorying — verbal/affective self-display; two poles: sinful boasting in flesh/works, and righteous glorying in the Lord"),
    ("E", "Conceit / being puffed-up", "e-conceit", "e-tier-answers",
     "Conceit / being puffed-up — cognitive over-inflation of the mind ('puffed up', 'swollen with conceit'; NT register)"),
    ("F", "Self-love / self-sufficiency", "f-self-love", "f-tier-answers",
     "Self-love / self-sufficiency — the terminus: the self turned in on itself as its own centre/god"),
]


def latest(slug):
    cs = sorted(glob.glob(f"{D}/wa-m08-{slug}-v*.md"))
    return cs[-1] if cs else None


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # resolve files
    for L, name, pslug, tslug, defn in CHARS:
        if not latest(pslug): print("MISSING profile:", pslug); return 2
        if not latest(tslug): print("MISSING tier-answers:", tslug); return 2
    synth = sorted(glob.glob(f"{D}/wa-m08-cluster-synthesis-v*.md"))
    if not synth: print("MISSING cluster synthesis"); return 2
    synth = synth[-1]

    # Stage A — characteristics
    print("== Stage A — 7 M08 characteristics (A, B, C1, C2, D, E, F) ==")
    for i, (L, name, pslug, tslug, defn) in enumerate(CHARS, start=1):
        seq = 100 + i
        ex = cur.execute("SELECT id FROM characteristic WHERE cluster_code='M08' AND char_seq=? AND source=? AND COALESCE(delete_flagged,0)=0", (seq, SRCDOC)).fetchone()
        print(f"   {L:4} seq={seq} [{'exists' if ex else 'CREATE'}] {name}")
        if a.live and not ex:
            cur.execute("""INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, notes, delete_flagged, created_at, last_updated_date)
                VALUES ('M08', ?, ?, ?, ?, 'v1.0', ?, 0, ?, ?)""",
                (seq, f"{L} - {name}", defn, SRCDOC,
                 f"M08 A-F capture 2026-06-21 (char {L}); char_seq=100+{i}; no set-aside applied (inclusion-by-default pending confirmation)", STAMP, STAMP))
    if a.live:
        conn.commit()
    charid = {r["char_seq"] - 100: r["id"] for r in cur.execute("SELECT char_seq, id FROM characteristic WHERE cluster_code='M08' AND source=? AND COALESCE(delete_flagged,0)=0", (SRCDOC,))}

    # Stage B — tier-findings + evidence-profile per char; cluster synthesis once
    typeids = {}
    for code in ("cf_char_synth", "cf_cluster_synth"):
        r = cur.execute("SELECT id FROM prose_section_type WHERE code=?", (code,)).fetchone()
        assert r, f"type {code} missing"; typeids[code] = r["id"]
    items = []
    for i, (L, name, pslug, tslug, defn) in enumerate(CHARS, start=1):
        items.append((i, "cf_char_synth", "tier_findings", latest(tslug)))
        items.append((i, "cf_char_synth", "evidence_profile", latest(pslug)))
    items.append((None, "cf_cluster_synth", "cluster_synth", synth))

    print("\n== Stage B — capture findings (dedup on source_file + characteristic) ==")
    n = 0
    for idx, tcode, layer, path in items:
        cid = charid.get(idx) if idx else None
        body = open(path, encoding="utf-8").read()
        hm = re.search(r"^#\s+(.+)$", body, re.M)
        heading = (hm.group(1).strip() if hm else os.path.basename(path))[:300]
        src = os.path.basename(path)
        vm = re.search(r"v(\d+_\d+)", src); version = vm.group(1) if vm else "v1_0"
        ex = cur.execute("SELECT id FROM prose_section WHERE source_file=? AND cluster_code='M08' AND COALESCE(characteristic_id,0)=? AND COALESCE(delete_flagged,0)=0", (src, cid or 0)).fetchone()
        print(f"   [{'exists' if ex else 'INSERT'}] {('char'+str(idx)+' '+CHARS[idx-1][0]) if idx else 'cluster':12} {layer:16} char_id={cid} · {len(body.split()):5}w · {src}")
        if a.live and not ex:
            cur.execute("""INSERT INTO prose_section
                (registry_id, section_type_id, heading, body, word_count, status, version, author, source_file, metadata_json, cluster_code, characteristic_id, delete_flagged, created_at)
                VALUES (NULL, ?, ?, ?, ?, 'approved', ?, 'claude_ai', ?, ?, 'M08', ?, 0, ?)""",
                (typeids[tcode], heading, body, len(body.split()), version, src,
                 json.dumps({"layer": layer, "char": (CHARS[idx-1][0] if idx else None), "model": "M08 A-F 2026-06-21"}),
                 cid, STAMP)); n += 1
    if a.dry_run:
        print("\n[DRY-RUN] no changes."); return 0
    conn.commit()
    print(f"\nLIVE: {len(charid)} M08 characteristics; {n} prose_section rows inserted.")
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
