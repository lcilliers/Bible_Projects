# Session log — 2026-09-02 — Verse-lexical Window 1 enrichment: design, checklist, two-verse prototype

**Scope:** Escalation #1379 (Verse_lexical rework: intrinsic contextual enrichment) — full design
dialogue from investigation through a consolidated, test-driven checklist, applied live to Ps 25:2
and Hos 2:4, plus a passage-boundary/genre architecture discussion (triggered by John 1:5) that
resolved into a concrete "one integrated read, self-determining sequential boundaries, 20-verse
hard cap" model. Design-only session — no code or schema changes applied (no Developer Mode marker
active); everything below is filed for review and for the Developer Mode session to build from.

## Escalations touched

- **#1379** (v1 → v7, still `in-progress`, `next_action=review`, assigned Researcher) — the whole
  session's work landed here. Not resolved — deliberately left open for the researcher's own
  practical-example + manual-verification pass before Developer Mode build. Key content across
  versions: self-correction of an incomplete first-pass investigation (v3→v4, found T4 already
  folded into the live `hib.set`/`hib_referent_option` mechanism, and the `operations-ingest`
  pipeline covering ground close to T6-9 under its own vocabulary); a consolidated checklist filed
  and applied to two real verses (v5); a live FK/passage-coverage investigation (v6); a
  session-close correction from a two-layer to a one-integrated-read model plus the 20-verse hard
  cap decision (v7).
- **#1378** (read only, `History` pulled for context — not modified) — the parent thread #1379 grew
  out of; still `raised`, untouched this session.

## Files created or changed

- `iba/docs/verse-lexical-enrichment-scope-v1-20260902.md` (new) — investigation + reconciliation:
  what T1-3/T4/T6-9 actually are vs. what's live in config, the `operations-ingest` correction, 7
  open decisions (A-G), genre marked CRITICAL.
- `iba/docs/verse-lexical-enrichment-checklist-v1-20260902.md` (new, then twice extended same day)
  — the consolidated, prototype-status Window 1 checklist: baseline fields, idiom test, purposeful
  classification by part of speech, chain/connections, related-words, polarity, entity-linking,
  data-quality checks, inert confirmation; later extended with the "one integrated read" correction,
  the 20-verse hard cap, and the proposed passage-coverage build (passage_id denormalization,
  passage-scoped build, completion marker, boundary suggester).
- `Workflow/Catalogue/verse-lexical-enrichment-applied-ps25-2-hos2-4-v1-20260902.md` (new) — the
  checklist applied live to Ps 25:2 (poetic) and Hos 2:4 (prophetic), grounded in real `iba.db`
  data throughout; surfaced a new checklist item (logical/causal connective), a live bug in
  existing T1-3 code (`H0853` direct-object-marker misclassified `role=content`), and a genuine
  unresolved cross-verse referent case (Hos 2:4's "her") handled correctly per the new discipline.
- `outputs/escalation/*` — routine `Escalation.ps1` List/History report output (list v45; history
  extracts for #1378 v1, #1379 v1-v2; superseded versions auto-archived to
  `outputs/escalation/archive/`). Not hand-authored content.

## Decisions made

**Researcher's own decisions** (not self-correctable — all substantive direction this session was
the researcher's, not mine):
- Scope of #1379 = Window 1 only (verse-lexical enrichment); Window 2 (HIB/phenomena/operations,
  the existing `operations-ingest` pipeline) stays untouched and out of scope.
- The T4 split: mechanical grammatical-nature classification (person/role) stays Window 1;
  actual referent-identity resolution stays Window 2 (`hib.set`/`hib_referent_option`), unchanged.
- Pronoun/relational-target resolution: attempt same-verse only; mark `unresolved` explicitly if
  not resolvable — never guess, never reach into adjacent verses from Window 1 itself.
- The full field/classification list for the checklist (position, surface, language, testament,
  genre-critical, idiom test, purposeful classification by POS, chain/connective tests,
  related-words discipline, polarity, entity-linking, data-quality checks, inert confirmation).
