# Session Log — 2026-09-01 — Catalogue closed, lexical-to-finding pipeline exploration, Dan 1:8 worked example

**Scope:** Continuation session (`/start-project` at session start). Split #1007's catalogue-scope
work from the characteristic-model reconciliation thread; ran a reclassification pass on the
Word/term (lexical) Scope-focus bucket that surfaced a structural deficiency in the catalogue
itself and closed #1007 on that conclusion; raised the vocabulary/glossary work as its own thread
and resolved (partially) whether it belongs in `cfg_enum`; then spent most of the session building
and repeatedly correcting a full worked example (Dan 1:8) of what a genuinely disciplined
lexical-to-finding reading looks like — surfacing a repeatable checklist, a primary-operation/chain
concept, genre and language as fields the schema doesn't yet carry explicitly, and a related-term/
lemma-key analysis method that caught two of its own errors live. Closed by producing three
digestible artefacts (checklist+catalogue mapping, a schema-checked JSON finding payload with an
honest gap assessment, and a characteristic-framed narrative) and raising #1379 to anchor the
verse_lexical rework this all points toward.

## Escalations touched

| # | Outcome | Notes |
|---|---|---|
| #1007 | **Closed** (v21, `state=closed`) | Researcher's own conclusion, recorded verbatim: the catalogue's questions, their data window, their expected answers, and those answers' role in the next phase are structurally deficient — not fixable by further reclassification. Full exploration trail linked in the resolution. Escalation #737/#738/#770/#784/#1022 (all on-hold, untouched this session) are separate, older on-hold threads not part of this closure. |
| #1376 | **Open**, raised | "Characteristic model — cross-db inventory and reconciliation." Seeded, per explicit researcher instruction, with only `1376-characteristic-tables-cross-db-inventory-v1/v2` — the wider legacy characteristic-doc corpus (~60 files) deliberately excluded. No further work this session. |
| #1377 | **Open, in-progress** (v4) | "Vocabulary/glossary definition." Raised, then updated three times: v2 added a full programme-prose read plus a `cfg_column` scan across both databases (found the delete-marker 4-spelling family, the `cluster` column's M-code/C-code split, and `scope`'s 4 unrelated meanings); v3 recorded the researcher's decision that this belongs in `cfg_enum`, strictly defined; v4 recorded the refinement that the prose-level concept collisions (characteristic, dimension, HIB, Phase 1/2) likely need a *new*, separate `cfg_*` mechanism — not designed or built, explicitly deferred. |
| #1378 | **Open**, raised | "Lexical-to-finding pipeline (per verse, per IB word)." The thread the whole Dan 1:8 worked example belongs to. No resolution — extensive exploration, checklist extracted, left open. |
| #1379 | **Open**, raised | "Verse_lexical rework: intrinsic contextual enrichment." Anchors the researcher's own closing statement that the depth of analysis demonstrated today should be built into `verse_lexical` natively, not reconstructed by hand each time. Seeded with the full worked-example document plus the researcher's own scale reflection (66 books / ~40,000 verses / ~3,000 characteristics), recorded as-is, not resolved. |

## Files created / changed

