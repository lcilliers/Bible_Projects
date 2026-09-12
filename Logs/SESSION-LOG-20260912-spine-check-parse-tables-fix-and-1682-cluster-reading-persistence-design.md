# Session Log — 2026-09-12 — Spine-check parse-tables fix, then escalation #1682's cluster-reading persistence design (family/observation/node/load-pass)

**Scope, one line:** root-caused and fixed a spine-check FATAL false-positive (a header-abbreviation
collision against the already-retired parse tables), synced the config layer to match; then spent
the bulk of the session on escalation #1682 — designing the durable, queryable home for the M10
cluster-reading output (family/observation/node tables plus the LLM-session/table-update-procedure
split), through several rounds of the researcher's own naming and architecture corrections, landing
on 4 focused component-design escalations (#1690–#1693) that remain open into tomorrow.

---

## Escalations touched, in order

| # | Short description | Outcome this session |
|---|---|---|
| #1681 | Spine check found 1 FATAL finding(s) | Root cause traced via git history (a header-abbreviation collision — `"part"`=particle vs H1506's own real gloss `"part"` — during the 2026-09-10 `lexicon.parse` rerun). Fix applied and verified (0 FATAL). `completed`/`approved`. |
| #1684 | Duplicate of #1681 (second spine-check pause, same root cause) | Same resolution as #1681. `completed`/`approved`. |
| #1685 | `configmaint.propose` crashed: `-Title` 77 chars, over the 60-char limit | My own input error — resolved self-correctable, retried with a compliant title same turn. `completed`. |
| #1686 | Retire `spine-extended-meaning-parse-completeness-fatal` rule | `cfg_method_rule` id=65 set `active=0`, superseded text with provenance. Applied live, `completed`. |
| #1687 | Update `spine.check` `cfg_step` doc text | Applied live, `completed`. |
| #1688 | Drop "discoverability" from `spine.check` report title | Applied live, `completed`. |
| #1689 | Mark `spine.check` discoverability report section inactive | Applied live, `completed`. |
| #1682 | Verse-meaning-family synthesis: read/output process design | Parent thread for everything below — updated v9→v13 this session: naming resolved (`ib_observation`/`ib_node`), the `cluster_subgroup` collision with #1683 surfaced and reasoned through, split into #1690–#1693. Still `in-progress`/`review`, fully `decision_required` — nothing applied to any database. |
| #1683 | M10's 32 legacy characteristic rows vs Window 2 | Investigated twice this session: (1) a concrete family-vs-legacy-subgroup comparison (no clean overlap anywhere); (2) a hard-delete feasibility check (confirmed troublesome — 9 tables, ~14,500 rows, collides with the project's no-physical-delete convention). Researcher decided: rename, don't delete — `zz_legacy_` prefix, corpus-wide scope, **`finding`/`verse_context` renamed WHOLESALE** (458,096 / 55,775 rows, not just the M10-linked slice), `prose_section` stays live (accepted broken references). Confirmed live: `finding` has no FK dependency on `iba.db` anywhere. Still `re-assigned`/`review`, nothing executed yet. |
| #1690 | Design: cluster-reading family table | Raised, then reframed entirely once family reverted to reusing `cluster_subgroup`/`mti_term_subgroup` rather than a new table. Column-by-column design filed, two real constraint changes identified (`label` NOT NULL gap in process (b)'s output; `mti_term_subgroup` uniqueness tightened to one-strong-one-family). FLAG-signposting mechanism proposed, not yet confirmed. Still `re-assigned`/`review`. |
| #1691 | Design: cluster-reading observation table | Raised, then substantially revised twice: naming (`ib_observation`), the LLM-session/table-update-procedure rule split (researcher's own annotations), JSON input/output specs per stage (including a new re-run requirement), a `source_json_serial` column, `stable_key` redefinition, and a data-driven start on the `tag`/`window` exploration the researcher asked for. Researcher explicitly said they are not yet finished with this one — still `in-progress`/`review`, several items intentionally left open pending their own further thought. |
| #1692 | Design: cluster-reading trace table | Raised; renamed `ib_node`; carries a real, still-unresolved defect (three genuinely distinct same-verse/same-surface/same-morph occurrences would be wrongly collapsed by the originally-proposed uniqueness constraint). Still `in-progress`/`review`. |
| #1693 | Design: cluster-reading load/reconcile pass | Raised as a 4th component (not one of the researcher's original 3) once the two-pass architecture (LLM session vs. table-update procedure) became explicit. Now the place where #1690/#1691/#1692's separate "table-update" responsibilities converge into one operational spec. Its own core problem — the same/broaden/new matching logic — remains completely undesigned, the single largest gap across all four escalations. Still `in-progress`/`review`. |
| #1694 | 37 M-codes in `cluster_strong` have no `cluster` table row | Raised as a secondary finding while investigating #1683 (checking where 19 "legacy-only" M10 strongs had actually moved to). `raised`/`review`, untouched since, awaiting the researcher. |

---

## Files created or changed

**Spine-check fix:**
- `iba/app/handlers/spine.py` — removed the entire strong→extended-meaning→parse FATAL check and its discoverability pass (both read the retired `strong_meaning_parsed`/`strong_lsj_parsed`/`strong_mounce_parsed` tables); `spine.check` is now verse/span/strong-sync only.
- `iba/app/ps/Spine-Check.ps1` — synopsis updated to match.
- `iba/app/BUILD.md` — entry #263, full root-cause + fix record.
- `cfg_method_rule` id=65, `cfg_step` (spine.check), `cfg_report` (spine.check title), `cfg_report_section` (spine.check discoverability row) — all updated live via `Config-Maintenance.ps1 -Step Propose`, approved by the researcher.

**#1682 and the 4 component designs (all new this session):**
- `iba/docs/1682-cluster-reading-data-model-v1-20260911.md` — edited in place across the whole session; now the shared reference the other 4 docs cite back to.
- `iba/docs/1690-cluster-subgroup-family-columns-v1-20260912.md`
- `iba/docs/1691-ib-obs-finalization-v1-20260912.md`
- `iba/docs/1692-ib-node-finalization-v1-20260912.md`
- `iba/docs/1693-table-update-procedure-finalization-v1-20260912.md`
- `outputs/markdown/1682-m10-family-vs-legacy-subgroup-comparison-v1-20260912.md` — the concrete family/legacy-subgroup comparison.
- `outputs/markdown/1683-m10-legacy-data-hard-delete-scope-v1-20260912.md` — the hard-delete blast-radius investigation.

**Memory:**
- `feedback_use_descriptive_nomenclature_not_invented_codes.md` (new) — the researcher's correction against inventing short/coded labels (e.g. `stable_key` for the JSON's own `synthesis_id`); indexed in `MEMORY.md`.

