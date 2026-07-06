# Gate-1 orphan terms — registry-assignment proposal (Step 1)

> **Step 1 of the compliance plan** (`wa-established-onboarding-architecture-and-compliance-plan-20260706.md`). For each of the 97 orphan strongs, propose the English `word_registry` word it should be onboarded under (its `owning_registry`). Registry ≠ cluster: the registry is the English word-study home; the cluster (`mti_term_subgroup`) is a later step. Date: 2026-07-06.
>
> **Rollback done first:** the bypass artefacts were removed by restoring `backups/bible_research.pre-psalms-gate1-20260706T092058Z.db` (Steps 1–2 intact: 18,075 role rows, 5,350 linkages; 0 gate1 rows). Safety copy of the pre-rollback state: `backups/bible_research.pre-gate1-ROLLBACK-20260706T141152Z.db`.
>
> Probe: `scripts/_probe_gate1_registry_homes_v1_20260706.py` (read-only). Registry vocabulary = 219 words (live DB).

---

## How each term was classified against the live registry

- **Group A — already OWNER (8):** an active `wa_term_inventory` OWNER row survived; only the `mti_terms` row was deleted by OT-DBR-009. Home registry is technically already set — **but for all 8 the surviving home looks semantically wrong** (e.g. *fool* owned by "hope", *affliction* by "gentleness"), so each needs a reconcile-vs-reassign decision.
- **Group B — XREF only (8):** present as a cross-reference in other registries, never made OWNER. Needs a home-registry decision + OWNER promotion.
- **Group C — no inventory (81):** truly un-onboarded. Registry assignment is a fresh judgement.

**Structural finding (the crux of the uncertainty):** the registry vocabulary is concept-based English words and has **no entry for several core concepts these terms express** — no `salvation`, `speech`/`telling`, `testing`, `vengeance`, `oppression`, or `violence` registry. Terms in those families cannot "fit an existing registry" cleanly; they need either a **new REGISTER** or a considered reassignment. This is exactly why they were never onboarded.

---

## Tier 1 — CLEAR (direct-synonym registry exists; propose to onboard as-is)

| Strong | Gloss | → Registry | Cluster hint |
|---|---|---|---|
| H0444 | to corrupt | **corruption** | M10 |
| H0536 | weak | **weakness** | M24 |
| H1161 | terror | **terror** | M01 |
| H1249 | pure | **purity** | M12 |
| H1252 | cleanness | **purity** | M12 |
| H1305 | to purify | **purity** | M12 |
| H2135 | to clean | **purity** | M12 |
| H1793 | contrite | **contrition** | M11 |
| H2186 | to reject | **rejection** | M06 |
| H3988 | to reject | **rejection** | M06 |
| H2427 | agony | **agony** | M03 |
| H2451 | wisdom | **wisdom** | M15 |
| H4784 | to rebel | **rebellion** | M30 |
| H6419 | to pray | **pray** | M21 |
| H8605 | prayer | **prayer** | M21 |
| H3970 | desire | **desire** | M29 |

*16 terms — recommend onboarding these under the named registry without further review.*

---

## Tier 2 — PROBABLE (one reasonable registry; minor judgement, flag if you disagree)

| Strong | Gloss | → Registry | Note |
|---|---|---|---|
| H5036 | foolish (nabal) | **foolishness** | M16 |
| H3684 | fool (kesil) | **foolishness** | M16 |
| H6612 | simple | **foolishness** | naïveté; could be its own sense |
| H7908 | bereavement | **mourning** | M03; vs sorrow/grief |
| H2342 | to writhe/tremble | **anguish** | M03; vs grief |
| H6277 | arrogant | **pride** | M08 |
| H7426 | be exalted | **pride** | M08; self-exaltation |
| H8217 | low | **humility** | M09 |
| H7646 | to satisfy | **contentment** | M46; vs "satisfaction" |
| H2489 | helpless | **weakness** | M24; vs vulnerability |
| H7326 | be poor | **weakness** | M24; vs vulnerability/humility |
| H3021 | be weary/toil | **weakness** | M24; vs suffering |
| H5848 | to faint | **weakness** | M24; vs despair |
| H6039 | affliction | **distress** | M24; vs weakness (Group A: home="gentleness"→ reassign) |
| H6199 | destitute | **weakness** | M24; vs vulnerability |
| H7723 | vanity/false | **deceit** | M14; vs "vanity"(none) |
| H3576 | to lie | **deceit** | M14 |
| H3577 | lie | **deceit** | M14 |
| H2665 | plot | **deceit** | M14; vs malice |
| H6141 | twisted | **perverseness** | M14 |
| H5003 | to commit adultery | **whoredom** | M10; vs "adultery"(none) |
| H7321 | to shout | **praise** | M22; joyful shout |
| H4066 | strife | **strife** | M02 |
| H2154 | evil (zimmah) | **evil** | Group B; vs malice/"purpose" |
| H7832 | to laugh/rejoice | **rejoicing** | Group B; vs joy/gladness |

*25 terms — a reasonable home each; confirm or redirect.*

---

## Tier 3 — UNCERTAIN (needs your call) — grouped by why

### 3.1 No registry exists for the concept → new REGISTER, or reassign

