# 2172 — September and October: what each delivered, and why they never met

Escalation: #2172. Status: Claude's analysis, for the researcher's own view. Nothing is proposed or
built.

Researcher, 2026-10-22 (verbatim): "you need to look at all the work you did in oct in the _analytics
folder, you did some good work. you also need to take into acount the open item register and the
claims register, and then also the tables that where used in the september timeframe.  then think
about why september failed to delivery, what was added in Oct and what went wrong in Oct ( I have my
views but first want your analysis)  the October additional tables need to work in unison with the
September process".

**Sources.** All counts are from iba.db, queried read-only on 2026-10-22. The escalations are cited
by id. For the October method I read
`_analytics/essay/spirit_soul_body/wa-essay-narrative-weave-method-and-ch10-structure-v2-20261004.md`,
`_analytics/Clusters/M02 - anger-wrath/anger-key-characteristic-process-proposal-v1-20261005.md`,
`_analytics/Clusters/M02 - anger-wrath/anger-strand-handoff-v1-20261005.md`, and the file inventory.
**I did not read all 233 October md files**: the inventory is from file names and dates. Points
marked *(inferential)* are my reading of the record, not confirmed.

## 1. September: the pipeline (12 to 23 September)

**What was built.** A four-stage reading pipeline, with the LLM called through the API:
verse-reading, char-subgroup, char-reading, char-answers (#1690 to #1697, #1711). Its records:

| Table | Role | Rows |
|---|---|---|
| `ib_observation` | one typed finding (stage, tag, strong, question, obs_text, meaning_source, status) | 11,480 |
| `ib_node` | the grounding: each finding's verse, strong, surface and morph; a CHECK makes an ungrounded finding impossible | 12,909 |
| `cluster_subgroup`, `cluster_subgroup_strong` | the reading unit inside a cluster | 13, 21 |
| `wa_obs_question_catalogue` | the question battery each stage answers | 116 |
| `run`, `run_batch` | what ran, resumable, no double spend | 4,491, 236 |
| `ib_observation_enhancer_log` | every rule-driven change to an observation | 7,183 |

**What it delivered:** observations for three clusters only: M67 (3,183), M83 (1,553) and M49 (954).
Another 5,712 word-level rows have no cluster. Status today: 6,527 draft and 4,953 withdrawn.
Nothing from it reached the narrative. `narrative_claim_source` has no kind that points to an
observation, and only 141 verses are both grounded in `ib_node` and cited in the narrative.

**Why it failed (the record):**
1. **Quality at scale.**
   - 5,207 word-level observations were generic, not grounded in the span (#1856), and 4,477
     were withdrawn.
   - 14 of 34 Stage 1 questions did not serve the stage's purpose (#1849).
   - Researcher, #1851 (verbatim): "Stage 1 of the analysis is not fit for purpose. Every attempt
     to rectify it failed spectacularly."
   - Researcher, #1851 (verbatim): "results are directionally right but noise threatens
     usefulness".
2. **Cost against benefit.** 23 September, #1851: the study was abandoned on cost/benefit grounds.
   29 September, #1899 (verbatim): "reading every cluster in full is likely to be far to costly
   with limited benefit."
3. **The unit was wrong.** 30 September, #1899 (verbatim): "The focus shifts to 'fan out' analysis
   rather than analysis by cluster." The inner being is a web, and the cluster batch cut across it
   (#1900).
4. **The effort went into the machinery.** In 11 days there were the FK fixes (#1734 to #1738), the
   18-error batch (#1727), the run_batch fixes (#1758 to #1760), the dedup that never fired
   (#1824), the status lifecycle (#1782 to #1793), the M0.7 gaps (#1831) and the dead gates
   (#1823). *(inferential)* Most of the session time went into making the pipeline run, not into
   reading.
5. **There was no route to the narrative.** The pipeline ended at char-answers. No stage took an
   observation into a claim or a chapter.

**What September got right:** the records. Every finding is a row, grounded in a verse and a
strong, with a status. A change is logged and a run is resumable. The infrastructure can show what
was found and where it rests.

## 2. October: fan-out strand reading, by me, in chat (30 September to 19 October)

**What was added: the method.** Strand reading:
- pull every hit of a word family (`strand-unit-pull`);
- read by surface, and give every hit a face;
- one observation row per key statement, with setting, meaning, implication, chain, verses, basis
  S/R, parties and disposition;
- a quote check against `verse`;
- a reconciliation of the units against the full vocabulary (no hit unread);
- a cross-ledger overview, then the sub-chapter;
- the researcher's approval per unit.

The anger strand is an example: 65 Strong's and 919 hits, every hit faced, 0 quote failures
(`anger-strand-handoff-v1-20261005.md`). The weave method put meaning first and structure last
(#1918, #1930, #1943).

**What was added: the tables.**

| Table | Role | Rows |
|---|---|---|
| `escalation_thread_item` (+ responses) | the open-item register: each strand's held items, matched by cluster, strong, verse (#2000) | 496 |
| `narrative_claim`, `_source`, `_telling`, `_change` | the claims register with full history (#2110, from 13 Oct) | 330 claims |
| `narrative_chapter`, `_section`, `_passage`, `_citation` | the narrative itself, with every verse it cites (#2155) | 38 chapters, 7,562 citations |
| `narrative_update`, `_update_ref` | each weave, its sources and the items it names | 160, 219 |

**What October delivered:** a narrative. 38 chapters, rewritten many times (Ch 10.10 is at v35,
Ch 11 at v39), citing 4,614 distinct verses. The claims register holds 330 claims: 306 current, 9 held
and 15 withdrawn. 260 are marked in the narrative. Most of the reading is of good quality, by the researcher's own
approvals of the unit ledgers.

**The output.** 233 md and 152 csv files live in `_analytics` for October, and 753 more are
archived.

## 3. What went wrong in October

1. **The readings never entered the September tables.**
   - Every October observation (FE-, AG-, AN-, LD- and the other series) is a row in an md table.
   - None is in `ib_observation`/`ib_node`. The last observation row is from 2026-09-23.
   - The October ledger row and the September observation are the same thing: a finding about a
     verse and a word, with a meaning and a basis. It is held in two places, and only the md one
     was used.
2. **The link from reading to claim went by hand.**
   - A claim's source is a verse, or a "study file" given as text (40 rows, e.g. "M47 reading
     pointers ...").
   - No claim points to the observation it came from.
   - A weave names its reading only as a file path in `narrative_update.source_files` (73 of 160
     updates name one).
   - So nothing can show that a reading's findings reached a claim. That is the #2172 failure.
3. **Coverage was never recorded.** `verse_meta.status` (exclude / citated / analysed) is NULL for
   all 29,760 verses. A reconciliation ("no hit unread") ran in a per-strand script and lived in an
   md file.
4. **The open-item register became a parking place.**
   - All 306 open items sit on threads that are on-hold (23 threads); 69 threads were superseded.
   - The open items: 163 clusters, 74 verses, 47 strongs.
   - Items were added much faster than they were settled (115 closed). *(inferential)* The register
     recorded what was found but did not drive what was done next.
5. **Escalations closed on bookkeeping, not on work.** #2162 was completed while its reading had
   not started (#2172 v1). Corrections found in readings were never applied (Heb 10:22,
   1Co 6:19b-20, Neh 6:13, Psa 69:9). The controls compared records with records (#2172 v2).
6. **The method lived in files and scripts outside the app.** The pull, face-assign, quote-check,
   reconciliation and chapter-match scripts were per strand, in `_analytics`; many were retired
   under #2200. Each strand had its own ID series and ledger shape. *(inferential)* Every new chat
   had to rebuild the method from handoff files, and this drift is the same "past precedent" pattern
   the governance rule names.
7. **The narrative outran the reading.**
   - 61 claims were added on 19 October alone.
   - 46 current claims have no live telling, and 13 have no verse source.
   - The flesh-and-body chapter (Ch 7) stayed at v8, with 426 of 606 verses told nowhere.
8. **The cost returned in another form.** September spent API tokens on noise. October spent session
   tokens on reading in chat (#1899's measure: 82.6M cache-read tokens in one session).

## 4. The common cause

September had **records without good reading**: grounded rows, a status and history, but noise from
an LLM applied verse by verse at scale.

October had **good reading without records**: careful, approved readings and a living narrative, but
held in files, linked by hand, with nothing in the database to show what was read, what was found,
and whether it reached a claim.

Neither connected reading to narrative through the database:
- September had no route out of `ib_observation`.
- October never wrote into it.

## 5. What "in unison" would have to mean (findings only, not a design)

The existing tables already pair up:

| September (finding side) | October (narrative side) | The missing join |
|---|---|---|
| `ib_observation` (+ `ib_node`): the finding and its verse | the October ledger row (md) | the ledger row *is* an observation, but was never written as one |
| `ib_observation` | `narrative_claim_source` | a claim does not name the observation it rests on |
| `verse_meta.status` | `narrative_citation` | a verse read is not marked analysed; a verse woven is not marked citated |
| `run`, `run_batch` | `narrative_update` | a weave is not tied to the reading run it came from |
| `escalation_thread_item` | `ib_observation` / claims | a held item is matched by cluster, strong, verse, but not to the findings that settle it |

Two questions decide whether this is the right reading of the record:
- Is the October ledger row the same unit as `ib_observation`?
- Was `verse_meta.status` meant to carry coverage?

I have not proposed how to join them, and I will not until you have given your own view.
