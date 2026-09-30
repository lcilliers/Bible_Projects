# Ruthlessness / cruelty — missing-term investigation (LIVING — single source of truth)

> **Doc version:** 1 · **Last updated:** 2026-06-28 · **living document** (edit in place; git = history). **This is the ONE record for this investigation.** It supersedes and folds in four earlier scattered docs (now archived — see §7). Do not create new docs for this thread; update this one.
>
> **Current status:** ⏸ awaiting researcher decision (§5). Registry 216 "Ruthlessness" created; STEP discovery + existence check done; new-cluster plan **reversed** (the concept already exists in M06).

---

## 1. Origin — how this surfaced
Working the Lev 25:43 fan-out, `perek` (H6531, "ruthlessly") was central to the verse but had **no study identity** — no cluster, no term, flagged by the verse's own lexical as an un-accounted coverage gap. Question: why is cruelty/ruthlessness absent, and how do we bring it in?

## 2. Why it was excluded (the diagnosis)
- `perek` H6531 has **zero trace** as a study term (not in `mti_terms`/inventory/root-family) — never extracted.
- The 215-word registry has **no anchor word for cruelty/ruthlessness/harshness/severity** (it has anger, wrath, bitterness, malice, contempt, pride; and strength/power/authority/dominion — but not cruelty).
- So `perek` had no English home → never pulled → survives only as a ride-along span.
- **Method-integrity validation of *why* the cascade missed it:** `wa-term-coverage-method-integrity.md` — the registry→terms→related-terms cascade is an expansion tool over a human-seeded English list + a shallow/leaky STEP `relatedNos` graph (perek's only STEP relation is the homonym "curtain"). It is an *index*, not a *census*; blind spots are structural. The verse-fanout is the coverage guarantor.

**Researcher note (foundational):** the registry development notes/history already recognise that IB-relevant words may surface mid-study that aren't in the registry, and map a path to add them and bring the study up to date. Since then, **new constructs** (clusters, ve_lexical, spans…) have developed that the original registry-management notes don't cover — so the add-path must be **updated to populate those too**, and the registry-management guide updated accordingly.

**Researcher steps directed:** (a) reread registry instructions — new-word discovery still applies; (b) add the word, follow all steps; (c) expect new terms/verses/relationships/cluster; (d) catch up constructs (ve_lexical, spans, gloss); (e) confirm all structural components complete.

## 3. STEP discovery — the term family
STEP discovery (7 anchors: ruthless, cruel, harsh, severity, rigour, violence, oppression, fierce) → 44 candidates. `perek` H6531 **missed by STEP's English search** (rare; ESV-glossed "ruthlessly/harshness") — but it sits in `arits`'s related cluster, so **servicing the family via STEP pulls it through.** Raw output: `research/discovery/*_term_map_20260628.json` (kept as source data).

**Researcher method correction (d):** we do **not** hand-pick individual Strong's — **STEP services the registry word and pulls the whole related family.** The family for this concept (per researcher's STEP view): `mar` H4751 (bitter), `az` H5794 (strong), `arits` H6184 (ruthless), `chamats` H2556 (oppress), `perek` H6531 (severity), `chamal` H2550 (to spare).

**Triage guidance (b):** Tier-1 core = add all; Tier-2 (harshness) = add **when used as a qualifier of a Tier-1 term**; Tier-3 = other concepts.

## 4. Existence check — THE REVERSAL (researcher comment a + c)
Checking every candidate against the DB overturned the new-cluster plan:

| term | gloss | in study? | cluster | owner registry |
|---|---|---|---|---|
| **`perek` H6531** | ruthless/harsh treatment | **NO — absent** | — | none |
| `arits` H6184 | ruthless one | yes | **M06** | dread |
| `akzar`/`akzari`/`akzeriuth` H393/4/5 | cruel / cruelty | yes | **M06** | strength |
| `aneleemon` G0415 | merciless | yes | M05 | mercy |
| `qasheh` H7186 | hard/severe | yes | M24 | distress |

**Cruelty/ruthlessness already EXISTS as a characteristic** — **M06 "Hate" [Analysis Completed]**:
- char 4 — *"Cruelty/Ruthlessness — Character disposition of merciless destructiveness."*
- char 106 — *"F — Cruelty and ruthlessness — the settled cruelty of a person."*
- already holds `arits` + the `akzar` family.

→ **A new cluster would duplicate M06.** Only **`perek` H6531 is genuinely missing.**

**Tier-3 existence (answering c):** mostly present (anger M02, evil M03/M27, bitter M03, strength M23) — **except VIOLENCE**: `chamas` H2555 (60×), `shadad` H7703, `shod` H7701, `lachats` H3906 are **absent from the whole study.** That is a genuine, separate gap.

## 5. ⏸ DECISION NEEDED (current open question)
1. **Confirm the reversal:** `perek` H6531 → added to **M06's existing Cruelty/Ruthlessness characteristic** (char 4/106), with **reg216 "Ruthlessness" as its owner registry**, cluster-assigned into M06 — **NO new cluster.** *(Reverses the earlier "new cluster" decision, which was made before the existence check.)*
2. **Scattered terms** (`arits`→dread, `akzar`→strength): re-home into reg216 now, or leave and XREF? *(recommend: leave for now.)*
3. **Violence** (`chamas` + kin, absent): open as a **separate registry-gap item**? *(recommend: yes — distinct concept.)*

## 6. Decision log
| date | decision | status |
|---|---|---|
| 2026-06-28 | Add "Ruthlessness" as registry word | done — reg216 created |
| 2026-06-28 | Word label = "Ruthlessness" (noun) | confirmed |
| 2026-06-28 | ~~New cluster for cruelty~~ | **REVERSED** (§4 — cruelty already = M06 char4/106) |
| 2026-06-28 | Complete term list via STEP (not hand-pick) | done — §3 |
| 2026-06-28 | ve_lexical still live/used | confirmed |
| — | perek → M06 via reg216; re-home?; violence gap? | **PENDING (§5)** |

## 7. Superseded documents (folded in here, archived for provenance)
- `wa-perek-ruthlessness-registry-exclusion-20260628.md` → §2 *(archived)*
- `wa-add-ruthless-registry-plan-v1-20260628.md` → §3/§8 *(archived; new-cluster framing now wrong)*
- `wa-216-ruthlessness-triage-v1-20260628.md` → §3 *(archived)*
- `wa-add-ruthless-existence-findings-v1-20260628.md` → §4 *(archived)*

## 8. Next steps once §5 confirmed (revised — much smaller than the original plan)
1. STEP-service the ruthlessness family so `perek` + relations come through; add `perek` H6531 as OWNER of reg216.
2. Assign reg216 → **M06** (Cruelty/Ruthlessness characteristic) — no new cluster.
3. Constructs catch-up for the new term's verses: spans/morphology, gloss, ve_lexical, verse-read finding; link into `verse_analysis_progress`/`ib_observation`.
4. **Completeness validation** — confirm every structural component is populated and the DB stays integrated (researcher step e).
5. Update `wa-registry-management-guide` with a "new-word: newer-constructs catch-up" section (the documented path gap).
6. Separately: log the **Violence** registry gap.
