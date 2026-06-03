# Cluster Publishing Instruction

**Version:** v1.0
**Date:** 2026-05-30
**Status:** Active baseline. Replaces the v3_0 cluster instruction §9 "Phase E" section. Replaces the loose files: `wa-sessionc-cluster-style-method-v1_1-20260512.md`, `wa-sessionc-cluster-ch{1..7}-instruction-v1_0-20260512.md`, `wa-sessionc-cluster-appendices-instruction-v1_0-20260512.md`, `wa-v3-publication-pipeline-design-v1-20260527.md`. Those files are retired by this document.

**Audience:** Claude Code (CC) for orchestration and ingest steps; Claude AI (chat) for chapter authoring and consolidation.

**Scope:** This document is the complete and authoritative instruction for publishing a cluster after its findings are signed off. Everything required for the publishing pipeline is contained in this document. No external publishing instruction file should need to be loaded.

---

## §1. What publishing produces

For each cluster, the publishing pipeline produces:

1. **Seven chapter prose rows** stored in the `prose_section` table, keyed to the section-type codes `sc_v2_ch1` through `sc_v2_ch7`. These are the canonical research-in-prose-form — comprehensive, bias-neutral, encapsulating all findings.

2. **One consolidated essay** in `.md` and `.docx` form, saved to disk in the cluster's publishing folder. The essay is a downstream derivation of the seven chapters. It is not stored in the database.

Nothing else is part of this publishing baseline. Appendices, tier prose, synthesis prose, single-pass essays, stitched-together books, and any other artefacts that have existed in prior iterations are not produced by this pipeline.

---

## §2. The fundamental claim about the chapters

The seven chapter prose rows in `prose_section` are the canonical research-in-prose-form. They have three properties:

- **Comprehensive.** They encapsulate every finding that survived Phase D. No finding is selectively omitted in service of a narrative.
- **Bias-neutral.** No particular take, framing, or thematic emphasis is privileged over another. The chapters report what the evidence carries.
- **Source for downstream derivations.** From the same seven chapters, many essays, summaries, alternate formats, and presentation styles can be derived. The §3 consolidated essay is one such derivation; others (a 500-word précis, a key-findings extract, an alternative chapter ordering) are equally valid future derivations, none privileged over another.

Any "particular take" belongs to a downstream derivation, not to the chapter prose itself. The chapters' completeness and neutrality is what gives every downstream artefact its evidential integrity — each can be traced back to the chapter prose, which can be traced back to the findings, which can be traced back to the verses.

The status transition `Analysis Complete` → `Publication Ready` fires when all seven chapter prose rows exist in `prose_section` for the cluster. The consolidated essay does not affect cluster status.

---

## §3. Pre-condition

Findings are signed off and committed to the DB. Specifically:

- Cluster status is `Analysis Complete`.
- All Phase D findings are loaded into `cluster_finding` and any post-Phase-D audit corrections are applied.
- The seven characteristics, their sub-groups, VCGs, and anchor verses are stable in the DB.

The publishing pipeline reads from the DB only. It does not read essays from disk, prior chapter drafts, or memory. The seven characteristic profiles, sub-group descriptions, key verses, and findings used to build the chapter inputs come from the DB at the moment of input generation.

---

## §4. Step 1 — Generate chapter inputs

**Owner:** CC.

**Action:** Generate seven input files in `Sessions/Session_Clusters/{CODE}/inputs/`, one per chapter.

**File naming:** `wa-cluster-{CODE}-ch{N}-input-v{V}-{YYYYMMDD}.md` for N in 1..7.

**Source:** the database. Specifically the input generator reads:
- `cluster` (cluster_code, short_name, description, status)
- `characteristic` (the 7 characteristics for the cluster)
- `cluster_subgroup` (the sub-group definitions, with `core_description`)
- `verse_context_group` and `vcg_term` (the meaning groups within each sub-group)
- `cluster_finding` (the per-characteristic findings, by tier)
- `wa_obs_question_catalogue` (the prompt structure for tier organisation)
- `verse_context` and `wa_verse_records` (the key verses with their per-verse contextual reading)
- `characteristic_subgroup` (the characteristic ↔ sub-group mapping)

**Per-chapter input structure:**

Each input file contains, in order:

1. **Header block** — cluster code, chapter number and name, generated timestamp, references to this instruction document.
2. **Cross-chapter consistency profile** — one-line profiles of every characteristic in the cluster, used for cross-chapter reference. The full profile is established in Chapter 2; other chapters only refer to characteristics by name as shown here.
3. **Chapter section header** — the chapter's title heading (e.g. `## 1. What this study is`).
4. **AI-WRITE zones** — one per writable section in the chapter, each containing a comment block with:
   - The length target.
   - The focus.
   - The required key verses (where applicable).
   - The source pointer (which findings or DB content to draw on).
   - The list of forbidden vocabulary to avoid.
5. **EVIDENCE blocks** — the structural inputs the AI writes from, as comment-delimited markdown blocks. Contains findings, sub-group descriptions, key verses with per-verse contextual readings.

The EVIDENCE blocks are inputs, not outputs. They are stripped from the chapter draft after authoring is complete (this happens automatically at the consolidation step).

**Script:** `scripts/_generate_cluster_session_c_inputs_v2_20260512.py` (existing, to be amended). The amendment removes appendix generation; the script produces exactly seven files per cluster.

**Pre-check before generation:**
- Cluster status is `Analysis Complete` or later.
- All seven characteristics have findings loaded.

**Post-check after generation:**
- Exactly seven input files exist in the `inputs/` folder.
- Each file is well-formed (contains the required structural blocks).

