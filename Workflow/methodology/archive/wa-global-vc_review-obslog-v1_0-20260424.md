# Obslog — VC_Review

**File:** wa-global-vc_review-obslog-v1_0-20260424.md
**Opened:** 2026-04-24
**Session topic:** Re-evaluation of Verse Context instruction — hypothesis that VC should run from term perspective, not registry perspective
**Governance:** Global rules v2.11 (per extract wa-global-rules-extract-20260421.json, 36 rules)
**Session reference:** VC_Review
**Prior output reference:** wa-versecontext-instruction-v2_9-20260424.md (instruction under review)

---

## Entry 001 — 2026-04-24 — Session opening, GR-TEMPO-001 failure corrected

**Researcher message (verbatim):**
> this session is about thinking and re-evaluating an instruction.  Verse Context is currently being approached from a registry entry perspective.  It takes the owner terms of a word, read all the associated verses, interpret the verses and consolidate the context of the verses into verse groups.  The main aim of verse context is the consolidate verses that all say the same thing into one group, and to designate a anchor verse that represents the verse group best.  My hypothesis is that there is no reason to run this from a registry perspective.  We simply need to run it from a term perspective. Verse context is not registry related.   This session is governed by the global rules.  Pay special attention to the descipline of the obslog.  Compliance is not an option.  The obslog reference is VC_Review

**Compliance failure — recorded:**
On session opening, Claude AI produced a chat response acknowledging the global rules were uploaded but did not read them before responding. Researcher challenged: "did you actually read to global rules?" This is a direct GR-TEMPO-001 failure — recognition-plus-continued-conversation replaced recognition-plus-action. Specifically: GR-LOAD-001 step (1) requires the rules to be read in full before any substantive work; Claude AI proceeded to clarifying questions without the read.

**Correction actions taken:**
1. Read wa-global-rules-extract-20260421.json in full (36 rules across 13 categories).
2. Opened this obslog as GR-LOAD-001 step (2).
3. Will state GR-CAD-001 activation as step (3) in chat.

**Files read this session so far:**
- wa-global-rules-extract-20260421.json (in full)

**Files NOT yet read but present:**
- wa-versecontext-instruction-v2_9-20260424.md (the instruction under review — primary subject)
- wa-programme-prose-extract-20260424.json (programme context)

---

## Entry 002 — 2026-04-24 — Next actions queued

Before engaging with the researcher's hypothesis, the following must happen:
1. Read wa-versecontext-instruction-v2_9-20260424.md in full (no skim, no sampling — per GR-LOAD-001 familiarisation semantics).
2. Read wa-programme-prose-extract-20260424.json in full for programme context.
3. Then engage with the hypothesis step by step.

This is the correct sequence; the earlier clarifying-question-first approach was wrong because it produced chat output before the source materials were read.

Note on the earlier clarifying questions: they remain open but secondary. They will be resolved as part of reading the instruction (the version question) and by noting that the obslog is newly opened in this session (the obslog-existence question).

---

## Entry 003 — 2026-04-24 — Readings completed

Files read in full:
- wa-global-rules-extract-20260421.json (all 36 rules, 13 categories)
- wa-versecontext-instruction-v2_9-20260424.md (the instruction under review, 1710 lines)
- wa-programme-prose-extract-20260424.json — targeted reads of:
  - `prog_instr_session_a` (section 52)
  - `prog_instr_verse_context` (section 46)
  - `prog_instr_dimension_review` (section 47)
  - `prog_data_terms` (section 24)
  - `prog_xref_architecture` (section 25)
  - `prog_data_verses` (section 26)
  - `prog_anchor_verse` (section 27)

## Entry 004 — 2026-04-24 — Observations relevant to the hypothesis (pre-response)

**The hypothesis (verbatim from researcher):**
> My hypothesis is that there is no reason to run this from a registry perspective. We simply need to run it from a term perspective. Verse context is not registry related.

**Observations from the data and documents read (pure observation, not interpretation):**

OBS-1 — Database architecture is already term-keyed, not registry-keyed
- `verse_context.mti_term_id` is FK to `mti_terms.id` (v2.9 §2.2)
- `verse_context_group.mti_term_id` is FK to `mti_terms.id` (v2.9 §2.1)
- Neither classification table has a `registry_id` or `registry_fk` field
- v2.9 §2.2 explicit: *"Programme-wide key: mti_term_id is the same integer regardless of which registry views the term. OWNER and XREF registries query the same verse_context records via this key."*
- prog_data_verses §26 explicit: *"The classification is attached to the term, not to the registry-view of the term."*

OBS-2 — The OWNER/XREF architecture already makes classification term-centric at the data level
- prog_xref_architecture §25: *"one term, one owning registry — and a companion mechanism that records the term's relevance to other registries without duplicating its classification"*
- *"A finding raised in the OWNER registry's Session B is the finding for that term across the programme; registries that reference the term as XREF inherit the finding through the shared mti_term_id path rather than producing a separate one."*
- v2.9 §0.2: XREF terms are NOT separately classified. Their verse_context is the OWNER term's verse_context, inherited via mti_term_id.

OBS-3 — Where "registry" currently appears in the VC instruction
Registry concerns in v2.9 currently drive:
(a) Batch construction ordering (§5.2): *"ordered by mti_terms.owning_registry_fk ascending (keeps terms from the same registry together where possible)"* — a soft preference, not a requirement
(b) Registry split across batches (§5.2): expected behaviour, not a constraint
(c) XREF coverage check (§0.2, §13.2): determines whether a *registry* can advance to Complete — but the check itself is a term-coverage check wearing a registry hat
(d) Registry completion check (§13.1): "are all this registry's OWNER terms classified?"
(e) Registry status advancement (§13.3): `verse_context_status` on `word_registry` — this is the gate for DataPrep
(f) Re-export per registry (§13.3): produces fresh full-word JSON
(g) Processing order (§6.1 step 7): *"Terms are processed in registry sequence, ascending by registry number"*
(h) Classification input framing (§6.1 step 1, v2.9 change): per-registry Session A .md is now the "primary" input, batch JSON is "legacy"

