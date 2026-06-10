---
name: project_cc_generation_mode
description: BUILT+PROVEN (2026-06-10): CC-generation mode for the verse-read = scripts/_cc_verse_read.py — the verse-read done by Claude Code (Opus, subscription) instead of the Sonnet API, the cost win (subscription already paid; Opus > the Sonnet the API used). PARALLEL path: the API pipeline _apply_verse_read_meaning.py is left fully intact (revert = just use it); CC reuses its helpers by import. Handshake (in-session, no manual paste): --emit (next N unread M-cluster verse-blocks + T2 context) → CC writes @@@ records → --ingest (parse, write, route each term to its cluster). T2 RULES BAKED IN: M-clusters drive; T2 = context to embed, NEVER written (ingest skips non-M vcids via emit sidecar map). Resumable by idempotency. Attended (not unattended like the API overnight run).
metadata:
  type: project
---

**Researcher cost decision (2026-06-10):** the API runs are metered $ on top of the paid subscription; route
the verse-read through CC (Opus, subscription) instead. The API's only real edge was unattended overnight
automation; for cost AND quality (Opus > Sonnet), CC wins. See [[project_l2_verse_read_meaning_live]].

**`scripts/_cc_verse_read.py`** — parallel to the API pipeline (kept intact so we can revert).
- `--emit --limit N --out f.md`: assemble the next N unread **M-cluster** verse-blocks (verse-complete: all
  M-cluster terms at the ref lacking a meaning) + **T2 qualifiers as context** (embed, don't write). Writes a
  packet file + a `.map` sidecar (vcid→mid,cluster) so ingest routes authoritatively.
- CC reads the packets and writes `@@@…@@@END` records (the same field spec as the API; reuses
  `vrm.SYSTEM_PROMPT`).
- `--ingest --in f.md`: `vrm.parse_response` → `vrm.write_record`; **skips any vcid not in the map** (T2 /
  out-of-scope never written); flags via the same self-audit; `--status` shows X/Y coverage.
- Resumable by idempotency (emit pulls only unread); engine run/checkpoint logging not yet added (relies on
  idempotency for resume).

**Proven on M47 Constitution:** emit 3 verses / 8 WRITE-terms → CC generated 8 records → ingest wrote 105
findings, 0 skipped; verse-complete routing verified (Rom 9:1 → conscience/M47 · spirit/M25 · truth/M13 ·
holy/M22). M47 → 16%.

**M02 (Anger) run COMPLETE 2026-06-10 (run `ccvrm_M02_2026-06-10T05:00:27`):** engine run/checkpoint logging
IS in CC mode (per-cycle: records/expected/covered/shortfall/findings). **703/703 (100%)**, 97 cycles,
**17,029 fan-out findings**, **3 cycles with shortfall — all genuine term-drops I made under load (dropped a
term mid verse-complete), each CAUGHT automatically** by the emit-map vs written-vcids check (`missing_vcids`,
status→review) and corrected by idempotent re-ingest. The completeness check is proven across a full cluster.
Full thematic range mapped: wrath-noun/verb families (che.mah/cha.ron/cha.rah — judgment-wrath idiom,
cup/winepress, bounded/turned-away wrath, prophet-as-vessel, deferential "let-not-X-be-angry", righteous human
anger, self-anger dissolved, non-anger burning-zeal); jealousy/zeal (qa.na/qin.ah/qan.na "jealous God" + divine
NAME "Jealous" Exo 34:14); the large **riv** family (strife/quarrel AND forensic "cause/lawsuit/indictment" —
incl. covenant-lawsuit Hos 12:2/Jer 25:31, "plead my cause" advocacy, Job's pleadings); **tsur** "show
hostility/besiege" (the Babylonian/Assyrian siege narratives); za.eph "vexed and sullen" (Ahab); zal.a.phah
"hot indignation"; the Greek tail (eris, logomachia, paroxusmos pos+neg, zestos fervency-not-anger, erethizō,
thumomacheō, pikria). **Two cluster-quality items flagged in-place for the per-cluster gate:** (a) OT-DBR-009
homonym artifacts — tsur "bind/bag" (money/hair, 2Ki 12:10, 2Ki 5:23, Deu 14:25, Eze 5:3), che.mah poison/venom,
chay "as-I-live"/"alive", ka.phar pitch, che.sed reproach — flagged HOMONYM-ARTIFACT, not absorbed; (b) **tsur
"besiege" = a clustering misfit candidate** — pure military-siege uses carry thin inner-being content (affect
SILENT); also the enclose-sense (Psa 139:5 God hems-in, Song 8:9 board-up sister) wrongly M02-tagged, flagged
enclose-not-hostility. Session log: wa-sessionlog-20260610-M02-cc-verse-read-v2. **M02 is the 2nd cluster
complete (after M01); next: per-cluster gate, then another cluster.**

**Quality-check tooling (read-only):** `scripts/_generate_meaning_quality_check.py` (N random verses × M
terms: verse + tier findings + meaning); `scripts/_generate_verse_meanings_export.py` (full l2_meaning
export by term); `scripts/_generate_cluster_gate.py --cluster` (per-cluster gate: coverage + value-classified
tier profile + flag split + misfit surfacing); `scripts/_explore_tier_findings.py` (wide export / field
distribution / cross-tab).

**CORRECTION (2026-06-10) — tier findings are NOT positionally lost.** Earlier note said tier findings were
"stored positionally, no field-name column, ignore labels." That was an UNDER-READING of the schema. Every
l2_api tier finding IS labelled: `upsert_finding` writes a `finding_question_link(finding_id, question_id)`
to the obs-catalogue question for that field (FIELD_OBS/FACULTY_OBS/LOCATION_OBS in
`_apply_verse_read_meaning.py`; idempotency key = (vcid, mid, prov, obs_id)). 100% of 186,455 l2_api findings
are linked → fully recoverable verse→term→tier-field. Migration **M57 (schema 3.31.0)** adds read-only views
**`v_l2_tier`** (tier findings, catalogue-labelled with question_code/tier/component_title) and
**`v_l2_meaning`** (paragraph per verse-term). So verse-level tier data is fully explorable (per-field +
cross-tab). The researcher's "ignore sequencing" was only ever about the report, not the data — no backfill
needed. The `l2_meaning` paragraph remains the human deliverable.

**Pending:** retire the existing out-of-rule standalone T2 paragraphs (from earlier API fan-out + the FLAG→T2
moves) per [[feedback_t2_reference_flag_reclassify]]; finish M02 (~36% left); per-cluster gate before sign-off.