**Status:** generation does not change cluster status. Status remains `Analysis Complete`.

---

## §5. Step 2 — Author 7 chapter drafts

**Owner:** Claude AI (chat). One authoring session per chapter. Seven authoring sessions per cluster.

**Discipline:** the style/method discipline in §7 applies to every chapter authoring run.

**Per-chapter inputs to the authoring session:**

- The chapter's input file from `Sessions/Session_Clusters/{CODE}/inputs/`.
- The chapter's specification from §8 of this document (one §8.{N} sub-section per chapter).
- The style/method discipline (§7 of this document).

Both §7 and §8.{N} are inside this single instruction document. The chapter input file is the only external file loaded.

**Per-chapter output:**

A single completed Markdown file containing the chapter prose. Each AI-WRITE zone in the input is replaced with the finished prose. The `<!-- AI WRITE: ... -->` marker block and its placeholder line are removed. EVIDENCE blocks are preserved (they are stripped at consolidation).

**File naming:** `wa-cluster-{CODE}-ch{N}-draft-v{V}-{YYYYMMDD}.md`, saved to `Sessions/Session_Clusters/{CODE}/published/`.

**Authoring discipline per chapter:**

1. Read the chapter input file end to end.
2. Read §7 (style/method discipline) and §8.{N} (the chapter specification for chapter N).
3. Write prose into each AI-WRITE zone in order. Topic sentences carry the argument. Every analytical claim is grounded by a quoted verse.
4. After writing, run the reverse audit (§7.10).
5. After the reverse audit, run the self-review (§7.11).
6. Save the chapter draft.

**Ingest into the DB (CC):**

After each chapter draft is saved, CC ingests the body of the draft into `prose_section`:

```sql
INSERT INTO prose_section (
    section_type_id,        -- sc_v2_ch{N}.id
    cluster_code,           -- {CODE}
    characteristic_id,      -- NULL (chapter prose is cluster-scope)
    cluster_subgroup_id,    -- NULL
    heading,                -- chapter title
    body,                   -- chapter prose body (with EVIDENCE blocks stripped)
    word_count,             -- computed
    status,                 -- 'draft'
    version,                -- max(existing)+1, or 1
    supersedes_id,          -- previous version, if any
    superseded_by_id,       -- NULL on insert
    author,                 -- 'claude_ai'
    metadata_json,          -- {"generator": "publishing_step_2", "source_file": "...", "instruction": "wa-cluster-publishing-instruction-v1_0-{date}"}
    source_file,            -- relative path to the chapter draft
    delete_flagged          -- 0
);
```

**Idempotency:** the ingester computes `sha256(body)` and compares to the latest existing active row for `(cluster_code, section_type_id)`. If the hash matches, no new row is inserted. If it differs, a new row is inserted with the previous row marked `superseded_by_id = new.id` and `superseded_by_id IS NOT NULL` on the prior row; the new row's `supersedes_id` points to the prior. This allows safe re-runs when a chapter is re-authored.

**Script:** `scripts/_ingest_chapter_prose_v1_{date}.py` (to be created; supersedes the existing `_backfill_published_clusters_to_prose_section_20260527.py` for the publishing pipeline).

**Status transition:** when all seven `sc_v2_ch{1..7}` rows exist in `prose_section` for the cluster (any active version), the cluster status transitions from `Analysis Complete` to `Publication Ready`. This transition is performed by the ingest script when it detects the seventh chapter row landing.

---

## §6. Step 3 — Consolidate the seven chapters

**Owner:** Claude AI (chat). One consolidation session per cluster.

**Discipline:** the style/method discipline in §7 applies.

**Task:** consolidate the seven chapter prose rows into a single essay.

**Inputs to the consolidation session:**

- The seven chapter prose rows from `prose_section` (latest active version per chapter).
- The style/method discipline (§7).
- The consolidation specification (§6 itself; this section).

**Output:**

- A single `.md` file: `Sessions/Session_Clusters/{CODE}/publishing/wa-cluster-{CODE}-essay-v{V}-{YYYYMMDD}.md`.
- A `.docx` rendering of the same: `Sessions/Session_Clusters/{CODE}/publishing/wa-cluster-{CODE}-essay-v{V}-{YYYYMMDD}.docx`.

Both files are saved to disk only. **Neither file is stored in the database.**

**Consolidation discipline:**

The consolidation is a **stylistic harmonisation task, not a synthesis task.** No new findings, framings, emphases, or selections enter the consolidated essay. Everything in the consolidated essay must already be present in the seven chapter prose rows.

The consolidation removes:
- **Duplication.** The same point made in two chapters. Keep the better location; remove the other.
- **Repetitiveness.** Within a chapter, the same point made in two paragraphs. Keep the better paragraph.
- **Awkward chapter transitions.** The boundary between chapters reads as the seam it is; smooth it so the essay reads as one piece.
- **Tonal inconsistencies across chapters.** If two chapters drift in voice, register, or sentence rhythm, bring them into a single voice without rewriting either substantively.

The consolidation does not:
- Introduce verses not already quoted in the chapter prose.
- Introduce findings not already named in the chapter prose.
- Reframe what a chapter says.
- Add a thesis, argument, or take that is not already in the chapter prose.
- Select or prioritise content for narrative effect.

If the consolidator wants to write something not already in the chapter prose, the correct action is to stop and return to Step 2 to revise the relevant chapter, then re-run Step 3.

