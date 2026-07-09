"""_apply_m09_findings_capture_20260621.py — capture M09 (Humility, Meekness and Submission) characteristics A-H.

Locked set (8): A Self-humbling · B Lowliness · C Being-brought-low · D Obedience · E Submission ·
F Willing-heartedness · G Dignity · H Gentle-forbearance. Detail work complete (char-{a..h} evidence +
tier-findings + cluster synthesis). NO set-aside applied here: the M09 set-aside register (okneO Act 9:38,
diatassO Luk 17:10) is OPEN/awaiting researcher confirmation — every term stays in-scope. Set-aside
candidates are surfaced by the findings audit for decision (cf. M08 pattern).

File-as-finding · additive · idempotent (dedup on source_file + characteristic_id). NO Stage C.
char_seq = 100+n (avoids any legacy char_seq + UNIQUE keys).

  python scripts/_apply_m09_findings_capture_20260621.py --dry-run | --live
"""
import argparse, glob, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-21T00:00:00Z"
D = "Sessions-v2/M09-Humility/findings"
SRCDOC = "wa-m09-provisional-chars-v1_0-20260621.md"
# (letter, short_name, evidence-slug, tier-slug, definition)
CHARS = [
    ("A", "Self-humbling before God", "char-a-evidence", "char-a-tier-findings",
     "Self-humbling before God — the chosen inner act of lowering oneself before God, characteristically bound to repentance and averting wrath/judgement"),
    ("B", "Lowliness as settled disposition", "char-b-evidence", "char-b-tier-findings",
     "Lowliness as settled disposition — humility as an abiding interior orientation: lowly-mindedness toward self and esteem of others"),
    ("C", "Being brought low / humiliation", "char-c-evidence", "char-c-tier-findings",
     "Being brought low / lowly estate / humiliation — lowness as imposed or circumstantial condition, with its inner correlate (downcast spirit, bowed heart)"),
    ("D", "Obedience", "char-d-evidence", "char-d-tier-findings",
     "Obedience — the inner submission of the will expressed as heeding/compliance with an authority; the will that 'hears under'"),
    ("E", "Submission / yieldedness", "char-e-evidence", "char-e-tier-findings",
     "Submission / yieldedness — the ordering of oneself under another's authority; subordination as an inner posture, distinct from active obedience"),
    ("F", "Willing-heartedness / freewill devotion", "char-f-evidence", "char-f-tier-findings",
     "Willing-heartedness / freewill devotion — the volitional self-giving of a 'willing heart/spirit' to God's service and offering"),
    ("G", "Dignity / grave bearing", "char-g-evidence", "char-g-tier-findings",
     "Dignity / grave bearing — weighty, seemly, respectable bearing (gravity rooted in reverence)"),
    ("H", "Gentle forbearance / moderation of feeling", "char-h-evidence", "char-h-tier-findings",
     "Gentle forbearance / moderation of feeling — measured gentleness toward the failing, grounded in shared weakness"),
]


def latest(slug):
    cs = sorted(glob.glob(f"{D}/wa-m09-{slug}-v*.md"))
    return cs[-1] if cs else None


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    for L, name, eslug, tslug, defn in CHARS:
        if not latest(eslug): print("MISSING evidence:", eslug); return 2
        if not latest(tslug): print("MISSING tier-findings:", tslug); return 2
    synth = sorted(glob.glob(f"{D}/wa-m09-cluster-synthesis-by-tier-v*.md"))
    if not synth: print("MISSING cluster synthesis"); return 2
    synth = synth[-1]

    print("== Stage A — 8 M09 characteristics (A-H) ==")
    for i, (L, name, eslug, tslug, defn) in enumerate(CHARS, start=1):
        seq = 100 + i
        ex = cur.execute("SELECT id FROM characteristic WHERE cluster_code='M09' AND char_seq=? AND source=? AND COALESCE(delete_flagged,0)=0", (seq, SRCDOC)).fetchone()
        print(f"   {L:4} seq={seq} [{'exists' if ex else 'CREATE'}] {name}")
        if a.live and not ex:
            cur.execute("""INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, notes, delete_flagged, created_at, last_updated_date)
                VALUES ('M09', ?, ?, ?, ?, 'v1.0', ?, 0, ?, ?)""",
                (seq, f"{L} - {name}", defn, SRCDOC,
                 f"M09 A-H capture 2026-06-21 (char {L}); char_seq=100+{i}; no set-aside applied (okneO/diatassO OPEN, awaiting confirmation)", STAMP, STAMP))
    if a.live:
        conn.commit()
    charid = {r["char_seq"] - 100: r["id"] for r in cur.execute("SELECT char_seq, id FROM characteristic WHERE cluster_code='M09' AND source=? AND COALESCE(delete_flagged,0)=0", (SRCDOC,))}

    typeids = {}
    for code in ("cf_char_synth", "cf_cluster_synth"):
        r = cur.execute("SELECT id FROM prose_section_type WHERE code=?", (code,)).fetchone()
        assert r, f"type {code} missing"; typeids[code] = r["id"]
    items = []
    for i, (L, name, eslug, tslug, defn) in enumerate(CHARS, start=1):
        items.append((i, "cf_char_synth", "tier_findings", latest(tslug)))
        items.append((i, "cf_char_synth", "evidence_profile", latest(eslug)))
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
        ex = cur.execute("SELECT id FROM prose_section WHERE source_file=? AND cluster_code='M09' AND COALESCE(characteristic_id,0)=? AND COALESCE(delete_flagged,0)=0", (src, cid or 0)).fetchone()
        print(f"   [{'exists' if ex else 'INSERT'}] {('char'+str(idx)+' '+CHARS[idx-1][0]) if idx else 'cluster':12} {layer:16} char_id={cid} · {len(body.split()):5}w · {src}")
        if a.live and not ex:
            cur.execute("""INSERT INTO prose_section
                (registry_id, section_type_id, heading, body, word_count, status, version, author, source_file, metadata_json, cluster_code, characteristic_id, delete_flagged, created_at)
                VALUES (NULL, ?, ?, ?, ?, 'approved', ?, 'claude_ai', ?, ?, 'M09', ?, 0, ?)""",
                (typeids[tcode], heading, body, len(body.split()), version, src,
                 json.dumps({"layer": layer, "char": (CHARS[idx-1][0] if idx else None), "model": "M09 A-H 2026-06-21"}),
                 cid, STAMP)); n += 1
    if a.dry_run:
        print("\n[DRY-RUN] no changes."); return 0
    conn.commit()
    print(f"\nLIVE: {len(charid)} M09 characteristics; {n} prose_section rows inserted.")
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
