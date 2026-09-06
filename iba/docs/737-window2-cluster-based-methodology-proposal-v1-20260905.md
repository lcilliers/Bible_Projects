# Window 2 (HIB/IB) — Cluster-Based Analytic Methodology: Proposal

- **filename:** 737-window2-cluster-based-methodology-proposal-v1-20260905.md
- **date:** 2026-09-05
- **escalation:** #737
- **supersedes (in part):** `737-window2-preparatory-work-consolidation-v1-20260905.md` §1 (book/
  passage reading — researcher: **out of date, open for revision**) and §2 (the existing iba.db
  debate-pipeline infrastructure — researcher: **also out of date**). §§3–4 of that document
  (the M-cluster taxonomy, the verse-lexical base layer, the catalogue, governing config) still
  stand and are built on directly below.
- **status:** Proposal — unpacks the researcher's verbatim methodology overview (this session) into
  a concrete process, and answers/elaborates every item raised on the prior consolidation's §5.
  Nothing is built. Open items are named, not decided, at the end.
- **correction (same day, researcher instruction):** the first version of this document counted
  several tables without excluding soft-deleted rows — most consequentially the catalogue (§3.4),
  where 303 deleted `wa_obs_question_catalogue` rows were wrongly counted alongside the 131 live
  ones, fabricating a 286-row "universal" bucket that does not exist live at all. Every count below
  is now `deleted=0` (`delete_flagged=0` in `bible_research.db`) only; corrected figures are
  labelled "live" and the excluded deleted count is stated alongside each one.

---

## 1. The paradigm shift, stated plainly

**Old (retired):** reading proceeded **book by book** (Daniel, then the next book), and the unit
of debate-pipeline work was the **passage** (a run of consecutive verses within a book). This is
what iba.db's `passage`/`hib`/`phenomenon`/`operation`/`operation_party`/`passage_linkage`/
`passage_insufficiency`/`passage_emergent_question`/`passage_validation_note` schema was built for.
**Confirmed by the researcher: this reading order is no longer the plan, and the schema built
around it is out of date.**

**New:** reading proceeds **cluster by cluster**. A cluster (M-code only — see §3.6) is a family
of like phenomena. The chain that gathers what gets read is:

```
cluster (M-code)
  └─ cluster_strong (which strongs belong to this cluster)
       └─ strong (the word)
            └─ verse_lexical (every verse that strong occurs in, Window-1-processed)
                 └─ verse (the actual verse-set to read)
```

A verse is no longer selected because it sits inside a chosen book's chosen passage; it is
selected because **one of its words belongs to the cluster currently under analysis.**

---

## 2. The process, step by step

### Step 0 — Set the cluster to be analysed
A single M-code (e.g. M08 Pride & Arrogance) is chosen as the unit of work.

### Step 1 — Gather the verse-set
Every strong tagged to that cluster (`cluster_strong` where `cluster_code = <the M-code>`,
`deleted=0`) → every `verse_lexical` row carrying that strong (`deleted=0`) → the **distinct set
of `verse_id`s**. (Confirmed live and working: a direct join on `cluster_strong.strong =
verse_lexical.strong` returns real results — e.g. M08's own membership already resolves to a
concrete verse count when queried this way; no new join mechanism needs to be built for this step.)

