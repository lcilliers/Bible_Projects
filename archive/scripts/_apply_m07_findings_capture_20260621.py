"""_apply_m07_findings_capture_20260621.py — capture M07 (Shame) characteristics A-H only.

Per researcher decision (2026-06-21): capture A-H (6 core + F/G/H structural); SET ASIDE J, K, RESID.
M07 quirk: F+G findings are in a combined file (char-fg-findings-v2_0); H findings are in char-hjkr-findings-v2_0
(which also holds the set-aside J/K/RESID — only H is in scope). Dedup keys on (source_file, characteristic_id)
so the shared fg file attaches to both F and G. Additive · file-as-finding · idempotent. NO Stage C.

  python scripts/_apply_m07_findings_capture_20260621.py --dry-run | --live
"""
import argparse, glob, json, os, re, sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = os.path.join("database", "bible_research.db")
STAMP = "2026-06-21T00:00:00Z"
D = "Sessions-v2/M07-Shame/findings"
SRCDOC = "wa-m07-char-findings-index-v1_0-20260621.md"
# (letter, short_name, profile-slug, findings-slug, definition, coverage-note)
CHARS = [
    ("A", "Felt shame at falsified trust", "a-felt-shame-trust", "a-felt-shame-trust-findings",
     "Felt shame at falsified trust / dashed expectation", None),
    ("B", "Trust-to-vindication axis", "b-vindication-axis", "b-vindication-axis-findings",
     "Trust→vindication axis: shame vs honour as the outcome of hope in God", None),
    ("C", "Conscience - shame at one's own sin", "c-conscience-sin", "c-conscience-sin-findings",
     "Conscience — shame at one's own sin", None),
    ("Cneg", "Shamelessness", "cneg-shamelessness", "cneg-shamelessness-findings",
     "Shamelessness — the absence/inversion of the shame-faculty", None),
    ("D", "Borne disgrace / standing", "d-borne-disgrace", "d-borne-disgrace-findings",
     "Disgrace as a borne condition/standing (covering); imposed or deserved", None),
    ("E", "Agent dishonour / contempt", "e-agent-dishonour", "e-agent-dishonour-findings",
     "Dishonouring/despising another (the agent pole) + contempt-disposition", None),
    ("F", "Abasement of pride", "f-abasement-pride", "fg-findings",
     "Abasement — the bringing-low of pride (status reversal)", "findings file fg covers F+G"),
    ("G", "Honour-shame reversal", "g-honour-shame-reversal", "fg-findings",
     "Honour↔shame / glory↔shame reversal", "findings file fg covers F+G"),
    ("H", "Propriety norms", "h-propriety-norms", "hjkr-findings",
     "Propriety — what is shameful/disgraceful (decency norms)", "findings file hjkr covers H only here; J/K/RESID set aside"),
]


def latest(slug):
    cs = sorted(glob.glob(f"{D}/wa-m07-char-{slug}-v2_*.md"))
    return cs[-1] if cs else None


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true"); g.add_argument("--live", action="store_true")
    a = ap.parse_args()
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # resolve files
    for L, name, pslug, fslug, defn, note in CHARS:
        if not latest(pslug): print("MISSING profile:", pslug); return 2
        if not latest(fslug): print("MISSING findings:", fslug); return 2
    synth = sorted(glob.glob(f"{D}/wa-m07-cluster-synthesis-bytier-v1_*.md"))
    if not synth: print("MISSING cluster synthesis"); return 2
    synth = synth[-1]

    # Stage A
    print("== Stage A — 9 M07 characteristics (A-H; J/K/RESID set aside) ==")
    for i, (L, name, pslug, fslug, defn, note) in enumerate(CHARS, start=1):
        seq = 100 + i
        ex = cur.execute("SELECT id FROM characteristic WHERE cluster_code='M07' AND char_seq=? AND source=? AND COALESCE(delete_flagged,0)=0", (seq, SRCDOC)).fetchone()
        print(f"   {L:4} seq={seq} [{'exists' if ex else 'CREATE'}] {name}")
        if a.live and not ex:
            cur.execute("""INSERT INTO characteristic (cluster_code, char_seq, short_name, definition, source, version, notes, delete_flagged, created_at, last_updated_date)
                VALUES ('M07', ?, ?, ?, ?, 'v2.0', ?, 0, ?, ?)""",
                (seq, f"{L} - {name}", defn, SRCDOC,
                 f"M07 A-H capture 2026-06-21 (char {L}); char_seq=100+{i}; J/K/RESID set aside" + (f"; {note}" if note else ""), STAMP, STAMP))
    if a.live:
        conn.commit()
    charid = {r["char_seq"] - 100: r["id"] for r in cur.execute("SELECT char_seq, id FROM characteristic WHERE cluster_code='M07' AND source=? AND COALESCE(delete_flagged,0)=0", (SRCDOC,))}

    # Stage B — findings (tier) + profile per char; cluster synthesis once
    typeids = {}
    for code in ("cf_char_synth", "cf_cluster_synth"):
        r = cur.execute("SELECT id FROM prose_section_type WHERE code=?", (code,)).fetchone()
        assert r, f"type {code} missing"; typeids[code] = r["id"]
    items = []
    for i, (L, name, pslug, fslug, defn, note) in enumerate(CHARS, start=1):
        items.append((i, "cf_char_synth", "tier_findings", latest(fslug), note))
        items.append((i, "cf_char_synth", "evidence_profile", latest(pslug), None))
    items.append((None, "cf_cluster_synth", "cluster_synth", synth, "scope A-H; J/K/RESID set aside"))

    print("\n== Stage B — capture findings (dedup on source_file + characteristic) ==")
    n = 0
    for idx, tcode, layer, path, note in items:
        cid = charid.get(idx) if idx else None
        body = open(path, encoding="utf-8").read()
        hm = re.search(r"^#\s+(.+)$", body, re.M)
        heading = (hm.group(1).strip() if hm else os.path.basename(path))[:300]
        src = os.path.basename(path)
        vm = re.search(r"v(\d+_\d+)", src); version = vm.group(1) if vm else "v2_0"
        ex = cur.execute("SELECT id FROM prose_section WHERE source_file=? AND cluster_code='M07' AND COALESCE(characteristic_id,0)=? AND COALESCE(delete_flagged,0)=0", (src, cid or 0)).fetchone()
        print(f"   [{'exists' if ex else 'INSERT'}] {('char'+str(idx)+' '+CHARS[idx-1][0]) if idx else 'cluster':10} {layer:16} char_id={cid} · {len(body.split()):5}w · {src}" + (f"  ({note})" if note else ""))
        if a.live and not ex:
            cur.execute("""INSERT INTO prose_section
                (registry_id, section_type_id, heading, body, word_count, status, version, author, source_file, metadata_json, cluster_code, characteristic_id, delete_flagged, created_at)
                VALUES (NULL, ?, ?, ?, ?, 'approved', ?, 'claude_ai', ?, ?, 'M07', ?, 0, ?)""",
                (typeids[tcode], heading, body, len(body.split()), version, src,
                 json.dumps({"layer": layer, "char": (CHARS[idx-1][0] if idx else None), "model": "M07 A-H 2026-06-21", "note": note}),
                 cid, STAMP)); n += 1
    if a.dry_run:
        print("\n[DRY-RUN] no changes."); return 0
    conn.commit()
    print(f"\nLIVE: {len(charid)} M07 characteristics; {n} prose_section rows inserted.")
    print("integrity:", cur.execute("PRAGMA quick_check").fetchone()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