OBS-4 — The actual analytical unit in §6.2 is already the term
- §6.2 Step 1: "Read all verses" — for the term
- §6.2 Step 2: "Apply the relevance filter" — for each verse of the term
- §6.2 Step 3: "Group relevant verses" — for the term
- §6.2 Step 4: "Designate anchors" — per group, per term
- §6.2 Step 5: "Identify dual-context verses" — per term
- §6.2 Step 6: "Per-term classification summary" — per term
- Every step is scoped to a single term. Registry is not present in the analytical loop itself.

OBS-5 — What genuinely binds VC to registry (if anything)
From the readings, the remaining registry-coupled points are:
(i) `verse_context_status` is a field on `word_registry`, not on `mti_terms`. Therefore the "completion" signal is by registry.
(ii) DataPrep gate (v2.9 §13.3): *"This re-export is what opens the DataPrep gate"* — DataPrep is triggered per registry.
(iii) Re-export produces per-registry JSON.
(iv) Session B DataPrep reads the registry-level file.
(v) Session A's per-word (i.e. per-registry) .md is now named as primary classification input in v2.9 §6.1 step 3.

These are all downstream/upstream interface points, not core VC classification logic. They are the ways the registry envelope is observed at the boundary of VC, not within it.

**Preliminary interpretation (to be tested with researcher):**

The hypothesis appears consistent with the data architecture. The classification itself is already term-centric in the database and in §6.2's workflow. What the instruction labels as "registry perspective" looks like it is actually:
- Batch organisation convenience (soft — terms from one registry tend to cluster together, but this is batch assembly not classification)
- Registry-boundary reporting (the completion check, status advancement, re-export)
- Input document framing (the per-registry Session A .md is currently presented as primary input)

Whether removing the registry frame from VC would simplify the instruction, or whether the registry envelope serves a function that is not obvious from the text, is a question for the researcher.

**Questions that arise before I can reflect further:**

Q1 — When you say "run it from a term perspective," do you mean:
(a) The input document model changes — terms are processed as a programme-wide queue, grouped into batches by some term-level criterion (e.g. verse count, language, cluster), without per-registry Session A .md as the primary input?
(b) The workflow itself changes — §6.2's six steps are the same, but the batch and reporting envelopes are term-keyed instead of registry-keyed?
(c) Both?

Q2 — What happens to the completion signal that triggers DataPrep?
If VC stops tracking registries, something else has to advance `word_registry.verse_context_status` to Complete (or replace that mechanism) so DataPrep knows when to start. Is the proposal to:
(a) Keep the registry-level completion check but move it out of VC (so CC runs it as a derivative check from term-level classifications)?
(b) Replace the registry gate with a term-level gate (and DataPrep also becomes term-driven)?
(c) Something else?

Q3 — What about the re-export?
Currently VC produces a re-export of the full-word (per-registry) JSON as a trigger artifact. If VC is term-scoped, the re-export could be per-term or per-batch or removed entirely. Which reflects the intent?

These three questions are interpretive choices that affect the shape of any revised instruction. Per the session rules, I will pause here rather than speculate.

---

## Entry 005 — 2026-04-24 — Researcher's answers to Q1–Q3 (verbatim)

**Researcher message (verbatim):**
> Q1 - it is about both.  adding the registry into the process add noise, not value.
> q2 - it should exist on both. CC will update the registry when all the terms (owner and XREf) has gone through VC.
> q3 - there are approx 3000 owner terms.  Each terms will have its own input .md  depending on volume handling.  I can introduce multiple terms in a single sessions.  Each term is completed in its own right.

**Parsing the answers:**

A1 — Both input model AND workflow change. Registry frame is removed from both. Rationale: "adding the registry into the process add noise, not value."

A2 — Dual completion tracking. Term-level completion is primary; CC derives registry-level completion (verse_context_status = Complete) as a consequence of all terms (OWNER and XREF) in that registry having been classified.
- This preserves the DataPrep gate without putting registry into VC's core workflow.
- Registry becomes a CC-side aggregation, not a VC-side concern.

A3 — Scale and input unit:
- ~3000 OWNER terms in scope programme-wide (confirms the analytical unit count — this is the real workload of VC).
- Each term has its own input .md (per-term Session A .md, not per-registry).
- Multiple terms may be introduced in one session — session-level batching is at researcher's discretion, not driven by registry or batch id.
- Each term is completed in its own right — term is the atomic unit of completion, not registry and not batch.

---

## Entry 006 — 2026-04-24 — Consequences for the instruction (observation, pre-reflection)

The researcher's answers move the instruction's shape in a specific direction. Recording the observable consequences before reflecting.

C-1 — Input model
- Per-term Session A .md becomes the primary (and probably sole) classification input.
- The per-registry Session A .md model newly introduced in v2.9 §6.1 step 3 is displaced.
- The legacy batch JSON (VCB-{nnn}-extract-{date}.json) is also displaced — or, at least, no longer the organising unit.

C-2 — Workflow (§6.2)
- §6.2's six steps remain substantively unchanged (they were already term-scoped).
- What changes: the "processing order" in §6.1 step 7 ("Terms are processed in registry sequence, ascending by registry number") is removed or rewritten — terms are processed in whatever order the researcher introduces them into a session.
- Registry sequence is no longer a discipline of VC.

C-3 — Completion model
- The atomic completion unit is the term, not the batch and not the registry.
- Each term is completed when its verse_context and verse_context_group records are in place and R1–R4 hold for that term.
- Registry-level completion (word_registry.verse_context_status = Complete) is derived by CC once all OWNER and XREF terms for that registry have term-level completion.
- DataPrep gate is unchanged in mechanism (it still reads word_registry.verse_context_status) — but the signal is produced as a downstream consequence, not by VC itself.

C-4 — Re-export
- Per-registry re-export still happens (DataPrep reads the per-registry full-word JSON). But it is triggered by CC's derived registry-completion event, not by VC's own completion cycle.
- VC does not own the re-export step; it owns only the term-level classification.

