# wa-obslog — cluster allocation (unallocated strongs)

- **filename:** wa-obslog-global-cluster-alloc-v1-20260811.md
- **reference:** global (cross-programme cluster allocation)
- **session-name-abbreviated:** cluster-alloc
- **version:** v1
- **date:** 2026-08-11
- **prior output reference:** new working trail; consumes uploads cluster.csv, cluster_strong.csv, strong_without_cluster.csv
- **session type:** database-review / programme-control → obslog destination `outputs/session-logs/` (GR-OBS-001)

---

## Startup gate (GR-LOAD-001 v3_2)

1. Rules loaded — `wa-global-rules-all-v2-20260427.md` — 34 rules across 12 categories. Also read: `wa-global-rules-startup-v2-20260427.md`, the two passage-read instruments, and the span-synergy method (present in project files; not all directly governing this task).
2. Observations log initialised — this file.
3. Cadence discipline M1+M4 active.

---

## Researcher instruction (verbatim)

> this task is about cluster allocation.  Attached you will find a csv with all the clusters.  you will also find a csv for strongs that previously have been allocated to clusters.  and then you will find a list of strongs that have not yet been allocated to any cluster.  Your task is to allocate the strongs not yet allocated - to a cluster and prepare a json report to assign these strongs.  the list completed is only included to aid you on what approach was used previously.  I am not expecting re-assignment of this list.  Note that the T2 cluster is designed to allocate any strong that has not inner being relation. These strongs are all regarded as supplementing the strongs that have inner being significance. They must not be assigned to an inner being cluster.  There are also a Flag cluster.  This is only used in exceptional cases where the strong is inner being related, but it does not fit into any other cluster. startup with the global rule startup before any work is done.

---

## Observations — data as received (not interpretation)

- **cluster.csv** — 49 cluster rows, all `deleted=0`. Codes: `FLAG`, `M01`–`M47` (with gaps M32/M40 absent; M10 split into M10/M10b/M10c), and `T2`. Columns: cluster_code, short_name, description, gloss, deleted. The `gloss` field lists the concept-bearing terms already associated with each cluster in the form `gloss (transliteration)` — this is the semantic content of each cluster.
- **cluster_strong.csv** — 2801 already-allocated strongs (reference only; **no reassignment expected**). Columns: strong, stepGloss, language, cluster_code, short_name, source (`old-system-migration`), created_at. Distribution: **T2 = 895 (~32%)**, FLAG = 41 (~1.5%), M-clusters range 13–124.
- **strong_without_cluster.csv** — **1612 strongs to allocate.** 809 Hebrew, 803 Greek. Columns: strongNumber, stepGloss, stepTransliteration, language, count. `count` range 0–10000 (median 5; 14 have count=0). **No blank glosses.**

## Insufficiency flagged (GR-PROG-002 / persona: name insufficiency)

- Evidence per unallocated strong is a **short stepGloss (1–4 words) + transliteration + count only**. There is **no verse-level data and no full lexical definition** in the uploads. The previous allocation (`old-system-migration`) almost certainly drew on richer STEP/verse data that I do not have. Gloss-only allocation is defensible for clear cases and **weak for abstract/ambiguous glosses**. This is a material insufficiency and is surfaced to the researcher before bulk production.

## Forks surfaced to researcher (pre-production) — see chat

- F1 evidence basis (gloss-only; proceed + confidence flags?)
- F2 IB-significance boundary / T2 default rule
- F3 output schema (confidence + rationale + review flags?)
- F4 FLAG threshold
- F5 filename/prefix + date-format confirmation (persona requires prefix confirmation before first output; persona vs global-rules format is a standing open decision)

## Decisions

- (pending researcher response to forks)

---

## Researcher instruction — fork resolutions (verbatim)

> forks: 1 - yes; 2 - yes T2 for all that do not denote inner being 3 - looks ok  4- yes, this is expected to not be too many  5 - yes.   I suggest you first do all that is high, no decision from me needed, then show me the medium list - I may spot some trends that you can apply to get them high.  Note that it is OK to assign a strong to more than one cluster (although this should not be the rule) - this will mean the strong will be analysed in both clusters, which may be intended.  then when all the mediums have been resolved. present me with the low list to again look for trends to help you.

## Decisions recorded

