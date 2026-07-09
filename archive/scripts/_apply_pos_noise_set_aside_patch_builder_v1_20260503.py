"""_apply_pos_noise_set_aside_patch_builder_v1_20260503.py

Builds a REPAIR-class patch that auto-set-asides verse_context rows whose
OWNER Strong's is classified by STEP morphology as grammatical noise (Tier 1
cohort: pronoun, particle, preposition, conjunction, interjection, article,
suffix — adverb is NOT included; needs manual review).

Per-row update:
  is_relevant      -> 0
  is_anchor        -> 0
  is_related       -> 0
  group_id         -> null
  set_aside_reason -> 'no_inner_being'  (the controlled-vocab value)
  notes            -> structured token: 'auto_pos_noise:{pos}|case_{A|B|C}|2026-05-03'

The notes field carries the audit trail in a parseable form so the change
is fully reversible and traceable.

Inputs:
  outputs/markdown/step-pos-lookup-20260503.json

Outputs:
  Sessions/Patches/wa-global-repair-pos-noise-set-aside-v1-20260503.json
  outputs/markdown/pos-noise-set-aside-preflight-20260503.md
"""
from __future__ import annotations

import json
import os
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone

DB_PATH = os.path.join("database", "bible_research.db")
POS_JSON = os.path.join("outputs", "markdown", "step-pos-lookup-20260503.json")
PATCH_OUT = os.path.join("Sessions", "Patches",
                         "wa-global-repair-pos-noise-set-aside-v1-20260503.json")
PREFLIGHT_OUT = os.path.join("outputs", "markdown",
                             "pos-noise-set-aside-preflight-20260503.md")