C-5 — Batch concept
- The "batch" (VCB-{nnn}) as the organising unit is gone. Term is the unit.
- Sessions may carry one term or many — at researcher discretion.
- File-naming conventions (§6.4) built around {batch_id} need to be rebuilt around {term identifier}.
- Artefacts (observations file, session log, flags register, patch, Session B flags) either move to per-term scoping, or to per-session scoping with term identifiers inside.

C-6 — Flags register and Session B flags
- Currently end-of-batch artefacts. Need to be rethought. Options visible from the instruction's current shape:
  (a) Per-term — a small flags file per term when flags arise.
  (b) Per-session — one flags file per researcher session, covering whatever terms were processed.
  (c) Rolling programme-wide — one continuously-updated register.
- This is an interpretive choice for the researcher.

C-7 — Patch scope
- Currently one VERSECONTEXT patch per batch.
- Options: per-term, per-session, or batched-to-a-cadence.
- Per-term would produce many small patches; per-session would let several terms be written together. This is a workflow efficiency choice, not a correctness choice.

C-8 — XREF handling (§0.2)
- Largely unchanged in substance — XREF terms are still not separately classified; they still inherit via mti_term_id.
- But the registry-level XREF coverage check (§0.2, §13.2) becomes CC's responsibility as part of the derived registry-completion step, not VC's.

C-9 — Documents downstream of VC
- Dimension Review instruction — operates at cluster (registry-grouping) level. Its trigger is per-registry verse_context_status = Complete. Unaffected in mechanism, because the registry signal is preserved (just produced downstream of VC, not by VC).
- Session B Analysis Readiness — reads per-registry exports. Unaffected.
- Session B Analysis Output — reads per-registry exports. Unaffected.
- The registry envelope survives where it is needed (downstream stages); it is only removed from VC's own process.

C-10 — Programme prose
- prog_instr_verse_context (programme prose section 46) currently describes VC as operating "in batches — typically tens of registries at a time". This prose text will need revision to reflect the per-term model. This is a downstream programme-prose update, not a blocker.

---

## Entry 007 — 2026-04-24 — Open interpretive choices for the researcher

Before any drafting, three interpretive choices remain:

IC-1 — Scope of flags artefacts (per C-6 above): per-term, per-session, or programme-rolling?
IC-2 — Scope of patch artefacts (per C-7 above): per-term, per-session, or researcher-paced?
IC-3 — Observations log scope: currently per-batch (wa-vcb-{batch_id}-term-observations-...). With batch gone, does the obslog become per-session (dated), per-term, or programme-rolling?

These are authorship-adjacent choices that affect the shape of the revised instruction but not its analytical substance. Per GR-HF-001, they are candidates for specialist authorship within researcher direction — except that the researcher is the one with the visibility on what works best across multiple sessions. I will surface them and ask.

---


## Entry 008 — 2026-04-24 — Researcher has drafted the revised instruction and prose

**Researcher message (verbatim):**
> see attached for the revised versecontext, and the updated prose for verse context - to give effect to two major changes to verse context process: a) instead of json, an .md is introduced as the source for the process, b) the process is run by term.  Can you inspect the instruction and let me know if there is anything that is unclear or need clarification.

**Files uploaded:**
- wa-versecontext-instruction-v3_1-20260424.md (new instruction — researcher-drafted)
- wa-programme-prose-extract-20260424.json (updated prose — re-upload with revised prog_instr_verse_context)

**Task scope (explicit from researcher):** inspection for clarity and areas requiring clarification. Not a full rewrite, not interpretive challenge — a readability and internal-consistency review of the draft.

**Interpretive notes from earlier session carried forward:**
- The interpretive choices IC-1 / IC-2 / IC-3 from entry 007 will be answered *by what the draft actually says*, not debated separately. My job is to read what the researcher has drafted, note what is unclear or internally inconsistent, not to re-litigate the design choices.

Next actions:
(1) Read the new instruction v3.1 in full.
(2) Read the updated prose for prog_instr_verse_context (compare to the earlier version read in entry 003).
(3) Produce an inspection report — clarity gaps, internal inconsistencies, unresolved references, anything the AI-reader or the CC-reader would stumble on.

---

## Entry 009 — 2026-04-24 — v3.1 inspection findings (consolidated before response)

Reading v3.1 in full and comparing against the stated intent ("per-term input is primary", "registry envelope is CC-side derived"), the following inconsistencies, stale passages, and genuine unclarities are identified. Categorised by severity.

### Category 1 — Stale text carried forward from v2.9/v3.0 that now contradicts v3.1

F-01 — §0 "What Verse Context does" bullet list (lines 37–47)
Says: "Advances verse_context_status to Complete per registry when all OWNER terms are classified" and "Re-exports the full word JSON for each completed registry — the trigger for DataPrep".
Per v3.1 change note: VC itself does not advance verse_context_status; CC derives it from mti_terms.vc_status aggregate. And v3.1 §5.1 / §13.3 describe the re-render as a Session A .md (primary) with the full-word JSON re-export still happening — but the language of the bullet list is from the old registry-centric model.
Fix direction: rewrite bullets to say VC "writes mti_terms.vc_status = complete per term on apply"; registry-level advancement and re-export are CC-side derived consequences, not VC deliverables.

F-02 — §0 Stage sequence diagram (lines 59–76)
Still reads:
  "Verse Context Stage 1
    ├── Claude Code: batch construction from full exports
    ├── Claude AI: verse classification session
    ├── Claude Code: patch application + consistency validation
    ├── Claude Code: XREF status propagation
    ├── Claude Code: registry completion check + re-export
    └── loop until all OWNER terms classified"
The words "batch construction from full exports" contradict the new per-term .md model. "Loop until all OWNER terms classified" is fine but should make explicit that the loop runs at session level, not registry level.
Fix direction: replace "batch construction from full exports" with "per-term .md rendering from database". Add a line about per-term vc_status write so the CC role is visible in the diagram.

F-03 — §0 Pipeline note (line 78)
The self-standing-document note mentions "the legacy batch JSON where a split-registry session falls back to it". Under v3.1 §0.1 the legacy batch JSON is deprecated and the split-session case is handled natively by per-term .md. The fallback reference is stale.
Fix direction: strike the "or the legacy batch JSON..." clause.

