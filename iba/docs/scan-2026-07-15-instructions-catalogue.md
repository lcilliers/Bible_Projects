# Re-scan A — Instructions, Catalogue, Tiers, Schema (2026-07-15)

> Raw findings from the re-scan requested by the researcher 2026-07-15, run against `Workflow/Instructions/`, `Workflow/Catalogue/`, `Workflow/Tiers/`, `Workflow/schema/` (highest-numbered version of each doc). Feeds the coverage map ([iba-configurator-coverage-v1-20260715.md](iba-configurator-coverage-v1-20260715.md) → v2).
>
> **This is source material, not config.** Nothing here is authored into the configurator yet. Filed so the scan survives the session.

## ★ What this scan found that A.9 did not name

The plan's A.9 index has 92 items. This scan surfaced **~22 configuration items A.9 never lists**, and **closed three gaps A.9 flagged as "still to pull"**.

### Closed — the plan said these were unpulled

| A.9 "still to pull" | now known |
|---|---|
| Workflow/Tiers/ — exact standing-question counts + VE/SYNTH inventory | **126 active questions**: T0:9 · T1:18 · T2:6 · T3:33 · T4:18 · T5:9 · T6:13 · T7:20. 16 soft-deleted from the original 189 (DROP: T1.8, T1.2.3, T2.8, T5.7, T6.6, T6.7). **VE-01..VE-17** inventory exists; disposition ∈ `Layer A \| SYNTH \| DROP`, all 189 dispositioned, nothing deferred. |
| versecontext `vc_status` R1–R4 rules | **R1** `is_relevant=0` → group_id NULL, is_anchor=0, is_related=0 · **R2** `is_anchor=1` → is_relevant=1, is_related=0, group_id NOT NULL · **R3** `is_related=1` → is_relevant=1, group_id references a group with ≥1 active anchor · **R4** every term must have ≥1 active anchor before Session B may proceed. `vc_status='vc_completed'`; the atomic unit of VC progress is the **term**. |
| registry-management vocabulary | `session_b_status` (6) · `verse_context_status` (3, **derived — never set directly**) · cluster status (4) · `term_owner_type` (OWNER\|XREF) · `mti_terms.status` active filter = `extracted`+`extracted_thin` (GR-DATA-001) · status notes `extracted_theological_anchor`, `phase2_enrichment` |

### New vocabularies A.9 does not list

`role_provenance` (read-2026 · read-2026-supersede) · `vc_status` · patch postures (NEW-ONLY \| REVISE-ONLY \| MIXED \| NO-CHANGE) · quality scores (sound \| weak \| wrong) · verdict classes (READY \| READY-WITH-DEBT \| NOT READY) · check classes (PRECONDITION \| READ-OUTPUT \| ANCHOR \| INFO) · gate outcomes (GREEN \| AMBER \| RED) · skip-list reasons (concrete maxim \| imagery \| title \| reward-outcome \| personified-action) · T2 split (T2-content \| T2-grammatical) · stem vocabulary (Qal simple \| Hiphil causative \| Piel factitive) · disposition (Layer A \| SYNTH \| DROP)

### New rule-sets A.9 does not list

I2b (link quality — a cleanup item, **not** an I2 violation) · D1/D2 (the I12 umbrella) · VC rules R1–R4 · re-run rules R1–R6 · API circuit-breaker · API self-verification · Gate-1 span-orphan audit · audit-clean (7 checks) · the anomaly test · the staged sequence 0–5 · readiness check groups §A–F

## Integrity invariants — the full set, with pre-read class

Source: `wa-db-integrity-definition-authoritative-v1-20260711.md`; classes from `wa-book-lexical-readiness-assessment-AUTHORITATIVE-v3`.

