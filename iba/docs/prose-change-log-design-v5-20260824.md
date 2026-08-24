> **Superseded by [prose-change-log-design-v6-20260824.md](prose-change-log-design-v6-20260824.md).**
> Kept on disk for history only.

# Prose change log design — versioning integrity (#836)

Supersedes: [prose-change-log-design-v4-20260824.md](prose-change-log-design-v4-20260824.md) (v1–v4
kept on disk for history). New this round: §16 — research into established editorial/versioning
practice and AI-authorship discipline, requested directly by the researcher to help settle §10
("I don't really know how to approach §10"), rather than deciding it from this project's precedent
alone.

Status: still **design/analysis only**.

---

## 16. Research: named industry patterns for this exact problem (2026-08-24)

### 16.1 §10's Model A is a named, standard pattern — not a homebrew idea

Model A (mutate the current row in place; a paired history table captures what it looked like before
each change) is the working definition of **system-versioned temporal tables** — a real SQL standard
feature (SQL:2011), implemented natively in SQL Server, PostgreSQL, MariaDB, and Oracle. The way it's
described directly answers the mechanical question §10 raised: *"there's no special coding... you
simply use INSERT, UPDATE, and DELETE statements just like on any non-versioned table"* — the
application (or its write layer) does plain updates on the current-state table; a paired history
table captures the prior row automatically. One source frames it plainly as *"automatic auditing with
every change recorded... replacing hand-rolled SCD logic."*

The older, insert-a-new-row-per-version approach — data warehousing's **Slowly Changing Dimension
Type 2** — is structurally closer to Model B (today's `prose_section` shape: a new row per version,
tracked by `ValidFrom`/`ValidTo` or the equivalent chain fields). Both patterns are legitimate and
widely used; the field distinguishes them on **what "when" means**: temporal tables record *when the
system recorded the change*, while SCD2 is built to track *when the change was actually true in the
real world* (useful when a correction is backdated, or a fact's real-world validity period differs
from when it was entered). Worth one direct check with the researcher: for prose, is "when we applied
the edit" the only meaning of "when" that matters, or is there a case where prose needs to say "this
text was the correct/valid content as of an earlier real-world date, even though we're only recording
it now"? If not — and nothing in this thread has suggested it — Model A/temporal-table semantics are
the right fit, and this closes §10 as **decided in favour of Model A**, on the strength of it being
the standard, current pattern for exactly this problem, not just this project's own prior precedent
(escalation history).

SQLite has no native temporal-table feature to lean on — §11–§13's hand-built current+history table
pair is the correct way to get the same effect without it, and is exactly what the research describes
those engines' native feature as doing under the hood.

### 16.2 The bulky-body concern (researcher's original worry) — a real answer beyond "move it out"

v4 decided *where* prior text lives (history, not the live table) but not *how cheaply* it's stored
there. MediaWiki's revision-storage design is a directly relevant, battle-tested answer to the
researcher's original concern (bulky, slow to search, bloated indexes) at genuinely large scale:
**store the first revision of a page's text in full; store every following revision as a diff against
the previous one; gzip the result.** This combination reaches roughly a 98% compression ratio in
production. Two separable techniques worth naming individually, not as one bundled decision:

- **Compression alone** (gzip the stored `body` text in `prose_section_history`) — cheap, low-risk,
  no reconstruction logic needed (a version is still stored whole, just compressed on write and
  decompressed on read). Prose text compresses well. This alone captures a large share of the benefit
  with almost none of MediaWiki's complexity.
- **Diff-based storage** (store only the change from the previous version, reconstruct on demand by
  replaying diffs from a base) — the larger structural win MediaWiki actually relies on, but real
  engineering complexity: a diff/patch mechanism, reconstruction logic, and correctness testing that
  the *current* version can always be rebuilt exactly. Justified at Wikipedia's edit-volume scale;
  likely premature for this project's scale even under §0's "years of active editing" framing — a
  prose section being edited dozens of times over years is a very different volume than a wiki page
  edited thousands of times.

**Recommendation:** adopt compression now (folds cleanly into §13.1's `body` column — store it
compressed, decompress on read — no schema change beyond that), and record diff-based storage as a
named future option in §17 rather than building it now — worth revisiting only if actual version
counts per section grow large enough in practice to justify the added complexity, which isn't
knowable yet at this stage.

### 16.3 AI-assisted authorship/editorial practice (2026) — validates, doesn't change, what's already built

Current publishing-ethics guidance (Committee on Publication Ethics, cited across multiple 2026
sources) is clear on one point relevant here: AI cannot hold "authorship" in the accountability sense
— a human must own and be able to stand behind the output at every stage — and any AI contribution
should be disclosed and distinctly tracked, not folded silently into "who wrote this." This maps
directly onto a distinction already present in this project's schema and already carried into §13's
design, worth stating explicitly rather than leaving implicit: `author` (whose authorial voice the
text represents — `claude_ai`/`claude_code`/`researcher`) and `approved_by`/`approved_at` (who is
accountable for having signed off) are already two different fields, and §13's `changed_by` (who/what
technically executed this specific change — which may be Claude Code applying a researcher-approved
patch, distinct from either `author` or `approved_by`) is a third, correctly separate concept. No
design change follows from this — it confirms the three-way separation already proposed in v4 is the
right shape, rather than something to collapse into one "who" field for simplicity.

### 16.4 What this resolves, what's still open

- **§10 (Model A vs B): resolved in favour of Model A**, grounded in the temporal-tables precedent
  (16.1) — pending the one direct check above (does "when" ever need to mean real-world-valid-date,
  not just when-we-applied-it). If the answer is no, §11–§13's Model A design stands as filed.
- **§13.1's `body` storage: refine to store compressed**, per 16.2 — a small addition to the already
  proposed column, not a redesign.
- **New, named-but-deferred item for §17:** diff-based storage for `prose_section_history.body`,
  recorded as a future option if edit volume grows enough to justify it — not building now.
- **16.3 is confirmation only** — no open item.

---

## 17. Still open

- The one direct question in 16.1 (real-world-valid-date vs system-recorded-date) — answer needed to
  finally close §10.
- `change_reason` vocabulary's exact value list (carried from v4 §15).
- Diff-based storage for `prose_section_history` — named as a future option (16.2), not scheduled.
- Everything else carried from v4 §15, unchanged.

---

**Sources consulted this round:**
- [Temporal Tables in SQL Server Explained](https://sqlspreads.com/blog/temporal-tables-in-sql-server/)
- [Temporal Table Usage Scenarios — SQL Server | Microsoft Learn](https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-table-usage-scenarios?view=sql-server-ver17)
- [Temporal tables vs Slowly Changing Dimensions: The Real Data History Problem](https://sivaro.in/articles/temporal-tables-vs-slowly-changing-dimensions-the-real/)
- [Using Temporal Tables for Slowly Changing Dimensions — Tim Mitchell](https://www.timmitchell.net/post/2019/04/02/using-temporal-tables-for-slowly-changing-dimensions/)
- [The influence of Wikipedia on MediaWiki's architecture (AOSA)](https://aosabook.org/en/v2/mediawiki.html)
- [Manual:Revision — MediaWiki](https://www.mediawiki.org/wiki/Manual:Revision)
- [AI Policies in Academic Publishing: 2026 Guide & Checklist](https://www.thesify.ai/blog/ai-policies-academic-publishing-2026)
- [AI-Assisted Writing in Scholarly Manuscripts: What Authors Must Know](https://www.rstjournal.com/updates/ai-assisted-writing-in-scholarly-manuscripts-what-authors-must-know)