**Quality bar:**
1. Every claim in the consolidated essay can be traced to a specific passage in one of the seven chapter drafts.
2. No verse appears in the consolidated essay that is not already quoted in at least one chapter draft.
3. The consolidated essay reads as a single piece, not seven chapters stitched together.
4. The consolidated essay obeys the style/method discipline (§7) end to end.

**Status:** Step 3 does not change cluster status. Cluster status is already `Publication Ready` from the seventh chapter landing in `prose_section` at Step 2.

**Script:** `scripts/_consolidate_cluster_essay_v1_{date}.py` (to be created). Reads the seven chapter rows from `prose_section`, builds the input package for the AI session, receives the consolidated essay, saves the `.md`, and renders the `.docx` via the existing `_render_essay_to_docx_v1_20260527.py` script.

---

## §7. Style and method discipline

This is the discipline applied at every AI authoring step in this publishing pipeline (Step 2 chapter authoring and Step 3 consolidation).

### §7.1 What you are writing

A **plain-English published study** of a family of related inner-being characteristics from Scripture. The reader is an intelligent person who has no familiarity with this project's analytical vocabulary. They are reading the study as they would read any serious essay on the Bible's treatment of a theme.

Each chapter (Step 2) is a standalone unit of prose. The chapter authored in one session does not know what the other chapters say; cross-chapter consistency is maintained by the cross-chapter scaffold provided in every chapter input.

The consolidated essay (Step 3) is a single piece of prose. The consolidator does see all seven chapters and harmonises across them.

### §7.2 Voice and tone

- **Essayistic.** Continuous prose, not bullet points. Topic sentences carry the argument.
- **Evidential.** Every analytical claim is grounded by a quoted verse — never by appeal to general impression.
- **Reverent without being devotional.** This is a study of Scripture, not a sermon. Avoid liturgical phrasing.
- **Clear about what is shown and what is silent.** Where the verse evidence is silent on something meaningful, name it; where the silence is routine, do not.
- **Confident, not hedging.** Do not pad with "perhaps", "it could be argued", "in some sense" when the evidence is plain.

Address the reader in the third person. Avoid first-person plural ("we see that…") — it draws attention to the author. State the evidence and let it speak.

### §7.3 Words to avoid

The following project-internal terms must not appear in published prose.

| Avoid | Use instead |
|---|---|
| cluster | "this study", "these related characteristics", "the family of characteristics" |
| sub-group | "characteristic", "facet", "form" |
| VCG / verse context group | "meaning group" (rare); usually describe inline |
| anchor verse | "key verse", "central verse" |
| finding | "what the evidence shows", "what the verses tell us", "the pattern" |
| tier / T0 / T1 … | the thematic name (see §7.5) — never the code |
| catalogue prompt / question code | not exposed |
| constitutional location | "where this lives in the inner person", "the inner home of …" |
| inner faculty | "the inner capacity", "the part of the person that …" |
| sub-group code (M15-A etc.) / VCG code (M15-A-VCG01) | not in prose — used only in editing footnotes if at all |
| domain, findings | not exposed |

Avoid also the broader pattern of analytical category-words even where not listed: "constituted character", "structural opposite", "governing layer", "downstream effect", "receptive gateway", "content-base", and the like. These are project-internal vocabulary even though they do not appear in programme code form. Use plain theological language.

Words that **are** fine: wisdom, understanding, knowledge, inner life, inner person, heart, mind, will, conscience, soul, spirit, God, Scripture, character, attribute, characteristic, evidence, pattern, theme.

### §7.4 Citation discipline

**Every analytical claim must be grounded by a quoted verse.** No exceptions, except as relaxed for Chapter 1 in §8.1 below.

When you make a claim:

1. **Name the verse** in the prose using standard biblical citation (e.g. "as Pro 16:23 makes plain…", "Daniel's confession in Dan 2:20…").
2. **Quote it verbatim** — inline with quotation marks for short quotes, or in an indented block when the quote is long enough to warrant separation.
3. **Where the meaning-group context shapes the reading**, name it inline (e.g. "in the verses where wisdom is named as God's own attribute — most clearly at Dan 2:20 — …").

**Never** cite project-internal codes (finding-id, tier code, VCG code, prompt code).

The chapter input provides every verse you should quote with its full text inline. You do not need to re-source verses from external concordances.

**Minimum density:** each AI-WRITE zone that makes analytical claims cites at least two key verses verbatim from the list in its zone instruction. Deeper treatments cite more. The required verses per zone are listed in the input file's AI-WRITE comment block.

### §7.5 Analytical lenses (the seven thematic names)

The chapters of the study are organised around analytical lenses. The internal codes (T0…T7) must never appear in the prose. Use the thematic name instead when you need to refer to the lens:

| Internal code (NOT in prose) | Thematic lens (use this language) |
|---|---|
| T0 | The divine pattern — what Scripture says about God in this characteristic |
| T1 | What the characteristic is (definition, name, kind, boundary, modes) |
| T2 | Where the characteristic lives in the inner person |
| T3 | Which inner capacities the characteristic engages |
| T4 | How the characteristic moves — between God and the person, between persons |
| T5 | How the characteristic is formed, deepens, is tested, is transformed |
| T6 | How the characteristic relates to other inner characteristics |
| T7 | The view from outside Scripture — what physical and clinical sciences observe |

You will rarely need to name the lens explicitly. Most chapters frame the lens through their own opening prose and section structure; the reader does not need to be told "this is the T2 chapter".

### §7.6 The silence principle

**Name a silence only when its absence is meaningful.** A silence is meaningful when one of two conditions holds:

