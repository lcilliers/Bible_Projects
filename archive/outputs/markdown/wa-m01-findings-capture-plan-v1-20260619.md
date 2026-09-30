# M01 findings — capture plan + old/new cross-check (for review) · 2026-06-19

**Goal:** capture the new M01 tier findings into the DB, after cross-checking them against the existing
(old) M01 findings for notable *context* difference. **Status: nothing written to the DB.** Awaiting direction
on the decisions in §4.

## 1. The new findings (to capture)

- `Sessions-v2/M01-Fear/findings/WA-m01-findings-t{0..7}-v1_0-2026-06-18.md` — **173 findings, one per tier
  question** (12/20/28/33/24/18/18/20), uniform structure (`## T#.#.# — question` + `**Finding.**` prose),
  programmatically parseable.
- Each finding **collates all 11 characteristics (c1–c11)** in prose, with distribution counts from the
  revised by-characteristic JSON and verbatim verse quotes; per-characteristic silence recorded.
- Authored by Claude AI on **2026-06-18** against the **pre-refit 173-question spine**
  (`WA-tier-catalogue-current-state-v1-20260617`). No DB ops were done by Chat.

## 2. The old findings (already in the DB)

- `cluster_finding`, cluster_code M01: **755 active rows across all 173 obs_id**, from
  `WA-M01-consolidated-findings-v1-20260516` (**2026-05-16**).
- Structure per question = **1 consolidated row (characteristic_id NULL) + one row per sub-group M01-A…G**
  (the **7-characteristic** model; DB `characteristic` table holds 7 M01 rows, ids 64–70).

## 3. Three structural shifts (this is "notably different in context", not just form)

1. **7 → 11 characteristics.** Old findings are built on 7 sub-groups (M01-A…G); new on 11 (c1–c11). The
   cluster was re-characterised between 05-16 and 06-18. The DB `characteristic` table still reflects **7**.
2. **Granularity.** Old = consolidated + per-sub-group rows. New = **one collated finding per question**
   (per-characteristic nuance lives inside the prose). New is richer (counts + verbatim verses) and verse-first.
3. **Catalogue refit (yesterday).** New findings answer the old 173 questions, but the 2026-06-19 refit
   soft-deleted **47** of them (folded into primaries) and rewrote 126. **154 old rows** already sit on
   now-deleted obs_id; ~47 of the new findings likewise answer now-folded questions.

### Concrete sample — T0.1.1 (obs 224)

> **OLD (05-16):** "Across M01, fear … reflects and images the holiness, sovereignty, and relational depth of
> God … (1) supreme object of reverential fear (M01-A); (2) presence intrinsically overwhelming (M01-B, E);
> (3) sovereign over all terror (M01-C); (4) ground of inner stability whose withdrawal produces dismay
> (M01-D); (5) final judge before whom dread is rational (M01-F). … God does not fear (T0.1.2)."

> **NEW (06-18):** images God's "holiness, power, and covenant lordship" — the **object-side**; adds the
> load-bearing fact **divine_involvement = experiencer 0/975**; foregrounds **forgiveness** (Psa 130:4) and
> the Niphal *nora'*; gives a per-characteristic c1–c11 breakdown with counts; **c11 by contrast** (2Ti 1:7).

→ Core context **consistent** (God imaged object-side, never experiencer), but new is materially **richer +
re-evidenced + restructured to 11 chars**. The per-question verdict will vary; some will be genuinely new
context, most an enrichment.

## 4. Decisions needed before capture (my recommendation in **bold**)

- **D1 — Supersede the old?** New is a full re-build on a new characteristic model. **Rec: soft-delete the 755
  old M01 cluster_finding rows and insert the new, with a supersedes pointer (source_file/notes).** (Old stays
  recoverable via delete_flagged.)
- **D2 — Granularity to store.** **Rec: one `cluster_finding` row per question (173), characteristic_id NULL,
  finding_text = the finding prose** — matching the old "consolidated" row; the 11-char detail is in the prose.
  (We do *not* explode into per-characteristic rows, since the new build is question-level.)