| Strong | Gloss | Cluster | Options |
|---|---|---|---|
| H3468 | salvation (yeshuʿah) | M38 | **No `salvation` registry.** New "salvation", or nearest existing (none close) |
| H4190 | salvation (moshaʿah) | M38 | same |
| H8668 | deliverance/salvation | M38 | same, or a "deliverance" registry |
| H5826 | to help | M38 | help→salvation? weak IB link; possibly exclude |
| H5046 | to tell (nagad) | M42 | **No `speech` registry.** New, or exclude as non-IB |
| H1747 | silence | M42 | new "silence", or map to peace/stillness? |
| H0981 | to speak rashly | M42 | rash speech; new, or "anger"/"folly"? |
| H0974 | to test/prove | M35 | **No `testing` registry.** `temptation` (diff sense)? new? |
| H5254 | to test/prove | M35 | same |
| H5359 | vengeance | M02 | **No `vengeance` registry.** anger / wrath / resentment? |
| H5360 | vengeance | M02 | same |
| H2555 | violence (chamas) | M27 | **No `violence` registry.** evil / wickedness / Ruthlessness? |
| H8496 | oppression | M27 | **No `oppression` registry.** evil / Ruthlessness? |
| H6231 | to oppress | M27 | same (Group A: home="?") |
| H5949 | wantonness (aliylah) | M27 | "deeds/wantonness" — evil? or non-IB? |

### 3.2 Ambiguous among 2–3 near-equal registries

| Strong | Gloss | Cluster | Competing registries |
|---|---|---|---|
| H5937 | to exult | M04 | joy / rejoicing / gladness |
| H5970 | to rejoice | M04 | joy / rejoicing / gladness |
| H6149 | to please | M04 | delight / gladness |
| H0835 | blessed (ʼashrê) | M39 | blessing / gladness / joy (happiness) |
| H2898 | goodness (tuwb) | M39/T2 | goodness / blessing (Group A: home="love"→ reassign) |
| H6165 | to long for | M29 | longing / yearning / desire |
| H8373 | to long for | M29 | longing / yearning / desire |
| H6770 | to thirst | M29 | craving / longing / appetite |
| H1214 | to cut off (covet) | M29 | covetousness / greed |
| H3368 | precious | M29 | worth / desire / delight |
| H3365 | be precious | M29 | worth / desire |
| H3642 | to pine | M03 | longing / yearning / grief |
| H8428 | to wound | M03 | grief / suffering / sorrow |
| H3887 | to mock (lutz) | M08 | contempt / scorn(none) / pride |
| H3932 | to mock (laʿag) | M08 | contempt / pride |
| H3933 | derision | M08 | contempt / pride |
| H7047 | derision | M08 | contempt / pride |
| H6962 | to loathe | M06 | hatred / contempt (Group A: home="distress"→ reassign) |
| H7853 | to oppose (satan) | M06 | strife / hatred |
| H5010 | to disown | M06 | rejection / contempt |
| H5641 | to hide | M20 | doubt / concealment(none) |
| H5800 | to leave/forsake | M20 | betrayal / abandonment(none) |
| H7279 | to grumble | M20 | doubt / discontent(none) |
| H5640 | to close | M20 | concealment / non-IB? |
| H7683 | to go astray | M30 | disobedience / error(none) |
| H7686 | to wander | M30 | disobedience / error(none) |
| H8582 | to go astray | M30 | disobedience / error(none) |
| H5341 | to watch/keep | M30 | obedience / diligence |
| H4148 | discipline (musar) | M15 | wisdom / instruction(none) |

### 3.3 Group A — surviving OWNER home looks wrong (reconcile vs reassign)

| Strong | Gloss | Current OWNER home | Proposed instead |
|---|---|---|---|
| H2898 | goodness | love | goodness / blessing |
| H3684 | fool | hope | foolishness |
| H5036 | foolish | heart | foolishness |
| H5949 | wantonness | shame | evil / non-IB |
| H6039 | affliction | gentleness | distress / weakness |
| H6962 | to loathe | distress | hatred |
| H7045 | curse | shame | **Cursing** (registry exists) |
| H8444 | outgoing | surrender | unclear — see 3.4 |

### 3.4 Possibly not inner-being (verify before onboarding at all)

| Strong | Gloss | Concern |
|---|---|---|
| H7854 | Satan/adversary | proper-noun/agent, not an inner state → maybe exclude |
| H7283 | to throng | crowd motion, no IB sense evident |
| H6323 | to distract | rare; sense unclear |
| H6601 | to open wide | entice/seduce? or physical? |
| H2556 | to leaven | metaphor only; IB sense thin |
| H7342 | broad | "broad heart" = arrogance? or physical |
| H2149 | vileness | wickedness? or physical |
| H2611 | profane | hypocrisy / impurity / defilement? |
| H3689 | loins/hope (kesel) | two senses (seat vs confidence); which onboards? |
| H8496 | oppression | (also 3.1) verify IB |

---

## Recommendation

1. **Onboard Tier 1 (16) now** under the named registries — no review needed.
2. **Confirm/redirect Tier 2 (25)** — I've named a home for each; a quick yes/redirect.
3. **Tier 3 (56) needs your decisions**, in this order of leverage:
   - **New registries?** Decide whether `salvation` (+ maybe `deliverance`), `speech`, `testing`, `vengeance`, `oppression`/`violence` should be **created as REGISTER words** (they're core IB concepts with no current home) or folded into an existing one.
   - **Ambiguous families** (joy/desire/grief/mockery/doubt/error) — pick the canonical registry per family; I'll apply it across the members.
   - **Group A reassignments** — approve moving the 8 off their wrong homes.
   - **Non-IB candidates** — approve exclusion of any that aren't inner-being (e.g. H7854 Satan, H7283 throng).

*Filed 2026-07-06. Full per-strong data reproducible via the probe. Nothing written to the DB by this document.*
