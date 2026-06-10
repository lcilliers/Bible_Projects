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

**Pending:** retire the existing out-of-rule standalone T2 paragraphs (from earlier API fan-out + the FLAG→T2
moves) per [[feedback_t2_reference_flag_reclassify]]; optional engine-checkpoint logging for CC runs.
