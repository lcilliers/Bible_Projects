# #2381 — Fix affix and shared-span surfaces in verse_lexical: design (2026-11-07)

Input: the researcher's #2380 decision (options B and C): affix codes take their own gloss; the compound must be clear in `verse_lexical`; its construct must be easily derived downstream without pulling the main words into deep analysis when the primary words are used in matching; avoid option A (consumer filters). Analysis and counts: `outputs/escalation/2380-affix-surface-analysis-v1-20261107.md`. Nothing is built (B:105). Counts below are live from `iba.db` today; collection and surface-group content is model output and so inferential (B:4).

## 1. What was read (B:123)

- `span` (cfg_table use): one row per HTML span tag of a verse, source and immutable; a tag's codes are one unit as STEP presents them. `span.surface` "repeats across a word's codes".
- `verse_lexical` (cfg_table use): one row per Strong's code within a span; `surface` is "span.surface, denormalized", filled by `lexical.build`.
- Code: `iba/app/lib/lexical.py` `_layer1_fields` copies `span["surface"]` to every code; `span_code_surfaces` (the 28 Oct rule) overrides it only for non-particle codes whose exact gloss is the untagged word just before the span; the affix pattern is `discovery.particle_pattern` (`^[HG]9\d{3}$`).

## 2. Measured shape of the data (live, 378,166 live spans, 544,667 live rows)

| Span shape | Spans | Whose word is the surface? |
|---|---|---|
| one code | 259,243 | the code's own (250,123 content, 9,120 affix-only) |
| one content code + affixes | 83,419 (65,991 with 1 affix; 15,013 with 2; 2,415 with 3 or more) | the content code's; every affix row carries it wrongly |
| affix codes only (2 or more) | 1,459 | the unit's (an affix cluster such as H9006 (from) + H9013 (emphasis)) |
| two or more content codes (with or without affixes) | 34,045 | not derivable from STEP: the word belongs to one of them or to the unit |

Affix rows in shared spans: 131,024 over 43 affix codes. The largest are H9002 (and) 24,033, H9009 (the) 23,149, H9005 (to/for) 19,388, H9003 (in/on/with) 14,296, H9023 (his) 6,576. Seven affix codes have a bracketed STEP gloss (H9009 [the], H9011 [to], H9010 [the], H9008 [?], H9012 and H9013 [emph.?], H9014 [-]): 26,507 rows. A bracketed gloss means STEP shows no English word for that code.

Reach (rows that change or that read this column):
- 24 live source files read `verse_lexical` and mention `surface` (list in section 7); `iba/app/lib/surfacemap.py` and `iba/app/lib/surfacestructure.py` are the surface cycle itself.
- `ib_node` holds 69 rows with an affix strong (68 linked to a `verse_lexical` row). `reading_strand_hit`: 0 affix rows. `surface_subgroup`: 0 affix pairs (checked earlier).
- 28 existing `surface_term` surfaces equal an affix gloss word (and, for, his, the, ...). An affix row given its own gloss would join those terms; whether any collection holds one of them is not yet checked.
- Two real Greek content codes fall under the affix pattern (G9315 "to join in making an attack", G9577 "a vestige"; 2 live rows): the pattern `^[HG]9\d{3}$` is too wide for Greek. Noted for this build.

## 3. Design

### 3.1 Schema: what `verse_lexical` records (new columns, each registered in `cfg_column`)

