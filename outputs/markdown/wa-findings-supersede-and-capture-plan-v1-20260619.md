# M01 + M02 — supersede OLD findings & capture NEW findings: PLAN (no execution) · 2026-06-19

> **Decision (researcher, 2026-06-19):** mark the OLD findings (and items associated with them) to **restrict
> their visibility for further analysis** (retain, do not lose), and capture the **NEW findings** into the DB for
> future prose generation. Both M01 and M02 have new files in their `findings/` folders.
>
> **This is a plan for your sign-off. Nothing will be written until you approve.** Where there is a real fork I
> give a recommendation and mark it **[DECIDE]**.

---

## 1. Inventory — what exists now

### 1a. OLD findings in the DB (the 2026-05-16 consolidated set)

| Cluster | `cluster_finding` (old) | `finding` table (CLUSTER) | old characteristics | old sub-groups |
|---|---|---|---|---|
| **M01** | **755** rows · source `WA-M01-consolidated-findings-v1-20260516` (parts 1–4); statuses finding 516 / cluster_synthesis 141 / silent 98 | 27 `session_b_migration` + 5 `l2_rollup` = **32** | **7** (ids 64–70, model M01-A…G) | 8 (M01-A…G + BOUNDARY) |
| **M02** | **363** rows · source `WA-M02-consolidated-findings-v1-20260516`; finding 273 / cluster_synthesis 52 / silent 38 | 5 `session_b_migration` | **6** (ids 71–76, M02-A…F) | 7 (M02-A…F + BOUNDARY) |

**KEEP — not "old", must stay fully visible** (the new findings are built on these):
- `finding` **VERSE-level `l2_meaning`** — M01 1,034 · M02 703 (the verse-reads / measure grounding).
- `ve_lexical` (all per-occurrence fields), `verse_context`, `verse_context_group`, terms, verses.
- The **new** M02 `cluster_synthesis` row added by DIR-002 (the C7 scope finding) — not old.

### 1b. NEW findings on disk (the 2026-06-19 set) — three layers each

| Layer | M01 files | M02 files | grain |
|---|---|---|---|
| **A · atomic findings** | `WA-m01-findings-NEW-merged-bytier-v1` (one finding per question, **collating all 11 chars in prose**) | the **7** `…cN-…-tieranalysis` files (one answer **per characteristic per question**) | A1: question-level (M01) · A2: characteristic×question (M02) |
| **B · per-characteristic synthesis** | **11** `wa-m01-cNN-…-synth-v1_0` (c1–c11, across all tiers) | (the char tier-analysis files double as this) | characteristic × all-tiers |
| **C · cluster synthesis** | `wa-m01-cluster-synthesis-v1_0` | `wa-m02-cluster-findings-v1_0` (by phenomenon, F1–F10) **and** `wa-m02-cluster-synthesis-bytier-v1_1` (by tier) | cluster × all-tiers |

Layers B and C are explicitly authored as the **"prose-foundation… from which essays are written without
returning to source"** — i.e. the most directly useful layer for your prose-generation goal. Layer A is the
data-grounded backing.

**Asymmetry to resolve:** M01's atomic layer is **question-level** (11 chars collated per question); M02's is
**characteristic×question**. And M02 has **two** cluster-synthesis files (phenomenon vs by-tier). See [DECIDE-2]/[DECIDE-3].

---

## 2. Part 1 — Marker on the OLD findings (restrict visibility, retain)

**Mechanism (recommended):** `delete_flagged = 1` + a documented reason in `notes` —
`"superseded by 2026-06-19 NEW findings (11/7-char model); retained for reference, excluded from analysis"`.
Soft-delete = exactly "restrict visibility for further analysis" (every analysis query filters `delete_flagged=0`)
while **losing nothing** (rows retained, fully reversible by flipping the flag). No physical deletes.

**Scope to mark:**
1. `cluster_finding` rows whose `source_file LIKE 'WA-M0{1,2}-consolidated-findings-v1-20260516%'` — **755 + 363**.
2. `finding` CLUSTER-level rows for M01/M02 — **[DECIDE-1]**: the 27+5 `session_b_migration` and 5 `l2_rollup`
   are *not* the 05-16 consolidated set; they're earlier Session-B / L2 cluster rollups. Mark them too, or leave them?
   (Rec: **mark them** — they are old cluster-level findings the new synthesis replaces — but confirm.)
3. OLD **characteristics** (M01 64–70, M02 71–76) and **sub-groups** — mark superseded **only if** we create the
   new 11/7-char structure (Part 3). Tie this to Part 3.

**Explicitly NOT marked:** VERSE `l2_meaning`, `ve_lexical`, VCGs, terms, verses, the DIR-002 C7 row.

**Reversal:** a single `UPDATE … SET delete_flagged=0 WHERE notes LIKE 'superseded by 2026-06-19%'` restores all.