F-04 — §1 Two-System Model table (line 172)
Claude Code row reads: "Renders the per-registry Session A .md from the live database (primary input for the classifier)."
This directly contradicts v3.1's own change note item (1): "The per-registry .md is retained as a hybrid secondary view... but is no longer the primary classifier input."
Fix direction: change "per-registry Session A .md" to "per-term Session A .md" as primary. Per-registry .md is hybrid secondary.

F-05 — §5 Section 5 opening paragraph (line 376)
Reads: "The classifier's primary input is the Session A .md per registry. Claude Code renders it from the live database via scripts/build_session_a_prose.py."
Same contradiction as F-04. Direct conflict with v3.1's change note and with §0.1.
Fix direction: rewrite §5 opening to say the primary input is the per-term .md rendered by `scripts/build_session_a_prose.py --term`. Per-registry .md is hybrid secondary; legacy batch JSON is deprecated.

F-06 — §5.1 Trigger bullet list (lines 380–385)
All four triggers read at registry level ("a registry's Session A .md", "every classification session for that registry", "audit_word re-run for the registry", "Before a Dimension Review hand-off"). Under v3.1 the primary trigger is per-term rendering.
Fix direction: rewrite triggers in term-first voice. Per-registry renders still exist (for DimReview hand-off), but they are the secondary case, not the trigger list's primary frame.

F-07 — §5.2 Input selection criteria — "For a per-registry session (the default)" (line 389) / "For split-registry / multi-registry sessions (exception path)" (line 398)
This section structure remains organised around registry-as-default. The change note explicitly inverts this: per-term is default, per-registry is secondary. The taxonomy needs rebuilding.
Fix direction: reframe the two subsections as: (a) Per-term selection (default) — criteria at single-term scope; (b) Multi-term session composition (researcher-composed) — criteria for how multiple per-term .md's enter a session together. The current "split-registry" framing is obsolete.

F-08 — §5.3 Input document structure (line 408)
Reads: "The Session A .md is organised under six seeded prose_section_type handles..." but does not distinguish per-term .md structure from per-registry .md structure. Both exist (per the change note) but they have different content shapes — the per-term .md carries one term's data; the per-registry .md carries all terms for a registry.
Fix direction: describe the per-term .md structure specifically. The per-registry .md can be referenced as "same structure, all terms for a registry" or described separately.

F-09 — §5.4 Output file (lines 416–418)
"Primary output: data/exports/session_a/wa-{nnn}-{word}-session_a-{date}.md — the per-registry Session A .md" — again primary = per-registry. Contradicts v3.1 change note and §0.1.
Fix direction: primary output is the per-term .md at `Sessions/Session_A/terms/wa-{nnn}-{word}-{strongs}-session_a-{date}.md`. Per-registry .md is the hybrid secondary output.

F-10 — §6.4 Session discipline — file-naming breakpoint examples (lines 614–618)
Breakpoint identifiers listed are R19, R20, R20-R23 etc. — all registry-scoped. Under v3.1 the session is researcher-composed and may cover one term or many across any registries; a registry-range identifier is no longer the natural breakpoint.
Fix direction: replace with term-scoped or session-progress identifiers. Examples: `mti142`, `mti142-143-187`, or `terms1-4`, `final`. Or leave `final` as-is and let the researcher pick the breakpoint scope.

F-11 — §6.4 "No large in-memory accumulation" (line 648)
"For batches with more than approximately 50 terms, treat patch construction as a separate session..."
v3.1 makes the session the researcher-composed unit. The "batches" language is leftover from the abolished batch concept. Also — 50 terms was the batch-era threshold; the session model may call for a different threshold (e.g. per-session or verse-count-based).
Fix direction: replace "batches" with "sessions". Confirm the 50-term threshold still applies or reset it. A session with 50 terms is unusual in the per-term-per-session model (which expects 1..N where N is researcher-driven); a verse-count threshold (e.g. >1,500 verses) may be more appropriate.

F-12 — §6.4 "Instruction document size awareness" (line 658)
"When loading it alongside a large Session A .md (or, in the fallback path, a batch JSON)..."
Batch JSON is deprecated per change note. The fallback path as described no longer exists.
Fix direction: strike "or, in the fallback path, a batch JSON".

F-13 — §6.5 Deferred Flag Protocol (lines 665, 671, 696)
References to "end-of-batch" persist throughout. Under v3.1 the session replaces the batch; flags resolution is end-of-session.
Fix direction: global replace "end-of-batch" with "end-of-session". Also §6.5.1 "Does not prevent correct classification of the remaining verses in the batch" → "... in the session". Similarly §6.5.2 "sequential within the batch" → "within the session".

F-14 — §7.1 Patch types table (line 795)
VERSECONTEXT row purpose reads "Full batch — all terms in batch" and when-to-use reads "After completing all terms in a batch session".
Fix direction: "Full session — all terms classified in the session" / "After completing all terms in the session".

F-15 — §7.4 Operation ordering (line 985)
"Across terms: process terms in the order they appear in the input document (Session A .md or fallback batch JSON)."
Under v3.1 the session may have multiple per-term .md inputs. There is no single "input document" in which terms have an order. The researcher's session-composition order is authoritative.
Fix direction: "Across terms: process terms in the order the session composition specifies (the order in which the per-term .md inputs were introduced to the session)."

F-16 — §8.2 VCGROUP Patch structure (line 1140)
`"produced_by": "WA-VerseContext-Instruction-v1.8"` — stale version in the template.
Also Annexure C §12 VERSECONTEXT template (line 1622): `"produced_by": "WA-VerseContext-Instruction-v1.8"` — same stale ref.
Fix direction: update to `"wa-versecontext-instruction-v3_1"` or `{governing_instruction}` placeholder.

