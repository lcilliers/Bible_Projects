# CC Directive — Registry 068 Grace — Root Family Records: H2594 and H2600
**File:** wa-068-grace-sessionB-cc-directive-v5-2026-04-10.md
**Date:** 2026-04-10
**From:** Claude AI — Session B Stage 1 — deferred from Directive v4
**Registry:** 068 — grace

---

## What this directive covers

Two reinstated terms (H2594 and H2600) require CHEN root_family records in Reg 068's inventory. These were deferred from Directive v4 pending reinstatement confirmation. Both reinstatements are now confirmed stable.

**Note on pre-existing record:** CC's Directive v4 report identified an older CHEN record (id=258) at term_inv_id=285 for H2600 in a different registry's inventory. This is not the same row. Reg 068's H2600 entry is term_inv_id=5587 and has zero root_family records. Insert for ti=5587 only.

---

## Etymology

Both terms derive from the Hebrew root חנן (chanan):
- **H2594 cha.ni.nah** — feminine noun meaning *favour, compassion*. Derivative of chanan.
- **H2600 chin.nam** — adverb meaning *freely, for nothing, gratuitously*. Derived from chen (H2580), the noun of the same root.

Both belong to root_code=CHEN alongside H2580, H8469, H2587, H2603A, H8467.

---

## Operations required

**Insertion 1 — H2594 (cha.ni.nah)**
- term_inv_id = 5592
- root_code = 'CHEN'
- root_language = 'Hebrew'
- root_gloss = 'favor'
- note = 'Added 2026-04-10 Session B Stage 1 audit — reinstated term, etymological member of chen/chanan root family'
- delete_flagged = 0

**Insertion 2 — H2600 (chin.nam)**
- term_inv_id = 5587
- root_code = 'CHEN'
- root_language = 'Hebrew'
- root_gloss = 'favor'
- note = 'Added 2026-04-10 Session B Stage 1 audit — reinstated term, adverbial derivative of chen root'
- delete_flagged = 0

---

## Expected state after application

All seven active Hebrew CHEN-root terms in Reg 068 will carry CHEN root_family records:
H2580 (existing), H8469 (existing), H2587 (Directive v4), H2603A (Directive v4), H8467 (Directive v4), H2594 (this directive), H2600 (this directive).

---

## Reporting required

Confirm:
1. Two records inserted at ti=5592 and ti=5587
2. No duplicate records existed at these term_inv_ids before insertion
3. Updated root_family_count — expected 10 on next export (was 8 after Directive v4)

Then produce a fresh complete export: wa-068-grace-complete-[date].json reflecting all changes from Directives v2 through v5.
