# M05 (Love) — CC verification of Chat Flags 5 & 6

**File:** wa-m05-flag5-6-cc-verification-v1-20260619.md · **Date:** 2026-06-19 · **Author:** Claude Code
**Status:** VERIFICATION ONLY — no DB writes made. Both flags asked for CC verification (Flag 5) / a researcher scope decision (Flag 6). Per GR-PROG-005 / GR-PROC-002 nothing is corrected here; recommendations await your go-ahead.

---

## Flag 5 — chesed A/B split (data quality, HIGH) — **CONFIRMED**

Chat's read is correct, and stronger than stated: the "shame" bucket is **not partly** mis-routed, it is **entirely** mis-routed.

### H2617B che.sed — gloss `"shame"`, 289 occurrences
Per-occurrence senses (ESV `target_word`, top of distribution):

| n | sense | n | sense |
|---|---|---|---|
| 210 | steadfast love | 4 | loyalty / loyally |
| 25 | kindness | 3 | mercy |
| 12 | kindly | 2 | merciful / kind / faithfulness / devout / devotion |
| 11 | love | — | — |
| 6 | good deeds / favor | — | — |

- Occurrences whose sense is actually **shame / reproach / disgrace: 0**. Not a single one.
- Valence: righteous 69 · neutral 60 · sinful 14 · commanded 3 (the rest NONE) — a kindness/loyalty profile, not a shame profile.
- **All 289 are chesed-I (loving-kindness).** The `"shame"` gloss on the H2617B term row is a lexical-label error, not a real sense split. (The genuine chesed-II "reproach" sense — Lev 20:17, Pro 14:34 — is ~2 occ and is **not in this bucket at all**.)

### H2616B cha.sad — gloss `"to shame"`, but its 2 occurrences read `"merciful"`
Same artefact at tiny scale; H2616A ("be kind") and H2616B both resolve to the kindness sense.

### H2617A che.sed — gloss `"kindness"`, 169 occ → senses steadfast love 121, kindness 14, … **correct, no action.**

### Impact
chesed is the single highest-frequency term in M05 and the central OT love word. A term row mislabelled "shame" misleads any reader/analyst doing a term-level scan (exactly what tripped Chat), even though the **per-occurrence** sense and valence data underneath are correct. So the corpus data is sound; the **term gloss label is wrong**.

### Recommended correction (reversible, your call)
- Re-gloss **H2617B** `"shame"` → `"kindness"` (or `"steadfast love"`), and **H2616B** `"to shame"` → `"be kind"`, so the term label matches its occurrences. Low risk — touches the `mti_terms.gloss` label only; no occurrence, valence, or faculty data changes.
- I would do this via a governed `_apply_*` script (`--dry-run`/`--live`, pre-run backup, idempotent, integrity check) and leave the old gloss recorded in `notes` for reversal.

---

## Flag 6 — corporate / no-faculty band (scope) — **CONFIRMED**

Every term Chat named returns **zero** inner-being faculty across all its M05 occurrences:

| Strong's | term | occ | with-faculty |
|---|---|---|---|
| G1577 | ekklēsia (assembly) | 85 | 0 |
| G2842 | koinōnia (participation) | 24 | 0 |
| H4744 | miq.ra (assembly) | 22 | 0 |
| G2844 | koinōnos | 12 | 0 |
| H6116 | a.tsa.rah (assembly) | 11 | 0 |
| G2026 | epoikodomeō (build up) | 11 | 0 |
| G1731 | endeiknumi (show) | 7 | 0 |
| G2643 | katallagē (reconciliation) | 4 | 0 |
| G5381 | filoxenia (hospitality) | 2 | 0 |

**Contrast confirmed:** G3618 oikodomeō ("build") = **16/16 with faculty** — the metaphorical *edify / build up* (encouragement) sense is a genuine inner-being use, so the "build" family must **not** be swept aside wholesale.

These no-faculty terms describe the **corporate/relational context and acts in which love operates** (assembly, partnership, reconciliation, hospitality), not an inner-being characteristic. They are **set-aside / co-term candidates**, not a distinct characteristic band.

### Recommended handling (your decision — cluster vs set-aside)
- Treat the nine no-faculty terms as **set-aside** for M05's characteristic distillation (occurrence-level `verse_context.set_aside_reason`, or term-level `mti_terms.cluster_code=NULL` for any that are wholly out of scope), keeping oikodomeō/oikodomē in scope.
- This is a scope judgement, so I'll prepare a reversible set-aside script **only on your instruction**, mirroring the M03 out-of-scope pattern.

---

## What I need from you
1. **Flag 5:** approve the gloss correction (H2617B, H2616B) — yes/no.
2. **Flag 6:** decide cluster-vs-set-aside; if set-aside, I prepare the reversible script.
3. Both can wait until you finish M05 in Chat — no DB writes happen until you direct them.