F-17 — §13.3 Re-export (lines 1441–1447)
Text says: *"Then immediately re-export the full word JSON: `python -m engine.engine --export-word --registry={registry_no}`"* and *"This produces a fresh wa-{nnn}-{word}-extract-{date}.json carrying verse_context_status = Complete in its meta. This re-export is what opens the DataPrep gate."*
But §13.3 opening already says: *"Re-renders of the per-term .md's and any per-registry hybrid view are researcher-discretionary — they regenerate the same data from the canonical DB state; the state is already written."*
These two passages conflict. Is the JSON re-export still the DataPrep gate, or has the gate become "state is written in DB, DataPrep reads DB"?
This is a substantive ambiguity — not merely stale wording. See Category 3.

F-18 — §13.4 Completion report (lines 1464–1471)
The "partial registry split" report template reads: "OWNER terms remaining: {n} (to be included in VCB-{next_batch_id})". Under v3.1 batches are sessions, not sequential registry-coverage batches; "next batch id" is meaningless.
Fix direction: "OWNER terms remaining: {n} (to be classified in future sessions at researcher discretion)".

F-19 — §14 Stage 1 Completion (lines 1494, 1512, 1514)
"Stage 1 is complete when all 181 active registries..." — fine in intent. But "Batches processed: {n} (VCB-001 through VCB-{nnn})" — again batch sequence language. And the programme has 184 of 214 registries active per v3.1 §0.1, not 181 — but 181 is stated here and elsewhere as the fixed target.
Also §14.1 query comment: "Target: Complete = 181, In Progress = 0, NULL = 31 (excluded)" — 31 but §0.1 says 30 excluded.
Fix direction: (a) rewrite "Batches processed: {n} (VCB-001 through VCB-{nnn})" to "Sessions: {n} (VCB-001 through VCB-{nnn})". (b) Reconcile the registry count numbers — is it 181/184? 30/31 excluded? This needs researcher confirmation because different sections say different things.

F-20 — Annexure A Startup Summary Template (lines 1554–1572)
Heading reads "Verse Context v1.8 startup complete." and "Governing instruction: WA-VerseContext-Instruction-v1.8-20260331.md".
Version is stale by 13 versions (v1.8 → v3.1). The whole template is also batch-shaped, not session/term-shaped.
Fix direction: rewrite for v3.1 term-scoped model. Show per-term posture declarations in the template.

F-21 — Annexure C VERSECONTEXT patch template (line 1623)
`"produced_by": "WA-VerseContext-Instruction-v1.8"`. Same stale version as F-16.
Also the Annexure is labelled "deprecated" in the change note but still contains active JSON schemas. If it is deprecated, it should be clearly marked so a reader doesn't pattern-match from it for the VERSECONTEXT structure (which is in §7.2, not Annexure C).

### Category 2 — Internal references that may be broken

F-22 — §0.2 (line 133) references §14.5 ("completion check Section 14.5"). §14 has no §14.5. §14.1 is the monitoring query. §13 now holds the completion checks.
Fix direction: change to "§13.1 and §13.2" or similar.

F-23 — §0.2 references "the completed batch" (line 129). Batch concept is gone.
Fix direction: "the completed session" or "the session's patch".

F-24 — §6.4 (line 656) references "Section 7.6 programmatic pre-submission validation". §7.6 is the Anchor integrity rule, not pre-submission validation — §7.7 is pre-submission validation.
Fix direction: change §7.6 → §7.7.

F-25 — §11.3 (referenced in §7.7 bullet 4) — need to verify this section exists and matches. Section 11 heading not visible in what I read; likely is the Claude Code patch application protocol. If §11.3 is not consistency-rule section, the cross-reference is wrong.
Verification needed — I did not read the full §11. Flagging for researcher confirmation rather than fixing blindly.

### Category 3 — Substantive ambiguities needing researcher decision

A-01 — The JSON re-export vs DB-state-is-written question (F-17 above)
§13.3 both states "state is already written" (no re-export needed) and "re-export is what opens the DataPrep gate" (re-export is required). These positions are mutually exclusive.
The change note describes a re-render of per-term .md as discretionary. But the full-word JSON is not the per-term .md. Two separate re-export mechanisms appear to be in play, and the instruction does not distinguish them cleanly.
Possible resolutions:
(a) The DataPrep gate is the DB state (`word_registry.verse_context_status = 'Complete'`). The JSON re-export is an artefact for audit/human review but is not the gate.
(b) DataPrep still reads a per-registry JSON artefact; the re-export is still the gate; the "re-renders are discretionary" statement applies only to the per-term .md, not the full-word JSON.
(c) Both change — DataPrep reads the DB state, and the full-word JSON re-export is dropped entirely.
This is a researcher decision, not something I can resolve from the text.

A-02 — vc_status lifecycle values
§7.8 and §13 reference `mti_terms.vc_status` values `'complete'` and `'approved'`. `'approved'` is used as a valid completion state for XREF coverage (§13.2) and OWNER aggregation (§13.1, §13.3). But no definition is given of what `'approved'` means, when it is set, or by whom.
The instruction introduces a new lifecycle value without documenting its semantics. This is a gap the CC implementer cannot close from the instruction alone.
Possible interpretation (not to be assumed): `'complete'` = VC classification written; `'approved'` = something later in the pipeline confirms it (Dimension Review?). If Dimension Review upgrades complete → approved, that is outside the VC instruction but should be noted here as "set by downstream stage; VC does not write this value".
Needs researcher decision on (a) whether vc_status has further documented states (anywhere), (b) whether the VC instruction should reference only 'complete' or still accommodate 'approved' as a prior state that should not be overwritten.

A-03 — Prior-state posture when the incoming .md is stale
§6.1 step 4 requires the classifier to state a posture from the .md's posture block, and flag if counts m/d don't match the Existing verse_context groups table. But what if the .md was rendered at a time when the DB state has since changed (another session applied a patch between .md render and the classifier loading it)? The instruction does not describe the freshness obligation.
Needs clarification: should the .md be treated as authoritative (classify against it), or should freshness be verified against live DB state at session start?

A-04 — Session composition as researcher-driven — how does CC learn the composition?
§0.1 and §5 say the session is researcher-composed and may cover 1..N terms. §7.2 `terms_covered` is populated in the patch. But how does CC know ahead of time which terms are in the session — i.e. how is the session's term list conveyed to CC so it can render the right per-term .md inputs?
Possibilities: (a) researcher names the terms when requesting renders; (b) CC renders on demand term-by-term; (c) there is a "session manifest" artefact not mentioned in the instruction.
Minor unclarity but relevant to whether the session has a CC-visible identity before the patch arrives.