- **`Workflow/Catalogue/1007-tier-catalogue-word-term-lexical-v1-20260901.md`** (new) — the 16-question Word/term (lexical) bucket extracted as its own file from the v3 scope-focus doc.
- **`Workflow/Catalogue/1007-tier-catalogue-word-term-lexical-reclassification-review-v1-20260901.md`** (new) — the reclassification proposal (11 stay lexical, 3 move to a new "Characteristic — what it is" bucket, 2 flagged) that became the trigger for closing #1007.
- **`Workflow/Catalogue/1377-vocabulary-glossary-seed-v1-20260901.md`** (new, then archived to `archive/`) — first-pass glossary seed from #1007/#1376.
- **`Workflow/Catalogue/1377-vocabulary-glossary-seed-v2-20260901.md`** (new; supersedes v1) — added the full programme-prose read and the `cfg_column` cross-database scan.
- **`Workflow/Catalogue/1379-lexical-to-finding-worked-example-v1-20260901.md`** (new; the session's main body of work) — the Dan 1:8 dissection, built up over many rounds: raw `verse_lexical`/`span` data, the "defile" companion-word correction, an ESV-quote transcription error caught and fixed, a full 25-row per-term discipline pass (catching the `H1245`/"asked" and `king`/`chief`/`eunuchs` misses), a taxonomy of declared-vs-structural roles, the primary-operation/chain concept (evidenced via waw-consecutive morphology), genre/language-as-explicit-field findings, and a related-term/`lemma_key` analysis that caught and retracted two of its own errors (the "bake" dismissal, the "redeem/defile homonymy" claim).
- **`Workflow/Catalogue/1379-lexical-inner-being-checklist-v1-20260901.md`** (new) — the 12-test checklist extracted from the worked example, cross-mapped to the 16 Word/term (lexical) catalogue questions; surfaced two catalogue gaps (polarity, primary-operation/theme) with no home in the existing 16 questions.
- **`Workflow/Catalogue/dan-1-8-finding-payload-v1-20260901.json`** (new) — schema-checked (against the live `finding`/`finding_verse_link`/`finding_question_link`/`finding_citation` tables) JSON payload for two finding rows, with an honest, evidenced gap assessment: `finding_citation` cannot be used at all for this evidence (`source_table` is `CHECK`-constrained to `cluster_finding`/`cluster_observation` only); `characteristic_id` has no clean existing row to point to; `provenance`/`finding_status` have no controlled value that fits; most of the session's discovered content (defile, king, chief, eunuchs, wine) has no live `wa_verse_records`/`mti_terms` anchor at Dan 1:8 at all.
- **`Workflow/Catalogue/1379-dan-1-8-characteristic-narrative-v1-20260901.md`** (new) — the narrative deliverable, written from the characteristic's (resolve/volitional determination) perspective, using the programme's own finding/inferential/hypothesis distinction rather than one flat register.
- **`outputs/escalation/escalation-list-v41-20260901.md`**, **`outputs/escalation/1007-escalation-history-v3-20260901.md`**, plus archived prior versions — routine auto-generated reports from `Escalation.ps1` runs this session, not hand-authored.

## Decisions

**Researcher's own decisions:**
- Scoped #1376's seed to the two current cross-db-inventory files only, explicitly excluding the wider legacy characteristic-doc corpus.
- Concluded and closed #1007: the catalogue's structural deficiency (questions, data window, expected answers, and their role in the next phase) is not fixable by further reclassification.
- Decided `cfg_enum` (strictly defined) is the right mechanism for the column-value vocabulary findings under #1377, with a later refinement that prose-level concepts likely need a separate, new `cfg_*` mechanism — not designed now.
- Drove every substantive correction in the Dan 1:8 worked example: the "defile" companion-word point, the relational-target ("stakes/scaffolding") significance correction, the Phase-1-hides-from-Phase-2 architectural point, the "discoverable not declarative" methodological framing, the primary-operation/chain concept, genre/mode and language/testament as required explicit fields, and the redeem/defile pushback that led to the lemma_key test's retraction.
- Set the exact shape of today's closing deliverables (checklist + catalogue mapping; JSON finding payload with an explicit completeness check; a characteristic-framed narrative) and requested the session log close.

**Corrections made within the working document, at the researcher's prompting (not escalations, not `self_correctable` resolutions — live analytical corrections):** a truncated ESV quote (missing the verse's second sentence); an off-by-one span count; the "bake" relation wrongly dismissed as coincidental, then reversed on a real `lemma_key` match; the "redeem/defile" relation wrongly reclassified as homonymy, then retracted after the disambiguating test failed its own control case (`H1351`/`H1352`, undeniably one root, carry different `lemma_key`s too).

## Open items carried into next session

- **#1376, #1377, #1378, #1379** all remain open — none resolved this session, all seeded with enough context to resume without reconstruction (per each escalation's own `context` field and, for #1378/#1379, the worked-example document).
- **The `H0834A` same-code/different-gloss data-quality flag** (Dan 1:8, positions 2 and 12 — same Strong's+morph pair glossed "that" and "allow") was named in the worked example but **never raised as its own escalation** — left as a genuinely open, un-escalated item, not carried forward automatically.
- **The three closing deliverables are explicitly the researcher's own next-session digestion material** — "good material for me to digest next... I will clear and take these output further" — no further action taken on them this session by design.
- **The checklist has only been run against one Hebrew, narrative-genre example.** Its own next step (named in the worked-example doc, not started): run it against a plain non-idiomatic IB word, and against a Greek example, since the sequencing test (test 9) is explicitly known not to port to Greek unchanged.

## Git state

Branch `main`, commit `7f39d15c671bd2c28bd0c8b6a8bfae1536dfd555` (this commit necessarily precedes
the edit that filled in this section — the same wrinkle every prior session log hits), pushed
clean:

```
$ git push
To https://github.com/lcilliers/Bible_Projects.git
   ff122d74..7f39d15c  main -> main

$ git status
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

13 files changed, 1,777 insertions — all listed above under Files created/changed; nothing
unexpected staged.
