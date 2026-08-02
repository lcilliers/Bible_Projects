# Token-consumption diagnostic — what actually drove the 2026-07-30 daily+weekly cap exhaustion — 2026-08-02

Researcher's question: exactly what consumed Claude Code tokens during the Hosea work, and why did
it spike fast enough to exhaust both the daily and weekly allowance and force a two-day stop.
Answered by measuring the real on-disk output of that day's work (file sizes = a hard floor on how
much text was read and written through the conversation) and cross-checking against one real,
measured figure — the Hosea `report.book_narrative_generate` API call's actual token count — to
calibrate a chars-per-token ratio for this content, rather than guessing one.

## Two separate resource pools — only one of them is what got exhausted

- **Claude Code's own subscription usage** (the daily/weekly caps that were hit) — driven entirely
  by *this* conversation's own tool calls: every `Read` of a file, every `Edit`/`Write`, every reply
  generated.
- **`report.book_narrative_generate`'s Anthropic Messages API calls** — a *separate* API-key spend,
  billed in real USD, logged to `narrative-generate-usage.csv`. These do **not** draw on the Claude
  Code subscription caps at all.

The 2026-07-30 ledger shows 5 live narrative-generate calls that day (Dan $1.19, Joel $0.35, Mic
$0.51 + a $0.50 regenerate, Hos $0.79 — **$3.32 total, real API spend, irrelevant to the cap
exhaustion**). Worth ruling out explicitly since it's the most visible "AI cost" in the session log,
but it is not the mechanism — the debate-fill work is.

## Calibrating a real chars-per-token ratio

Hosea's narrative-generate call assembled a package of the 14 filled debate files (600,058 chars) +
`WA-hos-whole-book-read.md` (61,963 chars) + the two guidance docs (15,394 chars) = **677,415 chars**,
and the API's real measured usage was **231,610 input tokens**.

**677,415 / 231,610 ≈ 2.92 chars/token** for this content (denser than plain-English's usual ~4:1 —
markdown structure, Hebrew/Greek terms, citations tokenize less efficiently). Cross-check on the
output side: narrative file is 19,450 chars / 2.92 ≈ 6,661 estimated tokens vs. 6,366 actually
measured — within 5%. This ratio is used below for every other file-size-to-token estimate; treat
these as good approximations, not exact counts (Claude Code exposes no per-turn token telemetry to
scripts, so file size is the best available proxy — see the prior conversation turn on engine
instrumentation limits).

## What was actually read and written through the conversation — Hosea

| phase | chars | ≈ tokens |
|---|---:|---:|
| 14 `hos-N-verse-span-meaning.md` extracts (read in full, chunked where oversized) | 1,161,059 | ≈397,600 |
| 14 `WA-hos-N-debate.md` scaffolds (fully generated, verse by verse) | 600,058 | ≈205,500 |
| `WA-hos-whole-book-read.md` (gathered + hand-resolved) | 61,963 | ≈21,200 |
| **Hosea subtotal** | **1,823,080** | **≈624,300** |

This is a **floor**, not a ceiling: it counts only the text that ended up persisted to disk. It
excludes every bit of deliberation spent producing each verse's Observation / Operation /
Subject-Source-Target / eleven Interrogative questions / Decision (Hosea has ~197 verses across 14
chapters) that never gets saved anywhere — reasoning tokens are real and billed, but leave no file
to measure.

## Why "sudden" — Hosea didn't happen alone

Hosea was not an isolated event. Git history for 2026-07-30 (all times BST):

| time | commit | what |
|---|---|---|
| 05:37 | `1c4f2b23` | config-system audit + remediation (Phases 1-4) |
| 09:47 | `f40fdce6` | CONFIG-REPORT restructure, cfg_utility, lexiconparse config-driven, CSV bug fix |
| 11:09 | `5a9584ab` | escalation backlog cleared; `report.book_narrative_generate` **built** (new code) and proven live on Daniel + Joel |
| **14:51** | `0096332f` | **Micah (7 ch) complete end-to-end** — extracts read, debates filled, whole-book-read, narrative |
| **17:29** | `3772c2c8` | **Hosea (14 ch) complete end-to-end** — same full cycle |
| 18:36 | `473b71fb` | session close |

Micah's own footprint, measured the same way:

| phase | chars | ≈ tokens |
|---|---:|---:|
| 7 extracts | 1,109,513 | ≈380,000 |
| 7 debate files | 325,433 | ≈111,400 |
| whole-book-read | 37,623 | ≈12,900 |
| **Micah subtotal** | **1,472,569** | **≈504,300** |

**Micah and Hosea ran back to back in the same unbroken stretch — 11:09 to 17:29, about 6 hours 20
minutes — with no session-boundary reset between them.** Combined: **≈3,295,649 chars, ≈1,128,600
tokens** of raw extract-reads and debate-writes moved through one continuous context, on top of a
morning of config-audit conversation and new pipeline code (narrativegenerate.py + handlers) built
and reviewed in the same session before either book started.

Two compounding effects on top of that raw total, neither reducible from file sizes alone:
1. **No context clearing between chapters or between books.** Every later chapter's turn carries
   the full accumulated history of every earlier chapter still sitting in context (until
   auto-compaction fires — which itself costs tokens to summarize, then keeps accumulating again).
   By Hosea chapter 14, the conversation was still holding essentially all of Micah's ~504K-token
   footprint plus Hosea's own chapters 1-13.
