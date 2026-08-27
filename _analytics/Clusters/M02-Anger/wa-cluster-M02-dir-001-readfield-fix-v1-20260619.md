# Directive DIR-20260619-001 — M02 read-field corrections (valence + divine_involvement)

> Produced by: wa-directive-instruction-v1_4-20260506
> Governed by: wa-global-general-rules [current]
> Cluster: M02
> Produced date: 2026-06-19
> Researcher approval: PENDING

---

## Motivation

The evidence-verification pass against the four `ve_lexical` M02 extracts (`wa-m02-evidence-verification-v1_0-20260619.md`; obslog `wa-obslog-m02-oldnew-compare-v1-20260619.md`) found two read-resolution errors in the M02 measure layer (ve_lexical read-API outputs, schema 3.34.0). Both were surfaced as flags F-B and F-C:

**Correction A (F-B) — valence mis-attributed to divine wrath.** Six divine-wrath occurrences (a burning-heat lemma with `divine_involvement` = possessor/agent) carry `valence = sinful`. The verse evidence shows the sinful framing belongs to the **provoking human sin** in the verse, not to God's wrath — e.g. Num 32:14 "a brood of **sinful men**, to increase still more the fierce anger of the LORD"; 2Ki 22:17 "because they have **forsaken me**… to provoke me to anger"; 2Ki 23:26 "because of all the **provocations** … Manasseh"; Job 42:7 "for you have **not spoken** of me what is right". A divine-wrath term tagged sinful is analytically and doctrinally wrong (the F4/F10.1 anomaly). It should be `neutral` (or `righteous`). The co-occurring provoking term (`ka.as` / `ka.a.s`) in those verses is correctly `sinful` and must stay so.

**Correction B (F-C) — `divine_involvement` omission causing C1/C2 leakage.** Two occurrences of `cha.rah` whose text reads "the anger of the LORD was kindled" carry `divine_involvement = NONE` (`experiencer = other`), so they resolve to the human-anger characteristic (C1) instead of divine wrath (C2): Exo 4:14 (against Moses) and 2Ki 13:3 (against Israel). `divine_involvement` should be `agent` (God), which re-routes each to C2.

Both corrections must be made by **independent verse re-read**, not by re-running the read engine that produced the error (the F10.1 circularity caution: the C1/C2 split rests on this same read-resolved field).

---

## Scope

**Measure layer:** the `ve_lexical` read-API output rows holding the per-occurrence lexical fields (`valence`, `divine_involvement`) for M02 focus terms (source: ve_lexical v2_engine_iter1 + `*_read_api` + verse_morphology, schema 3.34.0). Claude AI is **not certain of the exact table/column names** for these read-resolved fields — CC resolves the storage location. Occurrences are identified by verse reference + Strong's + transliteration.

**Correction A — valence** (expected 6 occurrences; CC to confirm the exact set):

| Verse | Strong's | translit | current `valence` | target |
|---|---|---|---|---|
| Num 32:14 | H2740 | cha.ron | sinful | neutral |
| 2Ki 22:13 | H2534 | che.mah | sinful | neutral |
| 2Ki 22:17 | H2534 | che.mah | sinful | neutral |
| 2Ki 23:26 | H2734 | cha.rah | sinful | neutral |
| 2Ki 23:26 | H2740 | cha.ron | sinful | neutral |
| Job 42:7 | H2734 | cha.rah | sinful | neutral |

**Authoritative criterion** (supersedes the list if they differ): every M02 focus occurrence whose term is a burning-heat divine-wrath lemma (che.mah H2534, cha.rah H2734, cha.ron H2740, qa.tsaph H7107, qe.tseph H7110A, orgē G3709, and related burning-heat forms) **AND** `divine_involvement` ∈ {agent, possessor, giver} **AND** `valence = sinful`. The NEW findings cite **7** such occurrences; the verification confirmed **6** — CC reports the actual set found.

**Correction B — divine_involvement** (2 occurrences):

| Verse | Strong's | translit | current `divine_involvement` | target |
|---|---|---|---|---|
| Exo 4:14 | H2734 | cha.rah | NONE | agent |
| 2Ki 13:3 | H2734 | cha.rah | NONE | agent |

Consequence: each occurrence re-routes from the human-anger characteristic (C1) to the divine-wrath characteristic (C2). If the c1–c7 characteristic split is materialised anywhere (rather than re-derived at read time from `divine_involvement`), CC updates that derivation for these two occurrences.

---

## Outcome required

**Correction A:** every occurrence meeting the Correction-A criterion has `valence` re-resolved from `sinful` to `neutral` (CC may set `righteous` instead where the verse frames the wrath as explicitly just — CC notes any such case for AI review). The co-occurring provoking-term occurrences (`ka.as` H3707 / `ka.a.s` H3708B) in the same verses retain `valence = sinful` (unchanged).

**Correction B:** the Exo 4:14 and 2Ki 13:3 `cha.rah` occurrences have `divine_involvement = agent`; each resolves to the divine-wrath characteristic (C2); `experiencer` re-resolved consistent with God as subject.

No physical deletes (wa-patch-instruction [current] §5.4). All changes made by independent verse re-read.

---

## Completion confirmation

Return:

1. **Before A:** the set of M02 focus occurrences matching the Correction-A criterion (verse, Strong's, current `valence`) — to confirm the 6-vs-7 count.
2. **After A:** the same query — expected **0** divine-wrath occurrences (`divine_involvement` ∈ {agent, possessor, giver}) with `valence = sinful`.
3. **Provoking terms unchanged:** the `ka.as` / `ka.a.s` occurrences in Num 32:14, 2Ki 22:13, 2Ki 22:17, 2Ki 23:26 — confirm `valence` still `sinful`.
4. **After B:** Exo 4:14 and 2Ki 13:3 `cha.rah` — `divine_involvement = agent` and resolved characteristic = C2. Expected **2** rows.
5. **No collateral change:** confirm the total number of M02 occurrences whose `valence` or `divine_involvement` changed equals **8** (6 valence + 2 divine_involvement), or the actual count if the Correction-A set ≠ 6.

---

## Notes

- Source: `wa-m02-evidence-verification-v1_0-20260619.md` (flags F-B, F-C); obslog `wa-obslog-m02-oldnew-compare-v1-20260619.md`.
- These corrections feed the **not-yet-persisted** NEW M02 findings; apply them **before** the findings are written to `cluster_finding`, so the persisted findings carry the corrected valence and the corrected C1/C2 assignment.
- Method rationale: directive, not patch, because AI is not certain of the measure-layer schema for these read-resolved fields (per researcher instruction and wa-patch-instruction [current] §1.1 / wa-directive-instruction [current] §1.1).
- The C7 scope item is **not** in this directive — it is a separate decision raised to the researcher (see the accompanying message); the C7 directive will be produced once the resolution is chosen.
