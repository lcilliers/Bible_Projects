# Prose management — essence capture (v2)

**Escalation #784** (the vehicle for this whole planning process). **Still a capture, not a plan.**
Supersedes v1 — same two sources, corrected per researcher feedback 2026-08-22: the IBA-stage
mapping in §2, the book count in §3/§6, and a caveat now stated up front that v1 didn't carry.

---

## 0. The double-edged sword — stated plainly, because it's the central difficulty here

Researcher, verbatim, on reading v1's capture of Chapter 3: *"chapter 3 needs revision. it refers to
old and out of date terminology... We have a double edge sword at hand - we trying define how prose
management should work by reading stale prose management sections."*

**This is worth stating as its own finding, not folded quietly into a correction.** The two sources
this capture draws on are themselves prose held under the very system being designed — and the
researcher's own rewrite-in-progress (Programme chapters 1–3, intended, but only 1–2 actually
finished) means the boundary between "current, trustworthy source" and "stale, needs-rewrite source"
sits *inside* the material being read, not outside it. Confirmed scope of the staleness, researcher's
own words: **assume every book is stale except Programme chapters 1 and 2.** That includes the rest
of the Programme book (chapter 3 onward), and all of `Detail design`, `Findings`, and `Essays`
wholesale.

Consequence for this document: §1 and §4 below draw on Chapter 3. They are now flagged, not
withdrawn — read as a record of the *old* framing, useful as a starting point, not as settled
current truth, until Chapter 3 is rewritten.

---

## 1. What "prose" is, in this programme's own words — ⚠ sourced from Chapter 3, now flagged stale

Not documentation *about* the research — it is stated to be **the research's memory**:

> "The programme's analytical memory lives in the database... The database is where the programme's
> findings, interpretations, and analytical output are kept. It is not a storage layer beneath the
> research; it is the research's memory." (Ch3, *Session continuity and memory discipline*)

Three properties are stated as what prose **must be**:

> "The prose is self-contained — readable without the session that produced it; scoped — clear about
> what it refers to (registry, cluster, group, dimension, or programme-wide); and grounded — clear
> about the evidence it rests on." (Ch3, *Session continuity*)

This is the closest thing the old prose has to a stated *authoring principle*. Whether it survives
Chapter 3's rewrite unchanged is open — flagged, not assumed.

---

## 2. The production chain — corrected: 5 handles, mapped to current IBA-stage terminology

