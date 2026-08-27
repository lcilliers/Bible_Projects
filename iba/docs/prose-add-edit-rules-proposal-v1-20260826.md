# Prose add/edit operational rules + flag-fix angle (b) + D10 — proposal v1

**Escalation #890.** Raised fresh after #829/#831/#832/#835 were rejected (superseded) as
unreadable from their own history. **Grounded in two documents, not in the rejected threads:**
`iba/app/reports/prose-management-current-state-20260826.md` (live state check, 2026-08-26) and
`iba/docs/prose-management-784-conversation-capture-v1-20260823.md` (the original design
conversation, sections 1/6/7/13/15). Everything below was checked live against `iba.db`/
`bible_research.db` this round, not carried forward from any prior document. One self-contained
document — the "v1–v8 can't be read standalone" problem that #829 hit is deliberately avoided here
by covering all six items in one place, with all six decisions listed once, in §7.

**What #829 already built** (confirmed live in the clean-state check): dispatcher registration,
write-layer governance, `cfg_prose`, and `prose.flag` (angle a of the flag mechanism). This
proposal does **not** revisit any of that — it starts from the specific items the clean-state check
found were never actually designed.

---

## 1. Three creation modes — operational process

`iba/docs/prose-management-784-conversation-capture-v1-20260823.md` §1 named three ways a
`prose_section` row comes into being, with no operational process ever described for any of them.
`apply_session_patch.py` already has the mechanics (6 `prose_section` write ops, granted and
governed since #829) — what's missing is the *process around* invoking them, not the invocation
itself.

**(a) Authoring from scratch** — Claude (`claude_ai`/`claude_code`) drafts new prose under an
*existing* `prose_section_type`. This is routine authoring: insert with `status='draft'`, ordinary
review → `approved` flow (`cfg_status_flow`, already built). **No new gate needed** — this is
exactly what the 6 write ops + status flow already govern.

**(b) Converting another document** (a session log, a research doc, a prior Markdown file) into
formal prose. Same mechanics as (a), but with a traceability gap: nothing currently records *what
it was converted from*. `prose_section.metadata_json` (free-form JSON, already live) is the
existing field for exactly this. **Recommendation:** when a section originates by conversion,
`metadata_json` must carry `{"source_document": "<path>", "conversion_date": "<iso>"}` — a
convention, not a schema change.

**(c) Capturing from analytic findings** — the eventual link between the `finding` table (the
project's live analytical-findings store, ~340k rows) and prose. This is where the real structural
gap sits: `prose_section_finding_link` exists (0 rows) but its FK targets the legacy
`wa_session_b_findings`, not the live `finding` table (this is old #832's D3, correctly deferred
there and inherited here). **Recommendation, matching the researcher's own framing at §7 of the
784 doc** ("prose hasn't been seriously populated yet... heading toward the analytics phase next"):
mode (c) is **not operationally different from mode (a) today** — Claude drafts prose that discusses
findings, same insert/review/approve path, just without a structural link populated. Rebuilding
`prose_section_finding_link`'s FK is real work, but it has no urgency until the `Findings` book
actually has content to link (3 types, `book_label IS NULL`, essentially unpopulated per the
clean-state check) — recommend leaving D3 exactly where old #832 already put it, not re-opening it
here.

## 2. The two-patch creation trigger — who/when authorises a *new* `prose_section_type`

`cfg_behaviour_rule` `prose-section-two-patch-ordering` (built by #829) governs the *order*
(`CATALOGUE_POPULATION` before `PROSE`) but not *who may create a new type at all*.
`prose_section_type` is a controlled vocabulary — its own `cfg_table.use` text says it is *"the
only real enforcement behind `prose_section.section_type_id`"* — and the project already treats
controlled-vocabulary tables (`cfg_enum`, `word_registry.cluster_assignment`, etc.) as
researcher-gated, not something Claude adds to unprompted.

**Recommendation:** a new `cfg_behaviour_rule` (class=`sqlite`) —
*"A new `prose_section_type` row may only be inserted on explicit researcher instruction naming the
new code and its `book_label`/`source_stage` placement — it is controlled vocabulary, not
Claude-originated content, the same standard already applied to `cfg_enum` and other project-wide
controlled-vocabulary tables."* This is a policy statement made queryable, not new code — the
existing `CATALOGUE_POPULATION`/`PROSE` two-patch mechanism is unchanged; this just states who may
trigger the first half of it.

## 3. Delete-behaviour — a section vanishing from an edit file

`iba/docs/prose-management-784-conversation-capture-v1-20260823.md` §6 tested all three edit-file
edge cases live: **add** and **move** both refuse outright, loudly, safely. **Delete is the one
that fails silently** — the removed section's DB row is left completely untouched, no error, no
trace.

Three options, as originally framed:

| Option | Behaviour | Consistency with add/move |
|---|---|---|
| Refuse | Import fails outright, same as add/move — *"section N present in DB but missing from file"* | Matches exactly |
| Warn | Import proceeds, logs/flags the omission | Inconsistent — the only one of three that doesn't fail loudly |
| Retire | Import proceeds and archives the missing row (treats absence as an instruction to retire) | Riskiest — content removal triggered by *omission*, no explicit instruction anywhere in the file |

**Recommendation: refuse**, for the same reason add and move already refuse — an edit file is a
round-trip artefact (export → edit → import), not an authoring surface for structural changes
(create/delete/reorder all go through the separate two-patch/dedicated-operation path already, per
§6's own confirmed findings). A missing section is far more likely to be an accidental deletion
while editing than a deliberate retire instruction, and the existing tool has no path to *originate*
a section either (also refused) — deleting one should be symmetric with that, not the odd one out.
If a section is genuinely meant to retire, that becomes its own explicit patch operation (already
possible — `prose_section` has no dedicated "retire" op today, but `status='archived'` is a valid,
already-governed state), not a side-effect of silence in an edit file.

## 4. `prose_section_verse_link` — the verse-grounding gap

Named at §13 of the 784 doc as **the genuine drift risk**, distinct from (and more urgent than) the
citation-column-relocation-to-Concordance items (`registry_id`/`cluster_code`/`characteristic_id`/
`cluster_subgroup_id`) that old #832 correctly deferred to a not-yet-scoped future book. This one
sits directly on `governance.prose_canonical_authority`'s own `verse_primacy` concept — the
researcher's framing: *"the citation principle and the table design is there, the fact that it has
not been enforced is part of the issue of consistency and repeatability."*

**Live constraint found this round:** there is no single "one row per verse" table inside
`bible_research.db` to FK against — `verse_context`/`wa_verse_records` are both keyed
`(reference, term)`, not `(verse)` alone, and the canonical verse table now lives in `iba.db`
(`governance.scope_iba_db`), which SQLite cannot FK across from `bible_research.db`. This is the
**same constraint already accepted** for `wa_data_quality_flags.strong_id`/`.verse_id` (loose,
documented-only references, no enforced FK — noted in that table's own `cfg_column.use` text).

**Recommendation — same shape, applied consistently:**

```sql
CREATE TABLE prose_section_verse_link (
    prose_section_id INTEGER NOT NULL REFERENCES prose_section(id),
    verse_reference   TEXT NOT NULL,   -- e.g. "Ps 32:1", matching wa_verse_records.reference format
    link_type         TEXT NOT NULL DEFAULT 'discusses',
    created_at        TEXT NOT NULL DEFAULT (datetime('now')),
    PRIMARY KEY (prose_section_id, verse_reference, link_type)
);
```

Same shape/precedent as the already-declared `prose_section_finding_link`/`_dimension_link`
(composite PK, `link_type` default `'discusses'`), loose `verse_reference` instead of an FK (matches
`wa_verse_records.reference`'s existing string format, "1Ch 10:1"-style, not a cross-DB FK). Written
by the ordinary `prose_section` write path (insert/supersede already route through
`record_change_log`'s choke-point per #836) — a new, small `apply_session_patch.py` operation
(`prose_section_verse_link insert`) is needed, or citations could be extracted from `body` text at
write time; **recommend explicit citation** (a patch-supplied list, not text-mined) — text-mining
free-form citations reliably is its own hard problem and would silently under- or over-link.

## 5. Flag-fix workflow angle (b) — propose → approve → apply

Design already captured at `iba/docs/prose-management-iba-first-layer-proposal-v9-20260824.md`
§12.4, not built. `record_change_log.status` already has the `change_proposed`/`change_applied`/
`declined` vocabulary — checked live this round: **1,175 rows exist, every single one is
`change_applied`** — `change_proposed`/`declined` have never once been written. This confirms angle
(b) genuinely has zero implementation, not just an untested one.

**Process, as designed at #829 §12.4, restated concretely:**

1. **Propose** — given a `wa_data_quality_flags` row (angle a already raises these), search
   `prose_section.body` for the pattern the flag names (e.g. retired terminology). For each match,
   write a `record_change_log` row with `status='change_proposed'`, `target_table='prose_section'`,
   `target_id=<id>`, `payload` = the *proposed new text* (not the prior state — a deliberate,
   documented departure from `record-change-log-payload-is-prior-state`'s normal meaning, since
   nothing has changed yet; needs its own field-semantics note, not a silent exception).
2. **Approve** — researcher reviews the proposal set (a report, not a UI), approves/rejects per
   instance or as a batch — matches the escalation module's own `ready_for_approval → approved`
   handshake, reused rather than inventing a second approval vocabulary.
3. **Apply** — only after approval: write the approved text via `prose_section`'s ordinary
   supersede/update path (record-change-log-choke-pointed already), set the originating
   `record_change_log` row to `status='change_applied'`, and mark the flag `corrective_action`/
   `correction_date` on `wa_data_quality_flags`.

**New `cfg_step`:** `prose.flag_fix_propose` (search + write `change_proposed` rows),
`prose.flag_fix_apply` (write the approved change + close the flag) — both `kind='utility'`,
registered under the existing `prose` work package. No separate approval step needed in the
dispatcher — approval happens the same way every other `decision_required` item does, via
`Escalation.ps1`, not a bespoke mechanism.

## 6. D10 — `book_stage_map` vs. `book_label`, now that this is the prose-edit stage

Deferred 2026-08-24, verbatim: *"D10 will be edited in prose edit stage, not in this IBA processing
build."* This proposal *is* the prose-edit-stage design work — the deferral's own condition is now
true.

**Recommendation unchanged from v9's own analysis:** switch `prose.extract`'s book-filtering to
read `book_label` directly (already populated, already the more precise, per-row column) instead of
deriving book membership from `prose.book_stage_map`'s stage-list. This is a small code change in
`prosestore.py:book_stage_map()`/`extract_programme_prose()`, not a redesign — `cfg_prose`'s
`prose.book_stage_map` key would then either be dropped (if `book_label` alone is sufficient) or
kept only as the `--book` choice-list source (still useful for CLI validation) while the actual
filter switches to `book_label`. Affects exactly the 1 row named at #829 §0 (`prog_purp_
observations_framework`, id 78) — confirmed still the only disagreement, re-checked live this round
(no new `prose_section_type` rows added since).

---

## 7. Decisions needed (D1–D6)

| # | Decision | Recommendation | Researcher decision |
|---|---|---|---|
| **D1** | Mode (c) (capture-from-findings) — rebuild `prose_section_finding_link`'s FK now, or leave with mode (a)'s process until `Findings` book has content? | Leave as-is; not urgent (old #832's D3, unchanged) | — |
| **D2** | New `prose_section_type` rows — gate behind explicit researcher instruction (new `cfg_behaviour_rule`)? | Yes | — |
| **D3** | Edit-file delete behaviour — refuse / warn / retire? | Refuse (matches add/move) | — |
| **D4** | `prose_section_verse_link` — build now, with explicit-citation-list write op (not text-mined)? | Yes, build now | — |
| **D5** | Flag-fix angle (b) — build the propose/apply steps as designed at #829 §12.4 (§5 above)? | Yes | — |
| **D6** | D10 — switch `book_stage_map`-derived filtering to read `book_label` directly? | Yes | — |

## 8. Test plan (required up front, per `governance.module_utility_test_plan`)

| # | Case | Expected |
|---|---|---|
| 1 | Insert `prose_section_type` via patch, no prior researcher instruction on record | Refused (D2) |
| 2 | Insert `prose_section_type` per explicit researcher-named code | Succeeds |
| 3 | Export a chapter, delete one section block, re-import | Refused outright (D3), file left in place, DB row untouched |
| 4 | Export, edit 1 of N sections, re-import | Unchanged (already working) — 1 operation, file archived |
| 5 | `prose.verse_link` insert with explicit `verse_reference` list | Row(s) written, `record_change_log` entry present |
| 6 | `prose.flag_fix_propose` against a live `PROSE_QUALITY` flag with a matching term in ≥1 section body | `change_proposed` row(s) written, no `prose_section` write yet |
| 7 | `prose.flag_fix_apply` on an approved proposal | `prose_section` updated, `record_change_log` row → `change_applied`, flag's `corrective_action`/`correction_date` set |
| 8 | `prose.flag_fix_apply` attempted on a still-`change_proposed` (not approved) row | Refused |
| 9 | `prose.extract --book Programme` after D6 | Type id 78 now excluded from Programme, included in Detail design |
| 10 | `configmaint.validate` full run after all of the above | Clean |

## 9. Sequencing (once D1–D6 are answered)

1. `cfg_behaviour_rule` — new `prose_section_type`-creation gate (D2).
2. `prose_section_verse_link` table + `cfg_table`/`cfg_column`/`cfg_write_grant` rows (D4).
3. `apply_session_patch.py` — delete-behaviour refusal in `run_import_chapter` (D3, already has the
   refuse pattern for add/move to follow); new `prose_section_verse_link insert` op.
4. `prosestore.py`/`handlers/prose.py`/`Prose.ps1` — `prose.flag_fix_propose`/`.flag_fix_apply`
   steps (D5); `book_stage_map()`/`extract_programme_prose()` switched to `book_label` (D6).
5. `cfg_step` — register the 2 new steps under the `prose` work package.
6. Run the test plan (§8), results into the resolution on #890.
7. `GOVERNANCE.md`/`BUILD.md`/`USER-GUIDE.md` updates, same pattern as #829's own build record.

---

*Filed against escalation #890 — awaiting D1–D6 before build.*
