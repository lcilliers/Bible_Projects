# Window 2 (HIB/IB) — Preparatory Work Consolidation

- **filename:** 737-window2-preparatory-work-consolidation-v1-20260905.md
- **date:** 2026-09-05
- **escalation:** #737 (IBA Debate-Pipeline to research_db Migration — Gated; researcher v5:
  "this now becomes the main focus of attention... review the previous methods... deep dive to
  cleanout and prepare old analysis findings... let us first thoroughly plan it")
- **status:** Descriptive consolidation only. Nothing here is a decision or a plan — it is the
  ground under one, assembled from live DB inspection + every document found, not from memory.
  Section 6 names what is genuinely undecided rather than inventing an answer.

---

## 0. Terminology (researcher's own equivalences, this session)

**HIB / IB / Window 2 / "the debate work"** are the same thing, named at different times: the
analysis of what a verse's already-established facts (its words, grammar, movements) mean **for
the human inner being** — as opposed to **Window 1**, which stays inside the verse's own
language (span/morph/lexicon, no HIB question asked). The clearest statement of the boundary is
`iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md` §0 (quoted in full in the
comment on escalation #737 v7/v8's own investigation).

---

## 1. What Window 2 actually is, live in the app today

**Work package:** `operations-ingest` (`cfg_step`, iba.db), 4 steps, all `inactive=0`:

| ordinal | step | writes | gate |
|---|---|---|---|
| 0 | `hib.set` | `hib`/`hib_referent_option`/`verse_hib` | none — book-level register |
| 1 | `phenomenon.set` | `phenomenon` | sets `passage.phenomena_complete_at` once complete against `verse_hib` |
| 2 | `operation.set` | `operation`/`operation_party` | REFUSES until `phenomena_complete_at` is set |
| 3 | `closing.set` | `passage_linkage`/`passage_insufficiency`/`passage_emergent_question`/`passage_validation_note`/`passage.open_decisions_note` | REFUSES until every live phenomenon in the passage has a live operation |

This is a straight code implementation of **Steps 1–8 of
`Workflow/Instructions/WA-interpretation-questions-v1.4-2026-08-02.md`** (Step 1 = HIB register,
Step 3 = phenomena, Steps 4–5 = operations, Steps 7–8 = digest/closing) — the one method document
this pipeline is built against.

**Current live data (iba.db, `deleted=0`):**

| table | live rows | notes |
|---|---|---|
| `passage` | 42 (of 18,558 total — 18,516 soft-deleted) | 6 books only: Dan 13, Hos 14, Joel 3, Jonah 4, Mic 7, Obad 1 |
| `hib` | 21 (of 63) | all book=Dan |
| `phenomenon` | 177 | all in Dan |
| `operation` | 177 | all in Dan |
| `operation_party` | 250 | — |
| `verse_hib` | 485 | — |
| `passage_emergent_question` | 4 | — |
| `passage_insufficiency` | 1 | — |
| `passage_linkage` | 3 | — |
| `passage_validation_note` | 4 | — |

**Cross-check against memory (`project_iba_book_by_book_debate_phase`: "books 1-6 done —
Dan/Jonah/Joel/Obad/Micah/Hosea"):** the **passage split** exists for all 6 books, matching that
memory. But the **phenomenon/operation debate layer itself is live only for Daniel** — the other 5
books have passages but zero `phenomenon`/`operation` rows. Either the memory's "done" refers only
to the passage-boundary stage (not the full HIB→phenomenon→operation debate), or the other 5
books' debate output was built and then rolled back/soft-deleted at some point and never
re-applied here. Not resolved by this consolidation — worth a direct question to you (see §7).

---

## 2. Three generations of "cluster/debate" work — what to deal with from the past

### 2a. OLD — `bible_research.db` characteristic/sub-group/finding system (pre-IBA, Session-C era)

Full findings: escalation #1006's own review,
`_analytics/clusters/M08-Pride/wa-1006-cluster-subgroup-engine-review-v1-20260905.md` (resolved
today). Headline facts, not restated at length:

- Schema: `cluster` (49: M01–M47 + FLAG + T2) → `characteristic` (277) → `characteristic_subgroup`
  (146) ↔ `cluster_subgroup` (175) → `cluster_finding` (**19,997** rows, the actual analytical
  content) + `cluster_observation` (276, cross-cutting notes).
- **There is no engine.** ~15 bespoke, per-cluster, now-fully-archived `_apply_..._findings_*.py`
  scripts parsed hand-authored markdown (`Sessions/Session_Clusters/{CLUSTER}/...`) into
  `cluster_finding`. None is runnable today. Only **15 of 49 clusters** ever got findings loaded;
  35/49 have `characteristic` rows at all.
- The one genuinely reusable piece, `iba/app/lib/clusterassign.py`'s `match_precedent()` (exact
  gloss-string matching, single-match-only), was tested live against M08's real sub-groups today
  and **only works 13% of the time** — because M08's sub-groups are drawn on an *interpretive*
  dimension (where the pride is seated: heart / eyes-and-bearing / national / individual), which
  is a property of the **verse a word occurs in**, not of the Strong's code — exactly the kind of
  fact only a per-verse HIB read (Window 2) can supply, not a code-level tool.
- **The open fork this leaves, named by #1006 itself, unresolved:** (a) revive the manual
  per-cluster load pattern for the remaining 34 clusters against this legacy schema, or (b) treat
  this schema as **historical input only** and design Window 2 fresh. Not decided here.

### 2b. iba.db pilot debate data (Developer Mode builds)

Section 1's table above. A working, gated, code-enforced pipeline exists and has been exercised
on Daniel. It has never been run to completion against the new M-cluster taxonomy (§3a below) as
input — the M-cluster rebuild landed *today*, after this pilot data was written.

### 2c. The windows-debate design layer (`iba/docs/windows debate/`, 2026-08-10 → 08-13, 15 files)

This is "the previous methods associated with this" you referred to. Two documents matter most;
the rest are their source material (already digested into them):

- **`WA-inner-being-windows-register-v2_3-2026-08-12.md`** — the **"what"**: a register of 10
  "windows" (angles of observation) onto the inner being — W1 per-verse movement decomposition,
  W2 four-level cascade (verse→similar→cluster→cross-cluster), W3 span-synergy, W4 passage-read,
  W5 interpretation-questions, W6 faculty-as-observation, W8 Psalms/bible_research.db (**known
  cloudy, suspended**), W9 measure-layer, W10 cluster-workspaces — plus 7 calibration principles
  (C1–C7, e.g. "measurement informs never decides," "silence is a finding") and a vantage map. Only
  **3 of 10 windows (W3/W4/W5) are glass-verified against their actual source text**; the rest
  carry `from memory — verify`. All window-level forks are closed; the register is stable at v2.3.
- **`WA-past-works-pointers-v1.1-2026-08-13.md`** — a **descriptive scan of 17 further legacy
  methodology artifacts** (characteristic-role-lexical cycle, passage-completeness, db-integrity,
  reread-cadence, projection-spec, analytic-input-spec, the 06-25 synthesis-B reset, the T0–T7
  tier catalogue, VE-field-reliability, two-narrative rollout, the per-book method, D1–D13
  dimensions), each pointer tagged WINDOW/METHOD/LESSON/RELOOK. **Nothing is decided — it says so
  explicitly, twice.** It is held "for the relook," which per the register's own §0.2/§9 needs a
  fresh session run through the add-a-window protocol with you.
- **`WA-bite-structure-followup-v1.1-2026-08-13.md`** — the **"how"** (unit-of-work mechanics),
  explicitly **PARKED** ("the programme has turned to defining the windows before the analysis
  mechanics; do not action D1–D7 yet"). Working model: a **bite** = one lemma's verse-set within
  one M-cluster; **T3** (operation-verbs) is the operation-edge inside a bite, not a separate
  subject (unless D3 says otherwise); out-edges that point outside the verse become **threads**
  that roll up L1(verse)→L2(similar verses)→L3(cluster)→L4(cross-cluster) into the "web." **Seven
  open decisions (D1–D7)** gate commencement — what a bite is, micro-window scope, T3's role, the
  cross-thread join key, uneven cluster sizes, whether T2/FLAG are in scope, and roll-up timing.
  **D3 and D4 (the two load-bearing ones) are already substantially pre-answered** by the
  past-works scan: recognise-then-attach (not fragment-stitch), join key = the D1 relation-signal
  set (shared shape/binding-web/object-kind/pole-opposition/seat/cognate/adjacency), never the bare
  lemma. D1/D2/D5/D6/D7 remain genuinely open.

---

## 3. What's new to work with (post-dates all of §2)

### 3a. The new M-cluster taxonomy — "the primary entry point," per your framing

`iba.db` `cluster` (85 rows live) + `cluster_strong` (8,929 rows). Rebuilt **today**
(BUILD.md #236, escalation #1006 follow-up): the old 47 M-codes (M01–M47) were re-derived from an
evidence-checked keyword→family grouping run against every strong's `stepGloss` —
**78 families covering 87% of 2,971 corpus strongs**. Where a cluster's membership genuinely
split into unrelated families (M05 Love → 4, M10 Sin → 3, M15 Wisdom → 4, M41 → 4), the largest
family kept the old number and siblings got new codes M48–M84 (37 new codes; 41 existing codes
renamed). Plus **T2–T9**: structural/grammatical clusters (Supplementary, Operations, Adversarial,
Negator, Connective, Party-Divine/Human/Angelic) — not inner-being content, but load-bearing for
Window 2's own mechanics (T3=Operations is the working model's operation-edge in §2c above; the
Party-* clusters are exactly the HIB-candidacy signal Window 2 needs).

**Live open exception, deliberately left unresolved and explicitly tied to Window 2's own future
work — escalation #1523** (in-progress, your v2 comment verbatim): 772 strongs carry a non-T2
cluster with no `word_registry` link; 829 backfill-origin strongs have an already-clustered
sibling. Your ruling: *"these strongs were discovered on verses shared with other strongs — the
exception is expected to wash out naturally once those verses get analysed at the verse level...
handling multi-characteristic verses is one of the open questions the windows-debate work is
expected to surface."* **This is a direct, load-bearing dependency**: #1523 cannot close cleanly
until Window 2 defines how a verse carrying more than one relevant characteristic/strong is
handled — which is exactly bite-structure fork **D5/D6** territory (§2c), unresolved.

### 3b. Verse-lexical Window 1 — the corpus-wide base layer

`verse_lexical` (975,460 rows) + `verse_lexical_note` (173 rows). Built and repeatedly hardened
this week (#1383 full build, #1451 made genuinely verse-scoped, #1520 identity-stable CRUD
rewrite, all closed). This supplies, per verse, per code: span/position/surface, morph, role,
resolved_sense, party_kind, testament/language, is_negator, and (in the 173-row Layer-2 note
table) judgement-bearing findings — the mechanical substrate §2c's register calls "8 derivable, 6
partial" of the 16 movement dimensions; **role is explicitly NOT derivable from morphology alone**
— that is exactly the read Window 2 supplies.

### 3c. The catalogue — "the key questions to explore"

`wa_obs_question_catalogue` (bible_research.db), 434 rows total, by `scope`:

| scope | rows |
|---|---|
| universal | 286 |
| Verse-context | 36 |
| Word/term (lexical) | 27 |
| Characteristic relational | 17 |
| The HIB | 15 |
| Other non-human beings | 15 |
| Characteristic (HIB behaviour) | 15 |
| leviticus | 12 |
| The verse | 7 |
| Science | 4 |

Per `iba/docs/1446-verse-word-analytic-methods-extract-v2-20260904.md` §"catalogue check": **a
minority of the 181-question tier-catalogue set (a related but not identical enumeration — T0–T7,
126 questions, `Workflow/Tiers/`) are single-verse and belong to Window 1**; **a real, sizeable
set (~20) are pure lexical-aggregation, answerable by rolling up Window 1's own per-code data
across a term's full occurrence set** — no Window 2 read needed; **the rest are genuinely
characteristic/HIB-level** and are Window 2's actual job. Which exact rows fall in which bucket
has not been re-derived against the *live* `wa_obs_question_catalogue` table above in this
consolidation — that cross-walk (catalogue row ↔ Window 1 lexical-rollup vs Window 2 read) is
itself a concrete, boundable next step if you want it before the "thorough plan."

---

## 4. Governance already in force over this area

- `governance.scope_iba_db` / `governance.scope_research_db`: base data + process control lives in
  iba.db; findings/prose live in research_db — the literal reason #737 exists (the debate tables
  are findings, not base data, once Window 2 actually starts producing them at volume).
- `governance.programme_stages`: three stages — Base_data (STEP→lexical, i.e. §3b) → Analysis
  (deriving IB understanding, i.e. Window 2) → Publishing. Window 2 is squarely the Analysis stage.
- Escalation #770 (Content-Index Search redesign) and #1385 (content_index 14M-row explosion) are
  both **on-hold pending "analysis phase start"** — several other on-hold items are keyed to this
  exact moment, not just #737. Worth knowing they may come back into scope together.

---

## 5. What is NOT yet settled anywhere in the written record (named, not invented)

1. **D1–D2, D5–D7** of the bite-structure model (§2c) — the actual unit of Window 2 work, whether
   T2/FLAG are in scope, uneven cluster sizes, roll-up timing. D3/D4 are pre-answered; these are not.
2. **The §2a fork** — revive the legacy 34-cluster manual load, or treat it as historical input
   only and build fresh. Not decided by #1006, not decided here.
3. **7 old M-codes untouched by today's rebuild** (M10b, M10c, M17, M27, M29, M31, M32) — none of
   the 78 evidence-checked families claims them as a dominant parent; deliberately left alone
   pending a decision that BUILD.md #236 explicitly declines to make in passing.
4. **What "the output" of Window 2 actually is.** The windows register is explicit (§1, §11) that
   it is *scaffold toward* a later composite description of the inner being, not that description
   itself, and does not specify the description's own form. No document found in this pass
   specifies a target deliverable shape (a per-characteristic write-up? a database of movements? a
   narrative per book?) for Window 2's output. This is the one item in your instruction
   ("what output is expected to be") this consolidation cannot answer from the record — it needs
   you.
5. **The Dan-only debate-layer discrepancy against the "6 books done" memory** (§1) — not resolved,
   named for you to confirm or correct.

---

## 6. Suggested shape for the "thorough plan" session (menu, not a proposal)

Not decided, offered only as candidate agenda items once you're ready to plan:

- Un-park the bite-structure document and settle D1/D2/D5–D7 (D3/D4 already answered).
- Decide the §2a fork (revive vs historical-input-only) for the legacy 19,997-finding corpus.
- Decide whether/how #1523's 1,601 exceptions get re-examined once a verse-level multi-characteristic
  rule exists (they may simply resolve, per your own v2 comment).
- Run the catalogue cross-walk (§3c) so the exact Window-2-only question set is known before
  design, rather than assumed.
- Confirm or correct the Dan-only debate-data discrepancy (§1) before deciding whether Daniel's
  existing 177 phenomena/operations are reusable as a worked exemplar (the bite-structure doc's
  own "proposed first concrete step," §6 there, wanted exactly one worked exemplar before D3/D4
  were tested — Daniel may already partially be that, or may need re-doing against the new
  M-cluster taxonomy).

---

*Consolidation only. No design decision, migration, or build made or implied by this document.*