- **F1 yes** — proceed on gloss-only evidence, carry confidence high/med/low.
- **F2 yes** — **T2 for every strong that does not denote inner being.**
- **F3 yes** — schema: strongNumber, stepGloss, stepTransliteration, language, cluster_code, short_name, confidence, rationale, review_flag (+ multi-cluster support).
- **F4 yes** — FLAG kept rare (IB but no cluster fit).
- **F5 yes** — follow global-rules filename style (lowercase, `v1_0`, `YYYYMMDD`), prefix **WA/wa**.
- **Multi-cluster allowed** (not the norm): a strong may be assigned to >1 cluster → analysed in both; may be intended.
- **Workflow:** (1) produce HIGH now, no researcher decision needed; (2) present MEDIUM list for trend-spotting → promote where trends apply; (3) then present LOW list for trend-spotting.

## Method decided (decision-support, judgements remain Claude AI's — GR-PROG-005)

- The 2,801 already-allocated strongs in cluster_strong.csv are treated as a **labelled precedent set** (honours "included to aid you on the approach used previously"). Per-cluster English-gloss-token **profiles** are built from those labels + the cluster.csv gloss field.
- Each unallocated strong is scored by: (a) **exact/near gloss-string precedent match** to the labelled set (top signal); (b) **profile token overlap** with margin between best and runner-up.
- Confidence: HIGH = exact precedent match to a single cluster, or unambiguous clean single-cluster map, or clear non-IB → T2. MEDIUM = plausible single map, weaker margin / competition. LOW = abstract / competing / no signal.
- Computation supports the judgement; HIGH set is reviewed before release.

---

## Outputs produced (v1_0, 2026-08-11)

- **HIGH deliverable (ready to apply):** `wa-global-cluster-alloc-high-v1_0-20260811.json` — **398** assignments (198 Greek / 200 Hebrew; 88→T2, 310→IB). Single-cluster, gloss-precedent grounded (P1/P2). review_flag=false.
- **MEDIUM review:** `wa-global-cluster-alloc-medium-v1_0-20260811.json` + `.md` (grouped by suggested cluster) — **639**. Composition: precedent-conflict 118, profile-suggestion 405, translit-only 66, T2-hint 47, seat→M47 3. cluster_code = suggestion; alt = co-candidates.
- **LOW (held):** `wa-global-cluster-alloc-low-v1_0-20260811.json` — **575**. To be reviewed after mediums resolved (researcher sequence).
- Reconciliation: 398 + 639 + 575 = 1612 ✓ (all unallocated accounted for).

## Method notes for audit

- FLAG contamination fixed: cluster.csv FLAG gloss list (~130 previously-flagged terms) is NOT a positive assignment vote; FLAG only from real prior labelled allocations (P1). No HIGH item is FLAG.
- Seat words (heart/soul/spirit/mind/conscience/flesh) routed to M47, not T2.
- Translit-only (P3) singles demoted HIGH→MEDIUM (Hebrew/Greek homonym risk).
- Profile token-overlap = decision-support only; never drove HIGH.

## Candidate trends surfaced to researcher (for medium promotion)

- T-fn: function/particle + concrete non-IB (objects/places/peoples/non-seat body parts) → T2 (largest group).
- T-speech: sing/cry/shout — prior data splits M42 vs T2; need default.
- T-purity: blameless/clean/pure/undefiled/consecrate → M12.
- T-know: perceive/understand/know/discern → M15 (alts M41/M37).
- T-defile: defile/defilement/unclean/sexual-sin → M10c vs M10.
- T-weak: weary/sick/ill/incurable → M24 (alt M03).
- T-desire: desire/desirable/craving/lust → M29 vs M28.
- T-multi (analyse-in-both candidates): reject M06/M07; repentance/renewal M11/M45; testing/perseverance M34/M35.

## Open / next

- Awaiting researcher trend confirmations to promote mediums → HIGH, then LOW review.

---

## Researcher instruction — new cluster T3 (verbatim)

> thanks. what emerges from this is the need for new grouping. In T2 and Flag there are action words that describe one or other human operation: see, give, make, take, bow, look etc these words are not automatically paired with another cluster and therefore not allocated.  I suggest you run through T2 and Flag and allocate these to a new Cluster T3 General actions

## Interpretation (to confirm with researcher)

- **New cluster T3 "General actions"** = human action/operation words (verbs of operation) that are not tied to a specific inner-being cluster, currently falling to T2 or FLAG. A third category: not a specific IB characteristic, but a human operation (so distinct from T2 = no IB relation / supplementary objects & particles).
- Boundary: ACTION verb of human operation → T3; particle/object/place/people/state ("to be", "be red") → stays T2; action that clearly denotes a specific IB characteristic → its IB cluster.
- **Blocking scope question:** does T3 apply only to THIS task's unallocated strongs I routed to T2/FLAG, or also to the 895 previously-allocated T2 + 41 FLAG (earlier instruction: "not expecting re-assignment of this list")? — surfaced to researcher.
- **Edge forks to confirm:** perception (see/look/hear) → T3 vs M15; posture (bow/kneel/prostrate) → T3 vs M09/M21; speech acts (say/speak/cry/sing) → T3 vs M42.