| ID | Constrains | Pre-read class |
|---|---|---|
| I1 Referential | every FK resolves; 0 dangling | PRECONDITION |
| I2 Master-index coverage | every candidate `(verse, base-Strong's)` has ≥1 active `wa_verse_records`; **one row per term-in-verse, not per occurrence** | PRECONDITION |
| I2b Link quality | active record should carry a valid `verse_span_id` — **a cleanup item, NOT an I2 violation** | tracking |
| I3 Traceability | bidirectional: char→span→verse; verse→passage; passage→verses; verse→passage→lexical. **Never text-scan** | PRECONDITION |
| I4 Passage membership **(v2 strengthened)** | **EVERY verse of the book** has `passage_id` OR is skip-listed — not only candidate-verses | PRECONDITION |
| I4b Read completeness | verse-record verse with a `char_candidate` span but no lexical = 0 | READ-OUTPUT |
| I5 Ledger completeness | full genre-mandatory ledger; `none` explicitly written, never omitted; ZERO-dim = none | READ-OUTPUT |
| I6 Role screen | role stamped with provenance; **no characteristic span has God as bearer (105)**. "Unroled candidates = 0" **withdrawn** as a pre-read requirement | INFO pre-read |
| I7 Char-model linkage | `verse_span_index.ib_char_id` → `ib_characteristic`; enforceable as of M66 | READ-OUTPUT |
| I8 Soft-delete consistency | no active row on a soft-deleted parent; pair endpoints reference live spans | PRECONDITION |
| I9 Provenance | `role_provenance`, `ve_lexical.source_provenance`, `verse.process_marker` present + consistent | PRECONDITION |
| I10 Candidate flag | **directional**: every `role=characteristic` was a candidate. The converse does NOT hold | INFO |
| I11 Char-on-master | `verse_span_index.characteristic` populated from ve_lexical sense 101 | READ-OUTPUT |
| I12 Role–lexical coherence | umbrella for D1 + D2 | PRECONDITION |
| D1 Role backfill | active `ve_lexical` AND `role IS NULL` = 0 — backfill role **from** the lexical | PRECONDITION |
| D2 Lexical only on characteristics | active `ve_lexical` AND `role <> 'characteristic'` = 0 | PRECONDITION |
| I13 mti-uniqueness | at most **one active row per `strongs_number`**; duplicates `delete_flagged` | PRECONDITION |

**Rules of use:** "integrity-clean" = **ALL of I1–I13 pass**. A subset (I5+I6) is *ledger-clean*, **not** integrity. Book-close requires I1–I11. **Report violations with counts, never a bare "clean."**

**I13 reconcile ranking:** order by `(owning_registry_fk IS NOT NULL, status<>'delete', active_verse_record_count)` desc, keep top, flag rest — **never flag a row holding verse-records**.

## Gates and pass conditions

| Gate | Pass condition |
|---|---|
| **Verse-coverage (v2, MANDATORY)** | `verses-in-passages + explicit-skip-verses = book verse total`. Any non-skip-listed `passage_id IS NULL` = **HOLE, blocks the read** |
| **V1 value-domain** | controlled dims (`locus`/`direction`/`role`/`device`) hold in-vocabulary values |
| **V2 vocabulary drift** | controlled dims must not track chapter position. **`type` drift = RED**; other drift = AMBER |
| **V3 tag consistency** | identical `(lemma, operation)` readings must not get contradictory `direction` |
| **Gate 1 span-orphan audit** | diff full `verse_span_index` vs seed **BEFORE** any span-depth read. **Step 1, not a post-hoc check** |
| **Passage integrity invariant** | every `char_candidate` master span MUST have an active `wa_verse_records` — a violation, **not** a coverage choice |
| **API circuit-breaker** | round time > `N×` running mean or an absolute ceiling → **immediate STOP**; partial saved, resumable |
| **API self-verification** | `submitted = applied + NONE + no-row` — reconcile exactly, **no silent drops** |
| **Anomaly test** | genuine anomaly = `live_owner_count=0` AND `live_xref_count=0`. `owner=0, xref>0` = pure XREF, **requires no action** |

## Success measures G0–G10

Defined in `scripts/_check_reread_measures_v3_20260709.py`.

G0 digestion budget (unit-model-aware) · G1 nothing passed over · G2 worked-not-named · G3 grounding = pairs only · G4 distinctions preserved · G5 belonging honoured · G6 unexpected surfaced · G7 honest uncertainty (row present **AND value non-empty**) · **G8 — NOT EMITTED by the v3 runner** · G9 pair & qualifier integrity (keyed on span-ids) · G10 completeness ledger (genre-aware).