---

## 3. Part 2 — Capture the NEW findings (for prose generation)

Building on the agreed model (`wa-findings-capture-model-proposal-v1`, Path A): **`cluster_finding` as the home +
generic `finding_citation` for verses/pointers.** Per layer:

- **Layer A (atomic):** one `cluster_finding` row per finding. `obs_id` = the tier question; `characteristic_id`
  set (M02 char×question) or NULL (M01 question-level collated); `finding_status` = finding/silent/gap;
  `finding_text` = the answer; verse anchors → `finding_citation(source_table='cluster_finding', citation_type='verse')`;
  cross-refs → `citation_type='pointer'`; inferential/observation/interpretation → `finding_type`.
- **Layer B (per-char synthesis):** the synthesis prose has **no single `obs_id`** (it spans all tiers) — and
  `cluster_finding.obs_id` is NOT NULL. **[DECIDE-4]** two clean options:
  - **B-i:** store in the universal **`finding`** table at `level='CLUSTER'` (no obs_id needed), `provenance='char_synthesis'`,
    with `finding_question_link` rows for each tier it cites — the richer store, made for this.
  - **B-ii:** store in `cluster_finding` anchored to a representative `obs_id` (e.g. T1.1.1) with `finding_status='char_synthesis'` — keeps everything in one table but the obs_id is nominal.
  (Rec: **B-i** — synthesis is genuinely cluster-level and the `finding` table already holds `l2_rollup` there.)
- **Layer C (cluster synthesis):** same choice as B; store as `finding` `level='CLUSTER'` `provenance='cluster_synthesis'`
  (rec **B-i**), one row per synthesis section (M01 §1–§n; M02 F1–F10 / by-tier sections).

**Characteristic dimension** is essential for prose ("write the essay on c4 Terror"). `finding` has no
`characteristic_id`; `cluster_finding` does. This is the main pull toward keeping atomic findings in
`cluster_finding`. For Layers B/C in the `finding` table, the characteristic is named in the text and can be
linked via a small `finding`→characteristic note. **[DECIDE-4]** settles this.

---

## 4. Part 3 — Characteristic table (create new, supersede old)

You directed earlier that the characteristic files must update the `characteristic` table.
- **Create** the NEW characteristics: M01 **11** (c1–c11, from `WA-m01-characteristics-v1.0`), M02 **7** (c1–c7,
  from `wa-m02-ve-characteristics-v1_0`), with definitions + `cluster_subgroup` rows.
- **Mark superseded** the OLD characteristics (M01 64–70, M02 71–76) + their sub-groups (`delete_flagged=1` + note),
  once the new ones exist and the new findings link to them. Old findings already reference the old chars — fine,
  they're being restricted together.

---

## 5. Sequencing, governance, safety

1. Pre-run **DB backup** (snapshot) before any write.
2. Build everything as **reviewed JSON patches** (or `_apply_` scripts) with **`--dry-run` → your review → live**,
   the same governed path used for the catalogue refit and DIR-001/002.
3. Order: (a) create new characteristics/sub-groups → (b) capture NEW findings (linked to new chars) → (c) mark
   OLD findings + old chars/sub-groups restricted. (New must exist before old is hidden, so nothing is lost in between.)
4. **Idempotency guards** (skip if already captured/marked) and **completeness checks** (counts in vs out) on every step.
5. **Parsers** read the disk files → structured rows; I'll show you sample parsed output before the live write.
6. Fully **reversible**: marker flips back; captured rows identifiable by `source_file`/provenance and removable.

---

## 6. OPEN DECISIONS — I need these before building

