# Study foundations — critical re-evaluation

> **Living document · Doc version: 1 · Last updated: 2026-06-04.**
> **Purpose:** step back from the machinery and critically re-evaluate the study from first
> principles, across four areas: (a) the focus of the study, (b) the completeness of the raw data,
> (c) the fundamental rules for analysis, (d) the end point. The researcher reviews and rewrites
> in place; CC drafts and revises on direction. Versioned by git (living-doc policy, no filename `-vN`).

---

## 0. Why this document exists

The context of this critical evaluation:

This study began in January 2026 from two converging interests: (a) a deep and continuing exploration of how the God–Man reality works; and (b) the realisation that AI made it possible to study this at a scale never before achievable.

The exploration started with a cursory cycle through how AI operates on and reasons about data, within the context of the human spirit, soul and body and the Holy Spirit. It produced two studies of roughly 100 pages each — *Spirit, Soul and Body — What a Human Being Is Made Of*; and *The Holy Spirit — His Origin, His Nature, His Work, His Character, and How He Meets Us: a five-thousand-year journey from Genesis to the present day*.

These studies were the first real learning experience in using AI, and delivered a reasonably good outcome. Yet, though fairly comprehensive, they remained deficient and incomplete in coverage: the findings appeared strong at first, but deteriorated under further questioning, becoming progressively more questionable.

One key observation was that the characteristics of the spirit and soul — and, to a degree, the body — were vastly understated, meaning that many characteristics were simply never analysed or brought into focus.

This observation, in early February 2026, led to this project: a deep and as-comprehensive-as-possible study of every word that may be associated with the inner being in the Bible, to assess how the inner being works as the Bible describes it.

This project is now in its fifth month and has gone through numerous reworks, restarts, revised methodologies, discards and more.

The recurring errors across the programme have a single root: the impulse of AI to impose
tidy structure on a subject that has none — *every object must have one home, must reconcile, must be
completed, the gate must go to zero.* while the subject is **human inner life and behaviour: unpredictable,
not systemisable, infinitely variable.**  AI's fundamental learned tendencies — framing, filtering, assuming, imposing order, selecting the *reasonable* rather than the *correct*, and a lack of critical thinking — are a severe shortcoming. The study methodology must compensate for these in order to harness AI's genuine strengths: rapid reading and reasoning, digesting far more data at once than I can, and — honestly — surfacing observations I would not have made myself. This leads to the next major deficiency (AI's, and mine): the corpus of raw data is too large for AI to digest in one pass, so it must be broken into pieces. Breaking the material into logical units has been the single greatest source of rework and restarts — because every new method introduces fault lines, and AI keeps falling over on them, driven by its deep need to structure, organise, and create order.

Hence the decision today (2026-06-04): to stop and think again. The "remediation" effort (audit gates driven to zero, pointer/finding disposition, mass reassignment) is **closed down** — it was the wrong frame.

What is necessary is to re-evaluate:
a) The focus of the study
b) The completeness of the raw data
c) The fundamental rules for analysis of the data
d) The end point

The rest of this document is for re-establishing the foundations before any further analytical work.

###############################





---

## a) The focus of the study

*What, precisely, is this study trying to understand and produce?*

**Current understanding (to be reviewed):**
- The study examines **the inner life of mankind as disclosed in Scripture**, through the biblical
  vocabulary for it — ~214 English anchor words, each mapped to its Hebrew (OT) and Greek (NT) terms
  via Strong's, and grounded in the verses where those terms are used.
- "Inner being" means the **entire** human inner life — moral, emotional, volitional, relational,
  vertical and horizontal — with **no theological narrowing** (correction of 2026-05-17). Pure-human
  inner states are fully in scope.
- The vocabulary is organised into **clusters** (Fear, Anger, Grief, Joy, Love, Peace, Shame,
  Righteousness, …), each a region of the inner life described by several **characteristics**.
- **The distinctive aim is comprehensiveness of characteristics.** The project was born because earlier
  work *understated* the characteristics of the inner being (§0) — so its defining purpose is to surface
  and account for the **full range of characteristics**, especially those other treatments miss, in
  service of the larger questions: *how the inner being works*, and ultimately *how the God–Man reality works*.

**Tensions / open questions for critical review:**
1. Is the object of study the **vocabulary**, the **inner life itself**, or the **relationships**
   between inner-life states? These imply different analyses and different outputs.
2. Clusters and characteristics are *our* organising lens. How much weight should they carry, given
   the subject resists partition? Are they scaffolding for reading, or claims about reality?
3. Is the aim **descriptive** (faithfully account for what Scripture shows of the inner life),
   **comparative** (how the biblical account relates to other frameworks of human nature), or both?
4. Where is the line between *what the text says* and *what we synthesise* — and how is that line kept
   honest so synthesis never overwrites the data?
5. Given the genesis (understated characteristics), is **completeness of characteristic coverage** the
   study's primary success criterion — and how would we ever know a region's characteristics are not
   *still* understated?

---

## b) The completeness of the raw data

*Do we actually have all the data, and is it sound?*

What survives from the remedial process:

- **No orphans** — no object (term, verse, finding, pointer) is excluded from *all* analysis.
- **The audit as a completeness lens** — surfacing *all* objects bearing on a cluster that are not yet
  synthesised into its findings — used to prompt *holistic re-reading of the cluster*, never as a
  worklist to clear.

