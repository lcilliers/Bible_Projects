# wa-vcb-031-schema-instruction-v1.0-2026-04-08

**For:** Claude Code
**Batch:** VCB-031 | **Registry:** 213 — listen
**Date:** 2026-04-08

---

## Action required BEFORE applying PATCH-20260408-VCB031-VERSECONTEXT-V1.json

The patch introduces two new fields not yet in the schema. Apply these ALTER TABLE statements before running the patch applicator.

```sql
ALTER TABLE verse_context_group ADD COLUMN vertical_pass_flag INTEGER DEFAULT 0;
ALTER TABLE verse_context ADD COLUMN vertical_pass_flag INTEGER DEFAULT 0;
ALTER TABLE verse_context ADD COLUMN set_aside_reason TEXT DEFAULT NULL;
```

## Field definitions

**`vertical_pass_flag` (INTEGER, DEFAULT 0)**
Present on both `verse_context_group` and `verse_context`.
Tracks whether the record has been through a vertical pass analysis session.
- 0 = not yet analysed
- 1 = vertical pass complete

Set to 0 by this patch for all new records. Updated to 1 by Claude Code when vertical pass analysis is applied.

**`set_aside_reason` (TEXT, DEFAULT NULL)**
Present on `verse_context` only.
Controlled vocabulary for why a verse was set aside (is_relevant=0).
NULL on all relevant verses.

Valid values:
- `no_inner_being` — genuinely no inner-being content through this term
- `wrong_face` — inner-being content present but carried by another term; rediscover from that face
- `divine_subject` — inner-being content present but subject is divine not human
- `avf_homograph` — term is a lexical artefact or homograph with no connection to this registry
- `pending_revision` — set aside under current model; flag for review

## Post-schema post-patch checks

After applying the ALTER statements and the patch:

1. Confirm all three fields exist: `SELECT vertical_pass_flag, set_aside_reason FROM verse_context LIMIT 1;`
2. Confirm verse_context_group has vertical_pass_flag: `SELECT vertical_pass_flag FROM verse_context_group LIMIT 1;`
3. Run standard VCB integrity checks (R1–R4) for Registry 213
4. Confirm verse_context_status = Complete for Registry 213
5. Report count breakdown: relevant / set_aside / by set_aside_reason

Expected counts:
- verse_context_group records: 49
- verse_context records (total): 748
- is_relevant=1: 477
- is_relevant=0: 271
- set_aside_reason = no_inner_being: ~200
- set_aside_reason = wrong_face: ~40
- set_aside_reason = divine_subject: ~25
- set_aside_reason = avf_homograph: 1 (H0240)
