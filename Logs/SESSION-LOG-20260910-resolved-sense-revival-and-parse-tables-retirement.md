# Session Log — 2026-09-10 — resolved_sense revival, #1607 review round 1, lexicon.parse fixes, and retirement of the 3 parse tables

**Scope, one line:** cleared the Claude-held escalation backlog; revived `verse_lexical.resolved_sense`
from `strong_meaning_parsed` (ord=0); worked the first round of #1607's Layer 1/2 column decisions
and applied the no-judgement E1 batch; chased two real parse bugs the researcher found live (POS-tag
headers, a phantom-segment artifact) through to fixes; built a raw (unparsed) sibling view for
direct source-vs-parse comparison; prototyped an LLM contextual read as an alternative to mechanical
sense-picking, and — on the strength of that prototype's result — the researcher retired all 3
parse tables and called for the whole meaning-distillation method to be reconsidered, resuming
tomorrow.

---

## Escalations touched (22), by id, in order raised/first touched

| # | Short description | Outcome this session |
|---|---|---|
| #1659 | Register `create_vw_strong_gloss` script | Applied approved `cfg_utility` insert, verified, **completed** |
| #1661 | `verse_meta.status` column + PS routine | Built (`migration/add_verse_meta_status_column_v1_20260910.py`, `lib/versemeta.py`, `VerseMeta.ps1`), tested live, **ready_for_approval** |
| #1662 | 723 verses with null `text` | Root-caused (`raw.py` never wired to the derivation) and fixed (`lib/stepapi.py:preview_to_text`), backfilled, **ready_for_approval** |
| #1663 | `strong_meaning_parse` reconciliation (ord=1 vs ord=0) | Investigated, found `sort` is 0-indexed; superseded by the researcher's ord=0 decision; **completed** (approved directly) |
| #1664 | Register `apply_verse_plaintext_column` script | Proposed → approved → applied, **completed** |
| #1596 | `gloss_consistent_in_verse` stale flags | Investigated (already correct, keyed on `surface` since #1527 — flags were just stale, not wrong); closed on the researcher's ord=0/"retained" decision, **completed** |
| #1666–#1672 | E1 batch: `cfg_column.use` text fixes (`resolved_sense`, `is_negator`, `party_kind`, `note_type`, `target_verse_lexical_id`, `related_verse_lexical_ids`) | All 6 applied via individual `Config-Maintenance.ps1 -Step Propose` cycles, **completed** |
| #1607 | Layer 1/2 six-point column validation | Worked D1–D13/E1/E2 decisions in place on the action-plan doc; consolidated spec produced; **put on hold** — superseded in part by #1668's final verdict |
| #1668 | `strong_meaning_parse` data errors | Full investigation arc: POS-tag header bug fixed, `vw_strong_gloss.ord` fixed, G1375 phantom-segment bug fixed, over-segmentation finding reported, `vw_strong_meaning_raw` built, LLM-contextual-read prototyped, ending in the researcher's retirement verdict — **completed** |
| #1673 | `configmaint.propose` crash (JSON) | My own PowerShell quoting mistake (inline JSON mangled by PowerShell before Python saw it) — not a code defect; resolved **self_correctable** |
| #1674 | Register `create_vw_strong_meaning_raw` script | Proposed → approved → applied, **completed** |
| #1675–#1677 | Retire `strong_meaning_parsed`/`strong_lsj_parsed`/`strong_mounce_parsed` (`cfg_table.inactive=1`) | All 3 applied, **completed** |
| #1678 | Retire `lexicon.parse` step (`cfg_step.inactive=1`) | Applied, **completed** |
| #1679 | Retire `create_vw_strong_gloss` script (`cfg_utility.inactive=1`) | Applied, **completed** |
| #1680 | Revise meaning-distillation method (new) | **Raised**, `decision_required`, assigned Researcher — the explicit carry-forward for tomorrow |

---

## Files created or changed

**New:**
- `iba/app/migration/add_verse_meta_status_column_v1_20260910.py`
- `iba/app/lib/versemeta.py`
- `iba/app/ps/VerseMeta.ps1`
- `iba/app/migration/resolved_sense_revived_v1_20260910.py`
- `iba/docs/1607-layer1-layer2-consolidated-column-spec-v1-20260910.md`
- `iba/app/migration/add_lexicon_header_pos_tags_setting_v1_20260910.py`
- `iba/app/migration/create_vw_strong_meaning_raw_v1_20260910.py`

