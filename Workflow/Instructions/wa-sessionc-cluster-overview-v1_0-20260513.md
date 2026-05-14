# Session C Cluster Publication — Process Overview

**Document type:** Process overview / orientation reference.
**Audience:** the researcher and Claude Code returning to the process.
**Version:** v1.0
**Date:** 2026-05-13
**Supersedes:** none (new — codified after M15's successful first publication on 2026-05-12)

This document is the master reference for the Session C cluster publication process. It ties together the shared style instruction, the per-chapter instructions, the appendices instruction, the scripts that build per-chapter inputs and assemble the final document, and the artefacts produced at each stage. If you are returning to this process after a gap, start here.

---

## 1. What Session C Cluster produces

A **plain-English published study** of one cluster's family of inner-being characteristics — a reader-facing document, structured as seven chapters and three appendices, delivered as both a master Markdown file and a PDF. The study draws every analytical claim from the Phase 8 cluster_finding evidence stored in the database, with key verses quoted verbatim throughout.

The per-word Session C model (one study per registry word) is fully superseded by the cluster model. The published study is the only Session C output.

**Audience of the study:** an intelligent reader with no familiarity with the project's analytical vocabulary. The reader is reading the study as they would read any serious essay on the Bible's treatment of a theme.

---

## 2. Inputs and preconditions

A cluster is ready for Session C publication when:

| Condition | Where to check |
|---|---|
| `cluster.status = 'Analysis Completed'` | `cluster` table |
| Phase 8 catalogue pass complete (~189 prompts T0–T7 answered) | `cluster_finding` rows joined to `wa_obs_question_catalogue` |
| Every active sub-group has `core_description` populated | `cluster_subgroup` rows |
| Every active sub-group has at least one VCG with anchor verses | `verse_context.is_anchor=1` joined to `verse_context_group` |
| `cluster.short_name` populated (≤15 chars; used in filenames) | `cluster` table |
| Cluster's terms are placed via `mti_term_subgroup` | `mti_term_subgroup` |

If any precondition is unmet, fix before publication. The per-chapter input generator will render thinly or render placeholders if data is missing (e.g. `_(description pending)_` if a sub-group's `core_description` is empty).

**M15 precedent:** M15-H (Logos) had an empty `core_description` until 2026-05-12, when the researcher authored it (the Living Word indwelling the inner being, the embodiment of Christ as the Word of God). The publication pipeline was paused until that field was filled.

---

## 3. The instruction documents

Every chapter run loads the shared style/method document plus one chapter-specific instruction. The appendices share a single combined instruction.

| Document | Governs | Loaded by |
|---|---|---|
| [wa-sessionc-cluster-style-method-v1_1-20260512.md](wa-sessionc-cluster-style-method-v1_1-20260512.md) | voice, tone, jargon discipline, citation discipline, tier→theme mapping, silence principle, on-completion reverse audit, on-completion self-review | every chapter run + appendix run |
| [wa-sessionc-cluster-ch1-instruction-v1_0-20260512.md](wa-sessionc-cluster-ch1-instruction-v1_0-20260512.md) | Chapter 1 — What this study is (single ~300–500w opening) | the Ch 1 run |
| [wa-sessionc-cluster-ch2-instruction-v1_0-20260512.md](wa-sessionc-cluster-ch2-instruction-v1_0-20260512.md) | Chapter 2 — The characteristics in this study (~250w per characteristic) | the Ch 2 run |
| [wa-sessionc-cluster-ch3-instruction-v1_0-20260512.md](wa-sessionc-cluster-ch3-instruction-v1_0-20260512.md) | Chapter 3 — The divine pattern (cluster-wide spine + per-SG variation paragraphs, ~1500–2500w total) | the Ch 3 run |
| [wa-sessionc-cluster-ch4-instruction-v1_0-20260512.md](wa-sessionc-cluster-ch4-instruction-v1_0-20260512.md) | Chapter 4 — Where each characteristic lives in the person (T2+T3, ~800–1500w per SG) | the Ch 4 run |
| [wa-sessionc-cluster-ch5-instruction-v1_0-20260512.md](wa-sessionc-cluster-ch5-instruction-v1_0-20260512.md) | Chapter 5 — How each characteristic works (T4+T5+T1, ~800–1500w per SG) | the Ch 5 run |
| [wa-sessionc-cluster-ch6-instruction-v1_0-20260512.md](wa-sessionc-cluster-ch6-instruction-v1_0-20260512.md) | Chapter 6 — How each characteristic relates to the others (T6, ~400–800w per SG) | the Ch 6 run |
| [wa-sessionc-cluster-ch7-instruction-v1_0-20260512.md](wa-sessionc-cluster-ch7-instruction-v1_0-20260512.md) | Chapter 7 — The view from outside Scripture (T7 + general clinical-science knowledge, ~400–500w per SG) | the Ch 7 run |
| [wa-sessionc-cluster-appendices-instruction-v1_0-20260512.md](wa-sessionc-cluster-appendices-instruction-v1_0-20260512.md) | Appendices A (Terms), B (Key verses), C (Method note) — one combined run | the appendix run |

Chapter 8 (originally "What this study does not yet address") was dropped from the publication on 2026-05-12. Outstanding research and open questions are tracked instead in a separate post-publication report (see §10).

---

## 4. The scripts

| Script | Reads | Writes |
|---|---|---|
| `scripts/_generate_cluster_session_c_inputs_v2_20260512.py` | `cluster`, `cluster_subgroup`, `mti_term_subgroup`, `mti_terms`, `verse_context`, `verse_context_group`, `wa_verse_records`, `cluster_finding`, `wa_obs_question_catalogue` | 10 per-chapter input files (`Sessions/Session_Clusters/{CODE}/inputs/wa-cluster-{CODE}-{key}-input-v1-{date}.md`) |
| `scripts/_assemble_cluster_publication_v1_20260512.py` | the highest-version draft for each chapter / appendix in the publication folder | a single master Markdown file + a PDF in `Sessions/Session_Clusters/{CODE}/` |

No other scripts are involved in Session C cluster publication. The two scripts together are the deterministic CC side of the process — DB → inputs → (AI authoring) → assembled master + PDF.

---

## 5. The chapter/appendix structure

| Section | Title | Lens | Length |
|---|---|---|---|
| Chapter 1 | What this study is | cluster-wide T0+T1 synthesis | ~300–500w total |
| Chapter 2 | The characteristics in this study | sub-group descriptions + anchor verses | ~250w per characteristic |
| Chapter 3 | The divine pattern | cluster-wide T0 spine + per-SG T0 variations | ~1500–2500w total |
| Chapter 4 | Where each characteristic lives in the person | T2 + T3 | ~800–1500w per characteristic |
| Chapter 5 | How each characteristic works | T4 + T5 + T1 | ~800–1500w per characteristic |
| Chapter 6 | How each characteristic relates to the others | T6 | ~400–800w per characteristic |
| Chapter 7 | The view from outside Scripture | T7 + general clinical-science knowledge | ~400–500w per characteristic |
| Appendix A | Terms in this study | mti_term_subgroup (two layers: key + supportive) | ~700–1000w total |
| Appendix B | Key verses | verse_context anchors + analysis_note + meaning-group context | reference table |
| Appendix C | Method note | cluster metadata + plain-English acknowledgement | ~150w |

**Internal lens codes (T0–T7) never appear in the published prose.** They map to thematic names per the shared style document §5.

---

## 6. CC vs AI division of labour

The process is built on a clean split:

| Role | Does | Does not do |
|---|---|---|
| Claude Code (deterministic) | DB extraction, per-chapter input file generation, master-document assembly, PDF rendering | author prose, make analytical judgements, decide voice |
| Claude AI (interpretative) | author prose into AI-WRITE zones, weave evidence into essayistic chapters, write appendix commentaries and the method note | read the DB directly, run SQL, change structure of inputs, invent verses or findings |

AI never reads the DB. AI reads only the per-chapter input file, the chapter's instruction, and the shared style/method document.

---

## 7. End-to-end workflow

For a single cluster:

```text
1. Researcher confirms cluster preconditions (§2)
   ↓
2. CC: python scripts/_generate_cluster_session_c_inputs_v2_20260512.py --cluster {CODE}
   → produces 10 input files in Sessions/Session_Clusters/{CODE}/inputs/
   ↓
3. For each chapter (1, 2, 3, 4, 5, 6, 7):
   AI run: load wa-sessionc-cluster-style-method-v1_1 + wa-sessionc-cluster-ch{N}-instruction
          read the chapter's input file
          author prose into every AI-WRITE zone
          perform reverse audit (shared §10) + self-review (shared §11)
          return the chapter draft
   → saved as WA-{CODE}-ch{N}-draft-v{V}-{date}.md (V increments on each revision)
   ↓
4. Appendices (single run):
   AI run: load wa-sessionc-cluster-style-method-v1_1 + wa-sessionc-cluster-appendices-instruction
          read all three appendix input files together
          author prose into every AI-WRITE zone
          fill in missing "Meaning of the term in this study" cells in App B
          return three appendix drafts
   ↓
5. Researcher reviews each chapter and appendix draft; iterates with AI for v2, v3 as needed
   ↓
6. Drafts gathered in a publication folder
   (M15 used: Sessions/Session_Clusters/{CODE}/files published/)
   ↓
7. CC: python scripts/_assemble_cluster_publication_v1_20260512.py \
          --cluster {CODE} \
          --source "Sessions/Session_Clusters/{CODE}/files published" \
          --title "{Cluster title}" \
          --subtitle "{Subtitle}"
   → produces the master .md + .pdf in Sessions/Session_Clusters/{CODE}/
   ↓
8. (Optional, post-publication) Generate the outstanding-research report (§10)
```

Each chapter run is **independent** — AI sees only one chapter's input at a time. Cross-chapter consistency is enforced through the brief one-line characteristic profiles included at the top of every input file.

---

## 8. Artefacts produced

For one cluster, a complete Session C publication run produces (paths relative to project root):

```text
Sessions/Session_Clusters/{CODE}/
├── inputs/                                       # CC-produced; one per chapter+appendix
│   ├── wa-cluster-{CODE}-ch1-input-v1-{date}.md
│   ├── wa-cluster-{CODE}-ch2-input-v1-{date}.md
│   ├── wa-cluster-{CODE}-ch3-input-v1-{date}.md
│   ├── wa-cluster-{CODE}-ch4-input-v1-{date}.md
│   ├── wa-cluster-{CODE}-ch5-input-v1-{date}.md
│   ├── wa-cluster-{CODE}-ch6-input-v1-{date}.md
│   ├── wa-cluster-{CODE}-ch7-input-v1-{date}.md
│   ├── wa-cluster-{CODE}-appa-input-v1-{date}.md
│   ├── wa-cluster-{CODE}-appb-input-v1-{date}.md
│   └── wa-cluster-{CODE}-appc-input-v1-{date}.md
├── files published/                              # AI-authored drafts (multiple versions per chapter)
│   ├── WA-{CODE}-ch1-draft-v{V}-{date}.md
│   ├── WA-{CODE}-ch2-draft-v{V}-{date}.md
│   ├── ...
│   ├── WA-{CODE}-appa-draft-v{V}-{date}.md
│   ├── WA-{CODE}-appb-draft-v{V}-{date}.md
│   └── WA-{CODE}-appc-draft-v{V}-{date}.md
├── wa-cluster-{CODE}-publication-v1-{date}.md   # CC-assembled master document
└── wa-cluster-{CODE}-publication-v1-{date}.pdf  # CC-rendered PDF
```

Input filenames are lowercase `wa-`; draft filenames are uppercase `WA-` (a researcher convention used to distinguish AI output from CC output at a glance).

---

## 9. Quality controls

**Built into the shared style document (v1.1):**

- **Reverse audit on completion (§10).** Walk every finding in every EVIDENCE block in scope; confirm each is either present in the prose, justifiably omitted as routine-silent, or redundant. Walk every required-cite key verse; confirm each is quoted verbatim at least once. Walk each tier in scope; confirm engagement.
- **Self-review pass on completion (§11).** Repetition → overreach → padding → tonal drift → structural drift.
- **Order of operations (§12).** Write → audit → review → return.

**Built into each chapter instruction:**

- Per-chapter quality bar — specific structural and citation requirements that section must meet before passing.
- Per-chapter overlap-avoidance guidance — explicit statement of which other chapters cover which material, so the AI does not stray into adjacent territory.

**Built into the silence principle (shared §6, sharpened in v1.1):**

- Name a silence only when its absence is meaningful — *expectation-then-absence* or *silence-shapes-the-characteristic*.
- Routine absence needs no comment.

---

## 10. Outstanding research report (deferred deliverable)

After a cluster's Session C publication is complete, a separate CC-produced report is planned to inventory outstanding research and open questions for that cluster. Not yet built. Planned shape:

1. **Gap findings.** All `cluster_finding` rows where `finding_status='gap'` with prompt context.
2. **Under-developed lens (T7).** Inventory of T7 prompts where the sub-group was not separately addressed.
3. **LXX / Greek-of-the-Hebrew gap.** Standard programme-wide acknowledgement.
4. **Cross-cluster pointers.** `wa_cross_registry_links` and `SD_POINTER` flags touching the cluster's terms.
5. **Term-level open items.** Cluster terms with `status` in (`extracted_thin`, `candidate_delete`) or with open quality flags.
6. **VC-status anomalies.** Cluster terms whose `vc_status` is not `Complete`.
7. **Open observation prompts.** Catalogue prompts in scope but with no `cluster_finding` row.

Output: `Sessions/Session_Clusters/{CODE}/wa-cluster-{CODE}-outstanding-research-v1-{date}.md`. Built by a future script `_generate_cluster_outstanding_research_v1_{date}.py`. Spec lockable when the researcher is ready to consume.

---

## 11. M15 — the test case

M15 (Wisdom, Understanding and Knowledge) was the first cluster published through this process. Key facts:

| | Value |
|---|---|
| Cluster code | M15 |
| Short name | Wisdom |
| Description | Wisdom, Understanding and Knowledge |
| Status | Analysis Completed |
| Active sub-groups | 9 (M15-A through M15-H + BOUNDARY) |
| Anchor verses | 55 (across 55 VCGs) |
| Findings underlying the study | 1,724 (1,454 sub-group findings + 23 cluster-synthesis + 9 gap + 238 silent) |
| Master publication length | ~34,300 words / 212 KB |
| PDF size | 1.06 MB |
| Drafts produced | ch1 v2 · ch2 v2 · ch3 v2 · ch4 v3 · ch5 v2 · ch6 v2 · ch7 v2 · appa v1 · appb v1 · appc v1 |
| Final outputs | [wa-cluster-M15-publication-v1-20260512.md](../../Sessions/Session_Clusters/M15/wa-cluster-M15-publication-v1-20260512.md) and [.pdf](../../Sessions/Session_Clusters/M15/wa-cluster-M15-publication-v1-20260512.pdf) |

**M15 design decisions that shaped the process** (all incorporated into the instructions above):
- Plain-English audience discipline with explicit jargon-avoid list (after design v2 → v3).
- Per-chapter input files instead of a single monolithic framework (after design v3 → v4, validated by the Ch 4 test on 2026-05-12).
- Chapter 8 dropped; outstanding research moved to a separate post-publication report.
- The silence principle sharpened in style doc v1.1 after Ch 4's first draft showed how easy it is to over-cite silences.
- Reverse audit and self-review added to the shared style after Ch 4 confirmed the pattern works.

---

## 12. Reuse for future clusters

The instruction set and the two scripts are **cluster-agnostic** — they take a `--cluster {CODE}` argument and work against any cluster whose preconditions are met. For each new cluster, the per-cluster human inputs are:

1. **Confirm preconditions** (§2). If `core_description` is missing on any sub-group, author it.
2. **Choose the publication title and subtitle** (passed to the assembler as `--title` and `--subtitle`).
3. **Choose the publication folder name** convention (M15 used `files published/`; consistent naming aids the assembler's auto-discovery).

The instructions themselves do not change per cluster. If a future cluster's data shape requires structural changes to the chapters (e.g. a cluster with no Hebrew/Greek split because it's NT-only), revisit the relevant chapter instructions and bump versions per GR-FILE-003.

---

## 13. Change log

**v1.0 (2026-05-13):** First issue. Codifies the Session C cluster publication process after M15's successful first publication on 2026-05-12. Captures inputs, scripts, instructions, division of labour, end-to-end workflow, artefacts, quality controls, and the deferred outstanding-research report. M15 named as the precedent test case.
