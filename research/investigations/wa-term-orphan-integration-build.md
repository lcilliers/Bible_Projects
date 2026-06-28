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

## 5. Decisions needed before bulk execution
1. **Unmapped cluster** for oppression (`yanah`,`lachats`) + violence (`chamas`) — M27 / M06 / new? *(lean: M27 Evil for violence; oppression M06 or M27.)*
2. **Owner-registry** — confirm "new registry word only where no existing concept fits" (step 0 lookup); OK to create new words (e.g. Violence, Oppression) as needed?
3. **ve-lexical method** — generate via the existing generator (`_apply_generate_ve_lexical_v2.py` / `build_ve_lexical_extract.py`) in the **legacy VE** form (to match existing rows like Lev 25:43), or the **reset lexical**? (Affects consistency.)
4. **Batch order** — propose by cluster, starting **M06 (cruelty+hatred: perek, miseo)** building on reg216, then M24 weariness (largest), etc. OK?

## 6. Decision log
| date | decision | status |
|---|---|---|
| 2026-06-28 | Integrate the curated IB-orphans as OWNER terms into existing clusters + full ve-lexical (researcher directive) | accepted; planning |
| 2026-06-28 | 39 curated orphans → cluster mapping (§1) | drafted; 36 clear, 3 unmapped |
| — | unmapped cluster · owner-registry · ve-lexical method · batch order (§5) | **PENDING** |
