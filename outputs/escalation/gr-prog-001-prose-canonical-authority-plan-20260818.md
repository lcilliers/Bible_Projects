# GR-PROG-001 / prose-as-canonical-authority — alignment plan (parked)

**Raised:** 2026-08-18, in chat, by the researcher — dictated verbatim below, structured a–f.
**Status:** Parked. The researcher's explicit instruction: work the other five unhomed
`wa_rule_registry` principle-rules first (GR-DB-001, GR-REF-001, GR-PROC-001, GR-PROG-002,
GR-PROG-009 — see [`docs/governance-alignment-register.md`](../../../docs/governance-alignment-register.md)
row 5's open note, and the chat exchange this session that surfaced all six), then return to this
one.

## Background

`GR-PROG-001` ("the verse always leads") was one of six `wa_rule_registry` principle-rules found
2026-08-18 to have **no `cfg_*` equivalent** anywhere in `iba.db` after that table's blanket
retirement (2026-08-17, escalation #696). This item reframes GR-PROG-001's underlying concern —
project-context authority — one level up: **the programme book (the prose) is the canonical
authority on what the project is, and is not currently defined, scoped, or controlled in IBA at
all.**

## The instruction, as given (a–f)

> The programme book of the prose is the canonical authority on what the project is about. At the
> moment, prose is not defined, scoped, or controlled in IBA.

**a)** `cfg.governance` settings to anchor the entry point.

**b)** Create a separate `cfg_*` table for prose.

**c)** Update the table and column definitions in the `cfg_table`/`cfg_column` segments.

**d)** Create an escalation to align programme chapters 4–6, as these are not up to date.

**e)** Chapters 0–3 are reviewed and are no longer in draft. Derive config entries such as
`GR-PROG-001` and point them to the prose chapters for reference. Identify other critical configs
that matter also (e.g. the definition of inner being).

**f)** Include configs that will ensure changes in methodology and approach will flag if they need
updating in prose.

## What exists today (found while filing this, not yet acted on)

- Prose currently lives as dated markdown/JSON extracts under
  [`Workflow/Programme/programme_prose/`](../../../Workflow/Programme/programme_prose/) — most
  recent: `wa-programme-prose-programme-20260814.md`. Chapters present: 0 (Preamble), 1 (Programme
  purpose), 2 (Research methodology), 3 (Research approach), 4 (Data architecture), 5 (Data
  integrity & governance), 6 (Instruction corpus).
- **Possible discrepancy to verify when (e) is worked:** every section in that 2026-08-14 extract,
  including all of chapters 0–3, is still tagged `status: draft` in its own per-section metadata
  line (e.g. `Section id 15 · status draft · v2 ...`). This conflicts with the instruction's
  statement that chapters 0–3 "are reviewed and are no longer in draft." Not resolved here — flagged
  so whoever works item (e) checks the actual review status against the researcher directly rather
  than trusting either the file's stale `draft` tag or the instruction's summary uncritically.
- `bible_research.db` separately has a DB-canonical prose store (`prose_section`,
  `prose_section_type`, `prose_section_fts`, link tables — "publication parked" per `CLAUDE.md`
  §3) — a second, distinct prose mechanism from the `Workflow/Programme/programme_prose/`
  extracts. Item (b)'s new `cfg_*` prose table needs to say which of these (if either) it anchors,
  or whether it's a third, IBA-native store — not yet scoped, left for when this item is picked up.
- This escalation excludes `Workflow/Programme/programme_prose/` from `content_index` already
  (escalation #713, 2026-08-17) — that decision (search-index noise, not authority) is orthogonal
  to this item and doesn't need revisiting.

## Addendum 2026-08-18 — `GR-PROG-002` folded in, superseded by the prose rules

Researcher decision, same session: **`GR-PROG-002` (the programme's governing question) is
superseded by the prose rules** — its content is exactly prose chapter 1's "Defining Inner Being" /
"This Inner-Being Programme" sections (confirmed present in
`Workflow/Programme/programme_prose/wa-programme-prose-programme-20260814.md`, found while
scoping this item originally). **Every place `GR-PROG-002` is referenced must be replaced with a
pointer to the appropriate prose section, using the `cfg_*` settings this item builds** — i.e. this
retirement is gated on parts (a)/(b) landing first (the anchor setting + prose table have to exist
before anything can point at them).

**Reference-sweep scope, measured 2026-08-18** (`grep -rl "GR-PROG-002"`, project-wide): **26 files**
hit, of which the large majority (~20) are dated April–June 2026 under `archive/`,
`Workflow/Global_rules/`, `Workflow/Sessionlogs/`, `Sessions/`, `Sessions-v2/` — historical
snapshots of the old `wa_rule_registry` extract or pre-reset findings output, already superseded by
the 2026-06-25/2026-07-02/2026-08-03/2026-08-17 method resets and not in scope for editing (they're
the historical record, not live instruction). **Six live/recent hits actually worth checking when
this is worked:**

- `iba/app/verse-analysis/word_registry/Fear/wa-obslog-fear-synergise-v1-20260809.md`
- `iba/docs/cluster assignment process/wa-obslog-global-cluster-alloc-v1-20260811.md`
- `iba/docs/windows debate/wa-obslog-ref-body-act-verbs-v1-20260810.md`
- `Logs/session-log-v1-20260715.md`
- `outputs/markdown/ai-failures-source-extract-v1-20260724.md`
- `research/investigations/programme-prose-structure-design-v1-20260421.md`

Not opened or characterised further here (each may cite the rule as historical justification
within its own obslog narrative, which wouldn't need editing, or as live instruction, which would)
— left for whoever works this to actually read each one and judge, per
`feedback_never_model_output_on_prior_unreviewed_pass`-style discipline (don't presume from a grep
hit alone). `docs/governance-alignment-register.md` and this report itself also cite `GR-PROG-002`
— both are current governance record, correctly describing history, and don't need editing.

## Not started

No `cfg_*` writes, no table creation, no escalation-splitting into (d)'s chapter-4–6 alignment item
yet, no reference-sweep edits. This document exists solely so the instruction survives intact until
picked up — per `cfg_escalation.chat_routing` (a genuine open item raised in chat gets an escalation
the same turn) and `cfg_escalation.document_reference_grouping` (a multi-part package gets one
reference document, not restated inline across rows).
