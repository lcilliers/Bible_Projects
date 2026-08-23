# Escalation #784 — Prose Management: full conversation capture

**Purpose of this document.** Escalation #784 has run 34 versions across two days (2026-08-21 to
2026-08-23) and has been, by the researcher's own description, "an important conversation, albeit
very fragmented." This document captures it coherently — every thread of thinking, every finding,
every correction, every open question — without summarising away the substance and without proposing
solutions, comparisons, or builds beyond what was actually done in the moment. That work "will come
later." This is a record, not a plan.

It draws on the full escalation history (`Escalation.ps1 -Action History -Id 784`) and the actual
conversation, since some of the researcher's own framing carries more in the original wording than
the compressed escalation log entries do.

---

## 1. How the escalation started, and how its scope grew

**v1** (researcher): *"This item describe the design and build of Prose in the project and build the
management of prose into the IBA App."*

**v2** (researcher): asked for an inventory of every file in the project with "prose" in its name,
filed to `research/discovery/`.

**v3** (Claude): delivered the inventory — 269 files across 11 top-level directories, plus 6
directories carrying "prose" in their own name. Filed:
`research/discovery/prose-files-inventory-20260821.md`.

**v4–v5** (researcher): pointed at the architecture document (`docs/prose-store-architecture.md`)
and the four operative scripts (`build_programme_prose_extract.py`, `export_prose_chapter_edit.py`,
`import_prose_chapter_edit.py`, `search_prose.py`).

**v6** (researcher): *"Chapters 1–3 has already been rewritten to align the project description
with the latest methodologies and management processes. next task is to extract from IBA all
configs that is related to prose."* (Note: this "chapters 1–3 rewritten" claim was later corrected
by the researcher themselves — see §5 below — to actually being chapters 1–2 only.)

**v7** (Claude): extracted every `cfg_*` row in `iba.db` mentioning "prose" — `cfg_prose_chapter` (7
rows), `cfg_prose_concept` (2 rows), 15 `cfg_utility` rows, plus the full `prose_section`-family
`cfg_table`/`cfg_column`/`cfg_unique` catalogue. Headline finding: **all 15 prose-related
`cfg_utility` scripts, including the 4 named ones, were `inactive=1`** — mostly under escalation
#729 ("dormant, not exempt"), four of them also open `NON-COMPLIANT` under escalation #648. Filed:
`research/discovery/prose-config-extract-20260821.md`.

**v8** (researcher, verbatim instruction): *"staying in #784 you have rightly identified that the
tables, columns and scripts are not incorporated in IBA. activate the 4 scripts, make them
compliant, activate the tables and columns, and align it with the architecture."* This set the scope
for the whole build/plan effort that followed: reactivate the 4 scripts, fix their non-compliance,
incorporate the `prose_section` table family into IBA's operating config, align with the
architecture document.

---

## 2. The plan built progressively (v1 → v3 of the plan document) — and why that stopped being acceptable

Working from v8's instruction, Claude built code first, then a build plan, revising it three times as
each round surfaced something new:

- **Plan v1** (escalation v9): code written and tested live (`iba/app/lib/prosestore.py`,
  `iba/app/handlers/prose.py`, `iba/app/ps/Prose.ps1`, the 4 scripts rewritten to call into it). 13
  approval-gated config changes identified, not yet applied.
- **Plan v2** (escalation v11), after researcher pushback (v10, verbatim): *"#787 has no comment, no
  next-action, and no related_activity. This is a serious deviation from escalation config rules...
  your plan language and use of words and description is not easy to read... Note that prose
  management is not a utility, it is a full scale module of the project... every time you suggest to
  not do something, or decide to do it, quote the governance rule you are complying or the missing
  governance rule."* This produced: a real bug found and fixed as its own escalation (**#790** — the
  dispatcher's `raise_()` function skipped `cfg_escalation_requirement` entirely, affecting every
  dispatcher-raised escalation project-wide, not just prose; fixed, tested, approved); a full
  rewrite of the plan in plain language with literal config wording; a re-framing of prose as a
  module, not a utility, per `governance.module.config`; and a first audit of the architecture
  document's rules against config coverage — five rules found with no config backing at all (status
  CHECK values, author CHECK values, the `session_a_replace` exception, the two-patch pattern,
  supersede-only discipline).
