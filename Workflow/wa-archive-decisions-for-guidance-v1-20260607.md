# Archive decisions needing your guidance — 2026-06-07

> **Decision surface · v1 · 2026-06-07 · CC.** A focused refresh of the parked
> `wa-workflow-cleanup-register.md` (2026-06-04). Today's V3_2 work resolved many of the original `____`
> cells (v3_0 and remediation are now superseded), so this lists **only the items I am genuinely unsure
> about** + the few I'll execute confidently. **Mark the `Your call` cells** (`keep` / `archive` /
> `relocate→…`) and I'll sweep them. Reversible by design (move → folder `archive/`, never delete; git +
> manifest preserve everything).

---

## A · I'll execute these confidently (no decision needed — listed for transparency)

Given today's supersessions, these are now unambiguous and I'll archive/generate them when you hand me the go:

- **Generate a fresh `schema/database-schema-v3.28.0` snapshot** (all on-disk snapshots are stale at 3.17.0).
- **v3_0 design set** (Instructions/): `wa-v2_9-vs-v3_0-cycle-comparison`, `wa-v3-publication-pipeline-design`,
  `wa-v3_0-final-review`, `wa-v3_0-phase-b-control-design` → archive (v3_0 superseded by the V3_2 base).
- **Spent one-off logs**: `wa-finding-citation-backfill-20260527`, `wa-vcg-analytics-citation-correction`,
  `programme-snapshot-20260425`, `wa-programme-cluster-audit-v1/-v2` (superseded by v3 same day),
  `wa-global-database-*-20260419` (6 spent migration logs), old integrity/overview snapshots.
- **Dense April-2026 `wa-global-*` process logs** in `Sessionlogs/` → `Sessionlogs/archive/`; the stray
  `PATCH-*.json` → `Sessions/Patches/archive/`.

---

## B · Need your guidance (the genuine judgement calls)

| # | Item(s) | My lean | Why I'm unsure | Your call |
|---|---|---|---|---|
| 1 | `wa-tier-framework-definitions-v1_2` (methodology/) — prose definition of all 8 tiers | **keep** | You're reshaping tier definitions in `wa-study-foundations.md` §c; this is the thing being superseded, but §c isn't finalised — you may still consult it. | `____` |
| 2 | `wa-audit-framework-design-v0_1-20260526` (Instructions/) | **archive** | Today's `wa-cluster-audit-design-v1` is the V3_2 audit. But v0_1 documents the *old* aspect-spec audit (Groups A–E) — moot under V3_2, yet a record of the prior model. | `____` |
| 3 | `wa-v3_0-refinement-{0..4}` + `-discussion` (methodology/) | **archive** | v3_0 is superseded by V3_2 — but I want to be sure none of these fed the V3_2 design in a way you'd want kept live. | `____` |
| 4 | Remediation set (methodology/): `wa-cluster-remediation-orchestrator-design`, `-playbook`, `-audit-aspect-spec-v1` | **archive** | Remediation closed 2026-06-04 and V3_2's roll-up supersedes it (Session D moot). Archiving feels right, but they're recent and you may want the playbook as a reference. | `____` |
| 5 | Science prose drafts (Sciences/): `wa-prose-draft-purp-scienceandbible`, `wa-prose-draft-science-in-action-v4` | **relocate → Programme/Corpus_prose** | They're prose, not science extracts — but I'm unsure if they're spent drafts (→ archive) or live prose (→ relocate). | `____` |
| 6 | Misplaced extracts (Tiers/): `wa-tpopb-findings-catalogue-extract`, `wa-tpopc-btarget-flags-extract` | **archive** | Stale catalogue/flag extracts (DB is the live source) — but they could be relocated to `research/investigations/` if you still mine them. | `____` |
| 7 | Point-in-time snapshots (registry/, Clusters/, Program_reports/): `inner-being-words-snapshot`, `banked-registries-summary`, `wa-cluster-status-20260502`, `wa-programme-status-report-20260427`, stale `registry-overview`s | **archive** | The DB is the live source and git preserves these — but you sometimes consult snapshots as quick references. Archive all, or keep any named? | `____` |
| 8 | `.docx` records: `WA-M15-journey-reflection-v2`, `WA-lessons-learned-v1` | **keep (as records)** | These read as keepsake records, not spent working docs — but they're not governing either. Keep in place, or move to an `archive/records/`? | `____` |
| 9 | `wa-Session-A-Instruction-v8-final.docx` (Instructions/) | **unsure** | Is the `audit_word` engine model + `wa-sessiona-prose-instruction` now the canonical Session A, making this superseded? Or is this still the authoritative Session A doc? | `____` |
| 10 | `Programme/programme_analysis/` whole folder | **archive folder** | Appears entirely historical (status reports 0330–0420, dimension/root-family extracts, `word_registry.json/.csv`). Archive all, except anything you still consult? Name exceptions: | `____` |
| 11 | Bulk April historical set in `methodology/` (~45 files: per-word audit logs, April session logs/obslogs, superseded obs-question catalogues, `*.docx` design notes) | **archive (bulk)** | Per filing rules these are spent working docs — but it's a large bulk move on governing-adjacent material, so I want your blessing before sweeping. | `____` |

---

## C · Working analytics I'll leave unless you say otherwise

`Clusters/` working analytics (`wa-cross-cluster-gloss-analytics`, `wa-vcg-analytics-*`,
`wa-cluster-observation-resolution`) — these may still inform the V3_2 rebuild (cross-cluster, VCG analytics).
**Default: keep** until the rebuild is underway. Override any: `____`

---

*Mark B (and any of A/C you want to override). Then I sweep in one pass and update the cleanup register's
working notes. The full per-file detail remains in `wa-workflow-cleanup-register.md`.*
