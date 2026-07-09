"""_apply_m06_findings_capture_20260620.py — capture M06 (Hate, Contempt and Hostility) findings, in line with M05.

Stage A: 6 NEW characteristics A-F (char_seq 100+idx; letter-prefixed short_name to dodge legacy UNIQUE).
         definition embedded from the ib-characteristics §3 (source = that file).
Stage B: per char a tier-answers file (cf_char_synth/tier_findings) + a profile file (cf_char_synth/evidence_profile),
         plus the cluster-wide tier review/synthesis (cf_cluster_synth). Additive only. NO Stage C. Idempotent.

  python scripts/_apply_m06_findings_capture_20260620.py --dry-run | --live
"""
import argparse, glob, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-20T00:00:00Z"
D = "Sessions-v2/M06-Hate/findings"
SRCDOC = "wa-m06-ib-characteristics-v1_0-20260620.md"
# (letter, short_name, profile-slug, tiers-letter, definition)
CHARS = [
    ("A", "Aversive affect — felt hatred and settled rejection", "a-aversive-affect", "a",
     "The emotional core: an inner turning-away from a person or thing."),
    ("B", "Appraisive contempt — disdain", "b-contempt", "b",
     "A downward verdict on another's worth; treating-as-nothing."),
    ("C", "Loathing — visceral repugnance and detestation", "c-loathing", "c",
     "Aversion with a bodily, often ritual, colouring (the 'detestable / unclean')."),
    ("D", "Reproach, taunt and derision", "d-reproach", "d",
     "Hostility expressed in speech, and the borne social condition of disgrace it inflicts."),
    ("E", "Adversarial enmity — settled relational opposition", "e-enmity", "e",
     "A standing-against another; the disposition of being an opponent."),
    ("F", "Cruelty and ruthlessness", "f-cruelty", "f",
     "Not an episode but a trait: the settled cruelty of a person."),
]


def latest(pat):
    cs = sorted(glob.glob(pat))
    return cs[-1] if cs else None


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    paths = {}
    for L, name, pslug, tlet, defn in CHARS:
        paths[(L, "profile")] = latest(f"{D}/wa-m06-char-{pslug}-v1_*.md")
        paths[(L, "tiers")] = latest(f"{D}/wa-m06-char-{tlet}-tieranswers-v1_*.md")
    cluster_synth = latest(f"{D}/wa-m06-cluster-review-by-tier-v1_*.md")
    missing = [k for k, v in paths.items() if not v] + ([] if cluster_synth else [("cluster", "synth")])
    if missing:
        print("MISSING source files:", missing); return 2

    print("== Stage A — 6 M06 characteristics (A-F) ==")
    for i, (L, name, pslug, tlet, defn) in enumerate(CHARS, start=1):
        seq = 100 + i
        ex = cur.execute("SELECT id FROM characteristic WHERE cluster_code='M06' AND char_seq=? AND source=? AND COALESCE(delete_flagged,0)=0", (seq, SRCDOC)).fetchone()
        print(f"   {L} seq={seq} [{'exists' if ex else 'CREATE'}] {name}")
        if a.live and not ex:
            cur.execute("""INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, notes, delete_flagged, created_at, last_updated_date)
                VALUES ('M06', ?, ?, ?, ?, 'v1.0', ?, 0, ?, ?)""",
                (seq, f"{L} — {name}", defn, SRCDOC,
                 f"M06 6-char model 2026-06-20 (char {L}); char_seq=100+{i}; letter-prefixed short_name", STAMP, STAMP))
    if a.live:
        conn.commit()
    charid = {r["char_seq"] - 100: r["id"] for r in cur.execute("SELECT char_seq, id FROM characteristic WHERE cluster_code='M06' AND source=? AND COALESCE(delete_flagged,0)=0", (SRCDOC,))}

    typeids = {}
    for code in ("cf_char_synth", "cf_cluster_synth"):
        r = cur.execute("SELECT id FROM prose_section_type WHERE code=?", (code,)).fetchone()
        assert r, f"type {code} missing (run an earlier cluster capture first)"; typeids[code] = r["id"]
    items = []
    for i, (L, name, pslug, tlet, defn) in enumerate(CHARS, start=1):
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
        ex = cur.execute("SELECT id FROM prose_section WHERE source_file=? AND cluster_code='M06' AND COALESCE(delete_flagged,0)=0", (src, )).fetchone()
        print(f"   [{'exists' if ex else 'INSERT'}] {('char'+str(idx)) if idx else 'cluster':8} {layer:16} char_id={cid} · {len(body.split()):5}w · {src}")
        if a.live and not ex:
            cur.execute("""INSERT INTO prose_section
                (registry_id, section_type_id, heading, body, word_count, status, version, author, source_file, metadata_json, cluster_code, characteristic_id, delete_flagged, created_at)
                VALUES (NULL, ?, ?, ?, ?, 'approved', ?, 'claude_ai', ?, ?, 'M06', ?, 0, ?)""",
                (typeids[tcode], heading, body, len(body.split()), version, src,
                 json.dumps({"layer": layer, "char": (CHARS[idx-1][0] if idx else None), "model": "M06 6-char 2026-06-20"}),
                 cid, STAMP)); n += 1
    if a.dry_run:
        print("\n[DRY-RUN] no changes."); return 0
    conn.commit()
    print(f"\nLIVE: {len(charid)} M06 characteristics; {n} prose_section rows inserted.")
    print("M06 OLD characteristics intact:", cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code='M06' AND char_seq<=99 AND COALESCE(delete_flagged,0)=0").fetchone()[0])
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