- **[DECIDE-1]** Marker scope: also restrict the `finding`-table CLUSTER rows (`session_b_migration`, `l2_rollup`)?
  (Rec: yes.) And confirm VERSE `l2_meaning` stays visible (Rec: yes — it's the grounding).
- **[DECIDE-2]** M01 atomic grain: capture question-level (as authored, `characteristic_id` NULL), or reconstruct
  characteristic×question to match M02? (Rec: capture **as authored** — question-level for M01, char×question for
  M02 — the model supports both; don't fabricate a grain the analysis didn't produce.)
- **[DECIDE-3]** M02 cluster synthesis: capture the **by-tier** file, the **by-phenomenon (F1–F10)** file, or **both**?
  (Rec: capture **both**, tagged by `finding_type`, since they're complementary views.)
- **[DECIDE-4]** Synthesis home: Layers B/C in the universal **`finding`** table (rec B-i) or in `cluster_finding`
  (B-ii)? This is the one structural fork that shapes the schema usage.
- **[DECIDE-5]** Scope now: do **both M01 and M02** in one pass, or **M02 first** (it's the more complete/cleanest
  set) as a pilot, then M01? (Rec: **M02 first as the pilot**, validate, then M01.)

---

## 7. What I will produce once you steer §6

Per cluster: (1) a characteristic-creation patch; (2) a findings-capture patch (Layers A/B/C) with parsers and a
sample-parsed preview; (3) a marker patch for the old findings + old structure — each dry-run first, presented for
your review, applied only on your go-ahead, with before/after counts and a reversal note.

---

# REVISION — researcher steer 2026-06-19 (supersedes §3 capture model, refines §2/§6)

The researcher steered two things that simplify this substantially:

## R1. Marker scope (answers [DECIDE-1])

"The old Session B findings are **replaced** by the new verse-analysis method, **including any previous meaning
records**." So **restrict**:
- the old consolidated `cluster_finding` (M01 755, M02 363),
- the CLUSTER-level `finding` rows (`session_b_migration`, `l2_rollup`),
- **`wa_session_b_findings`** (legacy Session B findings — 2,883 rows across the programme; the M01/M02 subset),
- old characteristics (M01 64–70, M02 71–76) + old sub-groups.

**One boundary to confirm — [CONFIRM-A]:** the **verse-level `l2_meaning` reads** (M01 1,034 · M02 703) ARE the
output of the *new* verse-analysis method (the L2 "verse-read = meaning" pass, 2026-06-09) and are the evidence
the new files are grounded on. My read: **keep them visible** as the measure/grounding layer (like `ve_lexical`),
not restrict them. Confirm: keep `l2_meaning`, or does "previous meaning records" include these too? (`wa_meaning_parsed`/`wa_meaning_sense` are lexicon parses, not findings — keep regardless.)

## R2. File-as-finding (answers [DECIDE-2/3/4] — no dissection)

Researcher: *"it is unwise to artificially dissect the files to fit a DB structure; the files stand on their own
feet — what if the file is saved as a finding, not a dissection of the file."* **Agreed — this is the better model.**
Digestion for prose happens at cluster level, so atomic per-question rows aren't needed; dissecting risks loss and
imposes a false grain. **Each findings file → one record holding its whole content**, tagged for retrieval. Grain
may differ per cluster (M01 captures its 11 per-char synth + cluster-synth files; M02 its 7 char files + cluster
synth) — fine, since they're digested at cluster level.

**Home — recommended: the `prose_section` store, which is purpose-built for exactly this** (not a forced fit):
- native `cluster_code` · `characteristic_id` · `cluster_subgroup_id` (retrieval by cluster/characteristic),
- `heading` + `body` (the whole file content), `word_count`, `source_file`, `version`, `author`, `metadata_json`,
- **`supersedes_id` / `superseded_by_id` + `status`** — built-in lifecycle for the OLD→NEW relationship,
- a **`prose_section_type`** typology (I'd add types: `cluster_synth`, `char_synth`, `tier_findings`),
- **`prose_section_fts` (FTS5)** full-text search across the corpus of findings.
- Alternative: the universal `finding` table (level=CLUSTER, `finding_value`=content) — but it lacks
  `characteristic_id` and FTS, so it's a worse fit. **[DECIDE-4′]** prose_section (rec) vs finding.

> Note on naming: the table is called `prose_section`, but it is the right *structure* for a "file-as-finding"
> (whole body + cluster/characteristic + supersession + search). If you want these explicitly called "findings",
> we can add a `prose_section_type` of `cluster_finding_doc` — the semantics are ours to set.

**Candidate file set to capture — [DECIDE-FILES]** (the real findings, excluding working/audit/comparison/obslog docs):
- **M01:** 11 × `wa-m01-cNN-…-synth` + `wa-m01-cluster-synthesis` (+ optionally `WA-m01-findings-NEW-merged-bytier` as the atomic grounding record). = 12 (or 13).
- **M02:** 7 × `wa-m02-cN-…-tieranalysis` (latest version) + `wa-m02-cluster-synthesis-bytier` + `wa-m02-cluster-findings` (F1–F10). = 9.
- `ve-characteristics` files → drive the **characteristic-table** creation (Part 3), not stored as prose.

## R3. Revised open decisions (the rest of §6 is now settled by R1/R2)

- **[CONFIRM-A]** keep `l2_meaning` verse-reads visible (rec: yes)?
- **[DECIDE-4′]** capture home = `prose_section` (rec) or `finding`?
- **[DECIDE-FILES]** confirm the file set above (esp. whether to also store M01's merged-bytier atomic and both M02 cluster-synthesis files).
- **[DECIDE-5]** still: M02 pilot first, then M01 (rec)?

Once these four are set, I build: (1) characteristic create + old-char supersede; (2) file-as-finding capture into
`prose_section`; (3) restrict-marker on the old findings/meaning records — all dry-run → review → live, reversible.
