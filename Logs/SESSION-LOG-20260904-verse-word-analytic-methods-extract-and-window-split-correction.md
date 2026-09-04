# Session log — 2026-09-04 (continuation session)

**Scope, one line:** Spawned and built a comprehensive verse/word analytic-methods extract
(#1446) from #1443's closure, corrected it through several rounds against direct researcher
challenge (T1–T3 tier-label ambiguity across the project → #1447; then the Window 1/Window 2
boundary itself, corrected twice — first from a wrong "detect vs. interpret" framing to
subject/perspective, then to the real definitional rule the researcher stated plainly), then
applied that same corrected rule to #1383's own pending design documents (not just the extract),
and finally cross-checked #1446 §2a/§2b/§2c against #1383's full build spec, filling two genuine
gaps found. Session ends here at the researcher's initiative to clear context; #1383 and #1447
remain open, both `ready_for_approval`/assigned to Researcher.

## Escalations touched, by id, with outcome

- **#1443** — v2 → v3, **completed**. Researcher approved v2's resolution (the structural-pattern
  finding split into Stage 1 DETECT `structural_pattern` note_type vs. Stage 2 INTERPRET, parked)
  and instructed, verbatim: "Spawn a new escalation from this to extract all verse word analytic
  methods."
- **#1446** — raised (spawned from #1443), **completed** after multiple correction rounds, all
  logged on its own record via `-Action Correction` (the item was closed after each round, so
  Update could not be used for further rounds — used as the only available mechanism, not as
  ordinary workflow, each time noted as such):
  - v1: full extract filed, scoped to the 5 named reference documents narrowly (word/verse grain
    only).
  - Researcher: v1 silently excluded methods those 5 documents actually named. Rewritten as v2 —
    every method from every document folded in, nothing summarized past, six-layer genealogy.
  - Researcher: asked what T1/T2/T3 mean; found three unrelated schemes reusing the same label
    project-wide (Verse Reading Technique T1–T9, the deprecated tier catalogue T0–T9, live
    `cluster_code` rows T2/T3) — none cross-referenced anywhere. Spawned **#1447**.
  - Researcher: a 4th cluster meaning ("also with a completely different meaning") plus a
    correction that the glossary actually lives at `prose_section_type`/`prose_section`, not the
    `prose_section` id 64 I'd checked. Re-checked live: the real glossary (`glossary_programme`,
    "Word Index and Glossary") already had T2/T3/Tier entries; my original "checked live, zero
    entries" claim was simply wrong (wrong table). Corrected #1447 and the extract accordingly.
  - Researcher: embed #1383's Window 1/Window 2 split as a stated governing principle, not
    scattered notes. Added §0 — framed (wrongly) as DETECT (Window 1) vs. INTERPRET (Window 2).
  - Researcher: that framing is confusing and wrong — Window 1 already does real judgement work
    (idiom, structural-pattern labelling, connective classification); the actual split is
    subject/perspective (verse-in-itself vs. the same data through the HIB lens), not depth.
    Rewrote §0 accordingly.
  - Researcher: #1383 has *consistently* drawn this line as a mechanical one, and specifically: the
    §2d aggregation/rollup item and the `phenomenon` FK link are Window 2 work, not Window-1-
    adjacent; the "Layer 3 reporting" label made no sense. Rewrote §0 a second time with the actual
    definitional rule (`verse_lexical`/`verse_lexical_note` can never carry an inner-being concept;
    nothing in Window 1 decides phenomenon status) and reclassified §2d accordingly.
- **#1447** — raised (glossary gap: no cross-referenced definition anywhere for the 3 T1–T3
  schemes), corrected once (wrong-table claim fixed against the real glossary content), **left
  open** — `state=re-assigned`, `next_action=ready_for_approval`, `assigned_to=Researcher`. Three
  concrete open questions on record: add a T1 entry + entries for the Verse Reading Technique's own
  T1–T9 scheme (via which write path — no Developer Mode marker active this session); reconcile the
  glossary's stated T0–T7 tier range against the extract's own T0–T9 description; disposition the
  still-unplaced "T2 qualifiers" 4th label from the 2026-07-01 derivation-validation doc.
- **#1445** — v4 → v6, **completed** (carried over from the prior session, closed at this
  session's start): re-verified live that `cfg_table` (`bible_research`, `wa_flag_type_question_link`)
  was already `inactive=1` exactly as the researcher's approval described, cleared
  `needs_claude_followup` to reach `completed` (via the `followup_cleared_was_approved` transition
  rule — a `decision_required` item cannot have `next_action=approved` re-supplied by Claude).
- **#1383** — v22 → v26, **left open**, `re-assigned`/`ready_for_approval`/`Researcher`:
  - v23: recorded the researcher's Window 1/2 critique verbatim against #1383's own pending design
    (not just the extract), `next_action=revise`, assigned to Claude.
  - v24: applied the (first-round) correction to the actual design documents — a correction banner
    plus fixed the `passage_emergent_question` and FK-link items in the full build spec; shorter
    banners on the design-propose doc and the drift-mitigation doc (the "Layer 3" retraction).
  - v25/v26: per the researcher's follow-on instruction ("the design proposal at this point does
    not take 1446 2a, 2b, and 2c full into account"), checked every item in those three sections
    against the build spec. Two genuine gaps found and filled — new §B.18 (`recurrence_role_shift`
    and `cross_lemma_shared_gloss` note_types, each with a method rule and a quality check, plus two
    more method rules the extract had named but the spec never turned into rules) — and one false
    gap corrected (cross-verse `pronoun_resolution`/`entity_link` resolution was already supported
    by the existing `target_verse` field; the extract's "not yet built into schema" claim was wrong,
    fixed in both documents).

