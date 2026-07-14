# Proverbs book-close — audit, coverage-gap finding, and resolution plan

- **Date:** 2026-07-14
- **Trigger:** book-close (Phase 2 families + G0–G10 scored audit) after the 59-cycle reread.

## 1. Phase 2 — ib_characteristic family grouping (DONE)
- Ran `_apply_ib_char_family_grouping_v1_20260711.py --book 20 --live` (script parameterised with `--book`, defaulting to 19; two Proverbs-relevant families added — `sloth-diligence-industry`, `wealth-poverty-riches` — plus keyword extensions for injustice/crooked/prudence).
- **744 records → 45 families** (under the 50 cap), **0 NULL**, **6 `other-uncategorised`** (0.9% — a Strong's-only name, "meets"/encounter, an ambiguous "honor": legitimately unforced).
- Heaviest families (record/instance): wisdom-folly-teaching (68/274), inner-seat (49/164), righteousness-integrity (39/162), knowing-understanding (42/160), wickedness-ungodliness (26/138), desire-longing (45/112) — a distribution true to a wisdom book.

## 2. G0–G10 scored audit (DONE) — and the coverage gap it surfaced
`_check_reread_measures_v3_20260709.py --book 20 --label final` reports on the **whole book-20 span-index (segment model, 2,092 chars)**, which mixes my reread-2026 layer with the older July-3 poetic-lexical layer. Key results and their diagnosis:

- The reread-2026 layer (**1,942 chars**) is fully clean — every per-cycle gate passed across all 59 cycles.
- The audit's non-passing counts (G10: 150 chars missing a mandatory dim; G2: 81 no-operation; G6: 9 no-discovery) are **entirely legacy** — 146 `lexical-model-2026` + 4 `role-reassess-2026`; **zero read-2026**.

### The headline finding — a verse-level coverage gap
- Proverbs has **915 verse rows**. Only **799 carry a `passage_id`**; **116 have `passage_id = NULL`** (marker `Pro-24-poetic-lexical-20260703`, a pre-reread pass). They exist **only** as orphan rows (no duplicate passage-assigned row).
- My 59-cycle reread was **passage-driven** (pull passages by id). It covered **701/701 passages** — but the passage structure only spans the 799 passage-assigned verses. **The 116 orphan verses were never pulled** into the reread-2026 layer.
- So the earlier "Proverbs fully read (100%)" was true at the **passage** level but **not** at the **verse** level: reread-2026 covers **799 of 915 verses (87%)**. **This corrects that claim.**

### Anatomy of the 116 orphans
- **31 carry IB candidate/char content** — a genuine reread gap. Includes real inner-being verses: **24:10** (fainting in adversity), **30:7-8** (Agur's actual two-request prayer), several **sluggard** verses (6:9, 19:24, 26:13-14), **13:11** (wealth), **18:9** (the slack worker), and **31:15/24/27** of the woman of valour.
- **85 have zero candidate/char spans** — titles/intros (1:1), ambush-speech content (1:13-15), cistern/imagery (5:15-17), surety mechanics (6:1-2), the ant's detail (6:7-8): the same non-IB category as the 13 deliberate passage-level skips.
- Spread across chapters (heaviest: ch6:12, ch7:11, ch31:10, ch30:9, ch8:7, ch5:7, ch24:8).

They were **read once, under the older July-3 poetic-lexical pass** (hence their legacy chars/lexical); they simply were never re-covered by the authoritative reread-2026 layer.

## 3. Resolution
The apply engine (`_apply_reread_lexical_v1`) and conformance checks are **span-id based**, so the orphans can be read directly by verse without restructuring the (authoritative) passage model. Plan:
1. **Read the 31 content-bearing orphans** to the reread-2026 standard (full poetic ledger, Screen 0, couplings), applying + conformance-checking by span-id.
2. **Scan the 85 char-less orphans**; read any that carry genuine IB content on the verse, else confirm as legitimate skips (log the list).
3. **Demote the 98 leftover legacy chars on already-read verses** (old-model spans I read the verse but deliberately did not re-select — e.g. 22:4 reward-trio) to `standalone`/`read-2026-demote`, so the read layer is the sole authority on read verses.
4. Re-run the family grouping (to absorb any new records) and the G0–G10 audit; produce the baseline→delta.

## 4. Status of the three requested steps
- **Phase 2 families:** DONE.
- **Full audit / G0–G10:** DONE — surfaced the gap above; baseline→delta pending gap closure.
- **Follow-ups (OT-DBR-009, H3856):** pending.

**Correction to the record:** Proverbs is not yet reread-complete at the verse level. Closing the 116-orphan gap (≈31 content verses) is the honest completion, proceeding now.