**Modified:**
- `iba/app/lib/stepapi.py` (`preview_to_text`)
- `iba/app/handlers/raw.py` (`verses_one` now writes `verse.text`)
- `iba/app/tools/_apply_verse_plaintext_column.py` (imports the shared function instead of duplicating it)
- `iba/app/lib/lexical.py` (`resolve_code` — `resolved_sense` revived from `strong_meaning_parsed` sort=0)
- `iba/docs/1607-open-items-action-plan-v1-20260909.md` (every D1–D13/E1/E2 item updated in place)
- `iba/app/lib/lexiconparse.py` (`is_header_only_line`/POS-tag exclusion; segment-merge fix for phantom punctuation-only rows)
- `iba/app/migration/create_vw_strong_gloss_v1_20260910.py` (`ord` fixed to a real per-strong rank)
- `iba/app/BUILD.md` (entries #255–#262, full technical record of everything below)

**`iba.db` state (not git-tracked, recorded for completeness):** `verse.text` backfilled (723 rows);
`verse_meta.status`/`status_changed_at` added; `verse_lexical.resolved_sense` rebuilt corpus-wide
three times as the parse itself was corrected (544,590 → clean → cleaner rows each pass);
`strong_meaning_parsed`/`strong_lsj_parsed`/`strong_mounce_parsed` rebuilt twice then marked
`inactive`; `vw_strong_gloss` created, `ord` fixed, then marked `inactive`; `vw_strong_meaning_raw`
created (active); 6 `cfg_column.use` corrections; `cfg_setting lexicon.header_pos_tags` seeded; 5
`cfg_table`/`cfg_step`/`cfg_utility` rows set `inactive=1` for the retirement. Full detail: BUILD.md
#255–#262.

---

## Decisions made

**Researcher's own decisions (not Claude's):**
- `resolved_sense` = `strong_meaning_parsed` sort=0 row, no M-code restriction, untruncated (ord=0/ord=1 confusion resolved: `sort`/`ord` are 0-indexed and identical).
- `gloss_consistent_in_verse` retained as-is (no promotion to `span`).
- `verse_meta.status`/`VerseMeta.ps1` built as specified (status values: exclude/citated/analysed; comma-delimited reference input).
- The full #1607 D1–D13/E1/E2 batch of column decisions (recorded in the action-plan doc, several still open — see below).
- `status` (Layer 1) and `testament` (Layer 1) both slated for retirement — `Spine-Check.ps1` now covers what `status` approximated; `testament` is redundant with `verse_meta.testament`.
- **The 3 parse tables retired; the entire meaning-distillation method to be reconsidered** — the session's final, defining decision, made after reviewing the G3551/νόμος live case study.
- Explicit "no piecemeal" instruction (apply everything as one consolidated batch once the #1607 review is complete) — respected throughout; only no-judgement config-text fixes (E1) and clearly-scoped bug fixes were applied immediately, never a design decision or another full corpus rebuild pre-empted.

**Claude fixes, closed directly (self-correctable, no design judgement):**
- `verse.text` ingestion gap (#1662) — root cause + fix, though left `ready_for_approval` per the app's own state-machine convention rather than self-closed.
- `lexicon.parse`'s bare-POS-tag-header bug (`H0503`/`H6310`) and phantom-punctuation-segment bug (`G1375`) — both root-caused precisely against live STEP data before fixing, both verified corpus-wide after.
- `vw_strong_gloss.ord` (LSJ/Mounce using raw PK instead of a real rank).
- Escalation #1673 (own PowerShell quoting mistake, not a code defect).

---

## Open items carried into next session

1. **#1680 — revise the meaning-distillation method.** The load-bearing item. An LLM contextual-read
   prototype (verse text + `vw_strong_meaning_raw`'s 3 raw segments, no mechanical parse in the way)
   worked well on both a single-verse test (`John.10.34`) and a full 154-verse sweep (`G3551`/νόμος,
   6+ real sense-clusters found). Not decided: whether/how this becomes the actual Layer 1/2
   mechanism, how it interacts with the already-decided #1607 items, and what `resolved_sense` (or
   its replacement) should mean once meaning resolves at the verse-occurrence grain, not the
   Strong's-code grain.
2. **#1607 — on hold**, not closed. Items untouched by the meaning layer (D1 `role`, D4
   `ambiguity_note`/`pairing`, D11 `gloss_consistent_in_verse`, D12 `language`→`verse_meta`, D13
   `verse_meta`, E1/E2) still stand as decided and are ready to build once the method question is
   settled — they don't need to be re-litigated.
3. Still-genuinely-open sub-items from the #1607 action plan, not decided this session: D3 (
   `resolved_sense` truncation — likely moot now), D5 (Greek `narrative_morph` signal design), D6
   (confirm `updated_at` scope reading), D7 (`verse_lexical_note.passage_id` drop-or-repurpose), D8
   (`evidence_text` enforce-or-merge), D9 (`verb_argument` trigger condition), D10 (`H3477H`
   disposition).
4. Pending data-quality approvals unrelated to the meaning-layer question, still open: #1590 (Greek
   article role-tag misclassification), #1591 (`surface` 192-row defect — the prior repair attempt
   couldn't even reproduce the defect set, needs fresh investigation).
5. `verse_lexical.resolved_sense`'s current live values are **stale/provisional** — built from the
   now-retired parse. Not corrected this session; explicitly deferred to the method revision.

---

## Git state

<!-- filled in after commit, per governance.session_log_required_content -->
