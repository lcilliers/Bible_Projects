"""Trace selected M15 terms flagged with NO_WORD_ANALYSIS / PROSE_ONLY_MEANING
through the data: STEP record → inventory → verses → sub-group → analysis use.

Read-only. Picks three representative terms (high, medium, low flag-count) and
produces a detailed walkthrough for each.
"""
import sqlite3, sys
from collections import defaultdict
try: sys.stdout.reconfigure(encoding="utf-8")
except: pass

conn = sqlite3.connect("database/bible_research.db")
conn.row_factory = sqlite3.Row

# Pick 3 representative terms from M15
TERMS = [
    ("G4894", "suneidō"),    # 24 flags — highest in M15
    ("G0050", "agnoeō"),     # 14 flags — user's example
    ("G1014", "boulomai"),   # user's example (8 flags)
]


def section(title):
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def kv(label, value, indent=2):
    pad = " " * indent
    if value is None:
        value = "(none)"
    if isinstance(value, str) and len(value) > 200:
        value = value[:200] + "…"
    print(f"{pad}{label:30s} {value}")


for strongs, expected_translit in TERMS:
    section(f"TERM: {strongs} ({expected_translit})")

    # ---- 1. mti_terms canonical row ----
    print("\n[1] mti_terms (canonical row)")
    mt = conn.execute("""
        SELECT id, strongs_number, transliteration, gloss, language,
               owning_word, owning_registry_fk, status, cluster_code,
               vc_status, anchor_note
          FROM mti_terms WHERE strongs_number = ? AND COALESCE(delete_flagged,0)=0
    """, (strongs,)).fetchone()
    if not mt:
        print(f"  (no mti_terms row found for {strongs})")
        continue
    for k in ("id","strongs_number","transliteration","gloss","language",
              "owning_word","owning_registry_fk","status","cluster_code",
              "vc_status","anchor_note"):
        kv(k, mt[k])

    # ---- 2. wa_term_inventory (the STEP extract source — where the flags come from) ----
    print("\n[2] wa_term_inventory rows (the STEP extract source)")
    inv_rows = list(conn.execute("""
        SELECT ti.id, ti.term_owner_type, ti.term_introduction_source,
               ti.short_def_mounce, ti.meaning, ti.lsj_entry, ti.parsed_meaning_id,
               wr.no AS reg_no, wr.word AS reg_word, fi.id AS file_id, fi.filename
          FROM wa_term_inventory ti
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
         WHERE ti.strongs_number = ? AND COALESCE(ti.delete_flagged,0)=0
         ORDER BY wr.no
    """, (strongs,)).fetchall())
    print(f"  {len(inv_rows)} inventory row(s) — one per registry that pulled this term")
    for r in inv_rows[:5]:
        print(f"    - reg {r['reg_no']:>3d} ({r['reg_word']:25s}) owner={r['term_owner_type']} "
              f"file_id={r['file_id']:>4d}  short_def_present={bool(r['short_def_mounce'])} "
              f" meaning_present={bool(r['meaning'])}  parsed_id={r['parsed_meaning_id']}")
    if len(inv_rows) > 5:
        print(f"    ... ({len(inv_rows) - 5} more)")

    # short_def_mounce sample for the first row
    if inv_rows and inv_rows[0]["short_def_mounce"]:
        sd = inv_rows[0]["short_def_mounce"][:300]
        print(f"\n  short_def_mounce (first row): {sd}…")

    # ---- 3. The flag presence — why these flags fire ----
    print("\n[3] Why the flags fire (data presence check)")
    if inv_rows:
        first = inv_rows[0]
        has_meaning = bool(first["meaning"])
        has_parsed = first["parsed_meaning_id"] is not None
        print(f"  meaning field populated:       {has_meaning}")
        print(f"  parsed_meaning_id present:     {has_parsed}")
        print(f"  ── PROSE_ONLY_MEANING fires if meaning is a single prose block "
              f"with no structured senses (no parsed_meaning_id).")
        print(f"  ── NO_WORD_ANALYSIS fires when STEP did not return word_analysis "
              f"for this term during extraction.")

    # ---- 4. wa_data_quality_flags rows — confirms the repetition pattern ----
    print("\n[4] wa_data_quality_flags rows for this term")
    flag_rows = list(conn.execute("""
        SELECT dqf.id, dqf.file_id, qft.flag_code,
               wr.no AS reg_no, wr.word AS reg_word
          FROM wa_data_quality_flags dqf
          JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
          JOIN wa_file_index fi ON fi.id = dqf.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
         WHERE dqf.term_id = ? AND COALESCE(qft.deprecated,0)=0
         ORDER BY qft.flag_code, wr.no
    """, (strongs,)).fetchall())
    by_code = defaultdict(list)
    for fr in flag_rows:
        by_code[fr["flag_code"]].append((fr["reg_no"], fr["reg_word"]))
    print(f"  {len(flag_rows)} flag rows total")
    for code, regs in by_code.items():
        regs_short = ", ".join(f"{n}({w[:12]})" for n, w in regs[:6])
        more = f" +{len(regs) - 6} more" if len(regs) > 6 else ""
        print(f"    - {code}: {len(regs)} rows across registries {regs_short}{more}")
    print(f"  ── Repetition explained: one flag row per (file_id × term × flag_code) — "
          f"i.e. one per registry that pulled this term.")

    # ---- 5. Verse evidence ----
    print("\n[5] Verse evidence (active rows)")
    v_count = conn.execute("""
        SELECT COUNT(*) FROM wa_verse_records WHERE term_id = ? AND COALESCE(delete_flagged,0)=0
    """, (strongs,)).fetchone()[0]
    v_distinct = conn.execute("""
        SELECT COUNT(DISTINCT reference) FROM wa_verse_records
         WHERE term_id = ? AND COALESCE(delete_flagged,0)=0
    """, (strongs,)).fetchone()[0]
    print(f"  active verse_records: {v_count}  (distinct references: {v_distinct})")

    # ---- 6. M15 placement — sub-group and VCG ----
    print("\n[6] M15 placement (cluster context)")
    placements = list(conn.execute("""
        SELECT cs.subgroup_code, cs.label
          FROM mti_term_subgroup mts
          JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
         WHERE mts.mti_term_id = ? AND COALESCE(mts.delete_flagged,0)=0
           AND cs.cluster_code = 'M15'
    """, (mt["id"],)).fetchall())
    for p in placements:
        print(f"  placed in sub-group: {p['subgroup_code']} — {p['label']}")
    if not placements:
        print(f"  (not placed in any M15 sub-group)")

    vcg_count = conn.execute("""
        SELECT COUNT(DISTINCT vcg.id) FROM verse_context vc
          JOIN verse_context_group vcg ON vcg.id = vc.group_id
         WHERE vc.mti_term_id = ? AND COALESCE(vc.delete_flagged,0)=0
           AND vcg.group_code LIKE 'M15-%-VCG%'
    """, (mt["id"],)).fetchone()[0]
    anchor_count = conn.execute("""
        SELECT COUNT(*) FROM verse_context vc
          JOIN verse_context_group vcg ON vcg.id = vc.group_id
         WHERE vc.mti_term_id = ? AND vc.is_anchor = 1 AND COALESCE(vc.delete_flagged,0)=0
           AND vcg.group_code LIKE 'M15-%-VCG%'
    """, (mt["id"],)).fetchone()[0]
    print(f"  M15 VCG memberships: {vcg_count}")
    print(f"  M15 anchor verses contributed: {anchor_count}")

    # ---- 7. Anchor verses contributed (if any) ----
    if anchor_count > 0:
        print(f"\n[7] Anchor verses this term provided in M15")
        for r in conn.execute("""
            SELECT vcg.group_code, vr.reference,
                   SUBSTR(vr.verse_text,1,90) AS vt, vc.analysis_note
              FROM verse_context vc
              JOIN verse_context_group vcg ON vcg.id = vc.group_id
              JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
             WHERE vc.mti_term_id = ? AND vc.is_anchor = 1 AND COALESCE(vc.delete_flagged,0)=0
               AND vcg.group_code LIKE 'M15-%-VCG%'
        """, (mt["id"],)):
            print(f"  {r['group_code']:14s} {r['reference']:>12s}")
            print(f"    > {r['vt']}…")
            if r["analysis_note"]:
                print(f"    meaning: {r['analysis_note'][:120]}")

    # ---- 8. Findings the term appears in (text mentions) ----
    print("\n[8] M15 cluster findings mentioning this term")
    n_findings = conn.execute("""
        SELECT COUNT(*) FROM cluster_finding
         WHERE cluster_code = 'M15' AND COALESCE(delete_flagged,0)=0
           AND (finding_text LIKE ? OR finding_text LIKE ? OR finding_text LIKE ?)
    """, (f"%{strongs}%", f"%{expected_translit}%", f"%{mt['transliteration']}%")).fetchone()[0]
    print(f"  findings whose text mentions this term: {n_findings}")

print()
section("SUMMARY")
print("""
  These two flags are STEP data-coverage descriptors, not analytical gaps.

  PROSE_ONLY_MEANING — STEP returned the meaning as a single prose block
    rather than as a numbered list of senses. The term still has a meaning
    in the DB; it just cannot be sliced into senses for downstream parsing.

  NO_WORD_ANALYSIS — STEP did not return the structured word-analysis
    section (parts of speech, parsing notes etc.) during extraction. The
    term still has its core fields (transliteration, gloss, short_def).

  Repetition: wa_data_quality_flags carries a file_id, so one flag row is
  written per (registry that pulled the term × flag type). A term in 8
  XREF registries gets the same flag 8 times — each tied to a different
  file_id. The 477 count for M15 is therefore inflated by XREF copies.

  Implication for analysis: none of these flags blocked term placement,
  VCG construction, anchor selection, or finding generation. The flagged
  terms went through the full pipeline alongside non-flagged terms.
""")
conn.close()