**Current understanding (to be reviewed):**
- Raw data = the **verses** (`wa_verse_records`), the **terms** (`mti_terms`, Strong's), the **actual
  usage** signal (`span_strong_match` — the term genuinely used in the verse), and the **verse
  meanings** (Pass A) — the latter being "the data that rules all analytics."
- Coverage is drawn from STEP; the term/verse inventory has known integrity history (the
  `mti_term_id` vs `term_id` completeness gap; deleted-but-live terms; duplication / dedup;
  the FLAG and T2 holding groups for not-yet-placed material; the 2026-06-03 DB loss + recovery).

**Tensions / open questions for critical review:**
1. **Is the term inventory complete?** Every Strong's that bears on the inner life, captured once,
   with its true active usage — including the families we found wrongly deleted (e.g. suffering,
   grief, toil). What is our confidence, and how is it evidenced rather than asserted?
2. **Are the verse meanings (Pass A) complete and sound?** They govern everything downstream. Were
   they produced under a consistent standard? Do gaps (missing `analysis_note`/keywords on some
   clusters) reflect missing data or just a later convention?
3. **No orphans — is it actually true?** Can we demonstrate that every term/verse is in view
   somewhere (a cluster, FLAG, or T2), none silently dropped?
4. **What is "raw" vs "derived"?** `delete_flagged`, cluster assignments, dimensions — which fields
   are the data and which are our (revisable) interpretation? This must be unambiguous.
5. Duplication (one Strong's once, one verse-per-term once) — is the foundation clean enough to
   trust, or does residual duplication still distort counts and reading?

---

## c) The fundamental rules for analysis of the data

*By what principles is the data read into understanding?*

**Current understanding (to be reviewed):**
- **Verse meaning is the data and rules all analytics.** Analysis assesses **meaning in context** —
  the term's sense within its verse, read against the other members of the cluster.
- **Content and context lead** — never the mechanical classification.
- **Multi-belonging is real.** A term or verse can carry meaning in more than one cluster; the same
  verse legitimately appears in several. Where it does, it is **a finding in each** cluster it
  genuinely speaks to — not forced into one, not mechanically copied.
- **Ambiguity and openness are allowed.** Not everything resolves; the analysis may legitimately
  leave questions open because the subject is open.
- **All observations, however disjointed, are recorded.** Nothing is discarded for being untidy.
- **The method must compensate for AI's tendencies.** Because AI defaults to framing, filtering,
  imposing order and choosing the *reasonable* over the *correct* (§0), the rules must build in active
  counter-measures — critical re-reading, resisting premature closure, surfacing the disconfirming,
  never letting structure substitute for meaning.
- **Findings must be robust, not merely plausible.** The prior studies' findings "appeared strong but
  deteriorated under questioning" (§0). A finding earns its place only if it **withstands deeper
  questioning** against the verse evidence.

**Tensions / open questions for critical review:**
1. What makes a **finding** a finding — when does an observation about meaning earn that status?
2. What does **"adequately synthesised"** mean for a cluster — when has its inner-life region been
   genuinely accounted for (as opposed to box-ticked)? This is the crux the audit should serve.
3. How is **multi-belonging** expressed without either flattening it or duplicating it falsely?
4. How do **characteristics** function — are they discovered from the verses, or imposed, and how is
   the difference kept honest?
5. What is the role of **set-aside** material — material judged not to bear on a cluster's inner-life
   meaning is still part of the term's semantic record; how is it kept in view, not deleted?
6. Where does **the human analyst** lead and the AI assist — given the AI's demonstrated pull toward
   false completion?
7. **The unit-of-analysis problem (the central unresolved question).** The corpus is too large to read
   at once, so it must be broken into pieces — yet every partition so far has become a distorting
   structure (the "fault lines" of §0). How do we divide the data for digestion **without the division
   itself becoming a false claim** about the subject?

---

## d) The end point

*What is the study producing, and what does "done" mean for a subject that may never be "complete"?*

**Current understanding (to be reviewed):**
- The intended outputs to date: **cluster essays / publications** (a written account per cluster),
  word studies, and cross-cluster synthesis — i.e. a readable, evidenced account of the inner life
  region by region, and ultimately as a whole.
- **The quality bar is set by the prior studies' two failures (§0):** *comprehensiveness* (no
  characteristic understated) and *robustness* (findings that withstand deeper questioning, not just a
  strong first impression). "Done" must be measured against both — not against gate-completion.

**Tensions / open questions for critical review:**
1. Is the deliverable a **reference** (a structured account of the vocabulary and its meanings), a
   **narrative** (an essayed understanding of the inner life), or both at different layers?
2. Can a cluster ever be "finished," or is the right end-state a **faithful, open account** that
   names what is known, what is ambiguous, and what remains open — rather than a closed, gate-clean
   record?
3. What is the **whole-study** end point — a synthesis across all clusters of the biblical picture of
   human inner life? At what altitude?
4. Who is the **audience**, and what must the output let them do — and does that change the standard
   for "adequately synthesised" in (c)?
5. If completion-pressure is the enemy, what replaces it as the **measure of progress** — coverage of
   the data in view? depth and faithfulness of the reading? something else?

---

## Working notes / decisions log

- _2026-06-04:_ Document created. Remedial process closed down (§0). Awaiting researcher's critical
  review and rewrite of the four areas.
- _2026-06-04 (CC):_ Researcher rewrote §0 with the study's origin + AI-shortcoming diagnosis. CC then
  (a) light copy-edit of §0 for grammar/clarity, preserving voice; (b) augmented the four areas from
  §0's signal: §a — comprehensiveness-of-characteristics as the distinctive aim + open Q5;
  §c — "compensate for AI's tendencies" + "findings must be robust" + the unit-of-analysis/fault-line
  open Q7 (flagged the central unresolved question); §d — quality bar = comprehensiveness + robustness.
  British spellings intentional. Researcher to continue review/rewrite.