2. **Daily/weekly caps are calendar-based, not conversation-based.** Whether Micah and Hosea were
   technically one continuous conversation or several back-to-back ones on the same day makes no
   difference to the cap — two full books' worth of extract-read + debate-fill + whole-book-read,
   plus a morning of config/dev work, all landed inside one ~13-hour calendar window.

## Answer

The spike wasn't Hosea being unusually heavy per chapter — Micah's per-chapter footprint is
comparable. It was **two entire books' full pipelines (21 chapters total) plus a session of new
pipeline-code development, compressed into one calendar day with zero context-clearing checkpoints
between any of it.** ≈1.13M tokens of persisted read/write content alone, before counting
unpersisted reasoning tokens or the compounding cost of carrying forward already-processed chapters.
This directly corroborates the session-boundary proposal from the prior conversation turn (cap
scope per session, e.g. 3-4 chapters, checked against `passage.debate_status` to resume cold) — the
lever is bounding what goes into a session before the fact, since nothing in the engine can measure
or throttle it after the fact (see the prior turn's finding: the debate-fill step is never dispatched
through `run.py`, so it has no engine-side visibility at all).

## Follow-up — is the pipeline "document-first" when it should be "element-first"?

Researcher's next question, prompted by re-reading this diagnostic: it looks like the same data
gets recycled because the .md files are mechanically assembled from components and the whole
document has to be passed around to build the next one — would storing each analytical element in
the DB and assembling documents only from the elements a given document actually needs be more
efficient? Checked against the live code (`iba/app/lib/passagedebatereport.py`,
`iba/app/lib/wholebookread.py`, `iba/app/lib/narrativegenerate.py`), not reasoned from the doc
descriptions alone:

**The observation is correct as an architecture finding.** `passage` (the only table tracking
debate state) stores nothing but paths and a status flag — `debate_path`, `debate_status`,
`verse_span_meaning_path`. The actual interpretive content (Observation / Operation / 11
Interrogatives / Decision per verse, Emergent-questions log, Passage-level-linkages) exists **only**
as free text inside the `.md` files, never as DB rows. Two concrete places this shows up:

- `wholebookread.py:107` — `write_scaffold` re-parses every filled debate file with a regex heading
  match (`_EQ_HEADING_FALLBACK` and siblings) to pull out just the Emergent-questions/Linkages
  sections — fragile enough that the module's own docstring catalogues four different heading
  spellings across the corpus it has to tolerate.
- `narrativegenerate.py:90-125` (`gather_book`/`assemble_package`) — reads every filled debate
  file's **full raw text** (`path.read_text()`) and concatenates it verbatim into the API request
  body. Nothing is filtered or curated; the model receives the complete scaffold structure
  (headings, HTML-comment placeholders that happened to survive, the lot) for every verse of every
  chapter.

**But this is not the mechanism that exhausted the Claude Code caps.** Both of the above run as
plain Python file I/O inside a dispatched `run.py` step (`report.whole_book_read`,
`report.book_narrative_generate`) — the 600KB+ of debate text gets read by the *script*, not by
this conversation. It never enters Claude Code's own context; only a one-line outcome message comes
back. `narrative_generate`'s re-ingestion of full debate text costs real API dollars (it's the bulk
of the 231,610 input tokens on Hosea's live call, at $3/M — a few tens of cents of waste, resending
scaffold structure the model doesn't need) — a genuine, fixable inefficiency, but in the **separate,
already-cheap, already-metered pool**, not the one that forced the two-day stop.

**What actually drove the Claude Code cap** — established above — was this conversation's own
`Read` of each raw lexical extract and its own `Edit`/`Write` of each debate's interpretive content,
once per chapter, 21 chapters in one unbroken sitting. That work is not redundant and does not
disappear under an element-first redesign: producing the Observation/Operation/Interrogative/
Decision judgments for ~197 verses still requires an AI to read the source verse data and generate
that analysis exactly once, wherever the result is ultimately stored. Storing it as DB rows instead
of markdown would not shrink the read-the-source / write-the-analysis step itself.

**Where an element-first redesign would genuinely help, and where it wouldn't:**

- Would help: `report.book_narrative_generate`'s real API cost (assemble only the fields the
  narrative task needs, not whole scaffold files) and `report.whole_book_read`'s robustness (a
  structured query instead of regex heading-matching four different historical spellings).
- Would not help: the Claude Code cap itself. The one place this conversation *does* revisit
  already-produced content a second time is resolving whole-book-read's carried-forward items
  (re-engaging with Emergent-questions content generated earlier the same session) — a real but
  secondary contributor next to the 21-chapters-of-primary-reads-and-writes total above.

**Net assessment:** worth doing on its own merits (cheaper narrative-generate calls, more robust
whole-book-read) if the researcher wants to invest in it, but it should not be mistaken for a fix to
the problem that actually caused the stoppage. The session-boundary cap remains the lever for that;
an element-first DB redesign is a separate, smaller, orthogonal improvement to a pool that was never
the bottleneck.