1. **Expectation-then-absence.** Something in the evidence creates an expectation that is then not met — for example, the divine-image pattern holds across most characteristics, and then one characteristic has no divine version. The contrast itself is a finding.
2. **Silence shapes the characteristic.** The absence is what gives the characteristic its shape — for example, meditative inner activity is largely silent on God's own meditation, which marks meditation as the characteristically creaturely mode.

**Routine absence needs no comment.** If a particular inner location (say, the kidneys) is not named in the evidence for a particular characteristic, that is the default rather than a finding. Do not list silences as inventory; surface only the silences that carry weight.

The analytical record's "silent" findings are the candidate pool — but not every silent finding deserves prose treatment. Use judgement: ask "does naming this silence add to the reader's understanding of the characteristic, or is it filler?" When in doubt, leave it out.

### §7.7 Handling gaps in the analytical record

Some chapters (especially Chapter 7) will tell you that the analytical record is thin on a particular lens. In those cases:

- **State the gap honestly** in the prose — do not bluff.
- **Bring general scientific or scholarly knowledge** where the chapter's specification explicitly invites you to (e.g. Chapter 7 invites general clinical-science knowledge as a supplement).
- **Do not overclaim.** A short, careful reflection that acknowledges the thinness is better than an inflated treatment.

### §7.8 What you return (per chapter authoring run)

A **single completed Markdown file** — the chapter input file with prose written into every AI-WRITE zone, in place of the zone marker and its placeholder text.

- Keep the chapter title and section headers intact.
- Remove the AI-WRITE marker comment blocks (`<!-- AI WRITE: … -->`) — they are scaffolding.
- Leave the EVIDENCE comment blocks (`<!-- EVIDENCE: … -->`) — they are stripped at the consolidation step.
- Do not invent new sections or reorder existing ones.
- Do not write material that belongs to a different chapter. The chapter specification in §8 names what is in scope; everything else is out of scope for this run.

**File naming convention** for the chapter draft:

```text
wa-cluster-{CODE}-ch{N}-draft-v{V}-{YYYYMMDD}.md
```

Saved to `Sessions/Session_Clusters/{CODE}/published/`.

### §7.9 Cross-chapter consistency

Other chapters are written in separate runs. You will not see the other chapters' prose. To maintain consistency:

