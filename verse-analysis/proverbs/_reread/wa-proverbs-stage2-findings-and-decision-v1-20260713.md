# Proverbs re-read — Stage-2 findings + decision request (v1, 2026-07-13)

> After Stage-1 onboarding (I2 104→35), the remaining I2 gap is **35 spans = 33 term-present-no-record + 2 deferred**. Stage 2 was meant to be a mechanical "build the missing verse-records via `audit_word --registry`". It is **not** — the 33 spans are only **4 terms, and every one has a registry-home / gloss / duplication defect**. Building records via `audit_word` on their current registries would **propagate wrong associations**. Filed for a homing decision before any write. No DB changes made in Stage 2.

## The 4 terms (33 spans)

| strong | translit / true sense | Proverbs use | spans | current `mti_terms` home | problem |
|---|---|---|--:|---|---|
| **H7307** | *ruach* — **spirit** | broken/haughty/hasty spirit; "rules his spirit" | 20 | reg 4 **anger** (`owning_word=None`) | mis-homed: *ruach* is the spirit/constitution word; re-auditing anger would attach **all ~370** *ruach* occurrences to anger |
| **H7999** | *shalam* — repay/complete/be-at-peace | "the LORD will repay him" | 9 | **7 duplicate rows**: reg 117 peace (vr=48), reg 34 covenant (vr=5), + 5 empty/null-FK | duplicate `mti_terms` (OT-DBR-009 class) — needs dedup to one home first |
| **H6424** | *palas* — **weigh / ponder / make level** | "ponder the path" (4:26); "weighs all his paths" (5:21) | 3 | reg 56 **envy** (glossed "to envy") | wrong gloss + wrong home (*peles* = balance/scales, not envy) |
| **H3001** | *yavesh* — **wither / dry up** | "a crushed spirit **dries up** the bones" (17:22) | 1 | reg 146 **shame** | questionable home (yavesh = dry, not bosh = ashamed) |

## Why not just run `audit_word`

`audit_word --registry=N` re-pulls a registry's terms and builds `MISSING_VERSE` records **for every occurrence of those Strong's, all books**. So:
- registry 4 (anger) → would register **all** *ruach* verses under anger (semantically wrong, mass mis-association);
- registries 56/146 → would cement the *palas*→envy / *yavesh*→shame mis-homes.

The homes must be **corrected first**, then `audit_word` builds records against the *right* registry. (Per the audit_word-only rule, record-building still goes through `audit_word` — we just fix the home before running it.)

## Decision needed — where should each term live?

1. **H7307 *ruach* (20 spans)** — which existing registry owns the **spirit** sense? Candidates: a `spirit` / `heart` / constitution-seat registry (Psalms used FLAG/M47 Constitution for seats). *ruach* in Proverbs is mostly the **inner disposition/temper** ("hasty of spirit", "rules his spirit"). Options: (a) re-home to a spirit/heart/constitution registry; (b) keep per-sense split (anger-sense stays, general-spirit sense re-homed). **My recommendation:** re-home *ruach* to the spirit/seat registry (or create the association there) — it is a constitutional seat, not "anger".
2. **H7999 *shalam* (9 spans)** — **dedup** the 7 rows to one owning home. The Proverbs sense is "**repay/requite**" (God repays). **My recommendation:** keep the `peace` home (id 414, vr=48) as canonical, delete-flag the empty duplicates, then build records there. (This is a Group-A mti-reconcile — the clean-add path excludes it, so it is a deliberate reconcile step.)
3. **H6424 *palas* (3 spans)** — fix gloss to "weigh/ponder"; re-home away from *envy*. Best-fit existing registry for **pondering/weighing one's way**: likely `walk` / `way` / a wisdom-adjacent registry. **Needs a pick.**
4. **H3001 *yavesh* (1 span)** — "dry up / wither"; the Proverbs use is *a crushed spirit dries the bones* — the **operation is the crushed spirit**, so *yavesh* may be a **qualifier**, not a standalone characteristic. **My recommendation:** likely drop as an independent candidate (it qualifies "crushed spirit"); confirm.

## The 2 Stage-1 deferrals (unchanged)
- **H7189** (Pro 22:21, *qoshet* = truth) — mis-tagged to `worship`; re-home (truth/faithfulness) or drop.
- **H3856** (Pro 26:18) — ambiguous sub-entry + soft `despair` pick + borderline IB.

## Proposed next step
Give the homing decisions (1–4 + the 2 deferrals). Then per term: fix the home/gloss (or dedup H7999) → `audit_word --registry=<corrected>` to build records → re-check I2 → **0** (or the confirmed drops). Then Stage 3 (v2 passage builder) → readiness READY → Stage 4 read.

*Filed 2026-07-13. Read-only analysis; no DB writes in Stage 2. Blocks I2-closure until the homes are decided.*