- **Plan v3** (escalation v14): closed out `prose.extractor_version` (researcher decision: it labelled
  the tool's own version, controlled nothing, dropped from code entirely rather than config-driven);
  fixed a mis-apply of escalation #787 (wrote `key=NULL` instead of the real key — cleaned up as its
  own escalation #796); surfaced a second dispatcher bug (#795: `approve`/`reject`/`revise` all
  collapsing to the same `completed` status).

**Why this stopped.** Escalation #795's build (part of a larger design, #798/#799) contained a named
test in its own approved spec that was never actually run before the build was reported complete —
found twice, once per half of the same function. This produced a new, standing governance rule
(`cfg_behaviour_rule`, `test-plan-per-module-utility`, anchored via escalation #828), researcher
verbatim: *"the test plan will be introduced case by case... but the test plan method... run through
after the design, and the results of the test must be included in the resolution of the build."* The
full cycle is now: **plan/propose/design (in detail) → approve → build per the plan → approve**, with
a test stage that is required, not optional, and whose results go into the resolution, not just
asserted in prose.

Researcher, opening the next round of #784, verbatim: *"784 will from now on follow the new
governance rules for plan/propose - approve - build - test approve... note that the current plan
looks like it was a progressive spec build spec build which is no longer accepted."*

---

## 3. Plan v4 — the full-scope replan

Claude reviewed v3, confirmed the task at hand (bring both the read side and the write side of the
prose store under real IBA governance — wider than v3's Part A, which only ever covered the read
layer), and filed **plan v4** (`iba/docs/prose-store-iba-incorporation-plan-v4-20260822.md`) as one
document covering:

- **I.** Finish the read-layer config (unchanged content from v3).
- **II.** Dispatcher-register the 4 read operations (v3 had held this back).
- **III.** Bring the write side (`apply_session_patch.py`'s 6 `prose_section` operations) under
  governance — status/author enums, write grants, behaviour rules for the 3 architecture rules v3
  found missing — scoped narrowly, explicitly not a full rearchitecture of `apply_session_patch.py`.
- **IV.** A correction to v3 itself: the 3 read-layer settings belonged in a dedicated `cfg_prose`
  table (matching the `cfg_passage` precedent for `governance.module.config`), not generic
  `cfg_setting` — a standard-violation fix, not a new judgement call.
- **V.** A 20-case test plan, required up front by the new cycle.

One explicit judgement call was flagged rather than decided: whether the write-grant for
`apply_session_patch.py`'s 6 operations should be one writer identity or six (the plan defaulted to
one, stated why, offered to build the finer-grained version instead).

Explicitly out of scope, stated rather than dropped silently: migrating the full `patch_type`
registry into `cfg_enum`, rearchitecting `apply_session_patch.py`, the architecture doc's stale
current-state table, escalation #786 (a sibling, not a child), escalation #739 (chapters 4–6,
separately tracked).

Plan v4 was filed for approval. **It was never approved — the conversation moved to a different
question before that happened**, and v4 was later explicitly set aside (§4).

---

## 4. The scope correction — prose management is not the mechanical layer

Researcher, directly challenging the frame of everything built so far: *"Prose management is the
process of creating, reviewing, exploring, & updating the contents of what is now 5 separate books...
The creating operation have different elements. Authoring from scratch, converting other documents
to align style, capturing from analytic findings. This authoring process runs before it reaches
prose, but is deeply dependent on the definition of style, authoring rules... what you currently are
looking at in the 'architecture' is a slice of process management, and largely defines the mechanical
structure, but it does not deal with the whole prose management."*

Claude investigated rather than immediately re-designing:

- **The "5 books" claim, checked live:** `prose_section_type.book_label` (a real column, not even
  in the architecture document's own schema table — added later) had only **4** populated values —
  `Programme`, `Detail design`, `Findings`, `Essays` — plus 5 untagged section-types (137 populated
  rows): 3 "Cluster Findings" types that logically belonged under `Findings` but were never tagged,
  and 2 "Contributor source" types (`src_logos`, `src_aichat`), each described in its own record as
  *"capture once → route many."* No 5th book was found live — asked rather than guessed.
- **Style/authoring-rule documentation, checked:** existed once
  (`wa-sessionc-cluster-style-method-v1_1`, `wa-sessionc-cluster-overview`) but both are **archived**,
  tied to the pre-reset Session C method superseded by the 2026-06-25 method reset. No live,
  current document governs style, section-transitions, layout, or naming conventions anywhere.

The researcher then answered the "5 books" question directly: *"I see also I said 5 books, it
currently only have 4. book 5 is not yet in prose (concordance) which will be added later."*

The choice offered — keep v4 as the explicitly-scoped-down mechanical/storage layer, with the
authoring-process layer split into its own follow-on, or pause v4 approval until the wider picture is
clearer — was answered decisively: *"i think we first need to design it and then how it works in IBA
will fall out of it."* **Plan v4 was set aside** (not discarded — its storage-mechanics content
was expected to survive; its config-shaped pieces did not, for the reason in §4a below).

