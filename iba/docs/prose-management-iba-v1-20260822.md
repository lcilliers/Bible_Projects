# Prose management — essence capture (v1)

**Escalation #784** (the vehicle for this whole planning process, per researcher instruction
2026-08-22). **This is a capture, not a plan.** Two sources only, read in full, nothing else
synthesized in: [docs/prose-store-architecture.md](../../docs/prose-store-architecture.md) (the
mechanical/schema description) and the live Programme prose, Chapters 1–3, as currently held in
`bible_research.db` (`prose_section` rows, `book_label='Programme'`, `chapter_no` 1–3 — 19 sections,
~76,000 characters, read whole, not sampled). The plan components build out from here, researcher-led.

---

## 1. What "prose" is, in this programme's own words

Not documentation *about* the research — it is stated to be **the research's memory**:

> "The programme's analytical memory lives in the database... The database is where the programme's
> findings, interpretations, and analytical output are kept. It is not a storage layer beneath the
> research; it is the research's memory." (Ch3, *Session continuity and memory discipline*)

Claude AI (the analytical agent) does not live inside the database — it works from **snapshots**,
and getting the right snapshot in front of it "is itself a research act." Prose is one of the things
those snapshots are made of, alongside verse and term data.

Three properties are stated as what prose **must be**, because it has to survive being read by a
different session than the one that wrote it:

> "The prose is self-contained — readable without the session that produced it; scoped — clear about
> what it refers to (registry, cluster, group, dimension, or programme-wide); and grounded — clear
> about the evidence it rests on." (Ch3, *Session continuity*)

This is the closest thing the live programme prose has to a stated *authoring principle* — it says
what prose must achieve, not how (style, transitions, naming) to achieve it.

---

## 2. The production chain — prose is made at every phase, not just at the end

Chapter 3's *Tools and their roles* section, under "Programme prose held in the database," names a
**distinct order of prose produced at each phase of the per-word pipeline** (Ch2, *Programme flow*
names the same six phases: Session A, Verse Context, Dimension Review, Session B, Session C, Session
D). Prose at each phase is a different kind of thing, made a different way:

| Phase | What the prose *is* | Who authors it |
|---|---|---|
| **Session A** | "The listing of the extracted STEP data — the terms, the verses, the lexicon entries assembled as the word's source record." Mechanical, reproducible from structured data. | Claude Code (`author='claude_code'`) — the one stage permitted to author prose, because it's a prose *view* of data, not judgement. |
| **Session B Readiness** | "A data extract that brings together all the different angles of the word's data after Verse Context and Dimension Review... groups, dimensions, anchor verses, cross-references, term flags." The input to analysis, not yet the analysis itself. | Claude Code (mechanical extract) |
| **Session B Analysis** | "The primary result of the standing catalogue of questions: every analytic finding captured, every pointer for cross-registry synthesis recorded." | Claude AI — analytical judgement |
| **Session C** | "The reader-facing written study for the word... in plain, accessible language for an intelligent non-specialist reader... updated as Session B's findings are incorporated and again as Session D's synthesis informs it." Explicitly a **lifecycle**, not a single pass (v1 → v2 → v3, per the architecture doc). | Claude AI |
| **Session D** | "Prose produced at the level of clusters of related words, examining the inter-relationships of the inner-being characteristics... built from the accumulated pointer record... and the cross-registry analysis performed against it." | Claude AI |
| **Programme-wide** | "The self-description of the programme that this corpus is itself part of... held in the same database under the same schema, so that every session has a consistent, queryable self-description to draw on." | Claude AI, researcher direction |

**How each order reaches the database** is stated once, generally, in Ch3 *The two-AI division*
and *Session continuity*, not repeated per-phase: Claude AI writes an **obslog** (`.md`, the
session's working paper — "every finding, decision, gap, patch consequence, and open question" as
it happens); the researcher reviews it; Claude Code parses it into the database "via the Phase 2
writer pipeline," mapping obslog content categories to DB target tables, "with pre-write backup,
transactional commit, and post-write validation." Session A is the sole exception — mechanical,
reproducible content permitted to update in place (`session_a_replace`) rather than go through
that pipeline, because it carries no judgement to review.

---

## 3. Three orders of *published* output — stated, but not yet matched to the DB's own book structure

Chapter 2's *Publishing* section names three orders of finished output, independent of the six
phases above:

1. **Per-word study** — Session C's output, "designed to stand alone."
2. **Cross-word synthesis** — Session D's output, "produced when the per-word studies for their
   cluster are complete."
3. **Programme-level account** — assembled "when clusters have been worked through and their
   syntheses produced... built from the bottom up, word by word."

