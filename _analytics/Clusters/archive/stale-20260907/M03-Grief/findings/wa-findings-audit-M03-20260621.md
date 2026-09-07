# Findings audit — M03

_Run: 20260621 · read-only · spec wa-findings-audit-spec-v1_0_  

**GATE 1 (findings → DB):** PASS 6 · REVIEW 5 · WARN 3 · STOP 0
**GATE 2 (essay):** PASS 1 · REVIEW 3 · WARN 1 · STOP 0

> Each item below is written to be read on its own. The bracket shows the check id and severity; *STOP* = blocks unless you release it · *REVIEW* = needs your sign-off · *WARN* = hygiene · *PASS* = clear. Suggested action: CA-1 accept · CA-2 CC fixes the file · CA-3 you direct a file/DB fix · CA-4 set aside & redo in Chat.

## Gate 1 — findings

- **REVIEW** — 4 silent answer(s) are NOT explained by an expected cause and may be real gaps: A T1.4.3, F T1.5.2, I T1.4.3, J T1.3.1  `[FA-10 · REVIEW → CA-1]`
- **REVIEW** — The extract (generated 20260619) holds 835 verses but the current in-scope corpus is 595 (+240). The extract is stale — verses were set aside or re-clustered after it was built. Regenerate before re-using it as a Chat input.  `[FA-11 · REVIEW → CA-2]`
- **REVIEW** — Terms with NO inner-being faculty across all occurrences (candidate set-aside / co-term, your call): a.mal (trouble, 53), dim.ah (tears, 22), ma.rar (to provoke, 13), che.vel (pain, 9), basanizō (to torture: torture, 8)  `[FA-13 · REVIEW → CA-1]`
- **REVIEW** — 2 open interpretive fork(s)/flag(s) to acknowledge before capture: ## Open items carried to the cross-cluster pass | ## Review register (RESEARCHER DECISION required)  `[FA-16 · REVIEW → CA-1]`
- **REVIEW** — 1 possibly-unsubstantiated superlative(s) in the findings: "the largest single body of inner-being"  `[FA-23 · REVIEW → CA-2]`
- **WARN** — Silent-answer counts per characteristic — A:10; B:6; C:6; D:7; E:6; F:7; G:8; H:4; I:8; J:11. Marker is prose-style, so counts are approximate.  `[FA-08 · WARN]`
- **WARN** — Silence is marked with the 'prose' convention. The recommended standard is the M06-style 'X of Y per tier' coverage line; this cluster differs, so silence isn't a clean queryable field.  `[FA-09 · WARN → CA-1]`
- **WARN** — Extract carries a stale/missing provenance string.  `[FA-17 · WARN → CA-2]`
- **PASS** — All findings present: 10 characteristics, 10 tier-answer sets, 10 profiles, cluster synthesis.  `[FA-01 · PASS]`
- **PASS** — Characteristic set is consistent across definitions, tier-answers and profiles (10 each).  `[FA-05 · PASS]`
- **PASS** — No characteristic key collisions in the DB.  `[FA-06 · PASS]`
- **PASS** — Every characteristic carries a definition.  `[FA-07 · PASS]`
- **PASS** — 180 out-of-scope occurrences are documented with a set-aside reason.  `[FA-12 · PASS]`
- **PASS** — High-frequency term glosses are consistent with their per-occurrence senses.  `[FA-14 · PASS]`

## Gate 2 — essay

- **REVIEW** — Essay covers 10/10 characteristics. Grounding: 66 of 93 substantive statements carry NO verse citation (in the statement or the next sentence). Each uncited statement is either an ungrounded analytical claim (fix) or acceptable framing/synthesis (accept) — review. Examples: "Grief is the largest single body of inner-life language in the Bible's account of human sorrow,…" | "Scripture does not hurry the grieving toward consolation or treat their tears as a failure of f…" | "It records, at length and without embarrassment, the weeping of a bereaved father, the groaning…"  `[FA-21 · REVIEW → CA-1]`
- **REVIEW** — Researcher check: confirm the essay asserts nothing the captured findings don't carry (cannot be verified mechanically).  `[FA-22 · REVIEW → CA-1]`
- **REVIEW** — Possibly-unsubstantiated superlative(s) in the essay: "the largest single body of inner-life"; "the largest body of inner-life"  `[FA-23 · REVIEW → CA-2]`
- **WARN** — Project jargon leaked into the reader-facing essay: ['characteristic', 'finding']  `[FA-20 · WARN → CA-2]`
- **PASS** — All 23 cited verses exist in the corpus.  `[FA-18 · PASS]`

## To resolve

No STOPs. 

**8 REVIEW item(s)** need your decision (record the corrective action against each).