**Not git-tracked, recorded for completeness:** the `cfg_*` DB rows listed above (spine-check config sync) — no schema/data changes yet for the #1682 cluster-reading persistence work itself; everything there is still design-stage, nothing built.

**Other files in this session's full working-tree diff** (routine tool output, not authored deliverables): `outputs/configs/CONFIG-REPORT*.md` (regenerated automatically on every `configmaint.propose`), `outputs/escalation/*.md` and `research/discovery/spine-check*.md` (regenerated by `Escalation.ps1 -Action List/History` and `Spine-Check.ps1` runs), plus `Workflow/Chat_responses/Cluster-read naming conventions` (the researcher's own longer-note file, read in full and acted on) and three `scripts/SQLite/IBA_DB/*.sqlite3-query` scratch-query edits (the researcher's own IDE-extension query files).

---

## Decisions made

**Researcher's own decisions:**
- Spine check must exclude the parse tables entirely — they are retired/no longer maintained.
- Approved all 4 config changes (#1686–#1689) directly.
- Confirmed, testing the escalation tool's own refusal live: `decision_required` items require the Researcher's own approval regardless of self-assignment (D25 alone doesn't cover it) — corrected my initial attempt to self-close #1681/#1684.
- The entire findings database stays in `bible_research.db` (research_db); the old `finding`/`cluster_finding`/`characteristic`/`cluster_subgroup` data is not worth reconciling with — reproduce, don't fix.
- Family reverts to the *existing* `cluster_subgroup`/`mti_term_subgroup` tables — no competing new term.
- Hard-delete confirmed troublesome → **rename instead**: `zz_legacy_` prefix, corpus-wide scope; `finding`/`verse_context` renamed **wholesale** (not just their M10-linked rows); `prose_section` stays current, accepting that references from it into the renamed tables will break.
- Full naming pass on the new schema: `tag` (not `kind`), `verse_reference`, `surface`/`morph_code`, `window` (not `slant_label`), `obs_text` (not `statement`), `FLAG` (not `SUNDRY`), and finally `ib_observation`/`ib_node`/`cluster_subgroup` as the settled table names.
- No edit-history table for observations — "overkill," not expecting a large volume of edits.
- `stable_key` redefined as the link to the generating JSON file (its filename).
- Staging rule: each of (b)/(c)/(d)/(e) is a separate, independently re-runnable routine, each depending on the prior stage's JSON.
- Deduplication and editable-in-place-vs-new are table-update-procedure responsibilities, never the LLM session's — the LLM only assigns its own local per-JSON serial number and records its supporting node segments.
- `tag` must be `cfg_enum`-governed (closed), needs real data analysis before the answer/synthesis-stage values are settled — explicitly wants more exploration, not a proposal from this session.
- File naming convention must live in `cfg_setting`; `_analytics/Clusters/` should have per-cluster subfolders.
- Instruction to keep every substantive decision/finding recorded in the escalation table itself, not left in chat only — acted on mid-session (found and fixed one real gap, the finding/verse_context confirmation missing from #1683).

**Claude judgment calls, filed as open questions (not resolved unilaterally):**
- FLAG-signposting mechanism (a subgroup under the *same* cluster being read, not a placement under the separate `FLAG` cluster) — stated as a reading, not yet confirmed.
- Whether append-only for `synthesis`-stage rows needs mechanical (trigger) enforcement or is discipline-only.
- Whether `ib_node`'s denormalized field list is complete (e.g. verse text).
- Polymorphic single-table vs. two-table design for `ib_node`.
- `stable_key`'s scope (every stage, or `synthesis` only) now that its definition changed.
- The two items the researcher's own notes left genuinely unfinished — a truncated rule ("search for a similar observation before creating new - if...") and the "synergy stage" input JSON/concept itself — both explicitly left open rather than guessed at.
- The (c)/(d)/(e) separate-vs-merged-JSON question — gave a recommendation (keep separate) with reasoning, not decided.

**Claude fixes, closed directly (self-correctable):**
- The `-Title` 77-character crash (#1685) — retried with a compliant title same turn.
- The escalation-assignment bug on #1681/#1684 (left `assigned_to=Claude` after moving them to `ready_for_approval` — should have been `Researcher`) — caught when the researcher pointed it out, corrected immediately.

---

## Open items carried into next session

1. **Researcher is mid-work on #1691 themselves** — explicitly said "not yet done," a truncated rule in their own notes still needs finishing. Do not nudge; wait.
2. **FLAG-signposting mechanism** (#1690/#1693) — needs the researcher's confirmation or correction.
3. **`tag`/`window` taxonomies for `answer`/`synthesis` stages** — real data pulled as a starting point (§5/§6 of #1691's doc), but the researcher wants their own further data analysis before settling either.
4. **The "synergy stage" concept and its input JSON** — the researcher's own words: "not yet fully defined," and separately, in chat: "not yet clear in my head." A genuinely open conceptual question, not a build task.
5. **Append-only enforcement mechanism** (DB trigger vs. procedure-only discipline) for `ib_observation` `synthesis`-stage rows — undecided.
6. **`ib_node`'s uniqueness/`seq` defect** — still blocking; needs `iba.db.span.position` (or similar) brought into the design before this table is safe to build.
7. **The same/broaden/new matching-logic algorithm (#1693)** — the single largest remaining piece of undesigned work across all four escalations; nothing here yet beyond naming the open questions.
8. **#1683's rename plan is agreed but not executed** — no table has actually been renamed, no fresh `cluster_subgroup`/`mti_term_subgroup`/`characteristic`/`characteristic_subgroup` tables created yet.
9. **#1694** (37 unregistered M-codes in `cluster_strong`) — raised, awaiting the researcher's own review; unrelated to the #1682 thread beyond having surfaced during the same investigation.
10. Nothing from this session's design work has been built — no migration run, no `cfg_table`/`cfg_column` registration, no data moved. All 4 component escalations (#1690–#1693) remain fully `decision_required`.

---

## Git state

Session log written; commit and push to follow in the same unit of work per the standing
pre-authorization (CLAUDE.md §12). See the commit this log ships with for the confirmed hash and
`git status` result.
