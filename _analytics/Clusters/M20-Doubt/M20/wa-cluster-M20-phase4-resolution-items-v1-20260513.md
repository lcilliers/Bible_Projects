# M20 Phase 4 — resolution of open items (na.dad + apelpizo)

**Date:** 2026-05-13
**Author:** CC, in response to AI session's Phase 4 open items
**Status:** Researcher direction received

---

## Researcher direction (received 2026-05-13)

**On H5074 na.dad:**

> "My view on H5074 is it must be considered as the opposite of hope, and therefore belongs in M18. It is not the same as H5076, H5079 or H5206. This definitely should not be set aside."
>
> _(researcher correction 2026-05-13: M18, not M12)_

**Implications:**

- The 13 G-status verses for na.dad (in vcg_id=1306, group_code `5571-001`) **remain `is_relevant=1`**. No VCREVISE set-aside patch is to be authored.
- The term H5074 *na.dad* is **reassigned out of M20 into M18 (Hope, Expectation and Waiting)** (per researcher direction, confirmed 2026-05-13).
- The 13 G-status verses + their VCG follow the term into M18. Their existing inner-being meaning ("Term names wandering or fleeing as an inner experience — restlessness of sleep fleeing, the anguish of spiritual straying…") is retained; M18 may revise during its own Phase 6.
- The 13 Phase-2 set-aside verses (already applied) also follow the term — they remain set-aside but under M18.
- na.dad is **not** to be grouped with H5076 *ne.dud*, H5079 *nid.dah*, H5206 *ni.dah* — the root-NADAD sibling pattern does not apply here.
- na.dad is **co-located with apelpizo (G0560)** in M18 — both are inner-being instances of hope's structural absence (despair / inner straying).

---

## Action plan

### Action 1 — No VCREVISE patch for na.dad G-status verses

**Cancel the previously proposed VCREVISE set-aside patch for the 13 G-status verses.** They stay as-is. The verse list and IDs below are recorded for the record, not for action.

### Action 2 — Cluster reassignment directive (M20 → M18)

H5074 *na.dad* (mti_id=5571) is moved out of M20. The directive operates on `mti_terms.cluster_code` (and any related fields):

- **MOTIVATION** — Researcher direction (this document) confirms na.dad as the inner-being opposite of hope, distinct from its root-sibling impurity terms. Cluster reassignment from M20 to M18.
- **SCOPE** — Single mti_terms row update: `mti_terms.cluster_code = 'M18'` and `cluster_subgroup_id = null` (destination cluster will assign in its own Phase 4) for `strongs_number='H5074'`. The 26 active `verse_context` rows for `mti_term_id=5571` follow implicitly (they reference the term, not the cluster). VCG row `id=1306` / `group_code='5571-001'` also follows (no rename needed; the 5571-prefix means it's term-scoped, not cluster-scoped naming).
- **OUTCOME REQUIRED** — Exactly one mti_terms row updated; `cluster_code='M18'`; verse_context row count for mti_term_id=5571 unchanged.
- **COMPLETION CONFIRMATION** — `SELECT cluster_code, cluster_subgroup_id FROM mti_terms WHERE strongs_number='H5074'`; `SELECT COUNT(*) FROM verse_context WHERE mti_term_id=5571 AND COALESCE(delete_flagged,0)=0` returns 26.

Filename pattern: `wa-cluster-M20-dir-{NN}-term-rebind-na.dad-v1-20260513.md`. Sequence number = next available for M20 (dir-001 is the historical status-init; dir-002 will be the Phase 4 subgroup-assign per v1_6 §7 numbering; this reassignment is likely dir-003 or runs in parallel with subgroup-assign).

### Action 3 — apelpizo (G0560) reassignment to M18

Proceed as separately planned. apelpizo carries 1 verse, "to despair", current cluster M20. Destination M18 (Hope, Expectation and Waiting). Same reassignment-directive pattern as Action 2.

If confirmed destination for na.dad is also M18, both reassignments can be combined into one directive that updates two mti_terms rows.

---

## Reference data — Item 1: na.dad G-status verses (no longer to be set aside)

These 13 verses currently sit in **vcg_id=1306, group_code `5571-001`**, all `is_relevant=1`, one anchor (Psa 55:7 — vc_id=21655). Recorded here for the directive author to confirm the verse-context state survives the reassignment intact.

| vc_id | vr_id | reference | is_anchor |
|---:|---:|---|---:|
| 21655 | 169940 | Psa 55:7 | **1** |
| 21656 | 169919 | Gen 31:40 | 0 |
| 21657 | 169918 | Est 6:1 | 0 |
| 21658 | 169933 | Job 15:23 | 0 |
| 21659 | 169934 | Job 18:18 | 0 |
| 21660 | 169935 | Job 20:8 | 0 |
| 21661 | 169939 | Psa 31:11 | 0 |
| 21662 | 169938 | Pro 27:8 | 0 |
| 21663 | 169925 | Isa 16:3 | 0 |
| 21664 | 169926 | Isa 21:14 | 0 |
| 21665 | 169920 | Hos 7:13 | 0 |
| 21666 | 169921 | Hos 9:17 | 0 |
| 21667 | 169937 | Nah 3:7 | 0 |

VCG context description (preserved):

> Term names wandering or fleeing as an inner experience — restlessness of sleep fleeing, the anguish of spiritual straying…

---

## Reference data — Item 2: root family and sibling clustering (context only)

The researcher's direction overrides the root-family clustering pattern. Recorded here only to capture the data state for any future review.

| Strong's | Translit. | Gloss | Owner reg | Current cluster | Status after this direction |
|---|---|---|---|---|---|
| **H5074** | *na.dad* | to wander | R086 (impurity) | M20 | **Moving to M12 or M18 (TBC)** |
| H5076 | *ne.dud* | tossing | R086 (impurity) | M01 (Fear) | unchanged |
| H5079 | *nid.dah* | impurity | R086 (impurity) | M10 (Guilt) | unchanged |
| H5206 | *ni.dah* | filth | R086 (impurity) | M07 (Shame) | unchanged |

Root code: **NADAD** ("filth"). Researcher's reading: na.dad's inner-being content departs from the root-sibling impurity reading and aligns with the hope-opposite reading.

---

## Ready for AI directive authoring

1. **na.dad (H5074) → M18** — confirmed.
2. **apelpizo (G0560) → M18** — confirmed (assumed; if a different destination was intended, raise before authoring).
3. Since both terms target M18, AI may author **one combined cluster-reassignment directive** updating two `mti_terms` rows in a single operation, or two separate directives — either pattern is acceptable per `wa-directive-instruction [current]` §11.6. The combined form is simpler.

**Suggested filename (combined):** `wa-cluster-M20-dir-{NN}-term-rebind-to-M18-v1-20260513.md` (sequence number = next available for M20; dir-001 was the historical status-init, dir-002 will be the Phase 4 subgroup-assign per v1_6 §7, so this rebind is likely dir-003).

CC will pre-flight and apply once the directive is authored.