## T3 candidate output (this task's T2/FLAG only)

- File: `wa-global-t3-candidates-v1_0-20260811.json`.
- Of 335 T2/FLAG-routed: **clear general-action 131**, edge perception 6, edge posture 4, edge speech 1, stay-T2 193.
- Default T3 membership proposed = clear + perception + posture = **141** (per researcher examples see/look/bow). Speech (1) held → suggest M42.
- **Possible mis-routes surfaced by the T3 pass (were T2, look IB-paired — confirm T3 or redirect):** H0421 to wail→M03; H1204 to terrify→M01; G6156 to stand in awe→M01; G1921 to come to know→M15; H3513G to honour→M08/M22; G2840 to profane / G3891 to break the law→M10/M12; H0422 to swear / H5087 to vow / G0332 to take an oath / H6148 to pledge→M42/M13; G0599,H1478,H7901J to die/be dead→M25.
- NOT YET APPLIED. Awaiting researcher: (a) scope, (b) T3 metadata, (c) edge defaults, (d) mis-route redirects. On confirmation: create T3 record, move items, regenerate high/medium/low as v1_1.

---

## Researcher instruction — T3 becomes corpus-wide "Operations" (verbatim)

> 1 - sweep previously allocated T2 and Flag also for T3's.  2- change the short name to 'Operations'  3 - Operations are a new grouping that will allow for these strongs to be considered as an operation, and the context may pair it with a specific other cluster. Edge cases may be allocated to more than one cluster but avoid general spreading accross multiple clusters.   4 - can you re-assess all the other cluster allocations to spot Operations, and allocated mis-routed to T3, and if the are edge, then to T3 and leave them in the original allocation also.

## Decisions