- Genre marked CRITICAL — blocks the process gate; must resolve before further build.
- Genre is a property of the *passage*, not the verse or the book (confirmed via the John 1:5
  case — the Johannine Prologue's hymnic character mismatches its own book's flat "gospel-
  narrative" tag).
- A margin-of-error/overlap-tolerant passage-boundary suggester is acceptable — passaging's only
  job is bounding related verses together, not precise genre taxonomy.
- **Correction, same day:** rejected a two-layer (mechanical-then-enriched) model in favour of one
  integrated technical read per block, with self-determining sequential boundaries (each read
  determines the next read's starting point) rather than whole-Bible pre-segmentation.
- **Hard verse-count ceiling: 20 verses maximum per passage/block; must split if exceeded** —
  decided after I confirmed live that no such numeric ceiling exists in current code/config (only
  a qualitative self-assessment refusal, `passage.build`'s `scope-too-complex`).
- Plan for next session, explicitly stated: run the checklist on further practical examples, then
  do a manual deep-dive analysis of the *same* passages to verify the checklist's results against
  it, before switching to Developer Mode to build.
- Longer-range vision, explicitly deferred/not decided: once Window 1 is validated, focus shifts
  entirely to Window 2 (inner-being analysis), organised by characteristic/inner-being concept —
  recorded, not actioned.

**Self-correctable fixes Claude made and closed directly:** none. Everything this session was
either investigation/evidence-gathering or design content requiring the researcher's own judgement
call — no code or config was applied, so there was nothing to self-correct-and-close.

**Errors caught and corrected in place, same session** (worth naming distinctly from the above —
these were my own mistakes, corrected on the researcher's challenge, not researcher decisions per
se): an incomplete first-pass config search that wrongly claimed T4-T9 was never built anywhere
(corrected once `cfg_method_rule` was read in full); framing `operations-ingest` as if IBA had
adopted T1-T9 terminology (corrected — it's an independent, earlier line of work); leaning on
`verse.text` as T4's evidentiary source (corrected — violates T1's own "translation orients, is
not the evidence" rule); the two-layer verse-lexical model (corrected to one integrated read, this
turn).

## Open items carried into next session

1. **Researcher-led:** run the checklist on more practical example verses/passages; do a manual
   deep-dive analysis of the same passages to verify the checklist's results independently.
2. **Developer Mode build queue**, once the above is done: `passage_id` denormalization on
   `verse_lexical`; passage-scoped build; `passage.lexical_complete_at`-style completion marker;
   genre/chain-signal-based passage-boundary suggester; 20-verse hard cap enforcement; the standing
   `H0853` direct-object-marker `role`-classification bug in `lib/lexical.py:classify_role`.
3. **Still open, unresolved this session:** where a per-verse genre tag is actually sourced from
   (CRITICAL, blocking); the Greek/NT equivalents for the chain-sequencing test and the H9xxx
   role-classification heuristic — tied to the researcher's separately-noted, still-parked "verse-
   lexical does not work for large parts of NT" observation (not investigated this session, by
   explicit instruction).
4. **Deferred, not decided:** the eventual pivot to Window 2/characteristic-based inner-being
   analysis, once Window 1 is validated.

## Git state (this log's own completion trigger)

Staged and committed all outstanding changes in the working tree at session close (per
`governance.session_log_triggers_commit` / CLAUDE.md §12), not only this session's own files.

- Branch: `main`
- Commit: `9046e1833b73f80e89eae083a654300e002a13fc` ("session 20260902: escalation #1379 --
  verse-lexical Window 1 enrichment design, consolidated checklist, applied to Ps 25:2 + Hos 2:4")
- `git status`: `On branch main / Your branch is up to date with 'origin/main'. / nothing to
  commit, working tree clean`
- `git push`: succeeded — `276055f4..9046e183 main -> main`