A-05 — Orphan-group check scope under per-term model
§6.2 Step 6 orphan-group check is per-term (good). But what if an orphan group for term X has verses that have been reassigned to a group on a *different* term entirely (cross-term reassignment, e.g. where a homograph split moves verses between mti_term_ids)? The current text does not describe cross-term verse movement.
If cross-term movement is not possible in VC (because verse_context rows FK mti_term_id, and moving a verse between terms means deleting and reinserting), this should be stated. If it is possible, orphan-group disposition rules need to handle it.
Needs researcher decision / clarification.

### Category 4 — Editorial / cosmetic

E-01 — The change note (line 11) is a single paragraph packed with 9 numbered items. Readable but dense. A bulleted list would scan better. Not a defect, just a readability point.

E-02 — Prose (prog_instr_verse_context section 53) is clean of batch language but the `description` field of the prose type (line 1294: *"Operates in batches; re-exports the full word JSON per registry on completion"*) still carries the old framing. This is a prose-store metadata field, not body text, but it will show in listings and searches.
Fix direction: update the `description` field of the prose type to reflect the per-term model. This is a prose patch, not an instruction patch.

E-03 — The v3.1 draft has several legacy uses of "batch" in neutral contexts (e.g. §6.4 "large batches", §6.5.1 "the remaining verses in the batch"). Individually they are small, but cumulatively they anchor a mental model the researcher has explicitly moved away from.
Fix direction: a pass to replace "batch" with "session" throughout, retaining "VCB-{nnn}" as the session identifier (since `batch_id` is explicitly kept as the session identifier in §7.2). The word "batch" itself should be pruned outside its role as identifier prefix.

### Summary counts
- Category 1 (stale text, unambiguous fix direction): 21 items (F-01 through F-21)
- Category 2 (internal reference fixes): 4 items (F-22 through F-25, one pending verification)
- Category 3 (substantive ambiguities needing researcher decision): 5 items (A-01 through A-05)
- Category 4 (editorial/cosmetic): 3 items (E-01 through E-03)

Total: 33 items. Of these, 25 are mechanical edits aligned with the v3.1 change note's stated intent. The remaining 8 (Category 3 + E-01/E-02/E-03) need researcher input.

---

## Entry 010 — 2026-04-24 — v3.4 and patch-instruction v2.6 received for re-inspection

**Researcher message (verbatim):**
> the attached instructions updated steps to cater for the review notes.  Can you give it another read to see if you will now be able to follow the instructions to complete the work

**Files uploaded:**
- wa-versecontext-instruction-v3_4-20260424.md (VC instruction — revised from v3.1 based on inspection findings)
- wa-patch-instruction-v2_6-20260424.md (patch instruction — newly introduced to the inspection; governs the VC-2 applicator behaviour referenced in v3.1 §7.8)

**Task framing (explicit from researcher):**
The question is specifically executability: "will you now be able to follow the instructions to complete the work". This is not an abstract clarity review — it is a contract-check. Reading as the classifier who will execute, can I perform every step the instruction requires without having to guess, without internal contradictions, and with every cross-reference resolving?

**Approach:**
1. Read v3.4 in full (it is the instruction I would execute against).
2. Read patch-instruction v2.6 in full (it governs what happens to the patch after I produce it — and the v3.1 review raised the VC-2 applicator as a coupled concern, so the two documents need to be read together).
3. Walk the inspection findings list (F-01..F-25, A-01..A-05, E-01..E-03) against v3.4 — record which were resolved, which were partially resolved, which remain.
4. Execute a mental dry-run of §6.1 Startup → §6.2 classification of one term → §6.3 end-of-session → §7 patch production. Flag anywhere I would stop because the instruction does not tell me what to do next.

---

## Entry 011 — 2026-04-24 — v3.4 executability assessment

### Quick-reconciliation of the v3.1 findings
From the v3.1 inspection (entry 009), 33 items were raised. Against v3.4:

- **Category 1 (21 mechanical stale-text items):** the change notes for v3_2 claim all 21 were addressed. Spot-checking confirms this for §0 stage sequence (now term-scoped), §1 Two-System Model (per-term as primary), §5 opening paragraph, §5.1 triggers, §5.4 output, §6.4 breakpoints, §6.5 end-of-session, §7.1 table, §7.4, §14 counts. **Verified resolved in v3_2.**
- **Category 2 (4 internal reference items):** v3_2 notes claim §0.2 §14.5 → §13.1/§13.2 fix; §6.4 §7.6 → §7.7 fix; "completed batch" → "completed session". Not re-verified line-by-line but the change notes describe the fix intent correctly.
- **Category 3 (5 substantive ambiguities):**
  - A-01 resolved in v3_3 — DB state is the DataPrep gate; full-word JSON re-export is optional audit. Confirmed in §13.3 text.
  - A-02 resolved in v3_4 per change note — `approved` dropped; `complete` renamed `vc_completed`. **But see F-26/F-27 below — the rename is incomplete in the body text.**
  - A-03 resolved in v3_4 — per-term `.md` freshness via `md_version` gate. §6.1 step 4, §7.2 `input_versions`, patch instruction §15.2/15.3 all align. Clean.
  - A-04 resolved in v3_4 — `batch_id` optional. Aligned across v3.4 §7.2 and patch instr §15. Clean.
  - A-05 resolved in v3_4 by ruling that it is not a VC concern. No instruction change required. Clean.
- **Category 4 (3 editorial items):** change-note reformat claim is partial — the v3_2 change note is still one dense paragraph, and v3_3 + v3_4 added further dense paragraphs. Prose-description patch noted as separate PROSE patch. Not re-verified.

**Net reconciliation:** of 33 items, 30 are resolved or correctly dispatched. Three new issues arise from incomplete application of A-02 and one stale paragraph in §13.

### New issues discovered in v3.4 (executability-blocking, ordered by severity)

**F-26 — vc_status value vocabulary is half-renamed (SEVERE — executability-blocking ambiguity)**

