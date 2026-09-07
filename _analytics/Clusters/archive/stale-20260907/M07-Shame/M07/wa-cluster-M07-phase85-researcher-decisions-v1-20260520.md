# M07 Phase 8.5 — Researcher decisions on review items

**Date:** 2026-05-20
**Cluster:** M07 — Shame, Disgrace and Humiliation
**Per:** v2_8 §11A.2 step 4 — researcher review of AI dispositions
**Source:** `WA-M07-boundary-resolution-v1-20260519.md` (AI verdict document with 3 review items + 1 term-level decision)

---

## Verdict review summary

AI Phase 8.5 dispositions: **24 firm** + **3 RESEARCHER-REVIEW-REQUIRED** + **1 term-level RECOMMEND-RESEARCHER-REVIEW**.

The AI also surfaced a **structural finding**: ROUTE-TO-CLUSTER is unavailable for all 27 verses (no other-cluster terms exist at any of the BOUNDARY `wa_verse_records.id`). Every disposition is either SET-ASIDE or PROMOTE-TO-SUBGROUP.

---

## Researcher decisions

### 1. Pro 16:19 (vc=21172) — sha.phel — voluntary lowliness "with the poor"

- **AI recommended:** SET-ASIDE (verse evidences M09 voluntary-lowliness, not M07 shame)
- **Alternative:** PROMOTE-TO-SUBGROUP M07-I-NEW
- **Researcher decision:** **SET-ASIDE** (recommendation accepted)
- **set_aside_reason:** "sha.phel here names voluntary lowliness of spirit as a positive moral stance — not shame, disgrace, or humiliation; M09 characteristic; no M09 target term available for routing — outside M07 inner-being scope."

### 2. Pro 29:23 (vc=21162) — sha.phel — "pride brings him low; lowly of spirit obtains honor"

- **AI recommended:** SET-ASIDE (same M09 concern as Pro 16:19; cannot split the verse)
- **Alternative:** PROMOTE-TO-SUBGROUP M07-D (focus on "pride brings him low" half)
- **Researcher decision:** **PROMOTE-TO-SUBGROUP M07-D** (alternative chosen — preserve the enforced-abasement content in M07)
- **Rationale (per researcher):** the "pride brings him low" half is sufficient M07-D inner-being content to retain; the lowliness-honour half is a secondary M09-leaning observation that can be captured at Phase 9 T6 as a cross-cluster note rather than excluding the verse from M07 entirely.

### 3. Eze 17:24 (vc=21184) — sha.phel — high tree brought low / low tree raised

- **AI recommended:** PROMOTE-TO-SUBGROUP M07-D (judicial reversal; divine lowering of exalted in punitive context)
- **Alternative:** SET-ASIDE (tree metaphor not directly evidencing a human inner-being state)
- **Researcher decision:** **PROMOTE-TO-SUBGROUP M07-D** (recommendation accepted)

### 4. H8400 te.val.lul (mti_id=4712) — term-level decision

- **AI recommended:** SET-ASIDE-TERM (no is_relevant verses; Lev 21:20 set-aside at Phase 1)
- **Researcher decision:** **SET-ASIDE-TERM** (recommendation accepted)
- **Mechanism:** UPDATE `mti_terms SET status='excluded', delete_flagged=1` with audit note. No verse-level operations.

---

## Final disposition counts (all 27 verses + 1 term)

| Disposition | Count |
|---|---:|
| SET-ASIDE | **4** — Phili 3:2 (katatomē), Isa 52:14 (mish.chat), Psa 113:6 (sha.phel: God's condescension), Pro 16:19 (sha.phel: voluntary lowliness) |
| PROMOTE-TO-SUBGROUP M07-B | **1** — Lam 1:8 (ni.dah → shame as moral consequence) |
| PROMOTE-TO-SUBGROUP M07-D | **22** — 20 firm sha.phel divine-abasement verses + Pro 29:23 + Eze 17:24 |
| **Total** | **27** ✓ |
| Term-level SET-ASIDE-TERM | **1** — H8400 te.val.lul |

---

## Cross-cluster carry-forward notes (recorded for Phase 9 T6 + future cluster sessions)

- **Lam 1:8 ni.dah** — the M12 purity dimension of the term is preserved as a Phase 9 T6 (Structural Relationships with Other Characteristics) note for when M12 opens.
- **Pro 16:19 sha.phel SET-ASIDE** — note for M09 (Humility/Meekness) session open: this verse awaits pickup; sha.phel is M09's home-registry term and Pro 16:19 evidences M09's characteristic directly. CC should track this for the M09 session.
- **Pro 29:23 sha.phel PROMOTE M07-D** — the secondary lowliness-honour half is a cross-cluster relationship (M07 enforced-humiliation ↔ M09 voluntary-lowliness paired in one proverb); flag for Phase 9 T6.

---

## Next step

CC builds and applies the Phase 8.5 directive `WA-M07-dir-005-boundary-resolution-v1-20260520.md` with:
- Op A — SET-ASIDE (4 vc rows)
- Op C — PROMOTE-TO-SUBGROUP (23 vc rows: 1 to M07-B, 22 to M07-D)
- Op F — Clear BOUNDARY flags
- (Plus term-level Op for H8400 te.val.lul exclusion)
- Op E (VCG follow-on) — assign the 23 promoted verses to appropriate VCGs in their new sub-groups

---

*End of researcher decisions document.*
