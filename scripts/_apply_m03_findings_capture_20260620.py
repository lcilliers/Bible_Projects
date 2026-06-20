"""_apply_m03_findings_capture_20260620.py — capture M03 (Grief) findings, in line with M02.

Stage A: create the 10 NEW characteristics (A-J) from wa-m03-ve-characteristics (char_seq=100+idx; A=1..J=10).
Stage B: capture findings files as prose_section (file-as-finding, no dissection): per char a tier-findings
  (cf_char_synth, layer=tier_findings) + a profile/evidence file (cf_char_synth, layer=evidence_profile); the
  cluster-tier-synthesis (cf_cluster_synth) and the ve-out-of-scope set-aside record (cf_cluster_synth,
  layer=out_of_scope). Additive only. NO Stage C (old structure untouched, per the settled model). Idempotent.

  python scripts/_apply_m03_findings_capture_20260620.py --dry-run | --live
"""
import argparse, glob, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-20T00:00:00Z"
D = "Sessions-v2/M03-Grief/findings"
CHARSRC = "wa-m03-ve-characteristics-v1_0-20260619.md"
LETTERS = "abcdefghij"


def latest(pat):
    cs = sorted(glob.glob(pat))
    return cs[-1] if cs else None


def parse_chars():
    """letter -> (seq, short_name) from the ve-characteristics headings; definition from each profile's
       '## 1. What this characteristic is' paragraph."""
    t = open(f"{D}/{CHARSRC}", encoding="utf-8").read()
    names = {}
    for m in re.finditer(r"^###\s+([A-J])\s+—\s+(.+?)\s+·", t, re.M):
        names[m.group(1)] = m.group(2).strip()
    out = {}
    for i, L in enumerate(LETTERS, start=1):
        U = L.upper()
        prof = latest_profile(L)
        definition = names.get(U, U)
        if prof:
            pt = open(prof, encoding="utf-8").read()
            dm = re.search(r"##\s*1\.\s*What this characteristic is\s*\n(.+?)(?:\n##|\n###|\Z)", pt, re.S)
            if dm:
                definition = re.sub(r"\s*\n\s*", " ", dm.group(1)).strip()[:600]
        out[U] = (100 + i, names.get(U, U), definition)
    return out


def latest_profile(L):
    return latest_excl(f"{D}/wa-m03-char-{L}-*-v1_*.md", "tier-findings")


def latest_excl(pat, excl):
    cs = [f for f in sorted(glob.glob(pat)) if excl not in f]
    return cs[-1] if cs else None


def filelist():
    items = []  # (letter|None, type_code, layer, path)
    for L in LETTERS:
        items.append((L.upper(), "cf_char_synth", "tier_findings", latest(f"{D}/wa-m03-char-{L}-tier-findings-v1_*.md")))
        items.append((L.upper(), "cf_char_synth", "evidence_profile", latest_profile(L)))
    items.append((None, "cf_cluster_synth", "cluster_synth", latest(f"{D}/wa-m03-cluster-tier-synthesis-v1_*.md")))
    items.append((None, "cf_cluster_synth", "out_of_scope", latest(f"{D}/wa-m03-ve-out-of-scope-v1_*.md")))
    return items


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # ---- Stage A: characteristics ----
    chars = parse_chars()
    assert len(chars) == 10, f"parsed {len(chars)} chars, expected 10"
    print("== Stage A — 10 M03 characteristics (A-J) ==")
    for U, (seq, name, _d) in sorted(chars.items()):
        ex = cur.execute("SELECT id FROM characteristic WHERE cluster_code='M03' AND char_seq=? AND source=? AND COALESCE(delete_flagged,0)=0", (seq, CHARSRC)).fetchone()
        print(f"   {U} seq={seq} [{'exists' if ex else 'CREATE'}] {name}")
        if a.live and not ex:
            cur.execute("""INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, notes, delete_flagged, created_at, last_updated_date)
                VALUES ('M03', ?, ?, ?, ?, 'v1.0', ?, 0, ?, ?)""",
                (seq, f"{U} — {name}", _d, CHARSRC, f"M03 10-char model 2026-06-19 (char {U}); char_seq=100+{seq-100}; letter-prefixed short_name to avoid legacy UNIQUE(short_name) collision", STAMP, STAMP))
    if a.live:
        conn.commit()
    charid = {r["char_seq"] - 100: r["id"] for r in cur.execute("SELECT char_seq, id FROM characteristic WHERE cluster_code='M03' AND source=? AND COALESCE(delete_flagged,0)=0", (CHARSRC,))}
    seq_by_letter = {U: seq - 100 for U, (seq, _n, _d) in chars.items()}

    # ---- Stage B: capture ----
    typeids = {c: cur.execute("SELECT id FROM prose_section_type WHERE code=?", (c,)).fetchone() for c in ("cf_char_synth", "cf_cluster_synth")}
    for c, r in typeids.items():
        assert r, f"section_type {c} missing (run M02 capture first)"; typeids[c] = r["id"]
    print("\n== Stage B — capture findings files (prose_section) ==")
    n_ins = 0
    for letter, tcode, layer, path in filelist():
        if not path or not os.path.exists(path):
            print(f"   MISSING: {letter} {layer} -> {path}"); return 2
        cid = charid.get(seq_by_letter[letter]) if letter else None
        body = open(path, encoding="utf-8").read()
        hm = re.search(r"^#\s+(.+)$", body, re.M)
        heading = (hm.group(1).strip() if hm else os.path.basename(path))[:300]
        src = os.path.basename(path)
        vm = re.search(r"v(\d+_\d+)", src); version = vm.group(1) if vm else "v1_0"
        ex = cur.execute("SELECT id FROM prose_section WHERE source_file=? AND cluster_code='M03' AND COALESCE(delete_flagged,0)=0", (src,)).fetchone()
        print(f"   [{'exists' if ex else 'INSERT'}] {(letter or 'cluster'):7} {tcode:16} {layer:16} char_id={cid} · {len(body.split()):5}w · {src}")
        if a.live and not ex:
            meta = json.dumps({"layer": layer, "char": letter, "model": "M03 10-char 2026-06-19"})
            cur.execute("""INSERT INTO prose_section
                (registry_id, section_type_id, heading, body, word_count, status, version, author, source_file, metadata_json, cluster_code, characteristic_id, delete_flagged, created_at)
                VALUES (NULL, ?, ?, ?, ?, 'approved', ?, 'claude_ai', ?, ?, 'M03', ?, 0, ?)""",
                (typeids[tcode], heading, body, len(body.split()), version, src, meta, cid, STAMP)); n_ins += 1
    if a.dry_run:
        print("\n[DRY-RUN] no changes written."); return 0
    conn.commit()
    print(f"\nLIVE: characteristics now {len(charid)} (M03 new); prose_section inserted {n_ins}.")
    for r in cur.execute("SELECT t.code, COUNT(*) n FROM prose_section ps JOIN prose_section_type t ON t.id=ps.section_type_id WHERE ps.cluster_code='M03' AND COALESCE(ps.delete_flagged,0)=0 GROUP BY t.code"):
        print(f"   {r['code']:18} {r['n']}")
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
