# Configurator coverage — the A.9/C inventory against the framework (v1)

> **What this is.** The plan's **Appendix A.9** (the living index of configuration nodes) and **Appendix C.1–C.14** (the content inventory collated from three deep scans) say: *"Every item below must find a home in the configurator."* This maps all 92 inventory items against the framework built 2026-07-15, states where each is homed, and where the gaps are.
>
> Authority: researcher request 2026-07-15. Config state: `config_version` 0.1.3, 250 items, VALID. Method: programmatic — each inventory item checked against the live config by rule id, not by recollection.

## 1. Headline

| | count | |
|---|---:|---|
| Inventory items (A.9 + C) | **92** | |
| **HOMED** — authored in the config now | **43** | 46% |
| **GAP — home exists, file not authored yet** | **44** | 48% |
| **GAP — NO HOME ANYWHERE** | **5** | 5% |

**The framework accounts for 87 of 92 items by design.** Most gaps are not design holes — they are the eight Tier A/utility files still marked `pending`, plus additions to five authored files. **Five items have no home at all**, and they are not a random residue: see §4.

## 2. Coverage by group

| group | homed | gap | note |
|---|---:|---:|---|
| Dimensions | 3 | 0 | complete — `process/lexical.json` |
| Ledgers | 1 | 0 | `lexical.ledger` (RECONCILE) |
| Registers | 5 | 0 | complete — reconciliations + `cfg_*` entities |
| Pipeline | 9 | 2 | modules/order/deps/gates all homed |
| Characteristics/seed/registry | 3 | 1 | |
| Screen & role | 4 | 1 | |
| Gates | 5 | 6 | the measure families (V1/V2/V3, G0–G10, drift) unhomed |
| Provenance | 3 | 3 | |
| Read-quality | 3 | 4 | |
| Controls | 1 | 2 | |
| Vocabularies/enums | 1 | 2 | the 11 lexical enums homed; status + flag sets not |
| Principles | 2 | 5 | |
| Settings | 1 | 6 | |
| Naming/filing | 2 | 8 | |
| **Governance** | **0** | **4** | ⚠ entirely unhomed |
| **Study end-point** | **0** | **5** | ⚠ entirely unhomed — **and no file is planned** |

## 3. Every gap, and where it belongs

**44 gaps land in files the framework already names.** Nothing needs inventing:

| destination | state | absorbs |
|---|---|---|
| `wide/settings.json` | pending | model tier + escalation · budget/cost caps · DB path · backup/retention/NAS · engine constants/thresholds · cadences · digestion budget |
| `wide/principles.json` | pending | the nine principles · focus-point model · convergence-validity · multi-contributor spiderweb · behaviour guardrails · LRT · read-back/self-check |
| `wide/patterns.json` | pending | file-naming patterns (23) · label patterns (11) · versioning rules · output formats · patch-type registry + operations |
| `wide/governance.json` | pending | GR-* rules · FLAG-* flags · interaction protocols · directive spec · two-and-only-two change mechanisms |
| `wide/db-governance.json` | pending | STATED/INFERRED · soft-delete discipline · field-authority · cross-DB old-ref map · process-control policy |
| `wide/enums.json` | authored | status vocabularies · flag-code sets *(expansion — blocked on `meta.open.source-of-members`)* |
| `process/lexical.json` | authored | content-validity V1/V2/V3 · band-drift · success measures G0–G10 · passage-reading checkback gate |
| `process/base.json` | authored | readiness verdict classes + check groups §A–F · Stage-0 layout precompute |
| `process/characteristics.json` | authored | characteristic families/clusters · outward-glory→standalone |
| `wide/pipeline.json` | authored | worklist definitions · per-cycle/book-close cadence gates |
| `utility/filing.json` | pending | filing rules (archiving triggers · living-doc) |
| `utility/auth.json` | pending | secrets/keys |
| `process/findings.json` | pending | synthesis-B gates |

**This is a useful negative result.** The four hours of structure hold: every gap but five has an obvious destination, and the destinations were derived before the gaps were counted. The framework is not missing shape — it is missing content.

## 4. ⚠ The five with no home — and why they are the same five

- Three orders of output (records · syntheses · account)
- Audiences (scholar / leader / ordinary reader)
- Milestones M1–M3
- Science-lens policy (secondary corroborator)
- Standing-question catalogue (VE/SYNTH)

**These are not a residue. They are the study's END POINT.**

Plan §1.1 states the end point is **two-part**: *"a materially-evidenced findings corpus held entirely in the DB… and the products drawn from it — essays, study guides, ebooks/books, sermon series — for three audiences (scholar; leader/teacher; ordinary reader)."*

**The configurator models the first part and nothing of the second.** It is a complete account of how the study PRODUCES evidence and has no account of what the evidence is FOR.

This is the same hole seen from two other directions already:

- `open.pipeline.module-8-and-prose` — the **prose layer (layer 4 of 4)** has no process and no module. The nine modules end at findings.
- `enum.governs` has seven study processes; **none of them is prose or products**.

So three independent findings are one finding: **layer 4 does not exist in the application.**

**Is that wrong?** Not necessarily — the plan parks it deliberately (§5: *"Analysis & findings (least-defined): the study's higher-order outputs sit beyond segment 9"*), and publication is recorded as parked. The build order (§2.3) is framework → modules → prove sustainable → *then* re-run the study; products are rightly far behind that.

**But it should be a recorded debt, not a silence.** Half the stated end point currently has no home, no file, and no `pending` marker — it is the one part of the inventory the framework does not even gesture at. A parked decision that is written down is a plan; one that is merely absent is how a scope quietly shrinks to what the tooling happens to support.

