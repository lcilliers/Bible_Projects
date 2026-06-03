# M39 BOUNDARY exit — CC investigation and recommendation

**Date:** 2026-05-14
**Scope:** Phase 10 BOUNDARY exit (§13.6, §15) for M39's three BOUNDARY terms — H2868 te.ev, G1435 dōron, H7862 shay.
**Source data:** verse counts, VC classifications, VCG context_descriptions, anchor designations, and cluster landscape — all queried live from `database/bible_research.db` (post-Phase 9).
**Method:** present the DB facts, weigh AI's options against the evidence, recommend the option that best fits the data.

---

## H2868 te.ev — **Recommend Option A: cluster reassignment to M04 (Joy)**

### Facts

| Field | Value |
|---|---|
| Strong's, gloss, language | H2868 te.ev · "be good" · **Aramaic** |
| `mti_terms.owning_word` | **"gladness"** (← key signal: registered under a gladness lemma, not goodness) |
| Active verses | **1** (Dan 6:23) |
| VC state | `is_relevant=1`, in group `633-001`, span_match=1 |
| Group context_description | *"Te.ev as exceedingly glad: inner gladness at deliverance through trust in God"* |
| status / vc_status | `extracted` / `not_done` (registry-era leftover; the single verse is already classified relevant) |
| Anchor designation | Not currently anchored, but the single verse would be by default |
| Research flags for this term | None |

### Analysis

The verse evidence is unambiguous: Dan 6:23 names exceedingly glad — joy/gladness, not goodness or grace. The mismatch is structural:

- `owning_word="gladness"` says the term was registered as a gladness lemma.
- The mti_terms gloss ("be good") is the auto-gloss that incorrectly routed te.ev into M39.
- The actual verse content (Dan 6:23) and the existing group description (633-001) both treat te.ev as a gladness term.

M39 was the wrong home. The verse evidence belongs in a joy/gladness cluster.

### Cluster landscape

**M04 (Joy)** is the natural target:
- Status: `Not started` (no analysis to disrupt — adding one term is clean)
- Gloss explicitly includes: *"be cheerful (euthumeō), be cheerful (ba.lag), be glad (eupsucheō)"*
- Contains 14+ joy/rejoice/gladness terms already (G0020 agalliasis, G0021 agalliao, G5479 chara, H1523 gil, H2304 ched.vah, H7797 su.s, H8055 sa.mach, etc.)
- Aramaic-source terms are not exclusively excluded — the cluster's semantic scope covers OT and NT gladness.

### Recommendation

