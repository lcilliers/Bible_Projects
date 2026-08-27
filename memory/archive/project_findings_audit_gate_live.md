---
name: project_findings_audit_gate_live
description: A findings audit now gates findings-capture and essay production; run it for every cluster from M07 on
metadata: 
  node_type: memory
  type: project
  originSessionId: d51a2ae4-3564-40b3-84fd-2dc7fed902d8
---

LIVE (2026-06-21): a **findings audit** is the required pre-step before (a) capturing a cluster's findings into the DB and (b) producing the cluster essay. **Run it for M07 and every cluster onward — do not capture or write an essay without it.**

- **Spec:** `Workflow/Instructions/wa-findings-audit-spec-v1_0-20260621.md` (policy RESOLVED). 23 checks (FA-01…FA-23) across **Gate 1** (findings→DB) and **Gate 2** (essay).
- **Script:** `scripts/_audit_findings_v1_20260621.py --cluster MNN` (read-only; writes a plain-language report to `Sessions-v2/{CLUSTER}/findings/wa-findings-audit-{CLUSTER}-{date}.md`; non-zero exit on open STOP).
- **Outcomes:** STOP (blocks, but **researcher can release it** after CC reports it) · REVIEW (sign-off; blocks only if its corrective action is CA-3/CA-4) · WARN · PASS. **STOP set:** FA-01 files present · FA-05 characteristic-set consistent · FA-06 DB UNIQUE collision · FA-18 cited verse not in corpus.
- **Corrective actions:** CA-1 accept (researcher) · CA-2 minor in-file fix (CC may do alone) · CA-3 targeted file/DB fix (researcher-led) · CA-4 set aside & redo in Chat (researcher-approved).
- **Report must be self-explanatory** (policy 8.3) — plain language, no code-lookup needed.
- **Key checks proven useful:** FA-11 (stale-extract / verse-count reconciliation, e.g. M03 835 vs 595), FA-14 (gloss↔sense disambiguation artifact — caught chesed H2617B "shame"→"steadfast love"; M04 nichoach), FA-21 (essay coverage — all M03–M06 essays cover 100% of characteristics but cite only 2–4% of in-scope verses), FA-23 (scope-qualified superlatives — "the widest of any cluster").
- **Baseline (2026-06-21):** M03–M06 ran with **no STOPs**; REVIEW items only. (M07 in progress, M08 not started, M01–M02 are out-of-standard prototypes.)
- **Book-code gotcha:** verse existence must match on **book_id** not the literal string — the DB stores some books under >1 prefix (Php *and* Phili) and essays use shorter codes (2Co vs 2Cor). See `book_code_variants`.

Related: [[feedback_check_governance_layers_not_just_pipeline]] · [[project_findings_capture_file_as_finding]] · [[feedback_filing_is_first_class_governance]]