### 4a. The `chapter_names` correction — a general design principle, not a one-off fix

Illustrating the design-first principle, the researcher caught a concrete flaw in v4 itself:
*"you adopted the chapters into the config with prose.chapter_names. actually what prose.chapter_names
should be is to link this with the columns in the table that contains it — simply because the tables
were designed that the chapter numbers sequence and names are data driven, not preset in configs."*

Checked and confirmed: `cfg_prose_chapter` (already in `iba.db`) already held `chapter` + `title` for
chapters 0–6 — the exact content v4 was about to duplicate into a static `prose.chapter_names` JSON
blob. Further, `prose.book_stage_map` had the identical flaw — `book_label` and `source_stage` already
sit on the same `prose_section_type` row, so the mapping v4 proposed as static config was already a
live `GROUP BY` away. **General principle stated and confirmed, not just a single fix**: config that
duplicates a table's own columns is a second, driftable copy of the same fact; this table family was
built specifically so structure *is* the data.

---

## 5. Essence capture — `prose-management-iba-v1`/`v2`

Per instruction — *"start a new md as prose-management-iba-v1. Capture the essence of what the prose
management is as from the architecture document, and by reading programme, chapter 1 - 3."* — Claude
read the architecture document and all 19 sections of Programme chapters 1–3 in full (not sampled,
~76,000 characters) and filed `iba/docs/prose-management-iba-v1-20260822.md`, capturing:

1. **What prose is**, in the programme's own words: *"the research's memory"* — not documentation
   about the research. Stated properties: prose must be **self-contained**, **scoped**, **grounded**.
2. **The production chain** — a distinct order of prose at each of 5 authored phases (Session A,
   Session B [Readiness + Analysis], Session C, Session D, programme-wide), what each order actually
   is, and who authors it.
3. **Three published-output orders** (per-word / cross-word / programme-level) and an open question:
   they didn't obviously map onto the DB's 4 live book labels (`Essays` had only 11 rows against
   `Findings`' 583).
4. **Four disciplines already governing all prose authorship**: traceability/evidential warrant
   (finding vs. hypothesis vs. inferential), the two-AI division, session continuity (obslog → patch
   → DB), researcher decision authority. Real, but none touch style, transitions, or naming.
5. **The mechanical/storage layer**, condensed, explicitly framed as one slice of the whole.
6. **Four open gaps**, surfaced not guessed at: the "convert other documents" creation mode had no
   described process anywhere read; no live style/authoring-rules document exists; the 5th book was
   unidentified; the published-output-to-book mapping was unresolved.

### Correction to v2 — reading Chapter 3 exposed the staleness problem directly

Reviewing v1's capture, the researcher found the ground itself had shifted: *"chapter 3 needs
revision. it refers to old and out of date terminology... We have a double edge sword at hand — we
[are] trying [to] define how prose management should work by reading stale prose management
sections... I see also I said 5 books, it currently only have 4."* And a further correction: *"I
started to rewrite programme from the start and thought I completed 1-3, but now it looks like only
1-2."*

**Filed `prose-management-iba-v2-20260822.md`, supersedes v1**, with:

- **§0, new**: the double-edged-sword problem stated as its own finding — the sources this capture
  reads from are themselves prose held under the system being designed. Confirmed scope of
  staleness, researcher's own words: *assume every book is stale except Programme chapters 1 and 2.*
  §1/§4 (drawn from Chapter 3) carried forward flagged, not withdrawn or re-asserted as settled.
- **§2 fixed** per instruction — *"Config already provides the mapping between phase terminology in
  IBA and the session terminology. fix that in §2."* Found the config:
  `governance.programme_stages` (`cfg_setting`), a 3-way split — *Base_data* (old Session A),
  *Analysis* (old Session B/D), *Publishing* (old Session C) — quoted verbatim in its own text.
  Restructured to the researcher's preferred 5 handles (A/B/C/D + programme-wide, B's two orders
  collapsed into one row), with the IBA-stage mapping applied; programme-wide left unmapped rather
  than forced, since the config's own text only describes the per-word pipeline.