The A-02 ruling in the change note says: *"'approved' removed; 'complete' renamed 'vc_completed'. Applicator writes 'vc_completed'; aggregation checks 'vc_completed' only."* This was applied in some places but not others. As classifier I would not know which value the applicator actually writes:

| Location | Value used | Per A-02? |
|---|---|---|
| Change note (line 11) | `vc_completed` | Yes — correct |
| §0 "What VC does" bullet (line 44) | `'complete'` | **No — stale** |
| §0 stage sequence diagram (line 67) | `'complete'` | **No — stale** |
| §0.1 Registry-level signal paragraph (line 100) | `'vc_completed'` | Yes — correct |
| §0.2 XREF aggregation (line 134) | `'vc_completed'` | Yes — correct |
| §1 Two-System Model, Claude Code row (line 173) | `'complete'` | **No — stale** |
| §7.2 `terms_covered` description (line 852) | `'vc_completed'` | Yes — correct |
| §7.8 handoff SQL (line 1090) | `SET vc_status = 'complete'` | **No — stale** |
| §7.9.5 VCNEW applicator behaviour (line 1160) | `vc_status = 'complete'` | **No — stale** |
| §13.1 query body (line 1516) | `!= 'vc_completed'` | Yes — correct |
| §13.1 query comment (line 1517) | "at complete or approved" | **No — doubly stale** (mentions dropped `approved`) |
| §13.2 query comment (line 1523) | "NOT at complete/approved" | **No — doubly stale** |
| §13.3 / §13.1 opening header (line 1503) | "NOT at complete/approved" (comment) | **No — doubly stale** |

So the document declares one vocabulary (`vc_completed` only) and instructs the applicator to use both old and new terms. As classifier producing a patch, this does not block the patch itself (I do not write vc_status — CC does). But:
- The hand-off SQL in §7.8 still writes `'complete'`. If CC follows §7.8 literally, it writes `'complete'` to the DB. But §0.1/§0.2/§13 check for `'vc_completed'`. The aggregation check will then never find a complete term, and no registry will ever advance to `verse_context_status = 'Complete'`.
- The §7.9.5 VCNEW applicator behaviour also says `'complete'`. Same failure mode.

This is an execution-breaking inconsistency. The instruction must be internally consistent on the value the applicator writes and checks. Fix: global replace `vc_status = 'complete'` → `vc_status = 'vc_completed'`, and update SQL comments that reference "complete or approved" to "vc_completed".

**F-27 — §13.1 opening paragraph still references v3_1 (MINOR — provenance only)**

§13 opening line 1498: *"Under v3_1 the check reads from `mti_terms.vc_status` — no longer a scan of `verse_context` rows."* This is historical commentary. Still true, but the reference to v3_1 is stale (should say "under the per-term model" or be removed). Not executability-blocking.

**F-28 — §13.4 completion report template still shows the re-export as a default line (MODERATE — contradicts A-01)**

§13.4 (line 1572): the report template reads *"Re-export: wa-{nnn}-{word}-extract-{date}.json produced"*. Under A-01 (v3_3) the re-export is an optional audit artefact, not produced by default. The template implies it is always produced. Either:
- (a) Remove the line from the template (re-export is not produced unless requested); or
- (b) Make the line conditional: "*Re-export (if requested): ...*".

As classifier, I would not produce this report (CC does), so it is not blocking for me. But it is misleading: a researcher reading the report will expect the file to exist.

**F-29 — §7.8 handoff block itself is stale against v3.3 four-patch model (MODERATE — pre-dates v3.3 rewrite)**

§7.8 is the "Handoff to Claude Code" pseudocode block (lines 1075-1108). Its opening line reads:
*"Patch type: VERSECONTEXT"*

But v3.3 introduces the four-patch model (VCNEW, VCREVISE, VCSBFLAGS, VCSDPOINTERS) with legacy VERSECONTEXT kept for backwards compatibility. The handoff block:
- does not mention the four patches,
- speaks only of one patch,
- uses `'complete'` (F-26 above),
- does not mention `input_versions` (A-03).

Reading the v3.3 change note claim: "(6) §7.8 hand-off updated for four patches". The change was partially made — the opening mentions VC-2 extension — but the body was not revised. §7.9 carries the four-patch model cleanly; §7.8 is the old single-patch hand-off.

As classifier, if I follow §7.8 I produce one VERSECONTEXT patch. If I follow §7.9 I produce up to four patches. The instruction is internally inconsistent on what the classifier is supposed to produce at end of session. I would stop and ask.

**Fix direction:** either (a) rewrite §7.8 to describe the four-patch handoff explicitly; or (b) delete §7.8 and let §7.9 carry the handoff description. §7.9 is the authoritative and correct content; §7.8 is leftover.

**F-30 — Header table "Interaction model" row still says "VERSECONTEXT patch" (MODERATE — one place only)**

Line 17 header row: *"VERSECONTEXT patch with `_patch_meta.terms_covered`"*. This is the interaction-model summary row of the header table. v3.3 introduces the four-patch model; the header still describes a single patch.

**F-31 — Header table "Outputs" row still lists legacy single-patch file (MINOR)**

Line 14: *"Verse Context patch — `wa-vcb-{batch_id}-patch-v{n}-{date}.json`"*. Under v3.3 four-patch filenames are `wa-vcb-{batch_id}-patch-vcnew-v1-{date}.json` etc. (per §7.9.4). The Outputs row still shows one patch.

**F-32 — Header table "Inputs" row retains "Legacy fallback: Verse Context batch JSON ... retained for rare split-session compatibility" (MINOR — contradicts v3_2 claim)**

v3_2 change note claims: *"Fallback batch-JSON references struck."* The Inputs row still mentions legacy fallback. Not executability-blocking (a fallback mention is benign), but the change-log claim is inaccurate for this row.

### A mental dry-run — can I actually execute a session end-to-end under v3.4?

Walking through what I would do with one term (say mti_id=142 FRESH):