| Column | Holds | Why |
|---|---|---|
| `surface` (existing, meaning changed) | the English that belongs to THIS code: its own word where known, its own STEP gloss for an affix code; NULL where STEP shows none | matching on `surface` is correct again without a filter (option C) |
| `unit_surface` (new) | the span's whole word, as `span.surface` (what `surface` holds today) | the compound and its word stay readable on every row (option B) |
| `surface_kind` (new, enum) | `own` (the code's own word in the verse), `gloss` (the code's own STEP gloss), `marker` (bracketed gloss: no English word; `surface` NULL), `unit` (shared: the span's word, owner not determined) | one value tells a consumer how far to trust `surface` |
| `unit_size` (new) | number of codes in the span | 1 = not a compound |
| `unit_role` (new, enum) | `sole`, `head`, `affix`, `co_content` | the construct of a compound is read from role, with `code_ordinal` for order |

The compound's construct is derived with one join on `span_id`, ordered by `code_ordinal`: the head is the row with role `head`, affixes are the rows with role `affix`. A view `verse_lexical_unit` (one row per compound: head code, affix codes in order, unit word) would give downstream code a single source; a view is a new mechanism and is added by the procedure in `iba/app/GOVERNANCE.md`, not here.

Matching on the primary word never touches the affix: an affix row's `surface` is its own gloss (`and`, `to/for`) or NULL, so a collection or surface term for "children" matches only the head. The affix rows remain linkable to the head by `span_id`, so the compound ("and to the children") is derived, not stored twice.

### 3.2 Build (iba/app/lib/lexical.py)

1. `span_code_surfaces` is replaced by one rule set in `cfg_setting lexical.span_surface` (new keys, not code): affix code → own STEP gloss (`surface_kind=gloss`), bracketed gloss → NULL (`marker`), sole content code in the span → span word (`own`), the existing gloss-in-look-back match → that word (`own`), otherwise the span's word with `surface_kind=unit`.
2. `_layer1_fields`, `_CONTENT_FIELDS` and `write_readings_for_span` carry the new columns; writes stay identity-stable (a row keeps its `verse_lexical.id`; only changed content is updated), so `ib_node.verse_lexical_id` and `verse_lexical_note` stay valid.
3. `observationrecord.occurrence_surfaces` re-derives the rule by calling `span_code_surfaces`; after the fix it reads the columns instead, which removes a second copy of the rule.
4. The affix pattern is read from config as now; the Greek exception is a config change (a Greek pattern that excludes G9315 and G9577), through the Propose gate (bypassed in Developer Mode, recorded in `cfg_change_detail`).

### 3.3 Back-fill (no new corpus read, no STEP call)

Re-run `lexical.build` over the whole corpus (544,667 rows; every verse) after a database backup. It is a long job: per B:125 it starts through the Windows process service with a log under `Logs/`, not from this session. Counts of inserted, updated and unchanged rows are checked against the expectation in section 5.

### 3.4 Downstream repair, after the build

| Consumer | Effect | Action |
|---|---|---|
| `surface_term` (6,225 live rows; 3,526 of the 6,066 surface terms touch an affix row today) | affix rows leave the host word's term; 28 function-word terms gain their true affix rows | recompute term membership from `verse_lexical`; list terms whose membership changed; re-judge only changed terms (the judging runs on the local model, a cost to confirm) |
| collections (48 live) | members unchanged unless a member term lost its only evidence | recompute counts; report differences; no re-judging without your word |
| `ib_node` (69 affix rows) | node `surface` was the host's word | `noderesolve` re-points by `verse_lexical_id` and reports the 69 |
| `versescope`, `reading`, `priorcapture`, `recordingpass`, `strandreading`, `versecollate` | read `surface` for display and matching | review each use against `surface_kind`; adjust only where a use depends on the host's word at an affix row |
| reports (`handlers/reports.py`, `strongversereport.py`, `stage1coverage.py`, `Verse-Scope`, `StrongVerse-Report`) | display | show `unit_surface` where a verse is printed, `surface` where the code is |

## 4. Decisions for the researcher (the design's open points)

D1. **Scope of content codes.** Affix codes are settled (own gloss, your #2380 answer). What of content codes that share a span with another content code (34,045 spans; 70,981 rows)?
- (a) Affix codes only now. Content codes keep the span's word, marked `unit` only where the span has two or more content codes.
- (b) Affix codes, plus a closed list of function-word content codes given their own gloss (examples seen: H3588A (for/that), H0413 (to/toward), H0853 (object marker), H5921A (upon), G1519 (into)). Needs your list or a rule for what counts as function-word.
- (c) Affix codes, plus the existing look-back match widened to the whole span, the rest marked `unit`.
Recommendation (inferential): (a), then (c) as a second stage with its own count of changed rows, because a marked `unit` row is honest now and the true owner of the word cannot be derived from STEP.

D2. **Bracketed glosses** (26,507 rows; H9009 (the) is 23,149 of them). (a) NULL surface, kind `marker` (recommended: no English word exists in the verse, and a surface term "[the]" over 23,000 rows would be a meaningless term); (b) keep the bracket text as the surface.

D3. **Affix cluster spans** (1,459 spans of affix codes only; the single-affix spans stay `own`). Give each code its own gloss and role `affix`, with no head (`unit_role=affix` and no `head` row). Say if you would rather a head be named.

D4. **Name of the column that keeps the whole word:** `unit_surface` (recommended) or another.

D5. **Downstream re-judging.** After the build, re-judge only the surface terms whose membership changed (recommended), or re-run the surface cycle in full.

## 5. Verification plan (module test plan, `governance.module_utility_test_plan`)

Run after the build and recorded in the escalation:
1. Before and after counts per `surface_kind` and `unit_role`: sole + head + affix + co_content = 544,667; affix rows in shared spans = 131,024 (checked live today).
2. Row identity: the number of `verse_lexical.id` values before and after is equal; 0 rows soft-deleted that were live and unchanged in code.
3. For every affix row in a shared span, `surface` ≠ the head's word unless the head's gloss is that word; `unit_surface` = `span.surface` on every row.
4. The 69 affix `ib_node` rows re-point; 0 `ib_node` rows lose a `verse_lexical_id`.
5. The #2379 CSV rebuilt: 0 affix strongs in a collection's evidence rows other than through their own gloss.
6. Cases from your examples: H9005 in Isa 32:6 and Job 21:19, H2519 in Jer 23:12, the Gen 43:27 span (H2416A, H5750, H9043, H9008) by hand against STEP.
7. Parameter and option combinations: each rule key in `lexical.span_surface` on and off, on a fixture verse set; rerun gives 0 changed rows (idempotent).

## 6. Not yet established

- Whether any step other than the surface cycle depends on the host's word at an affix row (section 3.4 lists the readers; I have not traced each line).
- Whether any collection holds one of the 28 function-word surfaces.
- The order in which STEP lists a span's codes (examples show affixes before and after the content code), so role is set from the code, not from position.
- Whether the post-rebuild data-quality check carried forward from #1706 exists.
- The run time of a full `lexical.build`.

## 7. Files that read `verse_lexical.surface` (live source, not archive, not temp tests)

`iba/app/handlers/raw.py`, `handlers/reports.py`, `lib/charreadinggenerate.py`, `lib/lexical.py`, `lib/noderesolve.py`, `lib/observationrecord.py`, `lib/passagedebatereport.py`, `lib/priorcapture.py`, `lib/reading.py`, `lib/recordingpass.py`, `lib/stage1coverage.py`, `lib/strandreading.py`, `lib/strongreconcile.py`, `lib/strongversereport.py`, `lib/subgroupgenerate.py`, `lib/surfacemap.py`, `lib/surfacestructure.py`, `lib/versecollate.py`, `lib/versereadinggenerate.py`, `lib/versescope.py`, `ps/Debate-Run.ps1`, `ps/StrongVerse-Report.ps1`, `ps/Verse-Scope.ps1`, `ps/VerseLexical.ps1`.

## 8. Documentation owed with the build

`iba/app/BUILD.md` (new section), `iba/app/GOVERNANCE.md` only if a new kind of config table or check is added, `iba/app/USER-GUIDE.md` (VerseLexical.ps1 meaning of the columns), the PS worksheet if a parameter changes (`governance.ps_worksheet_sync_on_change`), cfg_table/cfg_column rows for every new column.