TIER1_POS = {
    "pronoun", "pronoun-personal", "pronoun-reflexive", "pronoun-demonstrative",
    "pronoun-interrogative", "pronoun-correlative", "pronoun-relative",
    "pronoun-reciprocal", "pronoun-possessive", "pronoun-indefinite",
    "particle", "preposition", "conjunction", "conditional-particle",
    "interjection", "article", "suffix",
    # adverb deliberately excluded — Tier 2 manual review
}
CONTENT_POS = {"noun", "verb", "adjective"}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    with open(POS_JSON, encoding="utf-8") as f:
        pos_data = json.load(f)
    pos_lookup = {k: v.get("pos") for k, v in pos_data["results"].items()}

    noise_strongs = {s for s, p in pos_lookup.items() if p in TIER1_POS}
    content_strongs = {s for s, p in pos_lookup.items() if p in CONTENT_POS}

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Build verse->content presence (any registry, any-content Strong's)
    content_q = ",".join(["'" + s + "'" for s in content_strongs])
    verse_content_any = set()
    verse_content_per_reg = defaultdict(set)
    for cr in conn.execute(f"""
        SELECT DISTINCT vr.book_id, vr.chapter, vr.verse_num, wr.id AS reg_id
          FROM wa_verse_records vr
          JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
         WHERE vr.delete_flagged=0 AND ti.delete_flagged=0
           AND ti.term_owner_type='OWNER'
           AND ti.strongs_number IN ({content_q})
    """):
        k = (cr["book_id"], cr["chapter"], cr["verse_num"])
        verse_content_any.add(k)
        verse_content_per_reg[cr["reg_id"]].add(k)

    # All active OWNER vc rows on noise Strong's
    noise_q = ",".join(["'" + s + "'" for s in noise_strongs])
    rows = conn.execute(f"""
        SELECT vc.id AS vc_id, vc.is_relevant, vc.is_anchor, vc.is_related,
               vc.group_id, vc.set_aside_reason, vc.notes,
               vc.mti_term_id, vc.verse_record_id,
               vr.book_id, vr.chapter, vr.verse_num, vr.reference,
               ti.strongs_number, mt.gloss,
               wr.no AS reg_no, wr.word AS reg_word, wr.id AS reg_id
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
          JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
          JOIN mti_terms mt ON mt.strongs_number = ti.strongs_number
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
         WHERE vc.delete_flagged=0 AND vr.delete_flagged=0 AND ti.delete_flagged=0
           AND ti.term_owner_type='OWNER' AND mt.delete_flagged=0
           AND ti.strongs_number IN ({noise_q})
         ORDER BY wr.no, vr.book_id, vr.chapter, vr.verse_num, ti.strongs_number
    """).fetchall()

    # Build operations
    ops = []
    case_counts = defaultdict(int)
    per_reg_anchor_loss = defaultdict(int)
    per_reg_total_loss = defaultdict(int)
    per_pos_counts = defaultdict(int)

    for i, r in enumerate(rows, 1):
        key = (r["book_id"], r["chapter"], r["verse_num"])
        if key in verse_content_per_reg.get(r["reg_id"], set()):
            case = "A"
        elif key in verse_content_any:
            case = "B"
        else:
            case = "C"
        case_counts[case] += 1

        pos = pos_lookup.get(r["strongs_number"], "?")
        per_pos_counts[pos] += 1
        if r["is_anchor"] == 1:
            per_reg_anchor_loss[(r["reg_no"], r["reg_word"])] += 1
        per_reg_total_loss[(r["reg_no"], r["reg_word"])] += 1

        # Construct notes — preserve original notes if any
        original_notes = r["notes"] or ""
        audit_note = f"auto_pos_noise:{pos}|case_{case}|2026-05-03"
        if original_notes:
            new_notes = f"{audit_note} | (original: {original_notes[:160]})"
        else:
            new_notes = audit_note

        op = {
            "op_id": f"OP-{i:05d}",
            "operation": "update",
            "table": "verse_context",
            "match": {
                "id": r["vc_id"],
            },
            "set": {
                "is_relevant": 0,
                "is_anchor": 0,
                "is_related": 0,
                "group_id": None,
                "set_aside_reason": "no_inner_being",
                "notes": new_notes,
            },
            "description": (
                f"R{r['reg_no']:03d} {r['reg_word']} {r['reference']} "
                f"{r['strongs_number']} '{(r['gloss'] or '')[:25]}' POS={pos} "
                f"case={case} (was relevant={r['is_relevant']} anchor={r['is_anchor']})"
            ),
        }
        ops.append(op)

    # Build patch JSON
    patch = {
        "_patch_meta": {
            "patch_id": "PATCH-20260503-GLOBAL-REPAIR-POS-NOISE-AUTO-SET-ASIDE-V1_0",
            "registry_id": None,
            "produced_date": "20260503",
            "produced_by": "scripts/_apply_pos_noise_set_aside_patch_builder_v1_20260503.py",
            "patch_type": "REPAIR",
            "session_b_status": None,
            "governing_instruction": (
                "auto-generated from STEP morphology classification "
                "(OSHB OSHM + SBLG_th Robinson schemes); "
                "Tier 1 cohort = pronoun/particle/preposition/conjunction/"
                "interjection/article/suffix; adverb excluded as Tier 2."
            ),
            "description": (
                f"Auto set-aside of {len(ops)} verse_context rows whose OWNER "
                f"Strong's is classified by STEP morphology as grammatical noise. "
                f"Per-row notes carry the audit trail "
                f"'auto_pos_noise:{{pos}}|case_{{A|B|C}}|2026-05-03'. "
                f"Case A = verse retained in registry via content term ({case_counts['A']} rows); "
                f"Case B = verse covered in other registries ({case_counts['B']} rows); "
                f"Case C = verse has no content-POS Strong's anywhere ({case_counts['C']} rows). "
                f"set_aside_reason='no_inner_being' (controlled vocab). "
                f"is_anchor and is_relevant cleared; group_id nulled."
            ),
        },
        "_patch_summary": {
            "total_operations": len(ops),
            "case_A_same_reg_content": case_counts["A"],
            "case_B_other_reg_content": case_counts["B"],
            "case_C_no_content_anywhere": case_counts["C"],
            "by_pos": dict(per_pos_counts),
            "registries_affected": len(per_reg_total_loss),
            "anchors_removed": sum(per_reg_anchor_loss.values()),
        },
        "operations": ops,
    }

    os.makedirs(os.path.dirname(PATCH_OUT), exist_ok=True)
    with open(PATCH_OUT, "w", encoding="utf-8") as f:
        json.dump(patch, f, indent=2, ensure_ascii=False)

    # Pre-flight markdown report
    L = []
    L.append("# POS-Noise Auto-Set-Aside — Pre-flight Report")
    L.append("")
    L.append(f"_Generated {now_iso()}_  ·  patch: `{PATCH_OUT}`")
    L.append("")
    L.append(f"**Total operations:** {len(ops):,}")
    L.append(f"**Registries affected:** {len(per_reg_total_loss)}")
    L.append(f"**Anchors removed:** {sum(per_reg_anchor_loss.values())}")
    L.append("")
    L.append("## Case breakdown")
    L.append("")
    L.append("| Case | vc rows | Description |")
    L.append("|---|---:|---|")
    L.append(f"| A | {case_counts['A']:,} | Verse retained in same registry via content term |")
    L.append(f"| B | {case_counts['B']:,} | Verse covered in other registries via content terms |")
    L.append(f"| C | {case_counts['C']:,} | Verse has no content term in any registry's inventory |")
    L.append("")
    L.append("## POS distribution of affected vc rows")
    L.append("")
    L.append("| POS | rows |")
    L.append("|---|---:|")
    for pos, n in sorted(per_pos_counts.items(), key=lambda x: -x[1]):
        L.append(f"| {pos} | {n:,} |")
    L.append("")
    L.append("## Top 30 registries by anchor loss")
    L.append("")
    L.append("| Reg | Word | Anchors lost | Total vc rows set aside |")
    L.append("|---:|---|---:|---:|")
    for (no, word), n_anc in sorted(per_reg_anchor_loss.items(),
                                     key=lambda x: -x[1])[:30]:
        L.append(f"| {no} | {word} | {n_anc} | {per_reg_total_loss[(no, word)]} |")
    L.append("")

    # Registries that would have zero anchors after the patch
    L.append("## Registries needing post-patch anchor follow-up")
    L.append("")
    L.append("Registries that lose anchors AND would have a low / zero anchor count "
             "after the patch — flagged for manual review.")
    L.append("")
    cur_anchors = {}
    for r in conn.execute("""
        SELECT wr.no AS reg_no, wr.word AS reg_word, COUNT(*) AS anchors
          FROM verse_context vc
          JOIN wa_verse_records vr ON vr.id = vc.verse_record_id
          JOIN wa_term_inventory ti ON ti.id = vr.term_inv_id
          JOIN wa_file_index fi ON fi.id = ti.file_id
          JOIN word_registry wr ON wr.id = fi.word_registry_fk
         WHERE vc.delete_flagged=0 AND vr.delete_flagged=0 AND ti.delete_flagged=0
           AND ti.term_owner_type='OWNER' AND vc.is_anchor=1 AND vc.is_relevant=1
         GROUP BY wr.no, wr.word
    """):
        cur_anchors[(r["reg_no"], r["reg_word"])] = r["anchors"]

    follow_ups = []
    for key, anc_lost in per_reg_anchor_loss.items():
        cur = cur_anchors.get(key, 0)
        post = cur - anc_lost
        if post <= 2:
            follow_ups.append((key[0], key[1], cur, anc_lost, post))
    follow_ups.sort(key=lambda x: x[4])
    if follow_ups:
        L.append("| Reg | Word | Anchors before | Lost in patch | Anchors after |")
        L.append("|---:|---|---:|---:|---:|")
        for no, word, cur, lost, post in follow_ups:
            L.append(f"| {no} | {word} | {cur} | {lost} | {post} |")
    else:
        L.append("_None — no registry drops below 3 anchors._")
    L.append("")

    L.append("## Apply")
    L.append("")
    L.append("```bash")
    L.append(f"# Dry-run first")
    L.append(f"python scripts/apply_session_patch.py {PATCH_OUT} --dry-run")
    L.append(f"")
    L.append(f"# Live")
    L.append(f"python scripts/apply_session_patch.py {PATCH_OUT}")
    L.append("```")
    L.append("")

    os.makedirs(os.path.dirname(PREFLIGHT_OUT), exist_ok=True)
    with open(PREFLIGHT_OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    conn.close()
    print(f"Wrote patch:     {PATCH_OUT}  ({os.path.getsize(PATCH_OUT):,} bytes)")
    print(f"Wrote preflight: {PREFLIGHT_OUT}")
    print()
    print(f"Operations: {len(ops):,}")
    print(f"  Case A: {case_counts['A']:,}")
    print(f"  Case B: {case_counts['B']:,}")
    print(f"  Case C: {case_counts['C']:,}")
    print(f"Registries affected: {len(per_reg_total_loss)}")
    print(f"Anchors removed:     {sum(per_reg_anchor_loss.values())}")
    if follow_ups:
        print(f"Registries with ≤2 anchors after patch: {len(follow_ups)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
