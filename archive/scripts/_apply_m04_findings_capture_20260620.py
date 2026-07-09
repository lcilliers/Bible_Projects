"""_apply_m04_findings_capture_20260620.py — capture M04 (Joy) findings, in line with M03.

Stage A: 7 NEW characteristics A-G (char_seq 100+idx; letter-prefixed short_name to dodge legacy UNIQUE).
Stage B: per char a tiers file (cf_char_synth/tier_findings) + a profile file (cf_char_synth/evidence_profile,
  latest v1_2), plus the cluster-tier-synthesis (cf_cluster_synth). Additive only. NO Stage C. Idempotent.

  python scripts/_apply_m04_findings_capture_20260620.py --dry-run | --live
"""
import argparse, glob, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-20T00:00:00Z"
D = "Sessions-v2/M04-Joy/findings"
CHARSRC = "wa-m04-ib-characteristics-v1_0-20260620.md"
# (letter, short_name, slug)
CHARS = [("A", "Rejoicing and gladness", "rejoicing-gladness"),
         ("B", "Delight", "delight-pleasure-in"),
         ("C", "Pleasantness", "pleasantness-quality"),
         ("D", "Wonder, marvel and amazement", "wonder-marvel"),
         ("E", "Thankfulness and gratitude", "thankfulness"),
         ("F", "Cheer, good courage and morale", "cheer-courage"),
         ("G", "Soothing / pleasing-aroma", "soothing-aroma")]


def latest(pat, excl=None):
    cs = [f for f in sorted(glob.glob(pat)) if not excl or excl not in f]
    return cs[-1] if cs else None


def defs():
    """letter -> first descriptive paragraph from ib-characteristics heading"""
    t = open(f"{D}/{CHARSRC}", encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"^###\s+([A-G])\.\s+.+?\n(.+?)(?:\n\n|\n\*|\n###|\Z)", t, re.S | re.M):
        out[m.group(1)] = re.sub(r"\s*\n\s*", " ", m.group(2)).strip()[:600]
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    definition = defs()

    # Stage A
    print("== Stage A — 7 M04 characteristics (A-G) ==")
    for i, (L, name, slug) in enumerate(CHARS, start=1):
        seq = 100 + i
        ex = cur.execute("SELECT id FROM characteristic WHERE cluster_code='M04' AND char_seq=? AND source=? AND COALESCE(delete_flagged,0)=0", (seq, CHARSRC)).fetchone()
        print(f"   {L} seq={seq} [{'exists' if ex else 'CREATE'}] {name}")
        if a.live and not ex:
            cur.execute("""INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, notes, delete_flagged, created_at, last_updated_date)
                VALUES ('M04', ?, ?, ?, ?, 'v1.0', ?, 0, ?, ?)""",
                (seq, f"{L} — {name}", definition.get(L, name), CHARSRC,
                 f"M04 7-char model 2026-06-20 (char {L}); char_seq=100+{i}; letter-prefixed short_name", STAMP, STAMP))
    if a.live:
        conn.commit()
    charid = {r["char_seq"] - 100: r["id"] for r in cur.execute("SELECT char_seq, id FROM characteristic WHERE cluster_code='M04' AND source=? AND COALESCE(delete_flagged,0)=0", (CHARSRC,))}

    # Stage B
    typeids = {}
    for code in ("cf_char_synth", "cf_cluster_synth"):
        r = cur.execute("SELECT id FROM prose_section_type WHERE code=?", (code,)).fetchone()
        assert r, f"type {code} missing (run an earlier cluster capture first)"; typeids[code] = r["id"]
    items = []
    for i, (L, name, slug) in enumerate(CHARS, start=1):
        items.append((i, "cf_char_synth", "tier_findings", latest(f"{D}/wa-m04-char-{slug}-tiers-v1_*.md")))
        items.append((i, "cf_char_synth", "evidence_profile", latest(f"{D}/wa-m04-char-{slug}-v1_*.md", "tiers")))
    items.append((None, "cf_cluster_synth", "cluster_synth", latest(f"{D}/wa-m04-cluster-tier-synthesis-v1_*.md")))

    print("\n== Stage B — capture findings files ==")
    n = 0
    for idx, tcode, layer, path in items:
        if not path or not os.path.exists(path):
            print(f"   MISSING {layer}: {path}"); return 2
        cid = charid.get(idx) if idx else None
        body = open(path, encoding="utf-8").read()
        hm = re.search(r"^#\s+(.+)$", body, re.M)
        heading = (hm.group(1).strip() if hm else os.path.basename(path))[:300]
        src = os.path.basename(path)
        vm = re.search(r"v(\d+_\d+)", src); version = vm.group(1) if vm else "v1_0"
        ex = cur.execute("SELECT id FROM prose_section WHERE source_file=? AND cluster_code='M04' AND COALESCE(delete_flagged,0)=0", (src,)).fetchone()
        print(f"   [{'exists' if ex else 'INSERT'}] {('char'+str(idx)) if idx else 'cluster':8} {layer:16} char_id={cid} · {len(body.split()):5}w · {src}")
        if a.live and not ex:
            cur.execute("""INSERT INTO prose_section
                (registry_id, section_type_id, heading, body, word_count, status, version, author, source_file, metadata_json, cluster_code, characteristic_id, delete_flagged, created_at)
                VALUES (NULL, ?, ?, ?, ?, 'approved', ?, 'claude_ai', ?, ?, 'M04', ?, 0, ?)""",
                (typeids[tcode], heading, body, len(body.split()), version, src,
                 json.dumps({"layer": layer, "char": (CHARS[idx-1][0] if idx else None), "model": "M04 7-char 2026-06-20"}),
                 cid, STAMP)); n += 1
    if a.dry_run:
        print("\n[DRY-RUN] no changes."); return 0
    conn.commit()
    print(f"\nLIVE: {len(charid)} M04 characteristics; {n} prose_section rows inserted.")
    print("M04 OLD characteristics intact:", cur.execute("SELECT COUNT(*) FROM characteristic WHERE cluster_code='M04' AND char_seq<=99 AND COALESCE(delete_flagged,0)=0").fetchone()[0])
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
