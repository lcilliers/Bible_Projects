# M38 — comment evaluation register (A6/A7/D2 → findings)

**Living register · 2026-06-02 · cluster M38 (Salvation, Redemption and Deliverance).**
Each gating comment (A6 flag / A7 stray SB finding / D2 pointer) is evaluated here on
its **full text and underlying data** to a decision: **create finding(s)** (one per
affected cluster) or **set aside non-evidenced** (recorded as informing, not deleted).
No Session-D routing (Session D is moot). Decisions are debated, not auto-applied; once
agreed they go into the spec JSON (`action`/`evaluation`/`reason`) and are written as a
patch. This doc is the context you review to decide.

**Standard for each item:** (1) the comment verbatim + source; (2) why it gates M38;
(3) factual verification against the DB; (4) candidate outcomes with **exactly what each
writes and implies**; (5) recommendation + residual uncertainty; (6) your decision.

---

## Item 1 — A7 finding id 33 · `DIM-039-001` (registry 39 *debauchery*) · link `M04,M38`

### 1. The comment (verbatim)
> Group 4986-001 in debauchery (#39, C12) contains 57 verses of salvation vocabulary
> (sōzō/sōtēria), anchored at Eph 2:8 ('by grace you have been saved through faith').
> Related verses span the NT salvation corpus: Mat 10:22, 19:25, 24:13, Mar 16:16, Luk
> 8:12, Joh 3:17, Act 2:21, 4:12, and more. This group is structurally unexpected in the
> debauchery registry but was placed there on the basis of the verse evidence — salvation
> vocabulary appears in debauchery-adjacent contexts. Session B analyst should assess the
> connection: is salvation specifically named as the remedy for debauchery/licentiousness
> in these contexts, does the term appear because the debauchery file included a broad NT
> lexical sweep, or is there a distinct theological pattern linking salvation and
> debauchery vocabulary in Scripture? … This is also a Session D synthesis candidate.

Source: `wa_session_b_findings` id 33 · type DIMENSION_REVIEW · raised 2026-04-06 (DimensionReview v1.2) · status `pending` · `cluster_link = M04,M38` (basis: *translit*).

### 2. Why it gates M38
The bridge term is **G4982 `sōzō` "to save"** (mti_terms id 4986). It is *owned* by
registry 39 (**debauchery**) — because debauchery's STEP extract did a broad NT lexical
sweep that pulled in `sōzō` — **but** the term-anchor re-clustering correctly placed
`sōzō` into **M38** (salvation), sub-groups A/B/C/F. A7 fires because a term living in
M38's sub-groups carries an unresolved Session-B note via its (legacy) owning registry.

### 3. Factual verification (checked against the DB today)
- **Eph 2:8** (the finding's anchor) is an **active M38-A anchor** under `sōzō`
  (`is_anchor=1, is_relevant=1`). The finding's own anchor is already M38's evidence.
- `sōzō` has **92 active verses in M38** (67 in M38-A *Eschatological salvation by faith*,
  12 M38-B, 12 M38-C, 1 M38-F; 16 anchors total). The salvation corpus is fully analysed
  in M38.
- The group the finding names, **VCG `4986-001` "Salvation of the inner person — saved by
  grace through faith", is `delete_flagged=1`** — dissolved by the re-clustering; its
  verses are now M38-A.
- The **M04 (Joy) link is spurious** — basis *translit* only; nothing in the text connects
  salvation-in-debauchery to joy/gladness/delight.

### 3b. What M38 already concludes about this (the backdrop you evaluate against)
Full cluster findings: `wa-cluster-M38-findings-digest-v1-20260602.md` (this folder).
The salvation corpus + Eph 2:8 are already analysed in **M38-A** — e.g.:

> **[21346 · CHAR-1]** "The corpus identifies several enabling inner conditions. (1)
> Faith/trust directed toward Christ — the primary and irreducible condition: **Eph 2:8**,
> Mar 16:16, Act 16:31, 1Pe 1:9… (4) Repentance and inner turning: Act 2:38… godly grief
> and will-turning away from sin…"

and five further M38-A findings cite Eph 2:8 (21328/21333/21343/21345/21347). The comment's
anchor and corpus are squarely inside M38-A's existing analysis.

**Test of the comment's actual hypothesis** ("a distinct salvation–debauchery pattern"):
a search of all 1,512 M38 findings for *debauch / licentious / asōtia / dissipat* returns
**one** hit (20842, char 127) — and it is about affective range, **not** salvation-as-
remedy-for-debauchery. So M38's own analysis carries **no** salvation–debauchery pattern.

**Reading:** the finding's open question is **answered** — it was a lexical-sweep artifact
in the debauchery STEP file; the re-clustering relocated `sōzō` to M38, where Eph 2:8 and
the salvation corpus are already analysed (3b), and M38 found no distinct salvation–
debauchery link. Nothing in the comment adds to or contradicts M38's findings.

### 3c. The actual relationship (verse-checked) — REVISES the reading above
Registry 39 (debauchery) **owns the salvation terms** G4982 `sōzō`, G4990 `sōtēr`,
G4992 `sōtērion` alongside G0810 `asōtia` / G0811 `asōtōs`. This is **not** a random
sweep: **`asōtia` is the alpha-privative of the save-root** (*a-* + *sōz-/sōt-*) —
literally "**un-saved-ness**", the abandoned / past-saving life (Thayer). The debauched
life is **morphologically and conceptually the negation of the saved state.**

Verse discipline (verse meaning rules analytics): a co-occurrence check finds **0 verses
containing both** a salvation term and a debauchery term (243 salvation-term verses, 0
overlap). So the relationship is **lexical / structural-opposite, NOT verse-co-occurrence.**
It belongs in the *vocabulary / structural-opposite* tier question — **T7.1.5
(finding 21509)**: *"Does the vocabulary include a term for the structural opposite or
absence of this characteristic?"* — whose current M38 answer gives the Eph 2:8 argument
and **never names `asōtia`**. That omission is the gap.

→ **Reverses the earlier set-aside reading.** Comment 33 evidences a real, missing
inter-characteristic finding (researcher, 2026-06-02): salvation's vocabulary carries its
own privative — `asōtia` ("un-savedness", debauchery) is the lexical and conceptual
opposite of the saved state.

### 4. Candidate outcomes — what each writes and implies

| Option | What it writes | Implication |
|---|---|---|
| **O1 — create inter-characteristic finding** *(recommended)* | New `cluster_finding` under M38-A on tier **T7.1.5** (vocabulary structural-opposite): *salvation's σωτ-root carries its own alpha-privative — `asōtia` (G810, debauchery) = "un-savedness", the lexical+conceptual opposite of the saved state; no verse co-occurrence (lexical relationship)*. Xref to source finding 33; mirror finding seeded in the **debauchery cluster** when its turn comes. Source finding 33 → `status='folded'` (adopted into the new finding). | A7 37→36; M38-A's T7.1.5 answer is completed with the `asōtia` term it had missed; the salvation↔debauchery structural relationship is recorded; debauchery cluster gets the reciprocal. |
| **O2 — set aside non-evidenced** | finding 33 → `set_aside` + note. **No new finding.** | *Rejected* — loses a real structural-opposite relationship M38 had not captured (the earlier reading; corrected by 3c). |
| **O3 — M04 (Joy) finding** | New finding in M04. | *Rejected* — the M04 link is a translit artifact; no joy connection. |

### 5. Recommendation + residual uncertainty
**O1 — create the inter-characteristic finding** (M38-A, tier T7.1.5; reciprocal in the
debauchery cluster). Grounded as a **lexical/structural-opposite** observation, explicitly
**not** a verse-co-occurrence claim (0 same-verse overlap). Confidence: high on the
relationship (the morphology + the 0-overlap fact are unambiguous); the **finding text +
exact tier placement** are the part to debate. Open question for you: anchor the finding
on **T7.1.5** (vocabulary opposite) alone, or **also** add a note under **T1.3.1**
(structural opposite — currently "perishing/apollumi") that `asōtia` is the *behavioural*
opposite while `apollumi` is the *eschatological* opposite?

### 6. Decision — researcher 2026-06-02
**O1 create finding, BOTH tiers (T7.1.5 + T1.3.1).** Reciprocal in `asōtia`'s cluster:
**yes, queue it.** `asōtia` (G810) is now in **M28 (Envy, Greed and Lust, Not started)** —
so the reciprocal is queued as an M28 pointer (M28 has no structure yet to hold a
finding). Spurious M04 link dropped.

### 7. Draft finding text — FOR REVIEW (nothing written yet)
**Two NEW standalone findings** (researcher 2026-06-02: the `asōtia` observation is a
separate concept — *not* merged into 21342/21509, which are left untouched). Each is a
self-contained `cluster_finding` in M38-A (char 122, sg 172), under the same `obs_id` /
tier as the existing finding shown for placement only. Both xref source `DIM-039-001`.

**(7a) NEW finding · M38-A · tier T1.3.1 (structural opposite)** — sits alongside 21342
(which keeps its eschatological-opposite answer):
> **[CHAR-1]** E — Salvation's structural opposite has a distinct **behavioural-existential**
> axis, separate from the eschatological opposite (perishing/*apollumi*, T1.3.1 primary).
> **ἀσωτία** (*asōtia*, G810, "debauchery/profligacy") and the adverb **ἀσώτως** (*asōtōs*,
> G811, Luk 15:13, "wildly") name the dissipated, self-abandoned manner of life that is the
> lived negation of the saved state. Where *apollumi* is salvation's *terminal* opposite
> (final ruin), *asōtia* is its *lived* opposite (the un-rescued life as actually practised).
> The two together bound what salvation rescues *from*: the end-state and the way of life.

**(7b) NEW finding · M38-A · tier T7.1.5 (vocabulary term for the opposite/absence)** — sits
alongside 21509 (which is left as-is; its content is a separate concept):
> **[CHAR-1]** E — The salvation vocabulary encodes its own privative. **ἀσωτία** (*asōtia*,
> G810) is morphologically *a-* (privative) + the σῴζω/σωτ save-root — literally
> **"un-saved-ness"** (so Thayer) — the dedicated lexical term for the *absence* of the
> saved condition, denoting the debauched/dissipated life. The opposition is **lexical, not
> verse-level**: *asōtia* and the σωτ-salvation terms (*sōzō*, *sōtēr*, *sōtērion*) share
> **no verse** (0 co-occurrence across 243 salvation-term verses); the relationship is the
> shared root negated, surfaced because STEP co-located them in registry 39. So salvation's
> vocabulary names its opposite not only conceptually (perishing) but morphologically — the
> word for the saved state contains, by negation, the word for the lost one.

**(7c) M28 reciprocal — QUEUE (no write to M28 yet).** `asōtia` (G810) is clustered to **M28
(Envy/Greed/Lust, Not started)**. New M28 pointer (`wa_session_research_flags`,
`cluster_link='M28'`): *"asōtia (G810, this cluster) is the alpha-privative of the σῴζω
save-root — 'un-savedness', the lived negation of the saved state (M38 salvation). When M28
is analysed, author the reciprocal opposite finding linking asōtia to salvation (cf. M38-A
findings 7a/7b)."* Source finding 33 (`DIM-039-001`) → `folded` (M38 side adopted into 7a/7b;
M28 side carried by the new pointer). cluster_link corrected M04,M38 → M38,M28.

### 8. Write plan — DONE (applied 2026-06-02)
Spec `wa-cluster-M38-comment-33-apply-v1-20260602.json`; applier
`scripts/_apply_comment_findings_v1_20260602.py` (guarded, dry-run default, needs
`"approved": true`). Result, verified by re-audit:
1. INSERTED two standalone `cluster_finding` rows — **22084** (obs 242, T1.3.1) + **22085**
   (obs 397, T7.1.5), char 122, `finding_status='finding'`; 21342/21509 untouched.
2. QUEUED M28 reciprocal — flag **717** `SD_CLUSTER`, `cluster_link='M28'`; source finding
   33 → `folded`, `cluster_link='M38,M28'`.
3. Citation extractor re-run — **Luk 15:13** (`asōtōs`) now cited on 22084 (6620→6624).
4. Re-audit M38: **A7 37→36**, **A6 stayed 24** (reciprocal did not gate M38).

**Rule learned (applies to the whole model):** a reciprocal/queue pointer for another
cluster must use **`SD_CLUSTER`**, not `SD_POINTER`. Both surface as a D2 pointer for the
target cluster (via `cluster_link`), but `SD_POINTER` is an A6 **gating** code and would
gate the *source* cluster through the shared registry (here reg 39 feeds both M38 and M28).
`SD_CLUSTER` is non-gating, so it queues for M28 without re-gating M38.

---

## Batch 1 — A7 DIMENSION_REVIEW (8 comments incl. 33)

**Policy (researcher 2026-06-02):** no set-aside / no parking in T2. Surface → reset →
assign to the associated cluster → `SD_CLUSTER` pointer for resolution at that cluster's
turn. If a target cluster is `Analysis Complete`, the applier resets it to
`Ready for re-analysis` (built into `_apply_comment_findings_v1`).

| id | observation | outcome | status |
|---|---|---|---|
| 33 | salvation × debauchery (asōtia = privative of save-root) | 2 M38-A findings (22084/22085) + M28 reciprocal | **DONE** |
| 107 | debauchery vs Spirit-filling | route → M28 (flag 718), fold | **DONE** |
| 128 | giving as inner-being diagnostic | route → M39 (flag 719), fold | **DONE** |
| 158 | obedience > sacrifice (sha.ma/qashav) | route → M30 (flag 720), fold + M41 mis-cluster flagged | **DONE** |
| 144 | atonement × mercy | (a) M38 covered (21139) → fold + M05 reciprocal (flag 721) | **DONE** |
| 127 | paradidōmi taxonomy (yielding) | homed → M44 (flag 722), fold | **DONE** |
| 146 | division vocabulary | homed → M44 (flag 723), fold | **DONE** |
| 147 | portion / divine-human correspondence | homed → M44 (flag 724), fold | **DONE** |
| 148 | Mark 1:10 schizō (over-broad VC) | homed → M44 + VC-classification flag (flag 725), fold | **DONE** |

**A7 progress: 37 → 28** — the full A7 DIMENSION_REVIEW group (9) processed. Division
(reg 52) and yielding (reg 180) homed to **M44** (researcher 2026-06-02).

## Batch 3 — A7 SYNTHESIS (28 comments) → **A7 CLEARED (28 → 0)**

All 28 SYNTHESIS comments were reg 111 (mercy)'s full T1–T7 Session-B synthesis — one
coherent body, gating M38 only via the atonement terms. **Home: M05** (Love/Compassion/
Kindness — mercy's plurality cluster; researcher 2026-06-02). **Consolidated** into a
single `SD_CLUSTER` directional-appendix pointer to M05 (flag **726**, referencing ids
1593–1620); all 28 folded for M38. At M05's turn, the appendix is checked against M05's
findings and de-duplicated. Spec: `wa-cluster-M38-comment-batch3-mercy-synthesis-v1-20260602.json`.

**A7 total: 37 → 0.** M38 gate fails 2 → 1 (only **A6** remains, 24 registry pointers).

## Batch 4 — A6 gating pointers (24) → **A6 CLEARED → M38 PASS**

The 24 A6 `SD_POINTER`s split two ways (researcher 2026-06-02): **19 mercy (reg 111)
inter-characteristic content pointers** (246–259, 627–631 — mercy ↔ guilt/justice/love/
shame/comfort/peace/despair/wisdom/compassion/blood) **moved to M05** (`SD_POINTER`→
`SD_CLUSTER`, `cluster_link=M05`); **5 reg-180/187 pure process / registry-design pointers**
(155/170/171/172/173) **resolved + closed** (Session D moot). The real sha.ma data issue
(170) is preserved via the M41 flag (720). Spec: `wa-cluster-M38-comment-batch4-a6-v1-20260602.json`.

**M38 verdict: PASS (0 GATE fails).** Non-gating residual: **A2** 24 (advisory false-
positives — cluster_synthesis discussing gaps) + **D2** 2 (pointers 147 soteriology-arc /
581 fellowship — adopt-or-route). Ready to close once those are dispositioned.

## Batch 5 — D2 + observations + closure contract (researcher principle)

Researcher principle (2026-06-02): every pointer/observation closes at completion as
**finding (tiered or observational) | resolved | set aside** — nothing parked.

- **D2 (2):** **581** (fellowship, reg 62) → rerouted to **M44** (no fellowship cluster).
  **147** (DIM-073-SD001, guilt→repentance→no-condemnation→justification soteriology arc)
  → **observational finding** `cluster_observation` **277** (M38 is the arc's terminus;
  cross-ref M10/M11/M26); pointer resolved. Not a tiered finding — no M38 tier home.
- **17 open `target=D` observations** (260–276, cross-register flags + structural notes) →
  **confirmed** as standing observational findings (most already actioned via this session's
  routing — `hilas*`→M05, `dorea/dorema`→M39). **276** (OT/NT atonement) covered by finding
  21142; M11 atonement-integration queued (flag **727**).
- **New auditor GATE — A10** "no open Session-D observations (Session D moot)": enforces the
  principle structurally; no cluster can complete with Session-D items parked. (Impact: M38
  only — no other in-progress cluster has open `target=D` observations.)
- **A2 (24):** no-action — these are already `cluster_synthesis` findings (not pointers);
  the heuristic mis-flags synthesis that discusses gaps. Advisory, non-gating.

**M38: verdict PASS, 0 GATE fails (incl. A10), A6/A7/D2 = 0, all observations closed.**
Re-audited, NOT closed (researcher hold). Fully closure-ready.

### Item — 144 `DIM-111-001` atonement × mercy — DECISION PENDING
**Evidence.** M38 char 125 (Conscience cleansed through atonement) already analyses the
mercy-disposition → atonement-mechanism → standing chain: **21139** ("God… compassion-driven…
oriented toward removal of guilt"), 21143 (God himself atones, Psa 65:3), 21145 (giver/
receiver asymmetry), 21152 (atonement as the resulting standing). Verse-check: `hilasmos`/
`hilastērios` occur in only 8 verses; **`eleos` (mercy) never co-occurs**; 1Jn 4:10 ties
propitiation to **love (`agapē`)**, not mercy. Mercy (reg 111) clusters mainly to **M05**
(Love/Compassion/Kindness, status *Ready for re-analysis*).

**Reading:** unlike 33, there is **no M38 gap** — atonement-from-divine-compassion is
already in M38 (21139). The generative finding belongs to the **mercy cluster (M05)**:
mercy/compassion's structural mechanism for altering human standing is atonement (M38).

**Options:**
- **(a) M38 covered → fold for M38 + `SD_CLUSTER` reciprocal to M05** (no new M38 finding). *Recommended.*
- **(b)** also add a thin M38 finding making the inter-cluster mercy↔atonement-mechanism link explicit (+ M05 reciprocal).
- Decision: __________
