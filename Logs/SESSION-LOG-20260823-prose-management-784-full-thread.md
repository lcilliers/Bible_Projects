# Session log — 2026-08-23 — Prose management, escalation #784 (full thread)

**Escalation:** #784, v1 → v35 across 2026-08-21 to 2026-08-23. **Session-start review by the
researcher confirmed the new development cycle applies going forward** (plan/propose/design in
detail → approve → build per the plan → approve, per `cfg_behaviour_rule`
`test-plan-per-module-utility`, escalation #828) — v1–v3 of the incorporation plan were judged
progressive spec-build, no longer acceptable practice.

## What happened, in order

1. **Re-planned #784 from scratch** as plan v4 (`iba/docs/prose-store-iba-incorporation-plan-v4-20260822.md`)
   — full-scope, single document, covering the read layer, dispatcher registration, the write-side
   governance gap, a `cfg_prose` table correction, and a 20-case test plan. Filed for approval.
2. **Scope corrected before v4 was approved.** Researcher: prose management is the whole
   creating/reviewing/exploring/updating process across 5 books, not the mechanical storage layer
   v4 (and the architecture document) actually covers. v4 set aside, not discarded. A concrete
   illustration followed: `prose.chapter_names`/`prose.book_stage_map` (both proposed in v4) were
   wrong in principle — they'd have duplicated data the tables already carry as real columns.
3. **Essence capture** (`prose-management-iba-v1`/`v2`) — read the architecture doc + Programme
   chapters 1–3 in full, captured the production chain, the disciplines already governing
   authorship, and open gaps. Corrected to v2 after the researcher found Chapter 3 itself stale
   (only chapters 1–2 are actually current) — surfaced as "the double-edged sword": designing prose
   management by reading prose that is itself part of what needs redesigning.
4. **File control designed and built.** Central finding: the architecture doc claimed edit files
   were disposable; the code makes them permanent (`prose_section.source_file`). Built and tested
   live: versioned, non-colliding export naming; auto-archive of edit files on successful import,
   with the DB's provenance pointer never briefly dangling. A second real bug surfaced mid-build —
   import was superseding every section in a bundled chapter file regardless of whether it changed
   — fixed and tested (only actually-changed sections now get superseded). Delete/add/move behaviour
   on the edit-file round-trip tested live; delete's silent no-op flagged as a genuine open decision.
5. **Two design threads opened, not built:** a prose-change-flag mechanism (decided to reuse/extend
   `wa_quality_flag_types`/`wa_data_quality_flags` rather than build new), and chapter-rewrite
   assistance (a Claude-Code-assembled briefing feeding Claude-AI authoring, mirroring Session B
   Readiness → Analysis) — named as downstream of the flag mechanism.
6. **A premise corrected with data.** Researcher considered whether `Detail design` was worth
   keeping given IBA now governs process. Checked live: it isn't process documentation at all — it's
   47% of the entire prose corpus, real per-word Session A/B/C research output from the old
   pre-reset method. The actual redundant-with-IBA candidate is the much smaller Programme chapters
   4–6, already tracked separately as escalation #739.
7. **Structural extracts of both books** (`prose-book-extract-detail-design`/`-findings`) —
   `Detail design` is 58% empty scaffolding from an abandoned pipeline stage; `Findings` is the
   opposite profile and is mostly *current*-method output, though its uniform "approved" status
   traced back to a hardcoded constant in an old one-off script, not real review.
8. **Design principles stated at a high level**, each checked against real content rather than
   accepted abstractly: prose is narrative, not data dumps — what's currently in both books is raw
   material for writing, not the writing itself. A four-book purpose model was given (Programme /
   "what the data says" / "what analysis says it means" / Essays), with a real content sample
   (Psalm 32) confirmed to already sit on the interpretive side of that line. "The verse is king"
   was confirmed as already-anchored governance (`cfg_prose_concept`), but `prose_section` was found
   to have zero structural verse-linkage — grounding exists only as free-text citations. The
   "missing 5th book" (Concordance) turned out to be two problems, not one: the base
   word/Strong's/verse concordance already works live in IBA today; the prose-integrated half is
   genuinely blocked by the same verse-linkage gap.
9. **The whole thread captured coherently**, per explicit instruction not to summarise or lose any
   thinking and not to propose solutions — `iba/docs/prose-management-784-conversation-capture-v1-20260823.md`,
   15 sections, ending in a plain inventory (built/tested, designed-not-built, open decisions, open
   questions) with no recommendations attached.

## What's actually built and live now

- `iba/app/lib/prosestore.py`: `CHAPTER_EDIT_OUT_DIR` regression fixed; versioned/non-colliding
  chapter-edit export naming; auto-archive of edit files on successful import; section-level
  (not chapter-level) supersede — only actually-changed sections get versioned.
- `docs/prose-store-architecture.md` §8.1 corrected to match the real (permanent, auto-archived)
  behaviour.
- `iba/app/BUILD.md` §174 records the code changes in full.

Everything else from this thread — plan v4's config layer, the prose-change-flag mechanism,
chapter-rewrite assistance, `prose_section_verse_link`, the raw-material-visibility problem, the
book-2/3 boundary, the Concordance — is **designed or discussed, not built**. See the full capture
document for the complete inventory.

## Researcher's stated plan for next session

> a) lightly build prose management into IBA — create the framework for process control, anchor
> what's already settled and known; don't try to solve everything, keep track of what isn't solved
> yet. b) bring the Programme chapters up to date. c) prepare for the analysis phase.

## Files touched this session

**New:**
- `iba/docs/prose-store-iba-incorporation-plan-v4-20260822.md` (set aside, unapproved)
- `iba/docs/prose-management-iba-v1-20260822.md`, `-v2-20260822.md`
- `iba/docs/prose-file-control-v1-20260822.md`
- `iba/docs/prose-book-extract-detail-design-20260823.md`, `-findings-20260823.md`
- `iba/docs/prose-management-784-conversation-capture-v1-20260823.md`
- `outputs/markdown/prose-edits/prose-edit-programme-chapter-2-20260822.md`,
  `-chapter-3-20260822.md` (sent to researcher for review)

**Modified:**
- `iba/app/lib/prosestore.py` (see BUILD.md §174)
- `docs/prose-store-architecture.md` (§8.1)
- `iba/app/BUILD.md` (§174, this entry)

**Escalation:** #784 carries the full decision/finding history (v1–v35); no other escalation
opened or touched this session beyond what was already closed before it started.