**Recommendation:** add `prose` to `enum.governs` and a `process/prose.json` marked **INACTIVE** — the status the researcher created on 2026-07-15 for exactly this case: *defined and correct, nothing uses it yet, and its purpose is knowledge retention.* That costs one file and closes the last hole in the inventory. It does not commit to building anything.

## 5. Recommended order to close the gaps

Driven by what is **blocking** rather than by what is biggest:

1. **`wide/patterns.json`** — 16 unresolved `cites` point at it right now (`pattern.id-frozen-at-mint`, `pattern.zero-pad-strongs`, `pattern.dimension-name-with-code`). Every process file cites rules that do not exist. **The kernel is already reporting these as warnings; they are a to-do list the config wrote for itself.**
2. **`utility/filing.json`** — 9 more unresolved cites (`filing.version-bump-on-same-name`, `filing.archive-superseded`, `filing.manifest-rebuild-after-write`).
3. **`utility/git.json`** — 1 unresolved cite (`git.commit-per-unit-of-work`).
4. **`wide/db-governance.json`** — homes the I1–I13 invariants, which `char.candidate-requires-verse-record` currently carries alone.
5. **`wide/settings.json`** — the STEP names are settled but `engine/constants.py` values are not encoded anywhere.
6. **`wide/principles.json`** — the largest single block (7 items) and the least mechanical.
7. **`wide/governance.json`** — the GR-*/FLAG-* register.
8. **`process/findings.json`** — the last unauthored study process.

Items 1–3 are not merely next; they are **already failing a check**. The kernel's 16 unresolved-citation warnings are the config saying, in its own voice, which file to write next.

## 6. What this exercise proved about the method

The mapping was done **programmatically against the live config, by rule id** — not by reading the config and judging. That matters: the same exercise done by recollection would have scored the framework higher. Three items I would have called homed were not (`STATED/INFERRED`, `field-authority`, `soft-delete discipline` — all real rules, all discussed today, none authored).

That is the whole thesis in miniature: **what you remember deciding and what the artefact contains are different things, and only the second one runs.**

---

## 7. Re-scan addendum (2026-07-15) — the inventory is bigger than A.9

Two re-scans were run after this map was drafted, at the researcher's suggestion. Full findings:
[scan A — instructions & catalogue](scan-2026-07-15-instructions-catalogue.md) ·
[scan B — rules, constants, settings](scan-2026-07-15-rules-constants-settings.md).

**They closed three A.9 gaps and added ~22 items A.9 never named.** The revised count:

| | v1 | **revised** |
|---|---:|---:|
| Inventory items | 92 | **~114** |
| Homed | 43 | 43 |
| Gap — home exists | 44 | **~66** |
| Gap — NO HOME | 5 | 5 |

**Closed** (the plan listed these as "still to pull"): the Tiers catalogue (**126 active questions** T0:9·T1:18·T2:6·T3:33·T4:18·T5:9·T6:13·T7:20, 16 dropped from 189, plus the **VE-01..VE-17** inventory) · the versecontext **R1–R4** rules · the registry-management vocabulary.

**Added** — 12 vocabularies (role_provenance · vc_status · patch postures · quality scores · verdict classes · check classes · gate outcomes · skip-list reasons · T2 split · stem vocabulary · disposition) and ~10 rule-sets (I2b · D1/D2 · VC R1–R4 · re-run R1–R6 · API circuit-breaker · API self-verification · Gate-1 span-orphan · audit-clean 7 checks · the anomaly test · staged sequence 0–5 · readiness groups §A–F).

**None of the additions needs a new file.** They land in the same eight pending files. §3's mapping holds — the framework absorbed a 24% larger inventory without a structural change, which is the strongest evidence yet that the shape is right.

### ★ The scans found one live danger and four new reconciliations

1. **The `.env` file is a loaded gun** — `STEP_API_BASE_URL=https://www.stepbible.org/api` (REMOTE) and `STEP_DEFAULT_VERSION=ESV` (UNTAGGED). The client hard-codes localhost + ESV_th and ignores `.env` entirely. **The only reason this study has tagged morphology is that the client ignores its own configuration.** `step.connection` v1 ruled "rewrite the client to read .env" — which would have silently destroyed the evidentiary floor. **Corrected at 0.1.4**; the values in `.env` still need fixing, and the order matters: fix `.env` first, then the client.
2. **DB-vs-config authority** — all four pattern registers (rules · file patterns · label patterns · patch types) declare the **DB** their source of truth. The configurator claims to be the single home for rules. Both cannot be true.
3. **Two version conventions** — GR-FILE-003 (`v{major}_{minor}` always) vs file-organisation-rules (`-v{n}` for session artefacts). Two pattern classes; needs a ruling.
4. **The `role` enum — new evidence.** `process-qualifier` may be a **sub-form of qualifier**, not a peer. That possibility is not in `recon.role-enum`'s variant list, and it changes the answer.
5. **G8 is absent** from the measures runner while G0–G7, G9, G10 emit; **two thresholds exist only in code** (the G0 digestion budget; the candidate:total band, which has **no value at all**).

### What the re-scan says about the method

The scans found **more in four minutes than A.9's three scans recorded** — including a defect that would have broken the study. Three observations worth keeping:

- **A.9 was a good index and an incomplete one.** It named ~92 of ~114. The 22 it missed were not obscure; they were in authoritative instruction docs. An inventory compiled by reading is always a sample.
- **The most dangerous finding came from reading VALUES, not names.** The earlier audit grepped  for key names and reported a mismatch. The re-scan read what the keys said. Same file, same day, opposite conclusion.
- **The framework did not move.** ~22 new items, zero new files. That is the test a structure has to pass.
