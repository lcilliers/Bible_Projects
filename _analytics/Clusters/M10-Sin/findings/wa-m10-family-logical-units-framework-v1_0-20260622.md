# WA M10-family — Logical-units capture framework + first-pass typing (PROPOSAL, for sign-off)

- **File:** wa-m10-family-logical-units-framework-v1_0-20260622.md · **Version:** v1_0 · **Date:** 2026-06-22
- **Author:** Claude Code · **Status:** **APPROVED with changes (2026-06-23). Built out in `wa-m10-family-logical-units-ledger-v1-20260623.md` + gap register `…-gap-register-v1-20260623.md`.**
- **Companion:** `wa-m10-family-collation-v1_0-20260622.md` (the state-of-work collation). This document is the *capture plan* that builds on it.

> **Decisions applied (researcher, 2026-06-23):**
> 1. **§5 `KIND` column removed.** Whether a unit is a status, a characteristic, a hybrid, or some *other* object is **at the heart of the synthesis, is not settled, and must flow from the evidence — not be imputed.** §5 now carries instead the **factual owner-cluster of each unit's Strong's** (from `mti_terms`).
> 2. **§6 recode executed** — the mis-migrated session-B findings have been moved off M10 (see §6).
> 3. **§4 resolved:** output = a **separate `.md` ledger** that indexes the DB (no new DB rows yet); **keep the 32 units.**
> 4. **New pre-synthesis task flagged (§10):** before any synthesis, **define what a "characteristic" vs a "status" is — and whether there are other object-kinds (or hybrids).**
> 5. **MERGED 2026-06-23:** M10b + M10c dissolved into **M10**, single **1–32** numbering (the §5 tables below are per-cluster/historical — old M10b #1–6 → #23–28, M10c #1–4 → #29–32; crosswalk + #→files in `wa-m10-unit-index-1to32-v1-20260623.md`).

---

## 1. What you asked for (restated)

- M10 is **not a pure characteristic cluster.** Its **primary object is the sin STATUS** — how the status is **defined**, how it **operates**, and how it **interacts** with (a) characteristics and (b) *other statuses*.
- **Characteristics are mixed in.** Some are likely **covered in other clusters**; some may need **full characteristic-treatment here**. Which is which is currently unknown — and surfacing that is part of the job.
- **Now: capture, not synthesis.** Organise the work already done (the rings + M10b evidence + digests) **together with the findings already in the DB** into **logical units** keyed by **verse / characteristic / status** — so we can then see the evidence gaps, fill them, and only *then* synthesize.

This document proposes **how** to do that, types all 32 units as a first pass, and shows one worked unit. **Nothing here is synthesis** — no meaning is derived; interactions are only *noted as held-open*, not resolved.

---

## 2. The raw material that already exists (what we are capturing)

| Source | What it is | Volume | Role in capture |
|---|---|---|---|
| **DB characteristics** (`characteristic`) | 32 defined units for the family (M10 ×22, M10b ×6, M10c ×4), each with a **definition** and, in many, **cross-register flags** | 32 | **The unit backbone** — these *are* the logical units (refined as needed) |
| **DB verse-findings** (`finding`, level=VERSE, `l2_meaning`) | prior per-verse meanings across the whole corpus incl. the CORE | **2,368** (M10 1487 · M10b 606 · M10c 275) | **The per-verse evidence layer**, attributable to units (98% map to ≥1 characteristic) |
| **DB linkage** (`mti_term_subgroup` → `cluster_subgroup` → `characteristic_subgroup`) | term→subgroup→characteristic path | 146/175/1196 rows | **The mechanism** that files verse-findings under units |
| **Chat rings + M10b evidence digests** | the disciplined fresh re-read (rings 390 occ; M10b 588 occ) + co-seated index, four/five faces, etc. | ~20 digests | **The qualitative evidence**, folded into each unit |
| **DB cluster-findings** (`finding`, level=CLUSTER, session_b) | 12 OPEN for M10, 1 for M10c | 13 | **Mostly mis-tagged migration noise** (about faith/mercy/covenant/contrition, not sin) — flag, do not treat as M10 contributions (see §6) |

> **Reconciliation:** the collation said the CORE was "not started." That was about the *new* rings-style pass. The DB **does** hold prior `l2_meaning` verse-read meanings for the core terms — so the core is not evidence-empty; it simply hasn't been re-read under the new neutral per-verse method. The capture uses those prior meanings as the starting evidence layer and flags where a fresh re-read is still owed.

---

## 3. The proposed "logical unit"

A **logical unit** = one **status** or **characteristic** of the M10 family. We seed the set from the 32 DB characteristics (they already embody the mix), and for each we capture **what we already have**, in this fixed shape:

```
UNIT  [cluster #seq]  short_name
├─ KIND            STATUS | CHARACTERISTIC | HYBRID            ← the §1 question, per unit
├─ HOME            this-cluster-in-full | shared | likely-elsewhere(→cluster)  ← "covered where?"
├─ DEFINITION      (from DB characteristic.definition)
├─ TERMS/LEMMAS    the focus lemmas that carry it (via subgroup links + digests)
├─ EVIDENCE — DB   count + pointers to the l2_meaning verse-findings filed under it
├─ EVIDENCE — Chat the rings/M10b digest observations bearing on it (held open)
├─ SEATING         the co-seated inner-being seats evidenced for it (held open)
├─ INTERACTIONS    how it touches other statuses / characteristics (NOTED, not resolved)
├─ CROSS-CLUSTER   the cross-register flags (from DB) + candidate other-cluster homes
└─ GAPS            what evidence is still missing (e.g. core not re-read; M10c scratch only)
```

- **Granularity = "per verse / characteristic / status" exactly as asked:** the unit is the **status/characteristic**; its **per-verse** evidence is the filed verse-findings (kept in the DB, indexed here — not re-copied).
- **It is an *index/organisation layer over the DB*, not a parallel store.** The verse-findings stay in `finding`; this document points to them. (Honours "all study work in the DB.")
- **Capture only.** EVIDENCE/SEATING/INTERACTIONS record what the digests and findings already say. We do **not** decide KIND/HOME authoritatively — §5 is a *first pass for your correction.*

---

## 4. Open design choices for you (so I build it right)

1. **Output form.** Proposed: a single **navigable .md ledger** (one section per unit) that *references* DB finding-IDs and digest files — not new DB rows. Capturing to the DB (new finding/observation rows) would come at synthesis, later. **OK, or do you want DB capture now?**
2. **Unit set.** Proposed: start from the **32 DB characteristics as-is**, re-typing them status/characteristic. Alternative: collapse the clear statuses into a smaller "status spine" + a characteristic list. **Keep 32, or reshape?**
3. **KIND/HOME authority.** Proposed: I produce the first-pass typing (§5); **you correct it**; the corrected typing drives the ledger. (You said you don't know which are covered elsewhere — §5 is my best read from the definitions + cross-flags + my knowledge of the other clusters, for you to adjust.)

---

## 5. The 32 units — factual signals only (no imputed kind)

> **`KIND` removed by direction** — status/characteristic/other is a *synthesis outcome*, to flow from evidence (see §10). The two columns below are **facts**, not judgements: **Owner** = the cluster(s) that *own the unit's Strong's* (`mti_terms.cluster_code`); **Cross-register flags** = the other clusters named *in the unit's own DB definition*; **DB** = attributable verse-findings.
>
> **Finding:** **every unit's terms are owned by its own M10-family cluster** (no term is owned elsewhere). So lexically these all sit *at home* in the M10 family — the "covered elsewhere" question is about **conceptual** coverage (the cross-register flags), **not** term ownership. A concept can be flagged to M11/M06/etc. while its *words* live here.

### M10 — Sin, Guilt, Transgression
| # | Unit | Owner | Cross-register flags (from DB definition) | DB |
|---|---|---|---|---|
| 1 | Wilful sinning | M10 | — | 264 |
| 2 | Unintentional sinning | M10 | — | 213 |
| 3 | Confession | M10 | — | 250 |
| 4 | Conscience suppression | M10 | — | 250 |
| 5 | Refusal to repent | M10 | — | 410 |
| 6 | Habitual defection | M10 | — | 250 |
| 7 | Contagious sin | M10 | — | 213 |
| 8 | Political revolt (pa.sha) | M10 | — | 37 |
| 9 | Sinful speech | M10 | **M06** | 22 |
| 10 | Specialised sinful mechanisms | M10 | **M14, M08, M31** | 5 |
| 11 | Sin as universal condition | M10 | — | 321 |
| 12 | Sin as enslaving power | M10 | — | 142 |
| 13 | Sin as divine record | M10 | — | 528 |
| 14 | Forgiveness sought & received | M10 | **M11** | 409 |
| 15 | Generational sin | M10 | — | 213 |
| 16 | The sinner as moral character | M10 | — | 64 |
| 17 | Guilt as inner-being state | M10 | **M03** (pu.qah) | 98 |
| 18 | Iniquity as accumulated moral crime | M10 | — | 162 |
| 19 | Transgression as boundary-crossing | M10 | — | 165 |
| 20 | Faithlessness as covenant-breaking | M10 | **M13, M31** | 103 |
| 21 | Perversion as inner inversion | M10 | **M03, M07, M23, M35** | 73 |
| 22 | Injustice as moral failure | M10 | **M26** | 72 |

### M10b — Wickedness, Evil, Abomination
| # | Unit | Owner | Cross-register flags (from DB definition) | DB |
|---|---|---|---|---|
| 1 | Wickedness as settled person-identity | M10b | (antithesis with M26 righteous, in text) | 278 |
| 2 | Evil as constitutional inner nature | M10b | — | 99 |
| 3 | Abomination — divine revulsion | M10b | — | 119 |
| 4 | Idolatrous abomination | M10b | — | 144 |
| 5 | Iniquity as active inner scheming | M10b | — | 85 |
| 6 | Evil expressed through speech | M10b | (slander/blasphemy — cf. M06) | 18 |

### M10c — Defilement, Impurity
| # | Unit | Owner | Cross-register flags (from DB definition) | DB |
|---|---|---|---|---|
| 1 | Ritual defilement-state | M10c | **M12** (structural opposite) | 260 |
| 2 | Moral-inner defilement-state | M10c | **M12** (structural opposite) | 123 |
| 3 | Corporate/covenantal defilement | M10c | **M12** (structural opposite) | 230 |
| 4 | Defilement by external spiritual agency | M10c | **M12** (structural opposite) | 30 |

**Conceptual cross-coverage to weigh at synthesis (from the flags, not a verdict):** Sinful-speech & Evil-through-speech ↔ **M06**; Forgiveness ↔ **M11**; Faithlessness ↔ **M13/M31**; Injustice ↔ **M26**; Perversion ↔ **M03/M07/M23/M35**; Specialised-mechanisms ↔ **M14/M08/M31**; Guilt(pu.qah) ↔ **M03**; all M10c defilement ↔ **M12** (opposite). All terms remain **owned by the M10 family.**

---

## 6. DB cluster-findings recode — EXECUTED 2026-06-23

The 12 "OPEN" M10 cluster-level findings were **session_b migration artefacts mis-tagged to M10** (registry-scoped findings about faith, vulnerability, contrition, goodness, mercy, covenant). Recoded off M10 to each finding's **registry-home cluster** (dominant live `mti_terms.cluster_code`), via `scripts/_apply_recode_sessionb_m10_findings_20260623.py` (snapshot `backups/bible_research_pre-recode-sessionb-m10_20260623.db`):

| Finding(s) | Registry | → recoded to |
|---|---|---|
| #129 | faith (59) | **M31** Faith, Belief and Unbelief |
| #821, #840, #1772 | contrition (30) | **M24** Weakness, Vulnerability and Suffering |
| #1450 | mercy (111) | **M05** Love, Compassion and Kindness |
| #2229, #2230, #2351, #2371 | covenant (34) | **M44** Relational Disposition |

**Left on M10 — flagged for your decision (no clean home; not guessed):**
- **#167** (vulnerability reg 206) — terms owned T2/M15; candidate **M24** (cluster name = "…Vulnerability…") or **M07** (shame sequence). 
- **#1098, #1129** (goodness reg 67) — registry terms split 3-way **M04 / M05 / M39**; pick one.

(Separately, **#108** on M10c — *akathartos* unclean-spirit — was left in place: it is on-topic for M10c #4 "Defilement by external spiritual agency" and is already CLOSED/superseded.)

The genuine DB contribution to the M10 family remains the **2,368 verse-level findings.**

---

## 7. One fully worked unit (the demonstrator)

> This is exactly what each of the 32 sections will look like. Built from real DB + digest data. Evidence held open.

### UNIT [M10b #1] — Wickedness as settled person-identity
- **KIND:** STATUS (a settled inner-being *type*, not an act).
- **HOME:** this-cluster (primary M10b status). **Interacts** strongly with **M26 (Righteousness)** — defined by antithesis with *tsaddiq*.
- **DEFINITION (DB):** *"The wicked person as an inner-being type — the individual whose core moral character is defined by wickedness. Will corrupted, God actively excluded from the mind (practical atheism), inner orientation persistently bent toward harm and injustice. Conscience suppressed or displaced by an inner voice of transgression. Wickedness is not merely a series of acts but a stable identity and inner condition; divine judgment falls specifically on this person-type because their inner character warrants it."*
- **TERMS/LEMMAS:** *ra'sha* (H7563, 248) · *re'sha* (H7562, 9) · *mirsha'at* (1).
- **EVIDENCE — DB:** 278 attributable `l2_meaning` verse-findings (via subgroup links). [Pointers to be listed in the build.]
- **EVIDENCE — Chat (held open):** the **four/five faces of ra'sha** —
  1. *Forensic verdict* — the guilty party in court (Deu 25:1; 1 Ki 8:32; 2 Ch 6:23).
  2. *Characterised interior* (bounded to Psalms/Proverbs) — heart-denial (Psa 10:13), soul-desire (Psa 10:3), concealed evil (Psa 28:3).
  3. *Fixed two-destinies antithesis* — cut off / perish / chaff (Psa 1:4; 37 passim; Pro 10–15).
  4. *Reversible condition* — summoned to **turn and live** (Eze 18:21,23,27; 33:11; Isa 55:7).
  5. *Theodicy / wisdom-crisis* — the wicked who *prospers* (Psa 73:3,12; Ecc 7:15; 8:14; 9:2).
  - type=status 258/258; faculty=moral_evaluation (term-intrinsic — defines the wicked, not an inner state).
- **SEATING (co-seated, held open):** genuine wicked-*heart* seatings are **few** (~5: Psa 10:13; 28:3; Pro 10:20; 15:28; 21:4) — the interior is **bounded, not pervasive**. *nephesh* co-seats (14) mostly "life/person" idiom.
- **INTERACTIONS (noted, not resolved):** ↔ **M26** (tsaddiq/ra'sha antithesis, pervasive); ↔ **M11** (the turn-and-live face = repentance seam); ↔ sin-status core (touches *a'von* ×9, *cha'ta* ×8, *chat'tat* ×7); ↔ M10b *a'ven*/*to'evah* (within-satellite).
- **GAPS:** ra'sha re-read under the rings/per-verse pass is complete (incl. +69 recovery); *re'sha* (9) cross-cluster-ownership unconfirmed; the DB l2_meaning layer predates the new neutral method (may need de-biasing at re-key).

---

## 8. What this is NOT

- Not synthesis, not meaning-derivation, not a status-vs-characteristic *verdict*, not a resolution of any interaction. Those wait until evidence gaps (the CORE re-read; M10c clean re-read) are filled.
- Not a new DB write (unless you choose §4.1 otherwise) — an index over what exists.
- Not a re-litigation of the collation's findings — it consumes them.

---

## 9. Proposed next step

**On your sign-off I will:**
1. Apply your corrections to the §5 typing.
2. Build the full **logical-units ledger** (`wa-m10-family-logical-units-v1-…`) — all 32 units in the §3/§7 shape, each with its DB finding pointers + folded Chat evidence + seating + held-open interactions + gaps.
3. Produce a **gap register** (the by-product you want): per unit, exactly what evidence is missing (core not re-read; M10c scratch-only; etc.) — the work-list that leads into gap-filling, then synthesis.

**Please confirm or adjust:** (a) the output form (§4.1 — md index vs DB capture); (b) keep-32 vs reshape (§4.2); (c) the §5 KIND/HOME typing (especially the "likely-elsewhere" calls — you know which clusters already cover these).

---

## 10. Pre-synthesis exploration (flagged by researcher, 2026-06-23) — REQUIRED before any synthesis

Before by-unit synthesis begins, run an explicit definitional exploration:

> **What is the definition of a "characteristic", and what is the definition of a "status"? Are there other "objects" that are neither — or hybrids?**

- This is the question the `KIND` column was removed to protect (§5): the kind of each unit must be **derived from the gathered evidence**, against clear definitions, not imputed up front.
- It is a **gate** on synthesis: the gap register (`…-gap-register-v1-…`) tracks each unit through *evidence-gathering → (this definitional gate) → by-unit synthesis*.
- Likely inputs: the existing programme notion of "characteristic" (the cluster model) vs the emerging "status" framing the M10 family forced; the M10/M10b/M10c evidence itself (e.g. ra'sha's five faces, the defilement-states, the generative *a'ven*) as test cases for the typology.

---

*Capture framework. No meaning derived; the status-vs-characteristic-vs-other question and all interactions remain open until §10 + evidence.*