### Step 2 — Data-readiness check on that verse-set
For every verse in the gathered set:
- **Layer 1 currency** — is its `verse_lexical` data current (not stale against the live
  `lexical.enrich`/`lexical.build` write path, per the #1520 identity-stable redesign)?
- **Layer 2 completeness** — does it have its judgement-bearing `verse_lexical_note` entries?
  **Live fact worth flagging now (live rows only, `deleted=0`):** `verse_lexical_note` holds only
  **173 rows corpus-wide** against **544,572 live** `verse_lexical` rows (430,888 further rows are
  soft-deleted — superseded content from the #1520 identity-stable rewrite, correctly excluded
  here). Layer 2 has only ever been piloted (per #1383/#1451), never run at scale. **For almost any cluster chosen, Step 2 will mean *running* Layer 2 for its verse-set for
  the first time, not verifying something already done.** This is a real, load-bearing prerequisite
  stage, not a formality, and should be sized accordingly per cluster before Window 2 work begins.

### Step 3 — Prepare the lexical dataset JSON
For every verse in the (now Layer-1-current, Layer-2-complete) set: assemble Phase 1 (Layer 1 —
mechanical: span/position/surface/morph/role/party_kind/testament/language/etc.) and Phase 2
(Layer 2 — judgement-bearing notes) into one JSON payload per verse (or a batched payload for the
cluster — an operational choice, not a design one).

### Step 3b — Fold in any existing Window 2 findings for verses already analysed
Because a verse can carry words from more than one cluster, a verse may already have been read
during a *previous* cluster's pass. Where that's true, its existing Window 2 findings are pulled
into the same dataset alongside the Phase 1/2 lexical JSON — so the debate step for the *current*
cluster sees what was already found for that verse, not just its raw lexical facts. **This is the
concrete mechanism that resolves escalation #1523's "washes out naturally"** (see §3.5 below): a
verse's full phenomenon set is never assessed in isolation per-cluster; each later pass inherits
the earlier one's findings for shared verses.

### Step 4 — Present the assembled dataset for analysis (the debate)
This is the actual HIB/IB analytical work, run against the dataset from Steps 3/3b:
1. **Identify all HIBs** present in the verse.
2. **Formulate all phenomena** — every phenomenon the verse's HIBs manifest, not only the one tied
   to the cluster's own nominal term.
3. **Answer the catalogue** — the earmarked, HIB-relevant subset of `wa_obs_question_catalogue`
   (see §3.4) is the analytic framework applied to every phenomenon, using the Phase 1/2 lexical
   data (and any prior findings from §3b) as evidence.

### Step 5 — Standing process discipline (non-negotiable, per the researcher's own wording)
- **Context beyond the cluster's own verse-set.** Resolving a verse may require reading backward
  or forward to adjacent verses for full context — even verses that carry no cluster-tagged strong
  themselves. The gathering step (Step 1) selects *which verses get a full debate pass*; it does
  **not** cap what can be *read* while resolving one of them.
- **Completeness, not selection.** The full verse, with **every** phenomenon it contains, is
  analysed together — never a subset or a cherry-picked phenomenon. (This is the direct structural
  fix for the old per-term/per-cluster tunnel vision that produced #1523's exceptions.)
- **Evidence discipline.** Every finding is grounded in the verse's and surrounding verses' actual
  evidence — consistent with the windows-register's C1 (observe, don't impose) and C6 (name
  inference as inference).
- **Open questions are findings, not gaps.** Anything unresolved is recorded explicitly as an
  unresolved finding — consistent with C5 ("silence is a finding, not a gap to fill").

---

## 3. Answers to the prior consolidation's §5, and elaboration where asked

### 3.1 — What D1–D2, D5–D7 meant, and how this new overview settles/supersedes them

These were labels from `WA-bite-structure-followup-v1.1-2026-08-13.md`, a document that was
**parked** in August and never finished. Restated plainly, with how §1–2 above now answers each:

- **D1 — "what is the base unit of work?"** The August draft's working guess was *one lemma's
  verse-set within one cluster*. **Answered differently by the new overview:** the base unit is
  **the cluster's whole verse-set**, read per-verse — not sliced further by lemma.
- **D2 — "run one lead window per verse, or all windows on every verse?"** ("Window" there meant
  the August register's W1/W5/W6 observational instruments — a different, now-largely-superseded
  sense of "window" than "Window 1/Window 2.") **Answered:** the catalogue itself is the framework
  applied per verse (Step 4.3) — there is no separate menu of instruments to choose among.
- **D5 — "uneven cluster sizes: bite by cluster, or normalise to a fixed count?"** **Answered as an
  operational, not a design, question:** every cluster gets its own full verse-set (Step 1),
  whatever its size; batching a large cluster's JSON payload (Step 3) is implementation detail.
- **D6 — "are T2/FLAG in scope? confirm T3 is in-scope as the operations layer."** **Now directly
  answered by you: only M-code cluster verses are included — no T-code cluster is a unit of
  analysis in its own right.** This also resolves the parked **D3** (T3's role) by the same stroke:
  T3 (Operations) is never read as its own cluster-pass; whatever operation-facts it carries live
  in `verse_lexical`'s own columns (`role`, `party_kind`, etc.) and surface only as evidence inside
  an M-cluster verse's debate, never as a cluster to gather verses *for*.
- **D7 — "does roll-up run continuously or after a cluster finishes?"** **Not addressed by the new
  overview, and not needed for it.** Roll-up/cross-cluster synthesis is the later stage described
  in `governance.programme_stages` (Analysis → eventual synthesis), downstream of per-cluster
  catalogue-answering. Left open, deliberately out of scope for this proposal.
- **D4 — "what do cross-verse threads match on?"** Not engaged by the new overview at all (it
  doesn't describe a thread/roll-up mechanism); still parked, still a later-stage question.

### 3.2 — §2a (the legacy `bible_research.db` cluster/characteristic/finding system): **not** historical-input-only — it is redone

Your instruction: *"§2a is not redundant and any cluster work around it is redone."* Recorded
plainly: the **18,364 live** `cluster_finding` rows (`delete_flagged=0`; a further 1,633 are
already soft-deleted and rightly excluded from this count — 15 of 49 old clusters ever had
findings loaded) are **not** carried forward as reusable analytical content and are **not**
treated merely as background reading either — every cluster's analysis is **redone** under the
Step 0–5 process above, including the 15 that already have legacy findings. Practical consequence,
flagged for a decision (not decided here): once a cluster is redone, its legacy `cluster_finding`
rows become superseded. The project's standing convention for superseded content elsewhere
(`inactive=1`/`deleted=1`, never a silent overwrite — see e.g. `cfg_lexical_code_class`'s
retirement, BUILD.md #228-#230) would apply the same way here; worth confirming when the first
cluster is actually redone, not before.

### 3.3 — The 7 untouched M-codes: elaborated with live numbers, not a bare list

Corrected against a fresh live query (the prior consolidation understated this): **all 7 codes
have real, live membership today** — they were not skipped because they're empty; they were
skipped by today's regex/keyword family-matching rebuild (#236) because none of its 78 derived
families happened to have one of these 7 as its dominant historical parent. "Untouched" means
*this specific rebuild script didn't touch them* — not that they're defunct or membership-free.

| code | short_name | live `cluster_strong` rows today |
|---|---|---|
| M10b | Wickedness | 43 |
| M10c | Defilement | 20 |
| M17 | Counsel | 30 |
| M27 | Evil | 48 |
| M29 | Desire | 40 |
| M31 | Faith | 18 |
| M32 | Covenant | 9 |

**Three of these (M10b/M10c/M27) carry a known, documented, unresolved judgement call** —
`iba/app/reports/m10bc-cluster-review-20260813.md` (2026-08-13): M10b/M10c were found as
near-empty stub clusters duplicating M10's own content; you chose **Option B** (repopulate them
properly rather than merge them back into M10) and a refined split was proposed (M10b ≈ 54
strongs "moral character" register; M27 renamed/tightened to "Idolatry, Ruin and Violence" ≈ 24
strongs; M10c gains 1 more candidate) — but that document's own §8 says *"nothing has been written
to iba.db yet."* Live counts today (43/20/48) are higher than the pre-relocation snapshot in that
review (1/4/not stated), so **some repopulation has evidently happened since** — but whether it is
*this* refined split, a partial version of it, or an unrelated ordinary backfill is not
established by this proposal and should be checked directly before M10b/M10c/M27 are chosen for a
Window 2 pass. **M17/M29/M31/M32 have no equivalent investigation on record at all** — no known
open question, but also no confirmation their membership is sound. Recommendation (not decided):
treat "is this cluster's membership actually settled?" as a per-cluster Step-0 pre-check, applied
the first time each of these 7 (and in principle every cluster) is picked up for a Window 2 pass,
rather than auditing all 85 clusters up front.

### 3.4 — The output: findings against an *earmarked, HIB-only* subset of the catalogue

Your ruling: *"the output is findings in response to the catalogue questions... the verse/term
questions covered in the lexical is not repeated, only the HIB relevant questions are included...
the exact questions to answer must be earmarked."* This is the single most concrete design
decision in your overview, and it needs an actual pass against the live catalogue to execute —
not just a scope-label filter.

**Correction from the prior version of this proposal:** the first pass wrongly included 303
soft-deleted rows (`deleted=1`) alongside the 131 live ones, which fabricated a large, misleading
"universal" bucket (286 rows) that does not actually exist live — it does not appear in the table
below at all. Re-run filtered to `deleted=0` only. `wa_obs_question_catalogue` (bible_research.db)
has **131 live rows total**, `status='active'` throughout, breaking down by `scope`:

| scope | live rows | disposition (proposed, not yet applied) |
|---|---|---|
| Word/term (lexical) | 27 | **Exclude** — Window 1's own job |
| Verse-context | 35 | **Exclude** (needs a quick confirm — see below) |
| The verse | 6 | **Exclude** (needs a quick confirm — see below) |
| The HIB | 15 | **Include** — HIB-scoped by definition |
| Characteristic (HIB behaviour) | 15 | **Include** |
| Characteristic relational | 17 | **Include** |
| Other non-human beings | 12 | **Include** (HIB-adjacent — party/referent questions) |
| Science | 4 | **Needs reading** — likely out of scope entirely, unconfirmed |

Proposed **Include** set (HIB-relevant): **59 questions** (The HIB 15 + Characteristic (HIB
behaviour) 15 + Characteristic relational 17 + Other non-human beings 12). Proposed **Exclude**
set (Window 1's own territory): **68 questions** (Word/term (lexical) 27 + Verse-context 35 + The
verse 6). **4** (Science) unresolved pending a read. 59 + 68 + 4 = 131, the full live catalogue —
no row unaccounted for, and no scope-label ambiguity left once the deleted rows are removed: every
live scope label maps cleanly to one side or the other except Science.

**This earmarking pass — confirming the Verse-context/The-verse exclusion and reading the 4
Science rows — is proposed as a discrete, boundable next step** (now genuinely small: at most 41
rows need an eyes-on read, not 434). It is a precondition for Step 4.3 above (the catalogue can't
be "the framework" for HIB analysis until it's known which of
its rows that means), so it belongs early in the build sequence, likely before the first real
cluster pass rather than after.

### 3.5 — Daniel's existing debate layer: confirmed redundant

Your ruling: *"the Dan debate layer is redundant."* Recorded — the existing **121 live**
`phenomenon`/**121 live** `operation` rows (`deleted=0`; a further 56 of each are already
soft-deleted and correctly excluded) and **21 live** `hib` rows for Daniel (built book-by-book,
under the retired reading order) are not carried forward or reused. Consistent with §2a's redo principle (3.2 above) and with the
whole-`§2 infrastructure is out of date` instruction — these rows are candidates for the same
superseded-content treatment as the legacy `cluster_finding` corpus, once a disposition rule is
set (3.2). Practically: Daniel's verses will simply re-enter the verse-set of whichever M-clusters
their words belong to, and get read again under the Step 0–5 process like any other verse — no
special-casing needed.

---

## 4. What §2's "infrastructure is out of date" means concretely — flagged, not resolved here

The existing iba.db schema (`passage`, `hib`, `phenomenon`, `operation`, `operation_party`,
`verse_hib`, `hib_referent_option`, `passage_linkage`, `passage_insufficiency`,
`passage_emergent_question`, `passage_validation_note`) is built around **passage** (a
book-relative span of consecutive verses) as the organising key. The new process organises around
**cluster** instead, and a verse's membership in a cluster's verse-set has nothing to do with
which passage or book it sits in. Two live tensions this raises, named for the actual planning
pass (not decided here):

1. **Where do new Window 2 findings get written?** `governance.scope_research_db` already states
   findings belong in `bible_research.db`, not `iba.db` — which is exactly what escalation #737
   was originally raised to fix by *migration*. Given §2's infrastructure is now itself out of
   date, the more direct route may be to **design the new cluster-scoped schema fresh, directly in
   `bible_research.db`**, rather than migrate the old passage-scoped tables at all — which would
   resolve #737 by superseding it rather than by moving its subject. Not decided here; flagged as
   the most consequential open architectural question this proposal surfaces.
2. **What (if anything) of `hib`/`phenomenon`/`operation`'s field-level shape survives?** The
   *concepts* (HIB register, phenomenon, operation/operation_party) are still named directly in
   your own overview ("identify all the HIBs... formulate all the phenomena..."), so the fields
   those tables already carry (e.g. `operation_party.role`/`kind`/`enablement_only`,
   `hib_referent_option.reading_text`/`textual_grounds`/`adopted`) are a reasonable starting
   vocabulary for a redesigned, verse/cluster-scoped version — not a reason to keep the
   passage-keyed tables as-is.

---

## 5. Open items carried forward (not decided by this proposal)

1. Confirm what actually happened to M10b/M10c/M27's membership since the 2026-08-13 review (3.3).
2. Run the catalogue earmarking pass (3.4) — confirm the Verse-context/The-verse exclusion and
   read the 4 Science rows (at most 41 of the 131 live `wa_obs_question_catalogue` rows need an
   eyes-on read; the rest already sort cleanly by live `scope`).
3. Decide the disposition of superseded content once the first cluster is redone: legacy
   `cluster_finding` rows (3.2) and Daniel's `phenomenon`/`operation` rows (3.5) — mark inactive,
   soft-delete, or archive-and-remove.
4. Decide where the new schema lives — redesign fresh in `bible_research.db` (§4.1), or migrate/
   adapt the existing iba.db tables. This is the actual resolution shape for escalation #737 itself.
5. D4 (cross-verse thread join key) and D7 (roll-up timing) remain parked — genuinely later-stage,
   not blocking the per-cluster catalogue-answering work this proposal describes.
6. Pick the first cluster to run Step 0–5 against end-to-end as a worked exemplar, once items 1–4
   above (or at least 2 and 4) are settled enough to try it for real.

---

*Proposal only. No schema change, migration, or DB write made or implied by this document.*
