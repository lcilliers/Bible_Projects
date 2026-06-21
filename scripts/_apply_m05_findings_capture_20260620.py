"""_apply_m05_findings_capture_20260620.py — capture M05 (Love) findings, in line with M03/M04.

Stage A: 6 NEW characteristics A-F (char_seq 100+idx; letter-prefixed short_name to dodge legacy UNIQUE).
         definition = §1 paragraph parsed from each per-characteristic profile file.
Stage B: per char a tiers file (cf_char_synth/tier_findings) + a profile file (cf_char_synth/evidence_profile),
         plus the cluster-wide tier synthesis (cf_cluster_synth). Additive only. NO Stage C. Idempotent.

  python scripts/_apply_m05_findings_capture_20260620.py --dry-run | --live
"""
import argparse, glob, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-20T00:00:00Z"
D = "Sessions-v2/M05-Love/findings"
SRCDOC = "wa-m05-cluster-synthesis-by-tier-v1_0-20260620.md"  # names + defines all six
# (letter, short_name, profile-slug, tiers-slug)
CHARS = [("A", "Love / affectionate attachment", "a-love", "a"),
         ("B", "Compassion", "b-compassion", "b"),
         ("C", "Kindness / steadfast-love (chesed)", "c-kindness", "c"),
         ("D", "Comfort", "d-comfort", "d"),
         ("E", "Gentleness", "e-gentleness", "e"),
         ("F", "Friendship", "f-friendship", "f")]


def latest(pat):
    cs = sorted(glob.glob(pat))
    return cs[-1] if cs else None


def definition_from_profile(path):
    """first prose paragraph under the '§1 — Definition' heading of a profile file."""
    if not path or not os.path.exists(path):
        return None
    t = open(path, encoding="utf-8").read()
    m = re.search(r"^##\s*§1[^\n]*\n+(.+?)(?:\n\n|\n##)", t, re.S | re.M)
    return re.sub(r"\s*\n\s*", " ", m.group(1)).strip()[:600] if m else None


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # resolve file paths up-front
    paths = {}
    for L, name, pslug, tslug in CHARS:
        paths[(L, "profile")] = latest(f"{D}/wa-m05-{pslug}-v1_*.md")
        paths[(L, "tiers")] = latest(f"{D}/wa-m05-{tslug}-tier-answers-v1_*.md")
    cluster_synth = latest(f"{D}/wa-m05-cluster-synthesis-by-tier-v1_*.md")
    missing = [k for k, v in paths.items() if not v] + ([] if cluster_synth else [("cluster", "synth")])
    if missing:
        print("MISSING source files:", missing); return 2

    # Stage A
    print("== Stage A — 6 M05 characteristics (A-F) ==")
    for i, (L, name, pslug, tslug) in enumerate(CHARS, start=1):
        seq = 100 + i
        defn = definition_from_profile(paths[(L, "profile")]) or name
        ex = cur.execute("SELECT id FROM characteristic WHERE cluster_code='M05' AND char_seq=? AND source=? AND COALESCE(delete_flagged,0)=0", (seq, SRCDOC)).fetchone()
        print(f"   {L} seq={seq} [{'exists' if ex else 'CREATE'}] {name}  · def {len(defn)} chars")
        if a.live and not ex:
            cur.execute("""INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, notes, delete_flagged, created_at, last_updated_date)
                VALUES ('M05', ?, ?, ?, ?, 'v1.0', ?, 0, ?, ?)""",
                (seq, f"{L} — {name}", defn, SRCDOC,
                 f"M05 6-char model 2026-06-20 (char {L}); char_seq=100+{i}; letter-prefixed short_name", STAMP, STAMP))
    if a.live:
        conn.commit()
    charid = {r["char_seq"] - 100: r["id"] for r in cur.execute("SELECT char_seq, id FROM characteristic WHERE cluster_code='M05' AND source=? AND COALESCE(delete_flagged,0)=0", (SRCDOC,))}

    # Stage B
    typeids = {}
    for code in ("cf_char_synth", "cf_cluster_synth"):
        r = cur.execute("SELECT id FROM prose_section_type WHERE code=?", (code,)).fetchone()
        assert r, f"type {code} missing (run an earlier cluster capture first)"; typeids[code] = r["id"]
    items = []
    for i, (L, name, pslug, tslug) in enumerate(CHARS, start=1):
        items.append((i, "cf_char_synth", "tier_findings", paths[(L, "tiers")]))
        items.append((i, "cf_char_synth", "evidence_profile", paths[(L, "profile")]))
    items.append((None, "cf_cluster_synth", "cluster_synth", cluster_synth))

    print("\n== Stage B — capture findings files ==")
    n = 0
    for idx, tcode, layer, path in items:
        cid = charid.get(idx) if idx else None
        body = open(path, encoding="utf-8").read()
        hm = re.search(r"^#\s+(.+)$", body, re.M)
        heading = (hm.group(1).strip() if hm else os.path.basename(path))[:300]
        src = os.path.basename(path)
        vm = re.search(r"v(\d+_\d+)", src); version = vm.group(1) if vm else "v1_0"
        ex = cur.execute("SELECT id FROM prose_section WHERE source_file=? AND cluster_code='M05' AND COALESCE(delete_flagged,0)=0", (src,)).fetchone()
        print(f"   [{'exists' if ex else 'INSERT'}] {('char'+str(idx)) if idx else 'cluster':8} {layer:16} char_id={cid} · {len(body.split()):5}w · {src}")
        if a.live and not ex:
            cur.execute("""INSERT INTO prose_section
                (registry_id, section_type_id, heading, body, word_count, status, version, author, source_file, metadata_json, cluster_code, characteristic_id, delete_flagged, created_at)
                VALUES (NULL, ?, ?, ?, ?, 'approved', ?, 'claude_ai', ?, ?, 'M05', ?, 0, ?)""",
                (typeids[tcode], heading, body, len(body.split()), version, src,
                 json.dumps({"layer": layer, "char": (CHARS[idx-1][0] if idx else None), "model": "M05 6-char 2026-06-20"}),
                 cid, STAMP)); n += 1
    if a.dry_run:
        print("\n[DRY-RUN] no changes."); return 0
    conn.commit()
    print(f"\nLIVE: {len(charid)} M05 characteristics; {n} prose_section rows inserted.")
    print("M05 OLD characteristics intact:", cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code='M05' AND char_seq<=99 AND COALESCE(delete_flagged,0)=0").fetchone()[0])
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