- **§3 corrected**: 5 real books, 4 currently in prose, 5th = **Concordance**, not yet populated.
- **§7, new**: chapters 2 and 3 exported via the current rebuilt `export_prose_chapter_edit.py` for
  the researcher to read directly (chapter 1's existing 2026-08-14 export was left as-is).

---

## 6. File control — the write process

Per instruction to think it through deep — *"the process of writing and uploading is going to rely
deeply on working with the right md files. that means the controls around filing and file control
must be deeply ingrained. naming, location, archiving, files being worked on, location of support
material all need to be thought through"* — Claude filed `iba/docs/prose-file-control-v1-20260822.md`.

### The central finding

The architecture document said edit files were disposable: *"Temporary edit files may be discarded
after the patch has been reviewed and applied."* Tracing the code directly, `run_import_chapter`
writes the edit file's own path into `prose_section.source_file` — **permanently**, as the row's own
provenance, not a transient log line. **The documentation was wrong, not the code.** A file's
disposability turns entirely on whether it was ever imported — giving a 5-state lifecycle: exported
→ in edit → patch pending → permanent (never discard) → stale draft (safe to discard only if never
imported).

### Concrete gaps found

1. **Naming** — no `-v{n}-` component; a same-day re-export would silently overwrite.
2. **Location** — `outputs/markdown/prose-edits/` existed only as lived practice, undocumented
   anywhere. Named as a real open choice (add to `file-organisation-rules.md` vs. a `cfg_prose`
   setting), not decided.
3. **Archiving** — `apply_session_patch.py` already archives the *patch* on success; nothing
   extended that trigger to the *edit file* the patch was built from, even though the patch's own
   `source_edit_file` field already named it.
4. **"Files being worked on" visibility** — proposed reusing the prose-change-flag mechanism (§7
   below) rather than a third parallel tracking concept.

### Build + test round 1 — versioning and auto-archive

Researcher, resolving the open items directly: *"export need to put the file in the correct location
for editing, all files must be version controlled. the import must get the file from the editing
location, and on succesful update move the file to archive... currently the name of the file makes
it impossible to link the file with the book-chapter-session."*

Built and tested live in `iba/app/lib/prosestore.py`:

- `run_export_chapter` now names every export `{stem}-v{n}-{date}.md`, `n` scanned across both the
  active folder and its archive so a version is never reused.
- `run_import_chapter` computes the archive destination *before* building the patch and uses that
  archived path — not the pre-move path — as `prose_section.source_file`, then moves the file on
  success. The DB's provenance pointer is correct from the moment the patch exists, never briefly
  dangling.

Tested live (throwaway artifacts, cleaned up after, DB `prose_section` max id unchanged at 1040
throughout): exporting chapter 2 twice produced `v1` then `v2`, no overwrite; a type-id export with
a real book+chapter correctly used the chapter stem; a type-id export with no book at all correctly
fell back to an unbooked-section name; importing an unedited export produced a patch whose
`source_file`/`source_edit_file` both pointed at the archived path, confirmed by reading the written
JSON. `docs/prose-store-architecture.md` §8.1 was corrected to state the real (permanent,
auto-archived) behaviour.

### Build + test round 2 — the section is the editing unit, not the chapter

Researcher: *"there is lot of other thoughts they may conflict or improve previous comments. chapter
number are not unique across prose. each chapter can have multiples sections. the sections is the
editing unit. if a chapter export is exported then all the sessions [sections] n the chapter will
have to changfe version wich is not necessary. so book exports and edit exports is not the same thing
and is used differently."*

This surfaced a real bug, confirmed by re-reading the code: `run_import_chapter` built a `supersede`
operation for **every** section block in the file, unconditionally — `ps.body` wasn't even in the
row query, so nothing was ever compared. Confirmed live: the round-1 test's own unedited import had
generated 7 supersede operations despite touching nothing — harmless only because that patch was
never applied.

**Fixed:** the import now fetches `ps.body`, skips any block whose text matches the current row
exactly, and refuses outright (*"nothing to import"*) if every block is unchanged — correctly leaving
the file in place, not archived. Tested live: an unedited import was refused, file confirmed still
present; editing exactly 1 of 7 sections produced a patch with exactly 1 operation, matching the
edited section, file archived only on this real-change path.

Also confirmed rather than assumed: "book exports" (`run_extract`, read-only, no markers) and "edit
exports" (`run_export_chapter`, marker-bearing, round-trip) were already separate code paths, not
conflated; and chapter numbers not being unique across the whole prose store was already handled,
since the filename stem includes `book_label`.

### Delete / add / move — behaviour confirmed live, one real risk named

Researcher: *"what will happen if a whole section is deleted or added or moved."* Tested all three
directly rather than reasoned from the code:

- **Delete** (removed a whole block from the file): **silently ignored.** The removed section's DB
  row came back completely untouched — same version, `superseded_by_id` still `NULL`, no error, no
  warning anywhere.
- **Add** (a block with a fabricated section id): **refused outright** — *"section 999999 is not an
  active current prose row,"* whole import fails, nothing written. This tool has no path to
  originate a new section at all; that needs the separate two-patch flow, entirely outside this tool.
- **Move** (hand-edited the `CHAPTER_NO` marker): **refused outright**, same shape — *"marker
  CHAPTER_NO changed: file=3, database=2,"* whole import fails, file left untouched. No operation
  anywhere (this tool or `apply_session_patch.py`) relocates or reorders a section.

Add and move fail safely and loudly. Delete is the one real risk — the only one of the three that
tells you nothing at all. **Flagged as a genuine open decision, not built**: should a section
disappearing from an edit file trigger an explicit refusal (matching add/move), a warning, or an
actual retire/delete path, rather than today's silent no-op.

---

## 7. The prose-change-flag idea

Emerging from the delete-behaviour discussion, researcher raised a design consideration: *"I / we
need an easy way to switch any section from authorative/final to need attention. The flag could be
raised at any point e.g. a new finding is created, a methodology is changed, a keyword is changed and
the change can have an impact on multiple sections. the flag is not, fix it immediately, it is, the
section is no longer authorative, and why... do we simply use the draft / final flag on
prose-session-type?"*

Checked directly: `prose_section_type` has **no** draft/final flag at all — status lives on
`prose_section`, not the type/dictionary table. Reusing `prose_section.status` itself was flagged as
probably wrong: it's a forward authoring-progress axis (draft → approved), this is a different axis
(an already-approved section becoming untrustworthy from an external cause) — collapsing them loses
either the "was reviewed" fact or the "why flagged" reason, and the enum alone can't carry a reason or
a trigger link. Surfaced relevant existing-but-dead infrastructure: `prose_section_finding_link` and
`prose_section_dimension_link` — both real tables, declared and indexed, both 0 rows,
`prose_section_finding_link`'s FK pointing at the legacy `wa_session_b_findings` rather than the live
`finding` table.

Researcher context: the `Findings` book and its link tables are empty because prose hasn't been
seriously populated yet — a couple of experiments only, not neglect — and the researcher is heading
toward the analytics phase next, which is why this groundwork is happening now. The researcher's own
emerging design: *"Maybe the prose-change-flag table (not yet conceptualised) is the change engine.
when a change is generated that have an impact on existing prose it goes to the flag. when it was
applied in prose the flag is cleared."* Concrete test case: retiring Session A/B/C terminology
permeates throughout prose — register once as a flag, apply via regex. Stated problem, verbatim:
*"the problem is when it is discovered, and when it is fixed is different cycles and it is very easy
to forget."*

A relevant precedent was named, not proposed as the answer: `wa_quality_flag_types` +
`wa_data_quality_flags` already do type-dictionary + flag-instance-against-a-target-row + description
for term-level data-quality issues — closest existing shape, though it has no raised/resolved
lifecycle (only `last_changed`), so it doesn't solve the "different cycles" problem as-is.

**Decision recorded**: the researcher confirmed this existing structure/principle is the right shape
to reuse — no separate new table/channel needed. The table(s) may be extended (lifecycle fields,
targeting `prose_section`, one-change-affects-many-sections, the regex/apply mechanism) but the core
principle stands. Not built — parked for the analytics-phase detail design.

---

## 8. Chapter-rewrite assistance

Reviewing the current chapters directly (2 and 3 largely on target, terminology updates due,
principles sound), the researcher asked directly: *"I cannot visualise at this stage to employ AI to
make these chapter edits, except potentially for some regex update assistance in a interactive chat
operation. Do you think there is a way to configure IBA that I can point to a chapter and as AI to
rewrite it with the correct information from the latest info in the project?"*

Answered directly: not as a single push-button rewrite operation — that would cross the two-AI
division Chapter 3 itself states (Claude Code operating vs. Claude AI authoring), the same
architecture just confirmed as sound. A real, buildable version exists in the same shape as the rest
of the programme (mirroring Session B Readiness → Session B Analysis): Claude Code assembles a
mechanical briefing (a config-driven terminology scan — `governance.programme_stages` is already this
in miniature — flagging stale terms in a chapter's body); Claude AI authors the actual rewrite from
that briefing; the researcher reviews it through the existing export/import/patch toolset, unchanged.
Explicitly named as **downstream of the prose-change-flag design (§7), not a separate track** — the
briefing is the consumption side of "what changed, which sections, why."

---

## 9. The `Detail design` book — a factual correction to its own premise

Researcher, considering whether `Detail design` still serves a purpose now that IBA governs process,
and whether to delete it or export-and-move it outside the project to save space:

Checked live before responding — the premise didn't hold. `Detail design` is 189 rows, **6.4 million
characters — ~47% of the entire prose corpus** (13.68M characters total). Sampled, it is **not**
process/methodology documentation — it's real per-word Session A/B/C research output (mechanical
lexical extracts, analytical findings, published word studies) for specific registry words (mercy,
kindness, goodness, love, grace, etc.), plus cluster chapter drafts, all produced under the old
pre-reset method. **Not redundant with IBA** — IBA governs process; this is findings content.

What *does* match the researcher's original description (a single source of "how the project works,"
genuinely overlapping with IBA's own governance) is **Programme chapters 4–6** (Data architecture /
Data integrity & governance / Instruction corpus) — only 38 rows, ~132K characters, already flagged
`not_yet_aligned` in `cfg_prose_chapter`, already tracked separately as **escalation #739**
(on-hold). Also found: the actual governing instruction corpus (`wa-claudecode-instruction` etc.) was
never captured into the DB prose store at all — it exists only as the 21 git-tracked files in
`Workflow/Instructions/` (2.0MB) — no DB-vs-IBA duplication problem there either.