## Numeric thresholds and cadences

| Rule | Value |
|---|---|
| Cycle size | **~12 passages**, then stop |
| DB write cadence | **after EACH passage** — non-negotiable, never batched to cycle end |
| Quality sample | **2–3 passages** per cycle |
| Quality bar | **≥90% sound, ZERO fidelity failures**. A missed pair on a `none`-call **is** a fidelity failure |
| `ib_characteristic` full rebuild | every **~5 cycles** + at book-close |
| Integrity-gated snapshot | every **N cycles, default 5** |
| Git commit | per cycle |
| Cluster size | max **~10 words** |
| M16 mandatory ledger | 101,102,104,105,106,107,108,**109,110,111**,112,114,115,116,**117,118** |

## Staged dependency sequence

| Stage | Action | Gate to advance |
|---|---|---|
| 0 | Seed — `char_candidate` stamped corpus-wide | seed present |
| 1 | Registry + term — every candidate's word registered (existing-registry-first) | 0 candidate base-Strong's missing from `mti_terms` |
| 2 | Verse-record — every candidate `(verse, term)` has active `wa_verse_records` | I2 = 0 uncovered |
| 3 | Passages — candidate-driven v2, whole book | I4 = 0; 0 candidate-verses unpassaged; + verse-coverage gate |
| 4 | Lexical read — role assign; `ve_lexical` for characteristics only | *(out of readiness scope)* |
| 5 | Integrity — I1–I11 + D1 + D2 pass | book-close acceptance |

**Readiness = stages 0–3 green.** This maps almost exactly onto the researcher's stage chain (registry → raw → base → [signoff] → lexical): **stages 0–3 ARE base, and "readiness" IS the base signoff.** Two independent derivations of the same boundary.

## ⚠ Conflicts and gaps the scan surfaced

1. **`role` enum conflict — NEW EVIDENCE for `recon.role-enum`.** `db-integrity-authoritative-v1` (**2026-07-12**) and `book-readiness-v3` say `characteristic \| qualifier \| standalone \| undecided`. `ve-lexical-catalogue-v1 §8` (**2026-07-02**) says `characteristic \| process-qualifier \| standalone \| uncertain`. The later doc probably wins — **but `process-qualifier` still appears in book-readiness §2.1 as "a qualifier sub-form", so it may be a SUB-VALUE rather than a peer.** That possibility is not in the reconciliation's current variant list and changes the answer: if it is a sub-form, the alias map is right; if it is a peer, it is not.
2. **G8 is absent** from the v3 measures runner while G0–G7, G9, G10 all emit. The docs only ever cite "G0–G10" as a range. Retired, or dropped silently? A measure nobody can name the absence of is the "scan gate silently non-operational" pattern.
3. **Two thresholds exist only in code, not in any doc**: the G0 digestion budget (a `BUDGET` const in the script) and the §C candidate:total "plausible band for the genre" (**band undefined**). Both must be configured, and one of them currently has no value at all.
4. **"integrity-clean" is defined three times with drifting ranges** (I1–I11, I1–I12, I1–I13) as amendments landed. The live definition is **I1–I13**. `I12` is itself cited two ways — as its own invariant and as the D1+D2 umbrella.
5. **Tiers VE/SYNTH is approved-in-principle but the DB is unchanged.** T0–T7 (126 questions) is the current state. **A configurator should model BOTH and gate the switchover** — not silently pick one.

## Disposition — where these land

Everything here is source material for:

- `wide/enums.json` — the 12 new vocabularies + the status/flag sets
- `wide/db-governance.json` *(pending)* — I1–I13 + D1/D2, the classes, the rules-of-use, the I13 ranking
- `process/base.json` — the staged sequence 0–3, readiness groups §A–F, verdict classes, verse-coverage gate, skip-list reasons, Gate-1 span-orphan
- `process/lexical.json` — V1/V2/V3, G0–G10, the M16 ledger, the quality bar
- `wide/settings.json` *(pending)* — every cadence and threshold
- `utility/api.json` *(pending)* — circuit-breaker, self-verification
- `wide/reconciliations.json` — items 1–5 above
