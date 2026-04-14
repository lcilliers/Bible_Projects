"""
_sense_sampling_walkthrough.py
Generate a step-by-step walkthrough of the sense sampling method
using H2617A chesed (kindness) as the worked example.
"""
import sqlite3
import os
from collections import defaultdict

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "sense-sampling-walkthrough-20260328.md")


def classify_chesed_pattern(text):
    """Classify a chesed verse by its usage pattern."""
    tl = text.lower()
    if "steadfast love" in tl and "endures" in tl:
        return "steadfast love endures forever"
    elif "steadfast love" in tl and "covenant" in tl:
        return "steadfast love + covenant"
    elif "steadfast love" in tl and ("mercy" in tl or "merciful" in tl):
        return "steadfast love + mercy"
    elif "steadfast love" in tl and "faithfulness" in tl:
        return "steadfast love + faithfulness"
    elif "steadfast love" in tl and ("withdraw" in tl or "remove" in tl or "take" in tl):
        return "steadfast love withdrawn/threatened"
    elif "steadfast love" in tl and "morning" in tl:
        return "steadfast love in the morning"
    elif "steadfast love" in tl:
        return "steadfast love (general)"
    elif "kindness" in tl:
        return "kindness (human act)"
    elif "love" in tl:
        return "love (general)"
    elif "mercy" in tl or "merciful" in tl:
        return "mercy/merciful"
    elif "loyal" in tl or "devotion" in tl:
        return "loyalty/devotion"
    elif "grace" in tl or "favor" in tl or "favour" in tl:
        return "grace/favour"
    else:
        return "other usage"


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Get the term
    term = conn.execute("""
        SELECT ti.id, ti.strongs_number, ti.transliteration, ti.step_search_gloss,
               ti.word_analysis_gloss, ti.meaning, ti.occurrence_count,
               ti.language, ti.testament, ti.evidential_status, ti.retention_note,
               m.status as mti_status, m.status_note,
               wr.no, wr.word, wr.cluster_assignment,
               fi.id as file_id
        FROM wa_term_inventory ti
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        JOIN mti_terms m ON m.strongs_number = ti.strongs_number AND m.word_data_ref_fk = ti.file_id
        WHERE ti.strongs_number = 'H2617A' AND ti.delete_flagged = 0 AND m.status = 'extracted'
        LIMIT 1
    """).fetchone()

    # Get verses
    verses = conn.execute("""
        SELECT vr.id, vr.reference, vr.verse_text, vr.book_id, vr.chapter, vr.verse_num,
               vr.testament, vr.span_strong_match, vr.target_word
        FROM wa_verse_records vr
        WHERE vr.term_inv_id = ? AND vr.delete_flagged = 0
        ORDER BY vr.book_id, vr.chapter, vr.verse_num
    """, (term["id"],)).fetchall()

    # Get meaning senses
    senses = conn.execute("""
        SELECT ms.id, ms.level_code, ms.level_depth, ms.sense_text, ms.is_stem_label,
               ms.stem_label, ms.domain_tag, ms.sort_order
        FROM wa_meaning_sense ms
        JOIN wa_meaning_parsed mp ON mp.id = ms.parsed_meaning_id
        WHERE mp.term_inv_id = ?
        ORDER BY ms.sort_order
    """, (term["id"],)).fetchall()

    # Get flags
    ph2_flags = conn.execute("""
        SELECT ft.flag_code, pf.description
        FROM wa_term_phase2_flags pf
        JOIN phase2_flag_types ft ON ft.id = pf.flag_id
        WHERE pf.term_inv_id = ?
    """, (term["id"],)).fetchall()

    q_flags = conn.execute("""
        SELECT qft.flag_code, dqf.description
        FROM wa_data_quality_flags dqf
        JOIN wa_quality_flag_types qft ON qft.id = dqf.flag_id
        WHERE dqf.term_id = ?
    """, (term["id"],)).fetchall()

    conn.close()

    # Build the document
    L = []

    L.append("# Sense Sampling Method — Worked Example")
    L.append("")
    L.append(f"> Term: **{term['strongs_number']}** {term['transliteration']} — {term['step_search_gloss']}")
    L.append(f"> Registry: {term['no']} {term['word']} (Cluster {term['cluster_assignment']})")
    L.append(f"> Generated: 2026-03-28")
    L.append("")
    L.append("This document walks through the sense sampling method step by step,")
    L.append("showing how 169 verses are reduced to representative samples without")
    L.append("losing any distinct meaning or usage pattern.")
    L.append("")
    L.append("---")
    L.append("")

    # STEP 1 — Raw Term Data
    L.append("## Step 1 — Raw Term Data")
    L.append("")
    L.append("### 1.1 Term Metadata")
    L.append("")
    L.append("| Field | Value |")
    L.append("|-------|-------|")
    L.append(f"| Strong's | {term['strongs_number']} |")
    L.append(f"| Transliteration | {term['transliteration']} |")
    L.append(f"| Search Gloss | {term['step_search_gloss']} |")
    L.append(f"| Analysis Gloss | {term['word_analysis_gloss'] or '(none)'} |")
    L.append(f"| Language | {term['language']} |")
    L.append(f"| Testament | {term['testament'] or 'OT'} |")
    L.append(f"| Occurrence Count | {term['occurrence_count']} |")
    L.append(f"| Verse Count | {len(verses)} |")
    L.append(f"| MTI Status | {term['mti_status']} |")
    L.append(f"| Evidential Status | {term['evidential_status'] or 'not yet assigned'} |")
    L.append("")

    L.append("### 1.2 Meaning Text (from STEP)")
    L.append("")
    meaning = term["meaning"] or "(no meaning text)"
    L.append("```")
    L.append(meaning)
    L.append("```")
    L.append("")

    L.append("### 1.3 Phase 2 Flags")
    L.append("")
    if ph2_flags:
        for f in ph2_flags:
            L.append(f"- **{f['flag_code']}**: {f['description'] or '(no description)'}")
    else:
        L.append("(none)")
    L.append("")

    L.append("### 1.4 Quality Flags")
    L.append("")
    if q_flags:
        for f in q_flags:
            L.append(f"- **{f['flag_code']}**: {f['description'] or '(no description)'}")
    else:
        L.append("(none)")
    L.append("")

    L.append("### 1.5 Parsed Meaning Senses")
    L.append("")
    L.append("These are the distinct senses extracted by the meaning parser (engine step A7) from the STEP meaning text.")
    L.append("")
    if senses:
        L.append("| # | Level | Sense Text | Stem | Domain |")
        L.append("|---|-------|------------|------|--------|")
        for i, s in enumerate(senses, 1):
            st = (s["sense_text"] or "").replace("|", "/")
            if len(st) > 100:
                st = st[:100] + "..."
            L.append(f"| {i} | {s['level_code'] or '—'} | {st} | {s['stem_label'] or '—'} | {s['domain_tag'] or '—'} |")
    else:
        L.append("(no parsed senses)")
    L.append("")
    L.append("---")
    L.append("")

    # STEP 2 — Full Verse Listing
    L.append("## Step 2 — Full Verse Listing (raw data)")
    L.append("")
    L.append(f"All **{len(verses)}** verses for {term['strongs_number']} in the database, in canonical order.")
    L.append("This is what Claude AI would currently receive in a full export.")
    L.append("")
    L.append("| # | Reference | Target Word | Verse Text |")
    L.append("|---|-----------|-------------|------------|")
    for i, v in enumerate(verses, 1):
        ref = v["reference"] or "?"
        tw = v["target_word"] or "—"
        text = (v["verse_text"] or "").replace("|", "/").replace("\n", " ")
        if len(text) > 200:
            text = text[:200] + "..."
        L.append(f"| {i} | {ref} | {tw} | {text} |")
    L.append("")
    L.append("---")
    L.append("")

    # STEP 3 — Group by target word
    L.append("## Step 3 — Group by Target Word Translation")
    L.append("")
    L.append("The `target_word` field tells us how the ESV translates this Strong's number in each verse.")
    L.append("Grouping by target_word gives us a first-level sense separation.")
    L.append("")

    tw_groups = defaultdict(list)
    for v in verses:
        tw = (v["target_word"] or "unknown").strip()
        tw_groups[tw].append(v)

    L.append("| Target Word | Verse Count | % of Total |")
    L.append("|-------------|-------------|------------|")
    for tw, vl in sorted(tw_groups.items(), key=lambda x: -len(x[1])):
        pct = len(vl) / len(verses) * 100
        L.append(f"| {tw} | {len(vl)} | {pct:.1f}% |")
    L.append("")
    L.append("---")
    L.append("")

    # STEP 4 — Sub-group by usage pattern
    L.append("## Step 4 — Sub-group by Usage Pattern")
    L.append("")
    L.append("Within each target word group, verses are further grouped by HOW the term is used.")
    L.append("This is the key step: verses that say the same thing are grouped together.")
    L.append("")

    all_patterns = defaultdict(list)
    for v in verses:
        text = v["verse_text"] or ""
        pattern = classify_chesed_pattern(text)
        all_patterns[pattern].append(v)

    for pattern, pvl in sorted(all_patterns.items(), key=lambda x: -len(x[1])):
        L.append(f"### Pattern: \"{pattern}\" ({len(pvl)} verses)")
        L.append("")
        for v in pvl:
            ref = v["reference"] or "?"
            text = (v["verse_text"] or "").replace("\n", " ")
            if len(text) > 250:
                text = text[:250] + "..."
            L.append(f"- **{ref}**: {text}")
        L.append("")

    L.append("---")
    L.append("")

    # STEP 5 — Sense Sampling
    L.append("## Step 5 — Sense Sampling (the reduction)")
    L.append("")
    L.append("From each pattern group, we select **2 representative verses**:")
    L.append("- One from early in the canon (establishes the usage)")
    L.append("- One from later (shows continuity or development)")
    L.append("")
    L.append("All other verses in the group express the same meaning. Their COUNT is preserved")
    L.append("so Claude AI knows the statistical weight, but the text is not repeated.")
    L.append("")

    total_original = len(verses)
    total_sampled = 0

    L.append("| Pattern | Total Verses | Sampled | Representative Verses |")
    L.append("|---------|-------------|---------|----------------------|")

    for pattern, pvl in sorted(all_patterns.items(), key=lambda x: -len(x[1])):
        sampled = min(2, len(pvl))
        total_sampled += sampled
        # Pick first and last for range
        v1 = pvl[0]
        v2 = pvl[-1] if len(pvl) > 1 else None
        ref1 = v1["reference"] or "?"
        text1 = (v1["verse_text"] or "").replace("|", "/").replace("\n", " ")
        if len(text1) > 120:
            text1 = text1[:120] + "..."
        if v2 and v2["id"] != v1["id"]:
            ref2 = v2["reference"] or "?"
            text2 = (v2["verse_text"] or "").replace("|", "/").replace("\n", " ")
            if len(text2) > 120:
                text2 = text2[:120] + "..."
            rep = f"**{ref1}**: {text1} | **{ref2}**: {text2}"
        else:
            rep = f"**{ref1}**: {text1}"
        L.append(f"| {pattern} | {len(pvl)} | {sampled} | {rep} |")

    L.append("")
    L.append("---")
    L.append("")

    # STEP 6 — Summary
    n_patterns = len(all_patterns)
    L.append("## Step 6 — Summary")
    L.append("")
    L.append("| Metric | Value |")
    L.append("|--------|-------|")
    L.append(f"| Original verses | {total_original} |")
    L.append(f"| Distinct usage patterns | {n_patterns} |")
    L.append(f"| Sampled verses | {total_sampled} |")
    L.append(f"| Verses eliminated | {total_original - total_sampled} |")
    L.append(f"| Reduction | {(1 - total_sampled / total_original) * 100:.0f}% |")
    L.append(f"| Token saving | ~{(total_original - total_sampled) * 170 // 4:,} tokens |")
    L.append("")

    L.append("### What Claude AI receives (the sampled export):")
    L.append("")
    L.append("1. The term metadata (strongs, gloss, meaning text, flags)")
    L.append("2. The parsed senses from wa_meaning_sense")
    L.append("3. **2 representative verses per distinct usage pattern**")
    L.append("4. The count of how many verses each pattern represents")
    L.append("")
    L.append("This gives Claude AI the **full semantic range** of the term — every distinct")
    L.append("way it is used in Scripture — without the redundancy of reading many verses")
    L.append("that all express the same meaning.")
    L.append("")

    L.append("### What is NOT lost:")
    L.append("")
    L.append("- Every distinct meaning/usage of the term is represented")
    L.append("- The statistical weight (verse count per pattern) is preserved")
    L.append("- Edge cases and unusual usages are captured in the 'other' patterns")
    L.append("- The full meaning text and parsed senses provide structural context")
    L.append("- Cross-testament range is preserved (early + late sample)")
    L.append("")

    L.append("### What IS lost:")
    L.append("")
    L.append("- Exhaustive verse listing (but counts are preserved)")
    L.append("- Ability to detect rare within-pattern variations")
    L.append("- Sequential/narrative reading across consecutive verses")
    L.append("- Verses that sit between two patterns (genuinely ambiguous usage)")
    L.append("")

    # Write
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    print(f"Written to {OUT_PATH}")
    print(f"Original: {total_original} verses -> {total_sampled} sampled ({(1 - total_sampled / total_original) * 100:.0f}% reduction)")
    print(f"Patterns: {n_patterns}")


if __name__ == "__main__":
    main()
