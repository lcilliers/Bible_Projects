# wa-cluster-M39-dir-003-B-mapping-v1-20260514

**Cluster:** M39 — Blessing, Favour and Grace  
**Directive sequence:** dir-003  
**Segment:** M39-B  
**Pattern:** cluster-process directive per wa-directive-instruction [current] §11.4  
**Authored by:** Claude AI  
**Date:** 2026-05-14  
**Status:** AWAITING RESEARCHER REVIEW — do not apply until approved

---

## MOTIVATION

Phase 7 applies the Phase 6 VCG reconciliation decisions for sub-group M39-B to the database.

Source documents:
- Phase 6 mapping: WA-M39-B-group-verse-mapping-v1-20260514.md
- Phase 7 pre-assessment: wa-obslog-M39-sessionb-v1-20260514.md §10.3
- Obslog session reference: wa-obslog-M39-sessionb-v1-20260514.md

This directive covers M39-B only. Dir-002 covers M39-A. Splitting at the sub-group boundary provides failure-radius isolation — a problem in M39-B processing cannot roll back M39-A work already applied.

Phase 6 produced 4 REFINE decisions (description updates) and 14 P-status verse group_id assignments. No new VCGs — no vcg_term inserts required.

**Flag 2 note (from WA-M39-B-group-verse-mapping-v1-20260514.md §5):** Num 24:1 (vr_id=4188, mti_id=542, tov) — possible wrong-face; its inner-being content ("it pleased the Lord to bless Israel") may sit closer to the M39-A divine-pleasure register (eudokia/ra.tsah) than the M39-B goodness-quality register. Decision: assign to 542-001 (tov wellbeing/moral approval) as the tov term's primary home; note the M39-A adjacency in findings. This is correct — the term tov is M39-B; the verse's divine-pleasure content is a bridge point to be documented in Phase 9 findings.

---

## SCOPE

### Operation 1 — `verse_context_group` description UPDATE (4 REFINE decisions)

| group_id | code | New core_description |
|---|---|---|
| 1587 | 542-001 | Term names the two-pole goodness characteristic of tov: (i) goodness as heart-quality — the inner moral excellence located in the heart before the act (1Ki 8:18 — "you did well that it was in your heart"), persisting through affliction (Psa 119:71), affirmed by God in right action (2Ki 10:30); and (ii) affective gladness-at-good — the heart merry or satisfied in contexts of festive wellbeing, pleasure, and communal celebration (Judg 16:25; Est 1:10; Song 4:10); the two poles are united in tov as the term for what is genuinely good in the inner person |
| 2837 | 632-001 | Term names the heart being glad or merry — the inner state of lightness and well-being expressed in festive eating, drinking, and communal celebration; with somatic consequences: the glad heart heals ("a joyful heart is good medicine," Pro 17:22) and the crushed spirit destroys ("a crushed spirit dries up the bones") — the goodness characteristic has a physical dimension |
| 2838 | 632-002 | Term names moral goodness and doing good: the inner moral orientation from which right action flows; goodness as the ground of divine acceptance (Gen 4:7 — "if you do well, will you not be accepted?"), requiring sustained intentional exercise (Psa 36:3 — "he has ceased to act wisely and do good"), and extending goodness outward toward others and community |
| 2839 | 632-003 | Term names the inner state of being pleased or finding something good — the approval, satisfaction, or favour that the inner person extends toward a person, course of action, or situation; includes the volitional-preference idiom ("what seems good to you" / "whatever seems best" — 1Sa 24:4; 2Sa 18:4; 2Sa 3:19), divine moral approval of human speech (Deu 18:17), royal approval (Neh 2:6), and communal endorsement (Jos 22:33) |

### Operation 2 — `verse_context` UPDATE: group_id assignment for 14 P-status verses in M39-B

