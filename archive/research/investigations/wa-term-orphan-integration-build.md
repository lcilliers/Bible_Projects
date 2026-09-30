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

## 1c. Newly discovered during fan-out (additions to the backlog)
Orphans surfaced by the verse-fanout method *after* the original audit — same treatment (onboard as OWNER into the target cluster, reset ve-lexical). The fan-out is now an active orphan-discovery channel (per `feedback_term_coverage_cascade_is_index_not_census`).

| term | strong | gloss | target cluster | IB occurrences | note |
|---|---|---|---|---|---|
| `a.qov` | **H6121A** | insidious / sly / deceitful | **M14 Deceit** | Hos 6:8 + Jer 17:9 (the *insidious* sense) | ✅ **ONBOARDED 2026-06-29** — OWNER reg217 "Slyness", status=extracted. Integrity: exactly +1 term, +2 verses, +1 registry, M14+1, no new breach. The physical "steep" sense (H6121B, Isa 40:4) correctly **excluded**. Found via Jer 17:9 fan-out (Exo 1:13 #109). |
| `oqvah` | **H6122** | cunning / craftiness | **M14 Deceit** | 2Ki 10:19 (Jehu's ruse) | ✅ **ONBOARDED 2026-06-29** — same OWNER reg217 "Slyness" (the sly/cunning root family). Integrity: +1 term, +1 verse, M14+1, no new breach. Sibling of `a.qov` (same `aqv` root); researcher: pull the cunning word through too. |
| `anash` | **H0605** | be incurable / sick / frail | **M24** *(flagged — M27 alt)* | 9 verses (Jer 17:9 + 8 incurable-wound/grief) | ✅ **ONBOARDED 2026-06-29** — OWNER reg218 "Incurability". Integrity: +1 term, +9 verses, +1 reg, M24+1, no new breach. Found via Jer 17:9 fan-out — the heart "desperately sick/incurable." Cluster M24 (lemma=incurable sickness/frailty); flag to redirect to M27 if the "desperately wicked" reading is preferred. Obs #110 (ruthlessness ground) + #111 (heart twofold diagnosis). |
| `arar` | **H0779** | to curse | **CLUSTER TBD** | 52 verses | ✅ **ONBOARDED 2026-06-29** — OWNER reg219 "Cursing". Integrity: +1 term, +52 verses, +1 reg, no new breach. Researcher: keep it (excluding curse ⇒ excluding blessing — a pair); **investigate deeper later** → cluster deferred (NULL, vc_status_note flags it). `me'erah` H3994 (curse-noun, role-noun) + Ararat H0780 (place) excluded. Found via Gen 49:7 fan-out (#43). |
| `ebrah` | **H5678** | fury / wrath / overflow | (M02 expected) | 30 verses | ⛔ **NOT onboarded — FLAGGED.** Not a new orphan: already in mti **delete-flagged** (`status='delete'`) under reg4/reg126/**reg178 "wrath"**. It was *deliberately deleted* (pre-RESET curation). Reactivating reverses that decision → **researcher call needed**: reactivate in reg178 (set delete_flagged=0, status, cluster M02) or leave? *(Lesson: check mti for delete-flagged existing rows before onboarding — not every "untracked" term is absent.)* |

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

## 7. Integrity anchors & controls (researcher priority)
Built the reusable anchor `scripts/_check_integrity_controls.py` (READ-ONLY): **snapshot** control totals + invariants → json; **compare** two snapshots → exact deltas. Run before/after every batch so we see *only* the expected change.
- **Control totals (anchors):** active counts per key table (mti, inventory owner/xref, verse_records, verse_context, ve_lexical, verse, span_index, registry) + **per-cluster member counts** (so we see which cluster grew).
- **Invariants (must stay 0):** duplicate OWNER per Strong's · verse_records orphan term_inv/book · verse_context orphan mti/verse_record · ve_lexical orphan verse_context.
- **Baseline (`snap-pre-perek`, 2026-06-28):** invariants CLEAN except **`dup_owner_strong=1` → `G0150`** — a **pre-existing** breach (OT-DBR-009), not from this build. Control = perek must **not increase** it.
- **Per-batch gate:** backup → snapshot pre → write → snapshot post → `--compare` (deltas == predicted, no new invariant breach, study tables untouched, coverage layer unchanged) → else rollback.
- **Reversibility:** DB backup per batch + documented per-term rollback (delete the term's rows across mti/inventory/verse_records/verse_context/ve_lexical).

## 8. Onboarding mechanics — use the engine, NOT a hand-script (template finding)
Inspected the template (`arits` H6184, M06 owner): dual `mti_terms` rows, owner+xref `wa_term_inventory`, `wa_file_index` stub, `word_registry_fk`, 40 verse_records, 20 verse_context, 226 ve_lexical. **Hand-scripting perek to match this legacy wiring risks an inconsistent/contaminating record.** → Onboard via the **canonical engine path** (`--register` done for reg216; `audit_word` creates the consistent record incl. file_index stub).
- **Batch 1 scope is naturally just `perek`:** the other reg216 cruelty terms (`arits`, `akzar`*, `aneleemon`) **already exist** (owned elsewhere) → they become **XREF** to reg216, not new owners. So reg216's only NEW owner = `perek`.
- **Open mechanic to confirm before the write:** `audit_word --registry=216` needs a Step-1 JSON extract containing `perek`; the discovery `term_map` is a different format. Resolve the extract path (build the Step-1 extract, or the minimal controlled insert that exactly replicates the template), then: backup → dry-run → snapshot/compare → live.

## 6. Decision log
| date | decision | status |
|---|---|---|
| 2026-06-28 | Integrate curated IB-orphans as OWNER terms into existing clusters + full (reset) ve-lexical | accepted |
| 2026-06-28 | 61 terms (39 primaries + 22 kin) → cluster mapping (§1, §1b) | done |
| 2026-06-28 | Unmapped → **M27**; owner-reg = new-only-if-needed; ve-lexical = **reset/v2 engine**; **M06 first**; **include borderline** | RESOLVED |
| 2026-06-28 | **PEREK PILOT — term layer DONE + verified.** Onboarded via engine audit_word (reg216); set status=extracted, cluster=M06, owner_type=OWNER. Controls: exactly +1 term, +1 owner, +6 verses, M06 +1, **no new invariant breach, no contamination**. | ✅ |
| 2026-06-28 | **Two engine onboarding bugs FIXED en route** (the recurring trip-up): (a) `audit_word --fetch-step` now auto-generates the Step-1 extract from STEP; (b) the file_index stub INSERT was missing NOT NULL `filename` → fixed. New-word onboarding now works end-to-end. | ✅ |
| 2026-06-28 | Triage gate proven: auto-fetch include_codes had `H6531`+`H6532` (curtain homonym) → curated to perek-only before live write (prevented contamination). | ✅ |
| — | **NEXT for perek:** verse_context units for its 6 verses → reset ve-lexical (mechanical `_apply_generate_ve_lexical_v2`) → link M06 char Cruelty/Ruthlessness. Then scale batch 1 to `miseo` + M06 kin. | pending |
| 2026-06-29 | **`a.qov` H6121A ONBOARDED** — OWNER reg217 "Slyness", M14 Deceit, status=extracted, 2 verses (Hos 6:8, Jer 17:9). Integrity compare = exactly +1 term/+2 verses/+1 reg/M14+1, no new breach. (term layer; verse_context + reset ve-lexical pending, as for perek.) | ✅ |
| 2026-06-29 | **`arar` H0779 (to curse) ONBOARDED** — researcher: keep curse (curse/blessing pair); investigate deeper later. OWNER reg219 "Cursing", **cluster TBD/deferred**, 52 verses. Integrity: +1 term/+52 verses/+1 reg, no new breach. |  ✅ |
| 2026-06-29 | **`ebrah` H5678 (fury) FLAGGED, not onboarded** — already in mti **delete-flagged** under reg178 "wrath" (deliberate pre-RESET deletion). Reactivation reverses that decision → researcher call. **New pre-onboard check added:** verify mti for existing delete-flagged rows before treating an "untracked" term as absent. | ⏸ pending researcher |
| 2026-06-29 | **VE-LEXICAL GAP found (researcher Q):** onboarded terms have verse_records but **0 verse_context / 0 ve_lexical** (perek 6v, a.qov/oqvah 3v, anash 9v, +arar 52v). Onboarding has been term+verses only. **Catch-up needed:** verse_context units → reset `_apply_generate_ve_lexical_v2`; make ve-lexical a standing part of the onboarding recipe. | ⏸ proposed |
| 2026-06-29 | **CONTROLS FIX (researcher: "why are the controls not working?")** — the integrity controls were **orphan-only** (FK dangling-child checks); they never tested **field-hygiene** or **completeness**, so an onboarded-but-incomplete term passed clean. Added to `_check_integrity_controls.py`: hygiene invariants `mti_delete_flag_null`/`inv_delete_flag_null` (must be 0) + a **COMPLETENESS** section `active_term_verses_no_vc` / `vc_active_no_velex` (surfaced). First run exposed **163 active terms with verses but no verse_context** and **2583 verse_context with no ve_lexical** (largely T2 particles + legacy) — previously invisible. | ✅ |
| 2026-06-29 | **Control now catches OUT-OF-CORPUS verse_records** (researcher: "must pick up if 2Sa 12:15 re-occurs"). Added `vr_out_of_corpus` = active verse_records whose reference has no row in `verse` (the index, ~76% of canon). **Currently 4** (anash 2Sa 12:15; arar Deu 28:17/28:18/Gen 9:25) — STEP full-Bible occurrences landing outside the corpus. **Def:** out-of-corpus = not in `verse` → no spans/measure layer → unanalysable. Also added the missing indexes (`verse.reference`, vr/vc/velex join cols) → snapshot now runs in **~1.6s** (was 30s+), so it's cheap to gate every write. | ✅ |
| 2026-06-29 | **`arar` → M06 (Hate)** (researcher) — cluster set; verse_context created for its **49 in-corpus** verses (3 out-of-corpus skipped) + ve_lexical generated (**49 units / 476 rows**). arar now fully complete (term+verses+VC+velex). | ✅ |
| 2026-06-29 | **`anash` 2Sa 12:15 = corpus-coverage gap, not a build error.** It's in the STEP json (full-Bible) but **outside the study's verse index** (canonical `verse` = 23,593 ≈ 76% of canon; 2 Sam 12 holds 25/31 verses). No canonical row / spans / measure layer → no ve-lexical possible. Its verse_record remains as a pointer; the premature VC was removed. **Onboard catch-up now creates VC only for IN-CORPUS verses.** Open: whether to add such verses to the corpus (researcher). | ✅ noted |
| 2026-06-29 | **Completeness control made T2-aware** (researcher: T2 only gets ve-lexical when in a verse with tracked terms). `vc_no_velex` split into **`vc_no_velex_clustered`** (actionable: non-T2, non-NULL IB-term VC missing velex) + `vc_no_velex_all` (raw context). | ✅ |
| 2026-06-29 | **VE-LEXICAL CATCH-UP done (clustered onboarded terms).** Created verse_context (`_apply_create_vc_for_onboarded.py`) + ran reset `_apply_generate_ve_lexical_v2` for perek/a.qov/oqvah/anash → **17 units, 185 ve_lexical rows**. `active_term_verses_no_vc` 167→163. **arar deferred** (generator scopes to `cluster_code IS NOT NULL`; its 52 premature VC removed — VC+velex wait for its cluster decision). **anash 2Sa 12:15 blocked** — that verse is **missing from the canonical `verse` table** (separate gap to investigate). | ✅ |
| 2026-06-29 | **`delete_flagged` NULL swept** — engine onboarding leaves `mti_terms.delete_flagged=NULL`; queries filtering `=0` silently exclude the term. Found 11 NULL (perek reg216 + 10 reg215/M46 wealth terms, all engine-onboarded) → set all to 0. Now a confirmed finishing-field for every onboarding. | ✅ |
| 2026-06-29 | **`anash` H0605 (incurable/desperately-sick) ONBOARDED** — researcher: the heart "desperately sick" is a rich, remarkable state worth capturing. OWNER reg218 "Incurability", **M24** (flagged; M27 alt for "desperately wicked"), 9 verses. Integrity: +1 term/+9 verses/+1 reg/M24+1, no new breach. Obs #110 (Exo 1:13 ruthlessness ground) + #111 (heart twofold diagnosis). **Jer 17:9 now 0 coverage gaps.** | ✅ |
| 2026-06-29 | **`oqvah` H6122 (cunning) ONBOARDED** — researcher: pull the cunning sibling through too. OWNER reg217 "Slyness" (now holds the sly/cunning `aqv` root family: a.qov insidious + oqvah cunning), M14 Deceit, 2Ki 10:19. Integrity: +1 term/+1 verse/M14+1, no new breach. a.qov untouched. | ✅ |
| 2026-06-29 | **Curation mechanism CLARIFIED (the recurring trip-up).** `audit_word` onboards from the extract's **`terms` array**, NOT `meta.include_codes` (include_codes only steers the gap report). `--fetch-step` fetches *and* ingests in one pass → relatedNos cascade onboards immediately (a.qov pulled the whole H6117-H6122 heel/footprint family). **Correct gate:** `word_study_extract` → **trim the `terms` array to the wanted code(s)** → `audit_word --extract-file`. Rolled back twice before getting this right; backup+snapshot+compare caught it both times. | ✅ |

## 9. Perek pilot — outcome (the validated template)
The end-to-end controlled path that now works for every term:
1. `audit_word --registry=N --fetch-step --anchors <codes>` → STEP extract auto-generated.
2. **Curate** the extract include_codes (drop relatedNos homonyms — e.g. curtain). *(integrity gate)*
3. Live `audit_word --registry=N` → onboards term + verses (creates file_index stub, mti, inventory, verse_records).
4. Set finishing fields: `mti_terms.status='extracted'`, `cluster_code=<M>`, `wa_term_inventory.term_owner_type='OWNER'`.
5. verse_context units → `_apply_generate_ve_lexical_v2.py` (reset ve-lexical, mechanical).
6. **Control gate each step:** `_check_integrity_controls.py --snapshot` pre/post + `--compare` → deltas == predicted, no new invariant breach, else rollback from backup.

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