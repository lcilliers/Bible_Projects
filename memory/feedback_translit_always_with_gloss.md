---
name: feedback_translit_always_with_gloss
description: "TEMPLATE RULE (2026-06-15): a transliteration is NEVER shown in isolation — always pair it with its gloss (and cluster where relevant)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 8a5e10ea-2d9d-4bb9-8ca3-fb979500309e
---

GOVERNING TEMPLATE RULE (researcher, 2026-06-15, vc=1630 review): **a transliteration must never appear in isolation** — always render it WITH its gloss. e.g. a compound co-term is `ne.phesh "soul: life" (M25)`, not `ne.phesh(M25)`. Applies to `ve_lexical` VE3 (compound) values, the templated narration ([[project_ve_lexical_normalisation_and_groundings]]), and any report/output that names a term by translit. The gloss is always available (mti_terms.gloss) — no excuse to drop it.

**Why:** a bare transliteration is unreadable to the researcher (who reasons by meaning, cf. [[feedback_use_cluster_full_names]]); the gloss is what carries the sense.

**How to apply:** whenever code emits `{translit}` or `{translit}({cluster})`, emit `{translit} "{gloss}" ({cluster})` instead.

Related: the same vc=1630 review surfaced deeper gaps (relational needs an OBJECT, the "how"/governing-predicate like "seized" isn't stored, location should derive from co-occurring constitutional TERMS not English seat-words, some T2 qualifiers are soft-deleted) — see `research/VE-lexical/wa-ve-narration-feedback-vc1630-20260615.md` and [[project_verse_extraction_cause_side_gap]].
