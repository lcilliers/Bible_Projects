"""Apply all corrections and additions to the programme report in one pass."""
import sqlite3
import os
from collections import defaultdict

DB = os.path.join(os.path.dirname(__file__), "..", "data", "bible_research.db")
REPORT = os.path.join(os.path.dirname(__file__), "..", "outputs", "wa-programme-status-report-20260328.md")


def main():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    with open(REPORT, "r", encoding="utf-8") as f:
        content = f.read()

    # ── FIX 1: Section 3.4 Quality Flags — filter to OWNER/active/non-excluded ──
    old_34 = content[content.index("## 3.4 Quality Flags"):content.index("## 3.5")]
    new_34 = """## 3.4 Quality Flags (OWNER terms, active, non-excluded registries)

| Quality Flag | Count | Notes |
|-------------|-------|-------|
| CONCRETE_PHYSICAL | 310 | Concrete nouns — flagged, not excluded. Verse analysis may reveal inner-being usage. |

**Note:** The engine-derived quality flags (NO_WORD_ANALYSIS, PROSE_ONLY_MEANING, THIN_DATA, SMALL_VERSE_SAMPLE, NO_VERSES, HIGH_FREQUENCY_ANCHOR) exist in the database but apply overwhelmingly to XREF copies and delete_flagged terms. When filtered to OWNER-only active terms in non-excluded registries, only CONCRETE_PHYSICAL remains as a meaningful quality indicator.

"""
    content = content.replace(old_34, new_34)

    # ── FIX 2: Section 3.5 PH2 Flags — filter to OWNER/active/non-excluded ──
    old_35_start = content.index("## 3.5 Phase 2 Flags")
    old_35_end = content.index("---", old_35_start + 10)
    old_35 = content[old_35_start:old_35_end]

    ph2_flags = conn.execute("""
        SELECT ft.flag_code, COUNT(*) as c
        FROM wa_term_phase2_flags pf
        JOIN phase2_flag_types ft ON ft.id = pf.flag_id
        JOIN wa_term_inventory ti ON ti.id = pf.term_inv_id
        JOIN wa_file_index fi ON fi.id = ti.file_id
        JOIN word_registry wr ON wr.id = fi.word_registry_fk
        WHERE ti.delete_flagged = 0 AND ti.term_owner_type = 'OWNER'
        AND wr.phase1_status != 'Excluded'
        GROUP BY ft.flag_code ORDER BY c DESC
    """).fetchall()

    new_35 = "## 3.5 Phase 2 Flags (OWNER terms, active, non-excluded registries)\n\n"
    new_35 += "Researcher-owned analytical flags on terms. These are **Claude AI's responsibility** — set during Session B analysis.\n\n"
    new_35 += "| PH2 Flag | Count |\n|----------|-------|\n"
    for r in ph2_flags:
        new_35 += f"| {r['flag_code']} | {r['c']} |\n"
    new_35 += "\n"

    content = content[:old_35_start] + new_35 + content[old_35_end:]

    # ── FIX 3: Section 5.3 — add total row ──
    old_sharing = "| 100% shared | 35 |"
    new_sharing = "| 100% shared | 35 |\n| **Total (non-excluded, with terms)** | **181** |"
    content = content.replace(old_sharing, new_sharing)

    # ── ADD: Section 5.4 — Term Sharing Pools ──
    insert_after = "| **Total (non-excluded, with terms)** | **181** |"
    idx = content.index(insert_after) + len(insert_after)

    section_54 = """

## 5.4 Term Sharing Pools — Natural Groupings

At a threshold of 15+ shared terms, the registries form 8 natural pools of interconnected words. These pools emerge from the data — they are not pre-assigned clusters. Words within a pool share substantial vocabulary and cannot be fully understood in isolation from each other.

| Pool | Size | Words | Pattern |
|------|------|-------|---------|
| **Pool 1** | 51 words | anger, desire, trust, faith, hope, heart, spirit, mind, Soul, will, purpose, thought, love, kindness, strength, power, authority, dominion, courage, generosity, delight, covenant, joy, conscience, guilt, repentance, sin, wisdom, knowledge, understanding, meditation, division, goodness, praise, insight, recognition, slander, lust, craving, despair, doubt, faithfulness, transformation, resentment, likeness, pray, ambition, dignity, discernment, wrath, might | Core inner-being megapool — everything connects through shared Hebrew/Greek vocabulary |
| **Pool 2** | 11 words | agony, anguish, awe, distress, dread, experience, fear, grief, reverence, sorrow, terror | Suffering/fear cluster — tightly interconnected through shared pain and dread vocabulary |
| **Pool 3** | 3 words | envy, jealousy, zeal | Tight triad sharing the Hebrew qana root family |
| **Pool 4** | 2 words | compassion, mercy | chesed/racham family |
| **Pool 5** | 2 words | justice, righteousness | tsedeq family |
| **Pool 6** | 2 words | shame, contempt | Shared dishonour vocabulary |
| **Pool 7** | 2 words | surrender, flesh | Shared submission/body vocabulary |
| **Pool 8** | 2 words | consecration, holiness | qodesh family |
| **Unconnected** | 47 words | | Not connected to any other registry at the 15-term threshold |

**Analytical implications:**

- **Pool 1 is the core challenge.** 51 words forming a single interconnected network. The existing cluster assignments (C01-C22) are the programme's strategy for breaking this megapool into manageable analysis batches.
- **Pool 2 is a natural analysis unit.** 11 suffering/fear words sharing vocabulary internally with limited external connections. Already spread across C05 and C06.
- **Pools 3-8 are the simplest shared-word analyses.** Each is 2-3 words sharing a specific root family. Can be analysed together in a single session.
- **The top 5 strongest pairwise connections** (anguish-distress 79, sorrow-anguish 70, sorrow-distress 66, sorrow-grief 56, wrath-anger 51) are all within Pool 2 or within obvious semantic families — confirming pools reflect genuine semantic structure.

## 5.5 Pool 1 Deep Dive — Sub-Structure of the 51-Word Megapool

At threshold 30+ shared terms, Pool 1 fragments into 6 sub-pools and 41 isolates:

### Sub-pools (strong internal bonds, 30+ shared terms)

| Sub-pool | Words | Semantic axis |
|----------|-------|--------------|
| **Volitional core** (9) | desire, faith, guilt, hope, purpose, thought, trust, will, pray | The will/intention/belief axis — strongest interconnection in the programme |
| **Power axis** (5) | courage, strength, power, authority, dominion | Physical/spiritual capacity vocabulary |
| **Heart-spirit** (2) | heart, spirit | The two primary inner-being seats (41 shared terms) |
| **Wisdom pair** (2) | goodness, meditation | Moral/contemplative vocabulary (30 shared terms) |
| **Love pair** (2) | kindness, love | chesed family (33 shared terms) |
| **Anger pair** (2) | anger, wrath | Rage vocabulary (51 shared terms — strongest pair in programme) |

### Isolates (41 words) — Gravitational Analysis

Each isolate is connected to Pool 1 at 15-29 shared terms but not at 30+. Their strongest connection reveals which sub-pool they gravitate toward:

**Gravitate toward purpose/thought axis:**
- might (27 shared with purpose), delight (26), mind (23), recognition (23), knowledge (21)

**Gravitate toward trust/faith axis:**
- faithfulness (28 shared with faith), despair (18 shared with trust), doubt (17), covenant (15), sorrow (13)
- The faith/trust/hope triad pulls in its opposite (despair, doubt) and its relational expression (covenant)

**Gravitate toward heart/spirit centre:**
- conscience (26 shared with heart), Soul (24 shared with heart and spirit)

**Gravitate toward love/kindness axis:**
- ambition (26 shared with love), compassion (13), devotion (6), worth (11 shared with kindness)

**Gravitate toward strength/power axis:**
- generosity (22 shared with strength), appetite (11), weakness (8)

**Gravitate toward desire axis:**
- craving (23 shared with desire), lust (18), covetousness (9), flesh (9)

**Gravitate toward wisdom axis:**
- wisdom (23 shared with insight), understanding (22), discernment (21)

**Other gravitational links:**
- envy/zeal (21 each — mutual pair), repentance/transformation/likeness (15-16 mutual — renewal vocabulary)
- joy (16 with delight), reasoning (12 with pray), sin (16 with guilt), resentment (15 with anger)
- praise (19 with power), slander (18 with might), malice (9 with sorrow)
- condemnation (1 with thought — near-isolate), contentment (5 with hope — near-isolate)

### Analytical implications for analysis ordering

1. **The Volitional Core (9 words)** should be analysed as a group or in close sequence — they are too interconnected to analyse independently.

2. **Natural analysis batches emerging from gravitational patterns:**
   - Wisdom sub-group: discernment, insight, understanding, wisdom, knowledge (all C02)
   - Desire sub-group: desire, craving, lust, appetite, covetousness, flesh
   - Trust sub-group: trust, faith, hope, faithfulness, despair, doubt, covenant
   - Love sub-group: love, kindness, compassion, mercy, devotion, worth
   - Power sub-group: strength, power, authority, dominion, courage, might, generosity

3. **Near-isolates** (condemnation with 1 connection, contentment with 5) could be analysed with the not-shared words — their cross-registry dependence is minimal.

"""
    content = content[:idx] + section_54 + content[idx:]

    with open(REPORT, "w", encoding="utf-8") as f:
        f.write(content)

    conn.close()
    print("Report consolidated — all fixes and additions applied in one pass.")


if __name__ == "__main__":
    main()
