# wa-vcb-022-patch-handoff-v1-20260404
**Purpose:** Transfer brief for VCB-022 patch construction session
**Date:** 2026-04-04 | **Batch:** VCB-022 | **Status:** Classification complete, flags resolved, ready for patch

---

## What this session must produce

One VERSECONTEXT patch file: `wa-vcb-022-patch-v1-20260404.json`

Following the structure and rules in WA-VerseContext-Instruction-v2.4 §§7–7.6.

---

## Input files required

1. **`wa-vcb-022-extract-20260404.json`** — batch extract (verse_record_ids, mti_term_ids, all verse data)
2. **`wa-vcb-022-term-observations-v2.8-20260404.md`** — authoritative classification record (v2.8, includes flag decisions)
3. **`WA-VerseContext-Instruction-v2.4-20260403.md`** — governing instruction (load §§7–7.6 only for patch session)

The decided flags register is embedded in the observations file v2.8 under `## FLAG RESOLUTION DECISIONS`.

---

## Confirmed batch classification (post flag resolution)

| Metric | Value |
|---|---|
| Terms | 120 |
| Verses | 2,470 |
| Relevant (verse_context inserts needed) | 1,438 |
| Set aside (verse_context inserts needed) | 1,032 |
| Total verse_context rows to insert | 2,470 |
| Groups to insert | 159 |
| Anchors | 275 |
| AVF terms — no group, no relevant inserts | 14 |

---

## AVF terms — confirmed (14 terms, no group_insert, no relevant verse_context)

These terms still require verse_context insert rows for each verse — all with `is_relevant=0, group_id=NULL`:

| mti | Strong's | Gloss | Verse count |
|---|---|---|---|
| 7110 | H2636 | chas.pas: to peel | 1 |
| 6964 | H3581A | ko.ach: reptile | 1 |
| 6905 | H4026G | Hananel Tower | 3 |
| 6909 | H4026H | Tower of Hundred | 1 |
| 6910 | H4026I | Tower of Ovens | 1 |
| 6897 | H5313 | niph.qa: cost | 2 |
| 7114 | H5958 | e.lem: youth | 2 |
| 6997 | H6971 | qoph: ape | 2 |
| 6995 | H7054 | qa.mah: standing grain | 8 |
| 6945 | H8651 | te.ra: door | 2 |
| 6946 | H8652 | ta.ra: doorkeeper | 1 |
| 7118 | H1831 | de.ma: juice | 1 |
| 7119 | H1833 | de.me.sheq: silk | 1 |
| 7187 | G3839 | pantē: always | 1 |

**Total AVF set-aside rows:** 27 (all is_relevant=0, group_id=NULL)

---

## Terms requiring careful programmatic validation before patch

These three terms have large verse sets with complex group assignments verified by pattern-matching during classification. Pre-submission validation (§7.6) is especially important for them:

### H1288 ba.rakh (mti=1299) — 249 verses
- 247 relevant (4 groups), 2 set aside (kneeling sense: vid=51016, vid=226205)
- Groups: 1299-001 (God blesses ~91 verses), 1299-002 (bless God ~50 verses), 1299-003 (human-to-human ~98 verses), 1299-004 (ironic/euphemistic ~8 verses)
- **Action:** Build complete vid→group dictionary from observations file §R194; verify total = 247 relevant + 2 set aside = 249

### H3966 me.od (mti=654) — 220 verses
- 93 relevant (6 groups), 127 set aside
- Groups: 654-001 (love/devotion 11v), 654-002 (fear/dread 18v), 654-003 (anger 14v), 654-004 (grief/distress 22v), 654-005 (praise/joy 13v), 654-006 (moral gravity 15v)
- **Action:** Verify all 93 relevant vids are assigned; verify 127 set-aside vids

### H4725 ma.qom (mti=6989) — 295 verses
- 34 relevant (4 groups), 261 set aside (88% rate)
- Groups: 6989-001 (chosen place 16+v), 6989-002 (theophanic place 4+v), 6989-003 (moral conditions 7+v), 6989-004 (eschatological joy 3+v)
- **Action:** Verify all 261 set-aside vids are accounted for

---

## Validation requirements (§7.6)

Before writing the patch file:

1. **Anchor reference verification** — every anchor vid listed in the observations file must be confirmed to exist in the extract JSON under the correct mti_term_id
2. **Duplicate key check** — no (verse_record_id, mti_term_id, group_id) combination appears twice
3. **Coverage check** — every verse_record_id in the extract appears exactly once across is_relevant=1 and is_relevant=0 rows for its term
4. **R1–R4 pre-check** — apply consistency rules before writing output

---

## Operation ordering (§7.4)

For each term, order operations:
1. verse_context_group inserts (new groups) — capture last_insert_rowid() for each
2. verse_context_group updates (none in this batch — all groups are new)
3. verse_context inserts — anchors first, then related, then set-aside
4. verse_context updates (none in this batch)

Across terms: process in batch JSON order (registry ascending, then JSON order within registry).

---

## Patch metadata

```json
{
  "_patch_meta": {
    "patch_id": "PATCH-20260404-VCB022-VERSECONTEXT-V1",
    "batch_id": "VCB-022",
    "produced_date": "2026-04-04",
    "produced_by": "WA-VerseContext-Instruction-v2.4-20260403",
    "session_b_status": null,
    "description": "Verse context classification — batch VCB-022, 120 terms, 2470 verses, registries 187-196 (excl. 195)"
  }
}
```

Expected _patch_summary values:
- total_operations: 2,470 verse_context inserts + 159 group inserts + any group updates = ~2,629
- group_inserts: 159
- verse_context_inserts: 2,470
- relevant_verses: 1,438
- set_aside_verses: 1,032
- anchor_verses: 275
- dual_context_verses: 0
- revisions_to_prior: 0

---

## No Session B flags

No Session B flags were raised during this batch. No sessionB-flags document is required.