"Save space" was quantified: 6.4M characters is roughly 6MB against a 766MB database — under 1%, not
a meaningful driver either way.

The real, reframed question for `Detail design` — not answered, stated as the researcher's own call:
is old per-word Session A/B/C output, superseded by the 2026-06-25 method reset, worth keeping as
history/reference, or is it dead weight now that the method has moved on?

---

## 10. The two-book structural extracts

Requested directly: *"an extract and summary of the prose-section-type separate mds for the two
books, and not including the prose-section large text blobs."* Two files filed:
`iba/docs/prose-book-extract-detail-design-20260823.md` and
`iba/docs/prose-book-extract-findings-20260823.md`.

**`Detail design`**: 45 section-types, **26 of them (58%) never populated at all** — the entirety of
`session_b_phase9` (11 types, fully specced, never run) and `session_d` (10 types), plus the
superseded `sc_v1` (5 types). What is populated is a small, uneven pilot: 20 words got Session A; only
4 of those 20 got Session B; the Session C content that exists is 4 cluster-level drafts, not
individual word studies, running 15–20× over their own stated length targets.

**`Findings`**: the opposite profile — all 6 types populated, zero superseded, zero draft (100%
approved), zero `claude_ai`-authored (100% `claude_code`). 570 of 583 rows (98%) are `lexical_prose*`
content whose own descriptions name the current live method by name (`lexical-model-2026`,
`verse-first lexicals`, `method v1-20260702`) — **not legacy content**, contrary to how both books
had been getting grouped together as "stale" earlier in this same conversation.