- Use the **brief characteristic profiles** provided at the top of every chapter input — these define how each characteristic is described across the study.
- Use the **thematic lens names** consistently (§7.5).
- Do not preview content that belongs to a later chapter (e.g. don't describe how a characteristic is formed in Chapter 4 — that belongs to Chapter 5).
- Do not summarise content from an earlier chapter at the start of yours unless the chapter specification explicitly tells you to.

If a claim feels like it would benefit from cross-chapter framing, trust the structure — the consolidation pass (Step 3) will harmonise across chapter boundaries.

### §7.10 Reverse audit on completion (chapter authoring only)

Before you return the chapter draft, perform an explicit reverse audit. The audit confirms that the chapter has used the evidence it was given.

For each per-characteristic section (or for the chapter as a whole where there are no per-characteristic sections):

**A. Findings coverage.** Walk through every finding in every EVIDENCE block inside that section's scope. For each finding, confirm one of:

1. The finding's claim is present in the prose (it does not need to be paraphrased verbatim — the claim must be reflected).
2. The finding is a **routine silent** finding whose omission is justified under §7.6 (the silence principle).
3. The finding was redundant with a finding already covered.

If a finding falls outside (1)–(3), you missed it. Add prose that incorporates it.

**B. Key verse coverage.** Walk through every key verse listed for that section. Confirm each key verse is quoted verbatim at least once in the prose. If any is uncovered, add a sentence that uses it.

**C. Lens coverage.** For each tier in the section's scope (e.g. Ch 4 = T2 + T3; Ch 5 = T4 + T5 + T1), confirm the chapter actually engages with that lens. If a lens is wholly absent, ask whether the prose is too narrow.

The reverse audit happens **before** the self-review (§7.11). Audit first, then read.

### §7.11 Self-review pass on completion (chapter authoring and consolidation)

After the reverse audit, read through the chapter (or the consolidated essay) from start to finish as a reader would. Look for and correct:

- **Repetition.** The same point made in two places. Pick the better location and remove the duplicate.
- **Overreach.** A claim that goes beyond what the cited verse(s) actually carry. Soften or remove; do not add an extra verse to prop it up unless the evidence is genuinely there.
- **Padding.** Sentences that add words but no content — throat-clearing, restating the section heading, signposting that the reader does not need.
- **Tonal drift.** Devotional phrasing creeping in; first-person plural; hedging language; jargon from §7.3 that slipped through.
- **Structural drift.** Section reading as a list of findings rather than essayistic prose; missing topic sentences; sentences that depend on a finding code the reader cannot see.

Edit in place. The output you return is the post-self-review version.

### §7.12 Order of operations on completion

For chapter authoring (Step 2):
1. Write the chapter.
2. Reverse audit (§7.10): findings coverage → key verse coverage → lens coverage.
3. Self-review pass (§7.11): repetition → overreach → padding → tonal drift → structural drift.
4. Return.

For consolidation (Step 3):
1. Consolidate the seven chapters.
2. Self-review pass (§7.11).
3. Trace audit: every claim in the consolidated essay traces to a specific chapter passage; every verse in the consolidated essay appears in at least one chapter draft.
4. Return.

---

## §8. Chapter specifications

The seven chapter specifications, one per chapter. Each specifies what that chapter does, how it is structured, what to write, length targets, and citation rules. The §7 style/method discipline applies to all seven; this section is the chapter-specific guidance layered on top.

### §8.1 Chapter 1 — What this study is

**What this chapter does.** Chapter 1 is the **opening of the published study**. It introduces the reader — who has no familiarity with the project or its analytical vocabulary — to the family of characteristics this study covers. The chapter answers, in plain English:

- **What these characteristics are.** Name the inner-life domain covered. Say what kind of inner-life material the reader is about to encounter.
- **What they cover together.** What inner-life territory the characteristics, taken as a set, address.
- **Why they belong together.** What makes this family a family — what they share as inner-being phenomena, the common features that lead the study to treat them as one body of related characteristics.
- **What they share.** Cross-cutting patterns — most importantly the divine-image pattern where one applies, the inner-being-located pattern, and any other cluster-wide shared structure surfaced by the cluster-wide evidence.
- **How they depend on each other.** Any visible interdependence — characteristics that produce or condition others, characteristics that operate together, the way the family's members reinforce each other.

The chapter is short: it orients the reader and **previews** what follows in one closing sentence. It does not analyse — analysis happens in chapters 3 through 7.

**Structure.** A single block of prose, ~300–500 words. One AI-WRITE zone. No sub-headers, no bulleted lists. Topic sentences carry the argument. The closing sentence previews the chapters that follow.

**What to write.**

- **Open** with what the reader is about to encounter. Name the inner-life territory plainly — the kind of inner life the characteristics together describe. Avoid abstract framing; say the thing.
- **Develop** the shared character of the family. The cluster-wide evidence below your zone (the cluster-synthesis findings at T0 and T1) names the patterns that hold across the whole family. Synthesise them into a coherent paragraph: what is true of every (or almost every) characteristic in this study? The divine-image pattern is usually the strongest such pattern. Other cluster-wide patterns may include shared inner location, a shared formative dynamic, a shared eschatological orientation.
- **Acknowledge variation within the family.** Where one or two characteristics break the cluster-wide pattern, the variation is itself a finding worth naming briefly — not catalogued, but flagged. Apply the silence principle from §7.6 — surface only variations that carry weight; routine non-uniformity is not surfaced.
- **Hint at interdependence.** Where the cluster-wide evidence shows characteristics conditioning or producing one another, name the pattern briefly. Do not exhaust it — Chapter 6 develops inter-characteristic relationships in detail.
- **Close** with one sentence that previews what follows. The reader should know, by the last sentence of Chapter 1, that the study will treat each characteristic in turn at depth (chapters 2–7).

**Citation rules.** Chapter 1 is the one chapter where citation density is **lighter** than the rest of the study. You may make framing claims that summarise the cluster-wide pattern without verse-by-verse citation, provided:

- The framing claim is **directly supported** by the cluster-synthesis findings in the evidence block (which themselves are grounded in the verse evidence across multiple characteristics).
- **At least one key verse** is quoted verbatim somewhere in the chapter to anchor the cluster-wide arc concretely. The verse you pick should be the one that most clearly establishes the strongest cross-cluster pattern.
- **Do not** make analytical claims about a single characteristic without citing a verse — for single-characteristic claims, normal citation discipline applies (per §7.4).

**Avoiding overlap with later chapters.**

- Per-characteristic description is the subject of Chapter 2. Do not describe each characteristic individually in Chapter 1.
- The divine pattern is the subject of Chapter 3. Chapter 1 may name the divine-image pattern as one of the cluster-wide shared features, briefly, without unfolding the per-characteristic divine treatment.
- Where the characteristics live / how they work / how they relate / the view from outside Scripture are chapters 4 through 7. Stay out of those territories.

### §8.2 Chapter 2 — The characteristics in this study

**What this chapter does.** Chapter 2 introduces each characteristic in the study in turn — short, focused sections that give the reader a working sense of every characteristic before the deep dives begin. For every non-BOUNDARY characteristic, you write a single ~200–300 word section that answers:

- **What this characteristic is** — its name (in plain English, not by code), the central inner-life phenomenon it names.
- **What it looks like in Scripture** — anchored by one or two key verses that capture the characteristic most clearly.
- **How it differs from the others in this study** — what distinguishes this characteristic from its closest neighbours in the family.

There is also a final, shorter section acknowledging the **supporting characteristics** (BOUNDARY) — terms that appear in the verse evidence supporting the study but are not themselves inner-being characteristics. Where the cluster has no BOUNDARY sub-group, this final section is omitted.

The chapter is the reader's **map** for what follows. After Chapter 2, the reader should know which characteristics will be treated, in what order, and roughly what each one is.

**Structure.**

1. Chapter opening (~50–80 words). A brief framing sentence or two saying that the Bible's vocabulary for this inner-life domain organises into N characteristics.
2. Per-characteristic sections, in order. One per non-BOUNDARY characteristic. Each section header is provided; you write only the body prose.
3. Supporting characteristics section (final). A short acknowledgement of the BOUNDARY terms. Omitted if no BOUNDARY sub-group.

**Per-characteristic section (~200–300 words):**

- **Open** with the characteristic in plain English — name it the way a non-specialist would understand it, not the way the analytical record names it.
- **Develop** the characteristic in 2–3 sentences. Draw on the sub-group description provided in the evidence below — the description is your *source*, not your *output*. Rewrite into plain English; do not paste the description verbatim. Anchor with one key verse quoted briefly inline.
- **Distinguish** the characteristic from its closest neighbours in the family in 1–2 sentences. This is the *positioning* sentence — what makes this characteristic this characteristic and not another.
- **Close** with a key verse that captures the characteristic most clearly — quoted verbatim, briefly framed.

The 200–300 word target is a guide, not a cap. Some characteristics need more; some with sparse evidence may close at 200.

**Supporting characteristics section (~150 words).** Names what the supporting terms are at the family level; says what role they play in the inner-life domain (they support the inner-life characteristics without being inner-life characteristics themselves); notes that they are not treated at full depth in the chapters that follow.

**Citation rules.**

- Each per-characteristic section quotes at least one key verse verbatim (the required minimum is listed inside the AI-WRITE zone in the input file). Two is better where they help establish the characteristic.
- The first verse you quote should be the one that most clearly establishes the characteristic.
- No quotation is required for the chapter opening or the supporting characteristics section.

**Avoiding overlap with later chapters.**

- Where the characteristic lives in the person is the subject of Chapter 4. You may name the inner location briefly when establishing the characteristic ("wisdom seated in the heart…"), but do not unfold the topography here.
- How the characteristic works (movement, formation) is the subject of Chapter 5. You may hint at how the characteristic operates ("given by God, expressed through speech"), but do not develop the dynamics.
- How it relates to other characteristics is the subject of Chapter 6. Use the "distinguish from neighbours" sentence to *position* the characteristic against the family; do not catalogue the relationships.
- The view from outside Scripture is the subject of Chapter 7. No clinical-science framing here.

### §8.3 Chapter 3 — The divine pattern

**What this chapter does.** Chapter 3 tells the story of **how Scripture attributes these characteristics to God**. It is the first chapter where the study turns to the analytical evidence in earnest, and it does so through a single unifying lens — the divine pattern. The chapter answers:

- **What does Scripture say about God in this family of characteristics?**
- **What is the cluster-wide divine-image pattern?** The arc that runs across most or all of the family.
- **Where does the divine treatment vary per characteristic?**

The chapter has two distinct structural parts: a **cluster-wide spine** that tells the unifying story, followed by **per-characteristic variation paragraphs** that note where each characteristic departs from or refines the cluster-wide pattern.

**Structure.** A single AI-WRITE zone covering both the spine and the per-characteristic paragraphs:

1. **Cluster-wide spine (~600–1500 words).** Continuous prose. The unifying arc.
2. **Per-characteristic variation paragraphs (~100–250 words each).** One short paragraph per non-BOUNDARY characteristic, in the order they appear in the cluster.

Total target: ~1500–2500 words.

**The cluster-wide spine.**

- **Open** with the cluster's primary divine claim — typically the divine-image pattern itself: each characteristic in this family is first God's own attribute, then the human person's image of that attribute. Anchor the opening with a key verse that holds the strongest divine-attribute claim in the family.
- **Develop** the spine across 3–6 paragraphs. Move through the cluster's divine treatment by *theme*, not by characteristic — possible themes include: God's own possession of these attributes; the giving of these attributes to the human person; christological consolidation; divine opposition to autonomous human claim; eschatological orientation.
- Not every cluster will have evidence on every theme. Use what the evidence carries.
- **Quote key verses verbatim throughout.** The spine is the chapter's primary verse-citation zone — claims about God should be densely supported.

**Per-characteristic variation paragraphs.** After the spine, write one short paragraph per non-BOUNDARY characteristic. Each paragraph answers:

- **Does this characteristic follow the cluster-wide pattern?** If yes, name it briefly and move on.
- **Where does it depart?** What is distinctive about this characteristic's divine treatment compared to the family as a whole?
- **If Scripture is silent on God's possession of this characteristic, and that silence is meaningful**, name it.

The variation paragraph should cite at least one key verse that holds the departure or that anchors the silence-as-finding.

**Citation rules.**

- The cluster-wide spine quotes at least five key verses verbatim.
- Each per-characteristic variation paragraph quotes at least one key verse verbatim, unless the paragraph is naming a silence-as-finding.
- At least one quoted verse names God explicitly as possessor or giver of one of the family's characteristics.

### §8.4 Chapter 4 — Where each characteristic lives in the person

**What this chapter does.** Chapter 4 takes each characteristic in the study in turn and goes deep on **where in the inner person it lives**. For every non-BOUNDARY characteristic, you write a single section that answers:

- **Where it lives.** Which named inner location does the verse evidence place this characteristic in — heart, mind, will, conscience, soul, spirit, body? Is it located narrowly or broadly? Are there divine-versus-human differences in location?
- **Which inner capacities it engages.** Of the standard inner capacities — perception, thought, memory, feeling, conscience, will, agency — which ones does this characteristic call into action, and in what relationship to one another?

**Structure.**

1. Chapter opening (~40–80 words).
2. Per-characteristic sections, in order. One per non-BOUNDARY characteristic.

**Per-characteristic section (~800–1500 words):**

- **Open** with where the characteristic sits in the inner person — the single most defensible inner location given the evidence — and quote the key verse that most clearly shows it.
- **Develop** the inner location with secondary evidence: other key verses that confirm, extend, or qualify the primary location.
- **Then turn to the inner capacities** the characteristic engages. Move through the relevant capacities in turn — perception, thought, memory, feeling, conscience, will, agency — citing key verses where the evidence shows the capacity active.
- **Where the evidence shows a divine-versus-human distinction in location**, make that distinction explicit and cite the verses on each side.
- **Where the evidence is silent on a specific inner location or capacity**, name the silence rather than fill it.
- **Close** the section with a sentence that captures what the inner topography of this characteristic looks like as a whole.

**Citation rules.**

- Each per-characteristic section quotes at least three key verses verbatim.
- At least one quoted verse comes from the meaning group that names the inner location.
- The first quoted verse in each section establishes the primary inner location.

### §8.5 Chapter 5 — How each characteristic works

**What this chapter does.** Chapter 5 takes each characteristic in turn and sets its inner topography in motion. For every non-BOUNDARY characteristic, you write a single section that answers:

- **How it moves.** Between God and the human person (downward — gift, command, indwelling; upward — knowing, asking, receiving). Between persons. In covenant. Against opposition.
- **How it is formed.** Conditions that produce it. Disciplines that deepen it. Trials that test and refine it. The eschatological trajectory.
- **How it modulates.** Modes of operation (immediate response vs. sustained character; act vs. condition; received vs. exercised).

This chapter draws on three lenses together: how it moves (T4), how it is formed (T5), modes (T1).

**Structure.**

1. Chapter opening (~40–80 words).
2. Per-characteristic sections, in order.

**Per-characteristic section (~800–1500 words):**

- **Open** with the most distinctive aspect of how this characteristic works — usually the dominant direction of movement. Anchor with a key verse that captures the movement.
- **Develop the movement.** Trace the characteristic's flow: where it comes from (origin); how it is exchanged or transmitted between persons; where it goes (expression); how opposition acts against it.
- **Then turn to formation.** How the characteristic comes into being and deepens within a person.
- **Then turn to modes.** Where the evidence shows the characteristic operating in distinct modes, name those modes and cite the verses that hold each.
- **Where the evidence shows a divine-versus-human distinction in how the characteristic works**, make that distinction explicit and cite verses on each side.
- **Close** the section with a sentence that captures the characteristic's working life as a whole.

**Citation rules.**

- Each per-characteristic section quotes at least three key verses verbatim.
- At least one quoted verse holds a movement claim.
- At least one quoted verse holds a formation claim.
- The opening of each section cites a verse that captures the characteristic's most distinctive movement.

### §8.6 Chapter 6 — How each characteristic relates to the others

**What this chapter does.** Chapter 6 takes each characteristic in turn and maps how it relates to the other characteristics in this family. For every non-BOUNDARY characteristic, you write a single section that answers:

- **What is it paired with?**
- **What is it opposed by?**
- **What produces it?**
- **What does it itself produce?**
- **What shared vocabulary or imagery binds it to its neighbours?**

This is the **map** of the family. After Chapter 6, the reader should understand each characteristic as a node in a network — not a stand-alone inner-life feature.

**Structure.**

1. Chapter opening (~40–80 words).
2. Per-characteristic sections, in order.

**Per-characteristic section (~400–800 words):**

- **Open** with the characteristic's most distinctive relational profile in a single sentence — typically the strongest pairing or the strongest opposition.
- **Develop** the relationships in turn: pairings, oppositions, what produces this characteristic within the family, what this characteristic produces, shared vocabulary or imagery.
- **Close** the section with a sentence that captures the characteristic's relational position within the family as a whole.

**Citation rules.**

- Each per-characteristic section quotes at least two key verses verbatim.
- At least one quoted verse shows a relational claim concretely.
- Where a production line is named (X produces Y, Y follows from X), the verse that holds the production claim is cited.

**Relationships to characteristics outside the family.** When the verse evidence shows a relationship that runs to a characteristic not in this study, name the relationship, but make clear that the outside characteristic is treated elsewhere in the wider research programme. Do not unfold it.

### §8.7 Chapter 7 — The view from outside Scripture

**What this chapter does.** Chapter 7 takes each characteristic in turn and gives the reader a short, honest reflection on what human and clinical sciences observe about the corresponding inner capacity. The chapter is unique in two respects:

- **The analytical record is thin on this lens.** Unlike chapters 4–6, the verse-evidence-grounded findings for this chapter are sparse. You are expected to bring **general scientific and scholarly knowledge** into the writing, alongside whatever the analytical record carries.
- **The chapter is structurally smaller per section.** ~400–500 words per characteristic, not 800–1500.

For every non-BOUNDARY characteristic, you write a single ~400–500 word section that answers:

- **What do human and clinical sciences observe about the corresponding human capacity?**
- **Where the scientific picture is in synergy with the biblical picture**, name the convergence.
- **Where the scientific picture is silent on what Scripture emphasises**, name the gap.
- **Where the scientific picture diverges from the biblical picture**, name the divergence.

**Structure.**

1. Chapter opening (~80–120 words). A brief framing paragraph that names the purpose of the chapter and explicitly acknowledges that this view-from-outside is under-developed in the analytical record at present.
2. Per-characteristic sections, in order.

**Per-characteristic section (~400–500 words):**

- **Open** by naming the corresponding human capacity in clinical-science terms.
- **Develop** in three movements: Synergy, Gap, Divergence.
- **Where the analytical record offers no view-from-outside material for this characteristic, say so plainly.**
- **Close** with a sentence on what a fuller treatment would investigate.

**Citation rules.** Different from the other chapters:

- Biblical citations are lighter. Cite at least one key verse verbatim per section — the verse the analytical comparison hinges on.
- Scientific claims do not require verse citation. Where you draw on general clinical-science knowledge, state the claim as scientific knowledge ("cognitive psychology typically describes…").
- **Do not invent specific studies, named researchers, or specific findings.** Stay at the level of well-established consensus claims.
- The under-development acknowledgement in the chapter opening is required.

---

## §9. What is retired by this document

The following files and processes are explicitly retired by this baseline. They are not part of the publishing pipeline going forward.

**Retired files (archive but do not load):**

- `wa-sessionc-cluster-style-method-v1_1-20260512.md` — its content is absorbed into §7 of this document.
- `wa-sessionc-cluster-ch1-instruction-v1_0-20260512.md` — its content is absorbed into §8.1.
- `wa-sessionc-cluster-ch2-instruction-v1_0-20260512.md` — its content is absorbed into §8.2.
- `wa-sessionc-cluster-ch3-instruction-v1_0-20260512.md` — its content is absorbed into §8.3.
- `wa-sessionc-cluster-ch4-instruction-v1_0-20260512.md` — its content is absorbed into §8.4.
- `wa-sessionc-cluster-ch5-instruction-v1_0-20260512.md` — its content is absorbed into §8.5.
- `wa-sessionc-cluster-ch6-instruction-v1_0-20260512.md` — its content is absorbed into §8.6.
- `wa-sessionc-cluster-ch7-instruction-v1_0-20260512.md` — its content is absorbed into §8.7.
- `wa-sessionc-cluster-appendices-instruction-v1_0-20260512.md` — appendices removed from the publishing pipeline.
- `wa-v3-publication-pipeline-design-v1-20260527.md` — superseded by this document.

**Retired sections in active instruction documents:**

- `wa-sessionb-cluster-instruction-v3_0-20260527.md` §9 "Phase E — Publication prose" — superseded by this document. The v3_0 cluster instruction should be amended to replace §9 with a one-paragraph stub pointing to this document.

**Retired prose_section_type codes:**

The following section type codes have never held data and are not part of the publishing pipeline. They should be marked `delete_flagged=1` in `prose_section_type` (or dropped entirely):

- `sc_v2_tier_T0` through `sc_v2_tier_T7` (8 codes — the tier prose model that was never used)
- `sc_v2_synth_opening`
- `sc_v2_synth_divine_pattern`
- `sc_v2_synth_appendix`

**Retired artefact formats:**

- Single-pass essay format (the 2026-05-27 catch-up form).
- Stitched-together book format (the M38 form produced by concatenation).
- Appendix A (terms), Appendix B (key verses table), Appendix C (method note) — these are reproducible from the database on demand and are not part of the publishing pipeline.

---

## §10. Scripts and section types — the publishing pipeline footprint

The complete script and DB footprint of the publishing pipeline.

**Scripts:**

- **Step 1 input generation.** `scripts/_generate_cluster_session_c_inputs_v2_20260512.py` (existing; to be amended to produce 7 chapter inputs only, no appendices).
- **Step 2 chapter ingest into DB.** `scripts/_ingest_chapter_prose_v1_{date}.py` (to be created). Reads chapter draft files, ingests into `prose_section`, handles idempotency via body-hash comparison, fires status transition when the seventh chapter row lands.
- **Step 3 consolidation.** `scripts/_consolidate_cluster_essay_v1_{date}.py` (to be created). Reads the seven chapter rows from `prose_section`, packages them for the AI consolidation session, receives the consolidated essay, saves `.md`, renders `.docx` via `_render_essay_to_docx_v1_20260527.py`.
- **DOCX renderer (existing).** `scripts/_render_essay_to_docx_v1_20260527.py` — used by Step 3.

**Section type codes used:**

- `sc_v2_ch1` through `sc_v2_ch7` — seven chapter prose codes.

**Tables read:**

- `cluster`, `characteristic`, `cluster_subgroup`, `characteristic_subgroup`, `verse_context_group`, `vcg_term`, `cluster_finding`, `wa_obs_question_catalogue`, `verse_context`, `wa_verse_records`, `prose_section`, `prose_section_type`.

**Tables written:**

- `prose_section` (Step 2 — chapter ingest).
- `cluster.status` (Step 2 — status transition to `Publication Ready` when seventh chapter row lands).

**Files written to disk:**

- Step 1: 7 chapter input files in `Sessions/Session_Clusters/{CODE}/inputs/`.
- Step 2: 7 chapter draft files in `Sessions/Session_Clusters/{CODE}/published/`.
- Step 3: 1 consolidated essay `.md` and 1 `.docx` in `Sessions/Session_Clusters/{CODE}/publishing/`.

---

## §11. Status

`Analysis Complete` is the precondition. Step 1 does not change status. Step 2 transitions to `Publication Ready` when all seven chapter rows are in `prose_section`. Step 3 does not change status.

The cluster is "published" when its status is `Publication Ready`. The cluster overview report should detect this state by querying `prose_section` for the seven chapter codes (see `scripts/_generate_cluster_overview_v1_20260508.py` — already updated to do so as of 2026-05-30).

---

## §12. Re-runs and updates

Each step is independently re-runnable.

**Step 1 (input generation):** safe to re-run any time. Overwrites the input files in `inputs/`. New input files reflect the current state of the DB.

**Step 2 (chapter authoring + ingest):** safe to re-run any chapter independently. The ingester's body-hash check (§5) handles idempotency. A re-authored chapter creates a new version row in `prose_section`; the previous row is marked superseded but preserved.

**Step 3 (consolidation):** safe to re-run any time. Reads the latest active chapter rows from `prose_section`. Overwrites the essay `.md` and `.docx` in `publishing/`.

When findings are updated (post-Phase-D correction, post-audit fix), the typical recovery flow is:

1. Update the relevant `cluster_finding` rows.
2. Re-run Step 1 — input files refresh from DB.
3. Re-run Step 2 for the affected chapters — chapters whose findings changed get new versions in `prose_section`; status remains or returns to `Publication Ready` when all seven are current.
4. Re-run Step 3 — consolidated essay rebuilds from the updated chapter rows.

---

*End of cluster publishing instruction.*