**§6.1 Startup — executable.**
- Load global rules — yes.
- Read prog_instr_session_a and prog_instr_verse_context from prose extract — yes. Mandatory statements are spelled out verbatim.
- Load per-term .md — yes.
- Step 4 version acknowledgement — yes, statement template is verbatim. I know what to do if `md_version:` header line is missing (stop and request fresh render).
- Step 5 prior-state posture — yes, FRESH template is verbatim. If RE-EVALUATION, counts must match Existing groups table (stop if mismatch).
- Step 6-8 startup summary, R1-R4 review, processing order — all clear.

**§6.2 classification of the term — executable.**
- Steps 1-5 (read, filter, group, anchor, dual-context) — clear and unchanged from prior versions. Annexure A/B templates exist.
- Step 6 per-term summary + observations file write + re-eval self-check + orphan-group check — all templates present. SB/SD observation capture noted (§7.9.3 detail).

**§6.3 end-of-session — borderline.**
Step 3 says "Produce the VERSECONTEXT patch (Section 7)". But §7 is the four-patch model (§7.9). Step 3 does not say "produce up to four patches per §7.9" — it says one patch. I would read §7 and discover §7.9, and work out that up to four patches are required. Not impossible, but §6.3 Step 3 language is out of date.

**§7 patch production — executable with careful reading.**
- §7.1 table lists VERSECONTEXT, VCGROUP, VCVERSE only. Does NOT list VCNEW, VCREVISE, VCSBFLAGS, VCSDPOINTERS. I would have to go to §7.9 to find the four new types.
- §7.2 header is "VERSECONTEXT patch — structure" but the shown `patch_id` uses `VCNEW` (line 822: `"PATCH-{YYYYMMDD}-VCB{nnn}-VCNEW-V1"`). The §7.2 heading says VERSECONTEXT; the example shows VCNEW. Ambiguity about whether §7.2 is defining VERSECONTEXT (legacy) or VCNEW (current). Both are listed as having the same structure — is that intended?
- §7.7 pre-submission validation covers the new four-patch cross-consistency (§7.7 v3_3 addition). Clear.
- §7.8 handoff — stale (F-29). I would follow §7.9 instead.
- §7.9 four-patch model — clear, self-contained, complete. Points to patch instruction §15 for authoritative details. Patch instruction §15 confirms match.

**Verdict on classifier workflow:** executable, but with explicit reconciliation between §6.3/§7.1/§7.8 (old single-patch voice) and §7.9/§6.2 Step 6 / §7.2 meta fields (four-patch voice). I would do the four-patch workflow because §7.9 is authoritative and §7.7 cross-consistency check depends on it.

**Verdict on applicator workflow (what CC would do reading this instruction):** NOT cleanly executable. §7.8 pseudocode says `vc_status = 'complete'` (old value). §0.1/§13 say `vc_completed`. §7.9.5 says `'complete'`. The DB would end up with `'complete'` written while the aggregation check looks for `'vc_completed'` — registries would never complete. CC must fix this via the patch instruction (v2.6 §15.2 clearly says `'vc_completed'`) and ignore the stale §7.8 + §7.9.5 references. If CC follows the VC instruction literally, VC fails silently at apply time.

### Summary of executability assessment

- **Classifier workflow (what Claude AI produces):** executable under v3.4 with one point of confusion (§6.3 Step 3 vs §7.9) and one place requiring cross-reading (§7.1 table vs §7.9). I can execute, but the researcher should be aware I will navigate to §7.9 for the authoritative workflow and may produce up to four patches when §6.3 implies one.
- **Applicator workflow (what CC does per this instruction):** NOT executable as written. §7.8 and §7.9.5 write `vc_status = 'complete'`, but §0.1/§13 require `vc_completed`. Either the vc_status value is wrong in §7.8+§7.9.5 (F-26), or the change note's A-02 ruling was only partially applied. CC must cross-reference with patch instruction v2_6 §15.2 (which is correct) to resolve.
- **Primary blocker:** F-26 (vc_status value inconsistency) — must be fixed before the instruction can be executed end-to-end without cross-referencing the patch instruction.
- **Secondary issue:** F-29 (§7.8 handoff pre-dates the four-patch rewrite) — not a blocker (§7.9 is authoritative and self-contained), but confusing.
- **Minor issues:** F-27, F-28, F-30, F-31, F-32 — cosmetic or reporting-template issues.

### Recommendation to the researcher

Single fix required before v3.4 is end-to-end executable without patch-instruction cross-reference:

1. **Global replace in v3.4 VC instruction**: `vc_status = 'complete'` → `vc_status = 'vc_completed'` at lines 44, 67, 173, 1090, 1160; update SQL comments at lines 1503, 1517, 1523 to reflect the new vocabulary (drop the "or approved" language).
2. **Rewrite §7.8 handoff block** to describe the four-patch apply sequence (VCNEW → VCREVISE → VCSBFLAGS → VCSDPOINTERS), version gate, version bump, and the correct `vc_status = 'vc_completed'` write. Alternative: delete §7.8 and let §7.9 carry the hand-off narrative. §7.9 is self-contained.
3. **Update §6.3 Step 3** from "Produce the VERSECONTEXT patch (Section 7)" to "Produce the session's patch set per §7.9 (up to four patches)".
4. **Update §7.1 patch-types table** to include the four session patches (VCNEW, VCREVISE, VCSBFLAGS, VCSDPOINTERS). VCGROUP and VCVERSE remain as separate targeted patch types; VERSECONTEXT may be marked as legacy/deprecated.
5. **Update header table rows** (Outputs, Interaction model) to reflect the four-patch output.

This is a focused v3.5 release — all items are mechanical corrections following through on the A-02 and v3.3 four-patch intent. No semantic decisions required.

After v3.5 lands, executability on both sides is clean: classifier produces up to four patches per §7.9 with `input_versions`; applicator runs the version gate and writes `vc_completed`.

---

## Entry 012 — 2026-04-24 — Session close

**Researcher message (verbatim):**
> you can close the session, all the changes have been applied, and we will do a test in a new session

Researcher confirms the v3.5 corrections identified in entry 011 have been applied. Closure action: produce the final session log per researcher-directive governance rules.

Session closes here. No further work in this obslog.

---