**Open alignment question, not resolved here:** the live database groups `prose_section_type` rows
under a `book_label` column with exactly four populated values — `Programme`, `Detail design`,
`Findings`, `Essays` (`book_order` 1–4) — plus five section-types (137 populated rows) still
untagged. Neither Chapter 1–3 nor the architecture document states how the three *published-output*
orders above map onto these four *book* labels, or whether they're meant to be the same grouping
under different names. On the surface: `Programme` clearly = the programme-level account;
`Findings` plausibly = Session B analysis + Session D synthesis (583 of the DB's 1,040 live rows
sit here — by far the largest book); `Essays` (only 11 rows, 1 section-type) is presumably the
per-word Session C study, but is nearly empty relative to the size of the registry; `Detail design`
(189 rows, spanning `session_a` through `session_c` in the current `book_stage_map`) doesn't
obviously correspond to any of the three published orders on its own. This is a genuine open
question for the plan to resolve, not guessed at here.

---

## 4. Disciplines that already govern *any* prose authored in this programme

Chapter 3 states four disciplines that apply across every phase above, not specific to any one of
them — these are the nearest thing that exists today to programme-wide "authoring rules," though
none of them touch style, section-transition, layout, or naming-convention territory:

- **Traceability / evidential warrant** — every claim is one of three things: a **finding** (traced
  to a specific verse, term, lexical source, or extract field), a **hypothesis** (not traceable —
  labelled or discarded), or **inferential** (plausible, not yet directly supported — retained,
  labelled, never silently promoted to a finding without evidence). "The verse leads... the verse
  is never bent to fit a pre-existing category." Governs the content of what gets written, at every
  phase.
- **The two-AI division** — Claude AI authors (drafts, interprets, judges); Claude Code operates
  (persists, executes, never originates analytical content). "An instruction that crosses the
  boundary... is a breach of the architecture, not a shortcut."
- **Session continuity / memory discipline** — obslog captures as work happens; session log is the
  handoff; a fresh, version-confirmed extract is the working source for the next pass; nothing
  substantive exists only in chat or only in memory.
- **Researcher decision authority** — every substantive output is reviewed and either accepted,
  corrected, or rejected by the researcher before it stands; "Claude AI... did not decide."

---

## 5. The mechanical/storage layer — what the architecture document actually covers

Condensed, since the full document is already on file
([docs/prose-store-architecture.md](../../docs/prose-store-architecture.md)) and v4 (superseded)
worked through it in detail. This is the **"how it's stored" layer** — a small, real part of the
whole picture, not the whole of it:

- Four tables + an FTS5 index: `prose_section_type` (the dictionary of section handles),
  `prose_section` (the content, one row per authored body), `prose_section_fts` (search), two link
  tables to dimensions/findings (both declared, both empty).
- `status`: `draft` → `in_review` → `approved` → `archived` (CHECK-constrained; only `draft` and
  `approved` are used in practice today — confirmed live: 0 rows at `in_review`).
- `author`: `claude_ai` / `claude_code` / `researcher` (CHECK-constrained).
- Supersede-only discipline: a revision is a new row, never an edit — except `session_a_replace`
  (Session A's mechanical extracts only, gated on `author='claude_code'`).
- Two-patch authoring pattern: `CATALOGUE_POPULATION` creates the section-type handles a chapter
  will use; `PROSE` fills them with content, referencing handles by code.
- Retrieval: extracts (JSON/MD/DOCX), FTS5 search, chapter export/import round-trip for hand-editing.

This layer is real and load-bearing, but — as the researcher's own framing puts it — it is a slice
of process management, not the definition of prose management.

---

## 6. What the live record does *not* yet answer — surfaced, not guessed at

Four gaps, stated plainly so the plan can address them deliberately rather than by omission:

1. **The three creation modes** (author from scratch / convert other documents to align style /
   capture from analytic findings) are only partly visible in what's been read. "Capture from
   analytic findings" clearly maps onto the Session B → Session C chain above. "Author from scratch"
   plausibly describes the programme-wide chapters (drafted by Claude AI under researcher
   direction, per Ch3). **"Convert other documents to align style" has no described process
   anywhere in Chapters 1–3.** The only trace of it found in the live database is two untagged
   `prose_section_type` rows — `src_logos` and `src_aichat`, both `source_stage='contributor'`,
   both described in their own `description` field as *"capture once → route many"* — which reads
   like an intended intake point for exactly this mode, but nothing in the read sources documents
   what it does or how it connects to the rest of the chain.
2. **Style / authoring rules** (section transitions, layout consistency, naming conventions) are
   not stated anywhere in Chapters 1–3, and the architecture document doesn't cover them either —
   confirmed against neither source, not assumed absent. A style-method document existed once
   (`wa-sessionc-cluster-style-method`, Session-C-specific) but is archived, superseded by the
   2026-06-25 method reset; nothing replaced it.
3. **"5 books"** — the live database names 4 (`Programme`, `Detail design`, `Findings`, `Essays`).
   Whether the 5th is `Contributor` (the two untagged `src_*` types above), a book not yet created,
   or a different way of counting than `book_label` currently reflects, is unresolved.
4. **How the three published-output orders (§3) map onto the four live book labels** — no source
   read states this mapping; §3 above shows the sizes don't obviously line up 1:1.

---

*Next: plan components build out from this capture, researcher-led, per instruction on escalation
#784.*