- **Scope = whole corpus.** T3 applies to this task's 1612 AND the 2801 prior allocations (T2, FLAG, and all M-clusters). Earlier "no reassignment" is overridden for the Operations pass.
- **T3 record:** cluster_code=T3, short_name=**"Operations"**, description="T3 - Operations: a strong considered as a human operation/movement; context may pair the operation with a specific cluster."
- **Model:** Operations is a cross-cutting grouping. A strong marked T3 is analysable as an operation; context may pair it with a specific cluster. Edge cases → T3 + one home cluster (multi allowed) but **avoid spreading across many clusters**.
- **Reassessment rule (#4):**
  - operation currently in T2/FLAG → **move to T3**.
  - operation currently in an M-cluster and it does NOT really denote that characteristic (**mis-route**) → **move to T3**.
  - operation currently in an M-cluster and it genuinely denotes it (**edge**) → **T3 + keep original**.
  - non-operation (state/noun/adjective) → untouched.
- **Operation detector (transparent, for confirmation):** gloss begins "to <verb>" with a dynamic head (excludes "to be/become/exist" and "be X" states). Mis-route flag = head verb in a generic-physical-action lexicon (do/make/give/take/carry/break/surround/cast/walk/place…). Heuristic; researcher confirms.
- **Review gate:** all outputs are assignment reports for researcher review; CC applies (GR-PROC-004).

## Operations pass — outputs (2026-08-11)

- **T3 record:** `wa-global-t3-cluster-record-v1_0-20260811.json` (short_name Operations).
- **Applied (reports for CC review):** T2/FLAG operations → T3. Task: **145** (folded into v1_1). Prior: **211** (`wa-global-prior-t2flag-to-t3-v1_0-20260811.json`). Total non-IB operations carved = **356**.
- **Task v1_1:** `wa-global-cluster-alloc-high/medium/low-v1_1-20260811.json` — HIGH 503 / MEDIUM 535 / LOW 574 (sum 1612 ✓); T3=145.
- **Master instrument:** `wa-global-operations-corpus-v1_0-20260811.json` — 1372 operations: carveout_t2flag 356, carveout_unassigned 146, mcluster_edge 795, mcluster_generic_review 75.

## Pending researcher decisions (not applied)

- **D-edge (blocking):** tag ALL **795** M-cluster operation-verbs with T3 (edge = T3 + keep), or only a borderline subset? "avoid general spreading" noted — need the boundary.
- **D-misroute:** 75 generic-verb ops in IB clusters; most look like genuine edges (to do good→M05, to give thanks→M22, to lie→M14). Researcher flags any TRUE mis-routes to MOVE (remove from cluster).
- **D-unassigned:** 146 unassigned-LOW operations kept in LOW (not forced to T3-only, to avoid burying IB ops like "to sanctify"→M12); resolve cluster first, then T3-edge/T3-only.
- **D-redirect:** ~dozen former-T2 items now in T3 that look IB (to wail→M03, to terrify/stand in awe→M01, to take heart→M47…): optionally add the IB cluster as edge.

---

## Researcher instruction — edge scope clarified (verbatim)

> Edge scope.  To love, for example, it is a verb/action that directly relates to a cluster. These should not be allocated to T3. where the verb or action has a direct meaning relation with a inner being cluster, then it would stay there, or be allocated to the IB cluster.  Edge is the association with a specific IB cluster cannot reasonably determined, or could be applied to a large number of clusters.   Edge should not be a goto type of allocation, it should only be considered if it can be applied to one or the other.

## Decision — edge rule (final)

- **Direct meaning-relation to an IB cluster → stays in / goes to that IB cluster. NOT T3.** (to love→M05.)
- **T3 (Operations)** = operation whose association with a specific IB cluster **cannot reasonably be determined**, OR that **could apply to a large number of clusters** (generic).
- **Edge (T3 + one cluster)** = rare; only where it genuinely sits between T3 and one specific cluster. Not a goto.
- Consequence: the **795 specific-verb ops already in IB clusters STAY (no T3 tag)** — confirmed, no change. Only the **75 generic-verb ops** need per-item disposition.

## Generic-verb operations — disposition under edge rule

- File: `wa-global-generic-op-disposition-v1_0-20260811.json`. Of the 75 generic-verb ops in IB clusters:
  - **STAY 39** (direct relation → keep in cluster, no T3). No change.
  - **T3 24** (bare generic / applies-to-many → Operations). Mostly task; 6 prior. Pending confirm (borderline: to press on/upon [M03], to take heed [M04]).
  - **RECLUSTER? 8** — sense ties to a different cluster; mostly the nasa "to lift" senses mis-pooled in M19: forgive→M11, guilt→M10, vow→M21, kindness→M05, bear→M23; plus to make peace→M33. Pending confirm (do not auto-apply; re-clustering prior/task work).
- Correction applied: "to lie" (M14) = deceive → STAY (not T3).
- 146 unassigned-LOW operations to be resolved in the LOW review (determinable→cluster; generic/undetermined→T3).

## Applied — generic-op dispositions (researcher confirmed both)

- **24 generic ops → T3** (borderline included; researcher: reassessed in verse context later).
- **8 reclustered:** make peace→M33; nasa senses forgive→M11, guilt→M10, vow→M21, kindness→M05; lift:bear→T3 (generic); put up with→M34 [tentative]; turn away→M06 [tentative].
- **Task v1_2:** `wa-global-cluster-alloc-high/medium/low-v1_2-20260811.json` — HIGH 519 / MEDIUM 519 / LOW 574 = 1612; **T3=164**.
- **Prior reassignments v1_1 (corrected):** `wa-global-prior-reassignments-v1_1-20260811.json` — **218** = 211 T2/FLAG→T3 + 6 generic→T3 + 1 recluster.
- **Bug fixed:** prior data has multi-cluster strongs; reassignment now per (strong,cluster) instance (dict-keying had dropped 21 rows). Recount confirmed 211 prior T2/FLAG ops.

## Status / next

- Confirmed & reportable to CC: T3 record; task v1_2 allocation; prior reassignments v1_1. (CC applies via patch after researcher review — GR-PROC-004.)
- **Next (researcher's original sequence):** MEDIUM trend-review (519 items) → then LOW review (574, incl. 146 unassigned operations → T3-or-cluster).

---

## Researcher decision — MEDIUM accepted (verbatim)

> my assessment of medium is that the suggested allocations are near enough, and your reasoning is applied consistent enough to provide a reasonable outcome.  given that this is not a final decision on the actual meaning, but a likely bucket in which it can be considered, I would agree and accept the medium allocations as suggested.  lets turn to the low.

## Decision

- **MEDIUM (519) accepted as suggested** — each medium item's suggested `cluster_code` is confirmed (a likely bucket for later verse-level assessment, not a final meaning decision). review_flag can be cleared on acceptance.
- Proceeding to **LOW (574)** review.

## LOW review — proposed dispositions

- Files: `wa-global-cluster-alloc-low-review-v1_2-20260811.json` + `.md` (grouped).
- Rule: operation → direct-relation cluster else T3; non-operation → IB cluster if gloss denotes inner being (transparent stem lexicon) else T2 (F2 default).
- Distribution (574): **T2 362 · T3 127 · IB-cluster pulls 85**.
- Fixed a substring-match bug (ill/sin) → token/stem matching with word boundaries; verified (to kill→T3, hissing→T2).
- Lexicon (stem→cluster) recorded in code; presented to researcher as the "trends" for accept/adjust.
- Awaiting researcher: accept low dispositions as suggested, or flag trends (e.g., pull specific items out of the T2 default).

## T2 likeness review (researcher request)

- File: `wa-global-t2-likeness-review-v1_0-20260811.md` (+ .json). Scope: full task-T2 = 542 (HIGH 48 · MEDIUM 132 · LOW 362). Prior-allocated T2 not included (offered).
- My likeness grouping (17 groups): Particles/function 60 · Proper names 8 · Deity 6 · People/roles 21 · Place 5 · Animals 1 · Plants/food 14 · Physical objects 17 · Body/anatomy 19 · Number 8 · Colour 8 · Time 10 · Space 7 · Death 8 · Legal/abstract 12 · State/condition 172 · Other/abstract 166.
- **Finding surfaced:** the Other bucket holds **64 items flagged ⚠IB?** (beauty, moral, courage, reverent, hunger, mockery, comfort, laughter, distressing, perverseness, conspiracy, strife, cunning…) that fell to the T2 default but read as inner-being — candidates to pull into IB clusters. Flagged for researcher review.

---

## Researcher reflection — descriptors (verbatim)

> the 'other' group is largely what I would call 'descriptors' that in most cases could be applied to IB.  The question is weather they would sensibly belong in T3, a separate bucket or remain in T2.  The clustering is mainly a tool to allow for the cluster to be subjected to verse level analysis.  The descriptors is likely to always pair with something else to enhance to meaning of the pair, they would hardly be analysed on their own.  That goes against them being assigned in a cluster. (although some of these descriptors is directly related to specific clusters, which means they could be allocated to that cluster.) or maybe the descriptor is paired with an operation and therefore belong in T3 to be analysed with it.  I do not want to get too hung up about it, because ultimately, when the verse is analysed, these will be pulled in automatically.

## Claude AI recommendation (pending researcher decision)

- **Not T3.** T3 = operations (things done). A descriptor is a quality — a different kind. It only meets T3 when it *qualifies an operation in a specific verse*, and that pairing is captured at verse-analysis time, not by lexical assignment. Blanket descriptors→T3 would blur what T3 is for.
- **T2 already fits.** T2's own definition is "supplementary — supplementing strongs that have IB significance." A descriptor that pairs to enhance another word IS exactly that. So T2 is the correct home, not a fallback.
- **Carve-out:** descriptors with a *direct single-cluster relation* (courage→M23/M34, reverent→M01, mockery→M06/M07) can anchor a verse group on their own → allocate to that cluster.
- **Separate bucket (e.g. T4 "Descriptors")** only worth it if the verse tooling will ask "is this a descriptor?" — a tag parallel to T3. Otherwise skip.
- **Default proposed:** leave descriptors in T2; pull only the directly-cluster-tied ones; do not create T4 unless the tag is wanted. Consistent with "verse analysis pulls them in automatically."

---

## Researcher decision — descriptors (agreed) + close

> agreed. can you finish off the final allocation json for all clusters as per the current assessment, then you can close this session. it is worthwhile recording the process in the closing session - we will use it again.

- **Descriptors:** option (a) confirmed — descriptors stay T2; only directly-cluster-tied pulled (20 pulled); no T4.
- **FINAL allocation:** `wa-global-cluster-alloc-final-v1_3-20260811.json` — 1612 assigned: **T2 522 · T3 291 · IB 790 · FLAG 9**.
- **Session log produced:** `wa-global-cluster-alloc-sessionlog-v1_0-20260811.md` (process, decisions, reusable method, pitfalls).
- **Session closed cleanly** (session log present per GR-OBS-001).

## Final deliverable set for CC (apply after review, GR-PROC-004)
1. `wa-global-t3-cluster-record-v1_0-20260811.json` (add T3)
2. `wa-global-cluster-alloc-final-v1_3-20260811.json` (1612 assignments)
3. `wa-global-prior-reassignments-v1_1-20260811.json` (218 prior changes)