## Files created or changed

- `iba/docs/1446-verse-word-analytic-methods-extract-v1-20260904.md` — created, then archived to
  `iba/docs/archive/` (superseded same day).
- `iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md` — created, edited in place
  through five further correction rounds (disambiguation block, §0 Window-split principle, §0
  rewritten twice, §2d reclassified).
- `iba/docs/1383-verse-lexical-window1-full-build-specification-v1-20260904.md` — edited: a
  correction banner; §(h)'s `passage_emergent_question` row resolved (was open); §(i) item 3
  reframed (FK link is Window 2's decision, not "deferred"); new §B.18 (2 new `note_type` values, 4
  new `cfg_method_rule` rows, 2 new `cfg_enum` values); §D.2 quality checks for the 2 new note
  types; §C.2's `target_verse` row corrected to state cross-verse resolution is already supported.
- `iba/docs/1383-verse-lexical-enrichment-design-propose-v1-20260903.md` — edited: correction
  banner added, pointing at the full build spec's own fix.
- `iba/docs/1383-verse-lexical-window1-method-and-drift-mitigation-v1-20260903.md` — edited:
  correction banner added, retracting the "Layer 3 reporting" framing as a category error.
- `outputs/escalation/*.md` — routine `Escalation.ps1 -Action List/History` report regenerations
  (session-start orientation, plus history pulls for #1443/#1444/#1445/#1446/#1447/#1383 during
  this session's own work); not deliverables in their own right.

## Decisions made

**Researcher's own decisions**, not self-correctable:
- Approved #1443's Stage-1-detect/Stage-2-interpret disposition for the structural-pattern finding.
- Instructed spawning #1446 to extract every verse/word analytic method.
- Identified the T1/T2/T3 tier-label collision (three unrelated schemes) and the further
  cluster-level T3 meaning, and corrected my glossary-location assumption
  (`prose_section_type`/`prose_section`, not `prose_section` id 64 alone).
- Corrected the Window 1/Window 2 split framing, twice — the second time with the actual
  definitional rule (no inner-being concept in Window 1's own tables; nothing in Window 1 decides
  phenomenon status) — and named this as a *consistent* error across #1383's own record, not a
  one-off in the extract.
- Directed applying that correction to #1383's actual pending design, not only the extract.
- Directed the #1446-§2a/§2b/§2c-vs-#1383-build-spec cross-check that surfaced the two genuine
  schema gaps (§B.18).
- This session's closing instruction: write this log; next session resumes the catalogue-questions-
  vs-proposed-verse-lexical-build cross-check (distinct from, and not yet started relative to, this
  session's own #1446-vs-#1383 cross-check).

**My own errors, corrected on the record, not glossed over**:
- v1 of #1446 silently excluded methods from documents the researcher had explicitly named —
  corrected in v2.
- Claimed "checked live, the glossary contains zero T1/T2/T3 entries" when I had in fact checked
  the wrong table (`prose_section` id 64, an old Session-B vocabulary section, not the real
  glossary) — corrected in #1447 v2 once the researcher named the right table.
- Framed the Window 1/Window 2 split as "detect vs. interpret" (a depth distinction), then even
  after softening that, still framed the `phenomenon` FK link and the aggregation/rollup item as
  "deferred Window 1 work" rather than recognising they were never Window 1's decision to make at
  all — both corrected only after the researcher named the actual definitional rule directly, not
  found independently.
- Claimed cross-verse pronoun/entity resolution was "not yet built into schema" in #1446, when the
  build spec's own existing `target_verse` field already supported it — found and corrected while
  doing the #1383 §B.18 cross-check, not before.

## Open items carried into the next session

1. **#1383** — full Window 1 build specification (plus its two companion documents) is
   `ready_for_approval`, corrected per this session's two rounds of researcher feedback. Not yet
   approved, rejected, or built. The 8 other open items already on its own record (§(i) items 1,
   2, 4-8 — audit-trail coverage, implementation-file choice, PS-surface choice, the two unbuilt
   party lexicons, the "verb triggered-by/impacts" schema-home question) are unchanged, still open.
2. **#1447** — glossary-definition gap for the three (or four, counting "T2 qualifiers") T-label
   schemes. `ready_for_approval`, three concrete questions on record (see above), none answered yet.
3. **Explicitly named by the researcher, this session's close**: resume the cross-check of the
   observation-question catalogue (`wa_obs_question_catalogue`) against the proposed verse-lexical
   build — a distinct, not-yet-restarted piece of work (earlier partial coverage exists in #1383's
   own v12-v15 catalogue-question-coverage documents from the prior session, but the researcher's
   own framing here is a fresh return to it, not a continuation assumed to pick up exactly where
   those left off).
4. Session ending by the researcher's own choice to clear context, not because any item above
   reached a natural stopping point.

## Git state — this log's own completion trigger