The striking author/status uniformity in `Findings` was traced to its actual source rather than left
as an open question: not `iba/app/handlers/lexical.py` (no hits at all) but two now-inactive one-off
scripts (`_apply_file_chapter_lexical_prose_v1_20260702.py`,
`_apply_file_passage_lexical_prose_v1_20260704.py`) whose `INSERT` statements hardcode `'approved'`
and `'claude_code'` as literal constants — confirmed by reading the code directly. "Approved" in this
book is a script default, not a researcher-review signal, even though the underlying content is
genuinely current-method.

---

## 11. Prose as narrative, not data — and the raw-material-visibility problem

Reviewing the extracts, the researcher stated a design principle and a reclassification: *"I can
start by saying what it should not be: tables and tables of raw data is out. Prose books are
essentially narrative, something that is readable, understandable interpretable, not raw data. it is
not the place for table data dumps. What is currently in these two books is the raw material for the
writing process."*

This reclassifies the current content of both books: `prose_section` is the narrative store; what's
currently populated is source material for a future narrative, not the narrative itself — true even
of the `lexical_prose*` content, which reads more narrative-shaped on the surface but is, at this
stage, interim working material, not finished book content. The researcher was explicit that
incompleteness isn't the current worry — most content is experimental, meant to build a sense of what
the books should eventually contain.

