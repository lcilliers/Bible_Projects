# Term-orphan integration build — bring the ~39 IB-orphans into the study (LIVING)

> **Doc version:** 1 · **Last updated:** 2026-06-28 · **living build doc** (update in place; decision log at §6). Subsumes the reg216/`perek` build (perek is one of these 39). Source of the orphans: the coverage audit in `wa-term-coverage-method-integrity.md`.
>
> **Researcher directive (2026-06-28):** pull the ~45 (curated to 39) term-orphans from STEP **with their verses**, **integrate into existing clusters**, do a **full ve-lexical for each verse**; **all become OWNER terms.**
>
> **Status:** ⏸ PLAN — confirm §5 decisions before bulk execution. Nothing pulled yet.

## 1. The 39 curated IB-orphans → target existing cluster
| cluster | n | terms (Strong's · concept · corpus verses) |
|---|---|---|
| **M06 Hate** | 9 | `miseo` G3404 hatred(27) · `perek` H6531 cruelty(6) · `laag` H3932 mock(13) · `empaizo` G1702 mock(8) · `qalas` H7046 scorn(3) · H3933 mock(5) · `gaal` H1602 abhor(8) · G0655 abhor(1) · `mukterizo` G3456 mock(0*) |
| **M24 Weakness** | 9 | `yaga` H3021 weary(24) · `ataph` H5848 faint(13) · `ayeph` H5889 weary(12) · H3543 faint(7) · `kahah` H3544 faint(7) · H5888 faint(4) · `dalal` H1809 weary(7) · `ekkakeo` G1590 fainthearted(4) · `kamno` G2577 weary(2) |
| **M05 Love** | 3 | `rak` H7390 tender(15) · `rakak` H7401 tender(8) · `feidomai` G5339 spare/pity(6) |
| **M16 Folly** | 3 | `anoetos` G0453 foolish(6) · `mataiotes` G3153 futility(3) · `akatastatos` G0182 unstable(2) |
| **M02 Anger** | 3 | `ragaz` H7283 rage(1) · `embrimaomai` G5433 rage(1) · `chalepos` G5467 fierce(1) |
| **M30 Obedience** | 2 | H6203 stiff-necked(24) · `sarar` H5637 rebellious(15) |
| **M08 Pride** | 2 | H6277 arrogant(4) · H3093 haughty(2) |
| **M03 Grief** | 2 | `nud` H5110 grieve/sympathy(22) · `laanah` H3939 bitter/wormwood(8) |
| **M14 Deceit** | 2 | `kubeia` G2940 cunning(0*) · `phrenapatao` G5422 self-deceive(0*) |
| **M01 Fear** | 1 | `raash` H7493 tremble/quake(28) |
| **? UNMAPPED** | 3 | `yanah` H3238 oppress(17) · `lachats` H3905 oppress(12) · `chamas` H2555 violence(54) |

*0 corpus verses = appears only in coverage/missing verses (Gal/Eph) — needs its own verse pull.

## 1b. Related-term clusters serviced (the family — researcher: "STEP services the terms")
Servicing each of the 39 primaries' STEP related clusters surfaced **62 further terms**. Triaged — **include the IB-kin, exclude homonym/proper-noun noise** (the leaky-relatedNos finding in action):

**INCLUDE — genuine IB-kin (~19), added to the integration set by cluster:**
- **M06 Hate:** `G1701` jeering · `G1703` a mocker · `H3934` mocking · `H7047`/`H7048` derision · `H1604` loathing · `G4767` hated
- **M24 Weakness:** `H3018`/`H3022` toil · `H3023` weary · `H3024` weariness · `G1587` to fail
- **M05 Love:** `H7391` tenderness (noun) · `G0857` unsparing · `G5340` sparingly
- **M16 Folly:** `G0181` disorder · `G3152` futile
- **M02 Anger:** `G1031` to gnash
- **M01 Fear:** `H7494` quaking
- **M30 Obedience:** `H5620` stubborn
- **Violence (unmapped):** `H2554` to injure  ·  **Oppression (unmapped):** `H3906` oppression (noun)

**EXCLUDE — noise (~37):** proper nouns (Delilah, Orpah, Goah, Nod, Yob, Joha, Ladan, the Ir-/City-of-Salt names…) and homonyms/concrete (`H6532` curtain via perek, `H8464` ostrich via chamas, `H2022` mountain, `H3938` to eat, `H5638` winter, `H1803` hair, `H4595` overtunic, `H5067` heap…). These are the relatedNos leaks — do not pull.

**BORDERLINE (researcher decide):** `H6202` to break-the-neck (kin to stiff-necked H6203?) · `H1800` poor · `H5112` wandering (via `nud` grief) · `H4816` weakness · `G0413` inexhaustible / `G3089` to loose (via `ekkakeo`).

→ **Integration set now ≈ 39 primaries + ~19 kin ≈ 58 terms** (plus borderlines if confirmed). The pipeline (§4) applies to all; servicing-then-triage is the rule, not primaries-only.

## 2. The 3 unmapped — need a cluster decision (§5.1)
No dedicated **oppression** or **violence** cluster exists. Options: (a) **M27 Evil** (violence/oppression as wickedness); (b) **M06 Hate** (the cruelty/hostility neighbour); (c) **M24 Weakness** (the *suffering* side — but these are the *act*, not the state); (d) **new cluster(s)**. *(My lean: `chamas` violence + `yanah`/`lachats` oppress are the *acts* of harm → M27 Evil or M06; not M24. Decide.)*

## 3. Owner-registry approach (§5.2)
Every term needs an `owning_registry_fk` (lexical home). Two routes per term:
- attach as OWNER under an **existing registry word** whose concept matches (e.g. weariness terms under a fatigue/weakness registry if one exists), OR
- **create a new registry word** where no existing concept fits (cruelty → `reg216 Ruthlessness` already done; likely new: Violence, Oppression; possibly Weariness, Mockery, Tenderness, Arrogance if absent).
**Execution step 0** = look up, per orphan, whether a matching registry word exists; new word only where absent. *(Surfaces the registry-completeness picture as a by-product.)*

## 4. Per-term pipeline (the full integration, per researcher)
1. **STEP pull** — `get_vocab_info` + `get_verse_records` (the term's verses, whole-corpus).
2. **Owner term** — `mti_terms` (OWNER, status extracted, `cluster_code` = target M-cluster) + `wa_term_inventory` (OWNER) + file_index stub.
3. **Cluster assign** — into the existing characteristic (e.g. perek/miseo → M06 char Cruelty/Ruthlessness & Hatred).
4. **Verses** — `wa_verse_records` + `verse` link + `verse_context` per verse.
5. **Full ve-lexical per verse** — generate the normalised lexical values (method = §5.3).
6. **Verify** — structural-completeness check per term (researcher step e).

## 5. Decisions — RESOLVED (researcher, 2026-06-28)
1. **Unmapped cluster** — oppression (`yanah`,`lachats`) + violence (`chamas`) → **M27 Evil.** ✓
2. **Owner-registry** — **new registry word only where no existing concept fits** (per-term step-0 lookup); create new words (e.g. Violence, Oppression) as needed. ✓
3. **ve-lexical method** — **RESET** = the v2 engine generator (`_apply_generate_ve_lexical_v2.py`, `source_provenance='v2_engine_iter1'`, incl. the RESET fields ve_nr 23-29). ✓ **Mechanical, not hand-analysis.**
4. **Batch order** — no preference → proceed cluster-by-cluster, **M06 first**. ✓ **Include the borderline kin** (rather include than exclude). ✓

## 5a. Scale + the de-risking finding
- **Integration set = 61 terms** (39 primaries + 22 kin incl. borderline) across **440 distinct corpus verses**; 5 terms have 0 corpus verses (need a STEP verse pull).
- **The reset ve-lexical is generated MECHANICALLY** by `_apply_generate_ve_lexical_v2.py` over the measure layer (verse_morphology + lexicon). So once a term's verses + morphology + verse_context units exist, the lexical is an **engine run** — the 440 verses are not a manual campaign.

## 5b. Refined per-term pipeline (mostly scriptable)
1. STEP pull (`get_vocab_info` + `get_verse_records`).
2. **Owner registry** — step-0 lookup; attach to existing registry word, or create a new one (Decision 2).
3. **Owner term** — `mti_terms` OWNER (cluster_code = target M-cluster) + `wa_term_inventory` + file_index stub (engine `--register`/`audit_word`).
4. **Cluster assign** — into the existing characteristic.
5. **Verses** — `wa_verse_records` + `verse` link + `verse_context` units. (Most verses already in corpus; the 5 zero-verse terms + any new verses need morphology ingest via `getBibleText`.)
6. **Reset ve-lexical** — run `_apply_generate_ve_lexical_v2.py` (mechanical).
7. **Verify** — structural-completeness check (researcher step e).

## 6. Decision log
| date | decision | status |
|---|---|---|
| 2026-06-28 | Integrate curated IB-orphans as OWNER terms into existing clusters + full (reset) ve-lexical | accepted |
| 2026-06-28 | 61 terms (39 primaries + 22 kin) → cluster mapping (§1, §1b) | done |
| 2026-06-28 | Unmapped → **M27**; owner-reg = new-only-if-needed; ve-lexical = **reset/v2 engine**; **M06 first**; **include borderline** | RESOLVED |
| — | **NEXT:** execute batch 1 = M06 (perek + miseo + mockery/abhorrence kin) — single-term pilot (perek) end-to-end first, with backup + dry-run | pending go |

researcher comments

addtional research

cha.mas (חָמַס H2554) 8 x to injure  
cha.mas (חָמָס H2555) 60 x violence  
cha.mats (חָמַץ H2556*) 8 x - to leaven (3 forms)
cha.mash (חָמַשׁ H2567) 1 x to take the fifth part  


a.nah (אֲנָה H0576*) etc. 1248 x - me (4 forms)
a.nah (אָנָה H0578) 2 x to lament  
a.nah (אָנָה H0579) 4 x to meet  
a.nach (אָנַח H0584) 13 x to sigh  
ya.nah (יָנָה H3238) 20 x to oppress  
ya.a.nah (יַעֲנָה H3284) 8 x ostrich  
na.ah (נָאָה H4998) 3 x be lovely  
a.nah (עָנָה H6030*) etc. 362 x - to answer (4 forms)
a.nah (עָנָה H6031*) 83 x - to afflict (3 forms)

la.chats (לָחַץ H3905) 19 x to oppress  
la.chats (לַ֫חַץ H3906) 12 x oppression  