| vr_id | mti_term_id | Reference | Target group_code | group_id | Rationale |
|---|---|---|---|---|---|
| 4188 | 542 | Num 24:1 | 542-001 | 1587 | "It pleased the Lord to bless Israel" — tov as divine inner pleasure-approval; assigned to 542-001 (wellbeing/moral approval); note M39-A adjacency (divine pleasure register) — to be documented in Phase 9 findings |
| 4189 | 542 | Num 24:5 | 542-001 | 1587 | "How lovely are your tents, O Jacob" — tov as the aesthetic-goodness of the beloved; fits 542-001 (inner wellbeing/approval/pleasure) |
| 4190 | 542 | Deu 5:33 | 542-001 | 1587 | "That it may go well with you" — tov as the covenantal blessing-outcome of obedience; fits 542-001 (wellbeing/approval) |
| 59830 | 632 | 1Sa 18:5 | 632-003 | 2839 | "This was good in the sight of all the people" — ya.tav as communal approval/pleasure; fits 632-003 |
| 59831 | 632 | 1Sa 20:13 | 632-003 | 2839 | "Should it please my father" — ya.tav as volitional-judgment/approval; fits 632-003 |
| 59832 | 632 | 1Sa 24:4 | 632-003 | 2839 | "Do to him as it shall seem good to you" — ya.tav as volitional preference; fits 632-003 |
| 59833 | 632 | 1Sa 25:31 | 632-002 | 2838 | "When the Lord has dealt well with my lord" — ya.tav as divine beneficent dealing/goodness; fits 632-002 (moral goodness in action); the divine dealing-well pattern |
| 4197 | 542 | 2Sa 15:26 | 542-001 | 1587 | "Let him do to me what seems good to him" — tov as volitional preference/judgment surrendered to God's disposition; fits 542-001 |
| 59838 | 632 | 2Sa 18:4 | 632-003 | 2839 | "Whatever seems best to you I will do" — ya.tav as volitional preference; fits 632-003 |
| 4198 | 542 | 2Sa 19:37 | 542-001 | 1587 | "Do for him whatever seems good to you" — tov as volitional preference/judgment; fits 542-001 |
| 59836 | 632 | 2Ki 25:24 | 632-002 | 2838 | "It shall be well with you" — ya.tav as promised wellbeing/flourishing from obedience; fits 632-002 (goodness-outcome of right relationship) |
| 12533 | 632 | Pro 15:2 | 632-002 | 2838 | "The tongue of the wise commends knowledge" — ya.tav as the quality of wise speech that makes good use of knowledge; fits 632-002 (goodness as inner moral orientation expressed outward) |
| 12542 | 632 | Jer 1:12 | 632-002 | 2838 | "You have seen well" — ya.tav as the quality of right/accurate perception; the goodness of discernment; fits 632-002 |
| 12560 | 632 | Eze 36:11 | 632-002 | 2838 | "I will do more good to you than ever before" — ya.tav as divine beneficent-goodness in eschatological restoration; fits 632-002 |

### vcg_term check

No NEW VCGs created in this directive. No vcg_term INSERT operations required.

---

## OUTCOME REQUIRED

1. Four `verse_context_group` rows (ids: 1587, 2837, 2838, 2839) have updated `core_description` values as specified above.
2. Fourteen `verse_context` rows have `group_id` populated (previously NULL):
   - vr_ids: 4188, 4189, 4190, 59830, 59831, 59832, 59833, 4197, 59838, 4198, 59836, 12533, 12542, 12560
3. No new `verse_context_group` rows created.
4. No `vcg_term` rows required.
5. `cluster.status` unchanged — remains `Analysis - In Progress`.

---

## COMPLETION CONFIRMATION

**Query 1 — Verify 4 VCG description updates (spot-check 2):**
```sql
SELECT id, subgroup_code, core_description
FROM verse_context_group
WHERE id IN (1587, 2838)
ORDER BY id;
```
Expected: 2 rows with updated core_description matching directive text above.

**Query 2 — Verify 14 verse_context group_id assignments:**
```sql
SELECT vc.verse_record_id, vc.mti_term_id, vc.group_id, vcg.subgroup_code
FROM verse_context vc
JOIN verse_context_group vcg ON vcg.id = vc.group_id
WHERE vc.verse_record_id IN (4188, 4189, 4190, 59830, 59831, 59832, 59833, 4197, 59838, 4198, 59836, 12533, 12542, 12560)
ORDER BY vc.verse_record_id;
```
Expected: 14 rows, each with group_id populated and matching target group codes above.

**Query 3 — Confirm no remaining P-status verses for M39-B terms:**
```sql
SELECT COUNT(*) AS remaining_p
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
JOIN mti_term_subgroup mts ON mts.mti_term_id = mt.id
JOIN cluster_subgroup cs ON cs.id = mts.cluster_subgroup_id
WHERE cs.cluster_code = 'M39'
  AND cs.subgroup_code = 'M39-B'
  AND vc.is_relevant = 1
  AND vc.group_id IS NULL;
```
Expected: 0.

**Query 4 — Cluster-wide H2 connectivity check (no relevant verses without group_id):**
```sql
SELECT COUNT(*) AS h2_count
FROM verse_context vc
JOIN mti_terms mt ON mt.id = vc.mti_term_id
WHERE mt.cluster_code = 'M39'
  AND mt.status IN ('extracted', 'extracted_thin')
  AND vc.is_relevant = 1
  AND vc.group_id IS NULL;
```
Expected: 0 (all M39 relevant verses now have group_id after both dir-002 and dir-003 applied).

**Application report:** CC saves to `Sessions/Session_Clusters/M39/WA-M39-B-group-mapping-applied-v1-20260514.md`.

---

*wa-cluster-M39-dir-003-B-mapping-v1-20260514*  
*References: WA-M39-B-group-verse-mapping-v1-20260514.md | wa-obslog-M39-sessionb-v1-20260514.md*