**Option A — Cluster reassignment to M04.** Mechanism: a small REPAIR-style cluster_code update on `mti_terms.cluster_code` (633: M39 → M04). The single verse_context_group row 633-001 remains intact (it's keyed by `group_code`, not cluster) — M04 inherits a fully-classified term ready for its Phase 6 reconciliation.

**Why not Option B (flag-for-decision):** the data is conclusive. Flagging without acting leaves M39 with a misclassified term whose content has no analytical relationship to grace or goodness. Defers a decision the data has already made.

---

## G1435 dōron — **Recommend a third option: promote to M39-A** (neither A nor B)

### Facts

| Field | Value |
|---|---|
| Strong's, gloss, language | G1435 dōron · "gift" · Greek |
| Active verses | **17** |
| VCGs designed for this term | **6** (6837-001 through 6837-006) |
| Anchor verses | **5** (Mat 2:11, Mat 5:23, Mat 15:5, Luk 21:4, Eph 2:8, Heb 9:9) |
| Research flags | None |

### VCGs (already in DB)

| Code | Theme | Verses (incl. anchors★) |
|---|---|---|
| 6837-001 | **Gift as act of worship** — offering as expression of inner devotion toward God | Mat 2:11★, Mat 8:4, Mat 23:18, Mat 23:19, Luk 21:1, Heb 8:4, Heb 11:4 (7) |
| 6837-002 | **Moral claim of relational conscience amid worship** — gift interrupted by reconciliation | Mat 5:23★, Mat 5:24 (2) |
| 6837-003 | Misuse of religious dedication — piety masking filial failure | Mat 15:5★, Mar 7:11 (2) |
| 6837-004 | **Inadequacy of ritual gifts to perfect the conscience** — gap between external offering and inner transformation | Heb 5:1, Heb 8:3, Heb 9:9★ (3) |
| 6837-005 | **Salvation as God's free gift** — not earned but received, establishing inner dependence and gratitude | Eph 2:8★ (1) |
| 6837-006 | Radical self-giving generosity — total offering from poverty as expression of complete inner trust | Luk 21:4★, Rev 11:10 (2) |

### Analysis

The DB facts directly contradict the framing of dōron as a BOUNDARY term:

- **17 verses · 6 sub-groups · 5 anchor verses** is the signature of a **characteristic-bearing** term, not a supportive/qualifying one.
- Three of the six VCGs (002, 004, 005) carry substantial inner-being content directly relevant to grace:
  - 6837-002 — conscience and worship integration
  - 6837-004 — the conscience-perfection gap (Heb 9:9 sits at the structural opposite face of grace)
  - 6837-005 — salvation-as-gift (Eph 2:8) is grace-as-gift, direct M39-A register
- The remaining three (001 worship, 003 piety-masking, 006 self-giving generosity) name inner-being content adjacent to grace (giving from inner devotion, grace propagation through human agency).

**Neither AI option fits the evidence:**

- **Option A (set aside within M39)** would discard 5 anchor verses' worth of analytical investment and 6 carefully designed VCGs. The Eph 2:8 anchor in particular is grace-as-gift — the M39-A signature register.
- **Option B (flag-for-decision)** defers a decision the data has substantively answered.

### Third option — promote to M39-A

The term carries inner-being content. The content is mixed (worship + grace + ritual critique + self-giving) but its core register is gift-as-grace, which IS the M39-A characteristic. AI was over-cautious in placing dōron in BOUNDARY.

**Mechanism:** mti_term_subgroup UPDATE for mti_id=6837 from M39-BOUNDARY to M39-A. The 17 verse_context rows and 6 verse_context_group rows remain unchanged. The term joins M39-A as its 12th term.

**Knock-on effect:** Phase 8 catalogue findings for M39-A do not currently include dōron evidence. Either:
1. Re-run the M39-A Phase 8 catalogue pass with dōron's 17 verses incorporated (substantial work), OR
2. Add dōron-specific finding rows under the existing M39-A prompts in Phase 10 as supplementary content (lighter touch), OR
3. Accept that the cluster_finding record reflects a slightly narrower scope of M39-A than the final term membership.

### Recommendation

**Promote G1435 dōron to M39-A.** Pair this with a finding-record decision: option 2 or 3 above. CC can supply a structured "what would supplementary M39-A findings look like for dōron" if helpful, but that is AI's analytical work.

**If you prefer to stay within AI's stated options:** Option B (flag-for-decision) is far preferable to A (set-aside). Setting aside 17 verses across 6 anchor-bearing groups would destroy a substantial amount of useful analytical structure.

---

## H7862 shay — **Concur with AI's proposal: set aside**

### Facts

| Field | Value |
|---|---|
| Strong's, gloss, language | H7862 shay · "gift" · Hebrew |
| Active verses | **3** (Psa 68:29, Psa 76:11★, Isa 18:7) |
| VCGs | **1** (2976-001) — *"the gift/tribute brought to God as the expression of inner homage, reverence, and acknowledgment of his supremacy"* |
| Anchor verses | 1 (Psa 76:11) |
| status / vc_status | `extracted_thin` / `not_done` — the `_thin` status formally marks low data volume |
| Research flags | None |

### Analysis

All three verses occupy the same narrow register: tribute brought to God (typically by foreign nations or all peoples) as an expression of reverence and acknowledgment of supremacy. The inner-being content is real — reverence, homage — but the register sits adjacent to fear/awe (M01) or worship/prayer (M21), not grace or goodness.

`extracted_thin` is the term-status flag for low-volume terms; 3 verses with a single VCG matches that profile.

### Recommendation

**Concur with AI — set aside within M39.** Mechanism: per-verse `verse_context.set_aside_reason` populated; `is_relevant=0`. Suggested reason text:

> *"H7862 shay names tribute/homage brought to God expressing reverence and acknowledgment of supremacy — inner-being register is reverence/awe rather than grace or goodness; outside M39's characteristic scope."*

`mti_term_subgroup` placement in M39-BOUNDARY stays (term remains in M39 but with all verses set aside, which is the §15.2 "set-aside" exit pattern).

---

## Mechanism summary (for the Phase 10 verification-corrections directive)

| Term | Recommended exit | DB operations |
|---|---|---|
| H2868 te.ev (633) | **Cluster reassignment to M04** | `UPDATE mti_terms SET cluster_code='M04' WHERE id=633`; **also** soft-delete the M39-BOUNDARY `mti_term_subgroup` row for mti_id=633 (since it's no longer in M39 at all). Verse + VCG rows unchanged. |
| G1435 dōron (6837) | **Promote to M39-A** | `UPDATE mti_term_subgroup SET cluster_subgroup_id=<M39-A.id> WHERE mti_term_id=6837 AND cluster_subgroup_id=<M39-BOUNDARY.id>`. Plus an analytical pass-or-flag for the 17 verses' Phase 8 coverage. |
| H7862 shay (2976) | **Set aside (stays in M39-BOUNDARY)** | `UPDATE verse_context SET is_relevant=0, set_aside_reason=<reason text> WHERE mti_term_id=2976`. `mti_term_subgroup` placement unchanged. |

These three operations should be packaged into the Phase 10 verification-corrections directive (§13.7) alongside the other Phase 10 work (gap resolution, anomaly review, `Analysis Completed` status flip).

---

*Source: `scripts/_tmp_m39_boundary_investigate.py` (archived after this report).*