This produced a new, named design thread: *"How to organise and make the raw data available to aid
the conceptualisation and writing more effective. If I cannot see it, I cannot write about it."*
Connected — not merged — to the chapter-rewrite-assist idea (§8): that idea was scoped narrowly to
"what changed since a chapter was last written"; this is the general case of the same problem,
surfacing any relevant raw material, for any of the three creation modes, not authoring-from-revision
alone.

---

## 12. The four-book purpose model — and the book-2/book-3 blur

Researcher, stated at a high level: *"programme book is a narrative of what the study is about, what
it tries to achieve, and how does it go about it. Detail design (I think this label is likely to
change) is the narrative about the data itself, what it comprise of, how does it look like, what does
it say by itself. Findings is all about what does the analysis and synergising of the data say about
the inner being. (again the name of the book is likely to change). There is a blur between book 2 and
book 3 which will need careful handling not to duplicate. Finally, the essay book is the short
stories, the digestible extracts that can be shared publically. only the ardent scholar will ever dig
into the first three books. the general reader will only connect to it through the essays."*

This gives each book a distinct *function*, not just a content type — Programme (mission/method),
book 2 (what the data says by itself), book 3 (what analysis/synthesis says it means), Essays (public
distillation of book 3, mostly), with books 1–3 for the scholar and Essays as the sole point of
contact for the general reader.

Rather than reason abstractly about the flagged book-2/book-3 blur, a real content sample was checked:
a `lexical_prose_chapter` row (Psalm 32) was read against the new line. Finding: it sits **clearly in
book-3 territory already**, not book-2 — actively interpretive (naming a "mechanism," drawing
inner-being conclusions, tagging inferred vs. stated), grounded in lexical data but doing synthesis
with it, not merely laying it out. Consequence named: a genuine book-2 (data-only, no interpretation)
doesn't exist as populated content anywhere right now — it would need to be a new, more restrained
kind of writing, not a relabeling of what already exists.

---

## 13. The verse-is-king constraint, and the structural gap it exposes

Researcher, stating the governing constraint for the whole multi-year effort: *"materialising this
ideal is likely to take a long time, maybe several years... from an IBA process control perspective,
the design and build and tools must be robust enough to facilitate this extended process, stay
consistent, keep track, and always stay tightly connected with the true purpose - the verse is king."*

Checked rather than treated as a new requirement: already anchored in governance —
`cfg_prose_concept` has a `verse_primacy` row pointing at Programme chapter 1, description matching
almost exactly: *"The verse is the primary unit of evidence; findings and dimensions emerge from
verse evidence, never bent to fit a pre-existing category."*

A real gap was found and flagged: `prose_section` has **no structural verse-link at all** — no
column, no junction table. `registry_id` links to a word; `cluster_code`/`characteristic_id` link to
the cluster taxonomy; nothing links to a verse. Verse-grounding today, confirmed from the Psalm 32
sample, exists only as citations embedded in free body text (`H3680`, `vv.1–2`, etc.) — real, but
invisible to the database, not queryable, not checkable at scale. Over a multi-year process, this can
only be audited by a human re-reading prose against citations by eye; nothing structural catches
drift. Named, not built: a `prose_section_verse_link` table, the same shape and precedent as the
already-declared-but-empty `prose_section_finding_link`/`prose_section_dimension_link`.