- **D3 — The 47 folded questions.** **Rec: capture all 173 against their original obs_id** (as the old rows
  already do for 154), tagging the 47 with a note `question folded_into=<primary> (refit 2026-06-19)`. Preserves
  every authored finding; reversible; a later fold/merge pass can consolidate when we choose.
- **D4 — 7→11 characteristic table.** **Rec: out of scope for this capture** — store findings at question level
  (char NULL) now; updating the `characteristic` table 7→11 is a separate structural change to decide on its own.

## 5. Cross-check (how I'll surface "notable context difference")

For each of the 173 questions I will place **old consolidated text** beside **new finding text** and classify
the delta: `consistent-enrichment` · `notable-new-context` · `contradiction` · `old-only` (no new) ·
`new-only`. Output: a filed register flagging the `notable-new-context` / `contradiction` rows for your eye.
**This is the natural point to route to AI** (per your note) — I can hand the side-by-side package to Chat for
a semantic "what changed" read, or do a CC-side heuristic first pass. Your call which.

## 6. Capture mechanics (once approach agreed)

Build a reviewed JSON patch (parse the 8 tier files → 173 findings → `cluster_finding` insert + soft-delete of
the old rows), dry-run, present, apply — same governed path as the tier-catalogue refit.

---

**Please direct:** D1–D4, and whether the cross-check goes CC-first or straight to AI. I'll then build the
cross-check register and the patch.

---

## 7. (a) Characteristic-table update — 7 → 11 (plan; nothing written)

**Source:** `Sessions-v2/M01-Fear/Analysis/WA-m01-characteristics-v1.0-2026-06-16.md` (the 11-characteristic
derivation the new findings are built on). The 11: 1 Reverent fear/awe · 2 Fear/afraid · 3 Dread · 4 Terror ·
5 Trembling · 6 Shuddering/horror · 7 Dismay · 8 Alarm · 9 Anxiety · 10 Astonishment · 11 Cowardice. (Plus 3
non-characteristic groups B1–B3 kept separate.) **Note:** that file's §E flags granularity/anchor/outliers as
*open* choices — the 11 are a "first derivation," provisional.

**Current DB:** `characteristic` has **7** M01 rows (ids 64–70 = the M01-A…G subgroup model). References to them:
- `cluster_finding.characteristic_id` — **648 rows** (the old per-subgroup findings; slated for supersession, D1)
- `characteristic_subgroup.characteristic_id` — **7 rows** (1:1 char→subgroup map, M01-A→sg58 …)
- (no other table carries `characteristic_id` for M01)

**Why this isn't a standalone table edit:** retiring the 7 while 648 old findings + 7 subgroup links still
point at them creates dangling references. The 7→11 char change, the old-finding retirement, and the new-finding
insert are **one model shift**. Two ways to sequence:

- **Option A (recommended) — bundle (a) with the findings capture, after the AI assessment.** One coordinated
  reviewed patch: insert 11 new chars, retire the 7 old, soft-delete the 648 old findings, insert the 173 new.
  Nothing dangles; the AI assessment (the OLD/NEW MDs) confirms the new findings first.
- **Option B — do (a) now, additively.** Insert the 11 new char rows immediately (zero-risk, satisfies "update
  the table"), leave the 7 old live-but-noted ("superseded by 11-char model; retire on findings capture"). M01
  then shows 18 char rows transiently until the capture retires the 7.

Either path is a governed reviewed patch (dry-run → review → apply), same as the catalogue refit.

## 8. Deliverables produced this turn (read-only)

- `Sessions-v2/M01-Fear/findings/WA-m01-findings-OLD-dbexport-bytier-v1-20260619.md` — 755 old findings, by tier question.
- `Sessions-v2/M01-Fear/findings/WA-m01-findings-NEW-merged-bytier-v1-20260619.md` — 173 new findings, by tier question.
- `scripts/build_m01_findings_oldnew_extract.py` — the reusable read-only extractor.

→ both ready to submit to AI Chat for the material-difference assessment.