Chapters 1–2 (current, trusted) still describe the phase structure prose is produced within — Ch2's
*Programme flow* names six phases (Session A, Verse Context, Dimension Review, Session B, Session C,
Session D); prose is authored at five of them (Verse Context and Dimension Review classify and
dimension verses but don't themselves produce a prose order).

**Fix applied, per instruction — "config already provides the mapping between phase terminology in
IBA and the session terminology":**

> `governance.programme_stages` (`cfg_setting`, verbatim): *"The research programme has three main
> stages: Base_data (STEP through lexical); Analysis (deriving understanding of the inner being);
> Publishing (essays and output for the results). Previously referred to as Session A (base data),
> Session B/D (analytics), Session C (publishing) — methodologies and processes have changed
> materially over time across all three."*

| # | Old session terminology | What the prose at this handle *is* | Who authors it | IBA stage (`governance.programme_stages`) |
|---|---|---|---|---|
| 1 | **Session A** | The listing of extracted STEP data — terms, verses, lexicon entries. Mechanical, reproducible. | Claude Code (`author='claude_code'`) — the one stage permitted in-place update (`session_a_replace`) | **Base_data** |
| 2 | **Session B** — two orders, same stage: *Readiness* (the pre-analysis data extract: groups, dimensions, anchor verses, cross-references, term flags) and *Analysis* (the standing-catalogue findings + SD pointers) | Data extract, then analytical findings | Claude Code (Readiness, mechanical) / Claude AI (Analysis, judgement) | **Analysis** |
| 3 | **Session C** | Reader-facing per-word study, v1→v2→v3 lifecycle | Claude AI | **Publishing** |
| 4 | **Session D** | Cross-registry synthesis, built from the accumulated SD-pointer record | Claude AI | **Analysis** (grouped with Session B per the config's own text — "Session B/D (analytics)") |
| 5 | **Programme-wide** | The self-description of the programme itself | Claude AI, researcher direction | *Not named in the 3-way split* — the config's three stages describe the per-word pipeline; programme-wide self-description sits outside/across it. Not forced into one of the three here — flagged, not guessed. |

**How each order reaches the database**, general across all five (Ch3): Claude AI writes an
**obslog** as work happens; the researcher reviews it; Claude Code parses it into the database
through the Phase 2 writer pipeline (pre-write backup, transactional commit, post-write validation).
Session A is the sole exception, permitted direct in-place update because it carries no judgement to
review.

---

## 3. Three orders of *published* output — book count corrected

Ch2 *Publishing* names three orders: **per-word study** (Session C), **cross-word synthesis**
(Session D), **programme-level account** (assembled once cluster syntheses exist).

**Correction, researcher 2026-08-22:** the live database's 4 `book_label` values (`Programme`,
`Detail design`, `Findings`, `Essays`) are not a typo of "5" as v1 flagged — there genuinely are
**5 books**, but only 4 are in prose yet. **Book 5 is `Concordance` — not yet in prose, to be added
later.** No open question remains about the count; what remains open (unchanged from v1) is how the
three *published-output* orders map onto the *book* structure — still not stated anywhere in the
sources read, and now additionally uncertain because `Detail design`/`Findings`/`Essays` are exactly
the books flagged stale in §0.

---

## 4. Disciplines that already govern prose authorship — ⚠ also sourced from Chapter 3, now flagged stale

Unchanged from v1, carried forward with the same flag as §1: traceability / evidential warrant
(finding vs. hypothesis vs. inferential), the two-AI division (Claude AI authors, Claude Code
operates), session continuity (obslog → patch → DB), researcher decision authority. Real, and likely
durable given how load-bearing they are elsewhere in the programme's live governance — but drawn
from the now-flagged chapter, so not asserted as settled without Chapter 3's rewrite confirming them.

---

## 5. The mechanical/storage layer — unchanged from v1

Condensed from [docs/prose-store-architecture.md](../../docs/prose-store-architecture.md), the "how
it's stored" layer: 4 tables + FTS5, `status` draft→in_review→approved→archived, `author`
claude_ai/claude_code/researcher, supersede-only discipline (`session_a_replace` the one exception),
two-patch authoring pattern, extract/search/export/import retrieval tools. Real, but a slice — not
the definition of prose management.

---

## 6. Open gaps — updated

1. **"Convert other documents to align style"** — still no described process in any source read.
   The only DB trace remains the two untagged `Contributor source` section-types (`src_logos`,
   `src_aichat`, own description *"capture once → route many"*).
2. **No live style/authoring-rules document** — unchanged; the one that existed
   (`wa-sessionc-cluster-style-method`) is archived, pre-reset.
3. ~~"5th book unidentified"~~ — **resolved**: `Concordance`, confirmed by researcher, not yet
   populated.
4. **Published-output-to-book mapping** — still open, and now compounded: the books it would need to
   map onto (`Detail design`/`Findings`/`Essays`) are themselves flagged stale (§0), so resolving the
   mapping and rewriting the content it points at may need to happen together, not in sequence.
5. **New, from §0**: nearly the entire body of existing prose (everything except Programme ch. 1–2)
   is stale source material for the very design exercise reading it. Any conclusion drawn from
   `Detail design`/`Findings`/`Essays` content, or from Programme chapter 3 onward, needs that
   caveat attached until rewritten.

---

## 7. Chapter exports produced this round, for review

Per instruction, re-ran the current (rebuilt) export script — confirms it runs clean against live
data, not just against chapter 1's existing 2026-08-14 export:

- `outputs/markdown/prose-edit-programme-chapter-2-20260822.md` (7 sections)
- `outputs/markdown/prose-edit-programme-chapter-3-20260822.md` (6 sections)

(Chapter 1's export already exists: `outputs/markdown/prose-edit-programme-chapter-1-20260814.md`,
2026-08-14, pre-dates this session's rebuild — not re-run, since chapter 1 isn't in question.)

---

*Next: plan components build out from this capture, researcher-led, per instruction on escalation
#784.*