Researcher, confirming and extending: *"the citation principle and the table design is there, the
fact that it has not been enforced is a part of the issue of consistency and repeatability."* — i.e.,
this specific unenforced-structure pattern is part of the same class of problem that led to building
IBA in the first place.

---

## 14. The missing 5th book — Concordance — and its risk, decomposed

Researcher: *"there is a final concept that emerged in the last month, that plays a part in this
final leg - the missing 5th book - the concordance - the cross reference - the index. I am still
seriously at a loss on how and when to bring that to life. The risk is that data connection drift and
that the concordance will never be able to be generated."*

Checked live rather than treated as one undifferentiated risk — the concordance turned out to be two
separate problems, not equally at risk:

1. **Base concordance** (word/Strong's/verse cross-referencing) — **already exists and works, live,
   in IBA today.** `report.strong_verse` does a whole-Bible Strong's-to-verse lookup
   (`verse_lexical.strong` exact match, inline-annotated, collision-handled). `report.word_registry_span`
   already walks the full `word_registry → word_strong → strong → strong_meaning_parsed →
   verse_lexical` chain for a registry word, every linked Strong's with its parse-meaning breakdown
   and unique surface-span applications. This half is not at risk of "never being generatable" —
   it's schema-enforced and already working; it could plausibly be assembled into a real book 5 now.
2. **Prose-integrated concordance** (verse → which prose/findings discuss it) — **this is the genuine
   drift risk**, and it's the same gap named in §13: no `prose_section_verse_link`, enforcement only
   by free-text citations a human has to read.

Consequence named for "how and when": the two halves don't need solving together — the base
concordance doesn't have to wait on the prose-verse-link work.

---

## 15. Where this stands

This section is an inventory of what exists and what's open, not a plan. Nothing below is a
recommendation.

### Built and tested live, this thread
- Prose store code incorporated into IBA (`iba/app/lib/prosestore.py`, `handlers/prose.py`,
  `ps/Prose.ps1`) — code written and tested; the corresponding config (dispatcher registration,
  write grants, status/author enums, behaviour rules) from plan v4 was never submitted for approval
  and remains unbuilt.
- `CHAPTER_EDIT_OUT_DIR` regression fixed (was writing to the wrong folder).
- Chapter-edit export versioning (`-v{n}-`), scanned across active + archive folders.
- Import-time auto-archiving of the source edit file, with `source_file` correctly pointing at the
  post-move location.
- The unconditional-supersede bug fixed — import now only supersedes sections whose body actually
  changed, and refuses outright if nothing changed.
- `docs/prose-store-architecture.md` §8.1 corrected (edit files are not disposable once imported).
- Escalation-module bugs found and fixed as their own items: #790 (`raise_()` skipping
  `cfg_escalation_requirement`), #795/#798/#799 (dispatcher decision collapse, resolution-kind axis).

### Designed, not built
- Plan v4's config layer (dispatcher registration, write grants, `cfg_prose` table, enums, behaviour
  rules) — set aside pending the wider design, not rejected.
- The prose-change-flag mechanism — shape agreed (reuse/extend `wa_quality_flag_types` +
  `wa_data_quality_flags`), not built.
- Chapter-rewrite assistance (mechanical briefing + Claude AI authoring) — downstream of the
  change-flag mechanism, not built.
- `prose_section_verse_link` — named as the natural fix for the verse-grounding gap, not built.
- Raw-material-visibility for writing — named as an open thread, not designed.

### Open decisions, not made
- Whether "delete a section from an edit file" should refuse, warn, or actually retire the section
  (currently silent no-op).
- Where the file-location rule gets written down (`file-organisation-rules.md` vs. a config setting).
- Whether `Detail design`'s old per-word content is worth keeping as history, or is dead weight now
  that the method has moved on.
- How the book-2/book-3 boundary should actually be held apart in practice, now that real content
  (Psalm 32) has been shown to already sit on the book-3 side of the line.
- How and when to bring the Concordance (book 5) to life — though the two halves of that problem are
  now known not to be equally urgent.
- What the final names of `Detail design`, `Findings`, and possibly other books should be — the
  researcher named both as provisional.

### Open questions the researcher raised, still unanswered
- Whether "link the file with the book-chapter-session" (§6) meant only the missing version number,
  or something else — flagged at the time, never confirmed either way.
