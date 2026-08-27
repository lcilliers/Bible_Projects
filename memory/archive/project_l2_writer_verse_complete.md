---
name: project_l2_writer_verse_complete
description: Fix (2026-06-09, researcher catch). The L2 writer was initially CLUSTER-SCOPED (wrote only the run-cluster's terms). The agreed design (feedback_characteristic_is_typed_term_in_verse) is VERSE-COMPLETE: entering by a cluster's verses, process each verse fully and write tier findings for EVERY in-scope term in it, each saved to its own term's cluster (via finding.mti_term_id). Rebuilt the writer verse-complete: M01 entry (922 verses) now writes 949 OTHER-cluster term-findings across 43 clusters that the narrow writer omitted; VERSE findings now span 45 clusters. Idempotent de-dup so each term-in-verse is written once.
metadata:
  type: project
---

**Researcher catch (2026-06-09):** with ~44% of verses cross-cluster (multi-term), the writer should write
findings in the OTHER clusters too — and that evidence was missing. Correct: my `_apply_l2_write.py` was
**cluster-scoped** (only the `--cluster` terms), but the design [[feedback_characteristic_is_typed_term_in_verse]]
is **verse-complete** (one verse-read completes ALL its in-scope terms, saved to each cluster).

**Quantified gap:** M01's 922 verses hold **2045 in-scope term-occurrences = 1036 M01 + 1009 other-cluster**
(44 clusters). The cluster-scoped writer wrote the 1036, omitted the 1009.

**Fix (rebuilt writer):** enter by `--cluster` (the verses containing its terms); process **every** in-scope
term-in-verse at those references; write each finding with its own `mti_term_id` (→ its cluster, automatic);
idempotent skip of already-written term-in-verses (verse-coverage / no-double-work). Faculty asserted only
per the *term's* cluster (M15 removed from the map — its cognition was induced, see
[[feedback_faculty_must_be_per_term_not_per_cluster]]; M01 affect kept).

**Result (live):** M01 entry now writes **949 other-cluster term-findings across 43 clusters** (M23 78, M05
70, M41 56, M30/M25/M22 39…); **VERSE findings now span 45 clusters** (was 2), total 15912. Running each
cluster as an entry + de-dup converges to full once-only coverage. The per-term lexical finding is still
isolated (L2 is not cross-term); the cross-term *relationships* remain the layer above. Pending refinements
unchanged: per-term faculty derivation; broad-gloss-polysemy escalation ([[project_l2_multicluster_learnings_20260609]]).
