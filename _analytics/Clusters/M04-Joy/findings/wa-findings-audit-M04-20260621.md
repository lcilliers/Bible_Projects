# Findings audit — M04

_Run: 20260621 · read-only · spec wa-findings-audit-spec-v1_0_  

**GATE 1 (findings → DB):** PASS 9 · REVIEW 3 · WARN 2 · STOP 0
**GATE 2 (essay):** PASS 3 · REVIEW 2 · WARN 0 · STOP 0

> Each item below is written to be read on its own. The bracket shows the check id and severity; *STOP* = blocks unless you release it · *REVIEW* = needs your sign-off · *WARN* = hygiene · *PASS* = clear. Suggested action: CA-1 accept · CA-2 CC fixes the file · CA-3 you direct a file/DB fix · CA-4 set aside & redo in Chat.

## Gate 1 — findings

- **REVIEW** — 1 silent answer(s) are NOT explained by an expected cause and may be real gaps: G T7.3.3  `[FA-10 · REVIEW → CA-1]`
- **REVIEW** — Terms with NO inner-being faculty across all occurrences (candidate set-aside / co-term, your call): ni.cho.ach (soothing, 43)  `[FA-13 · REVIEW → CA-1]`
- **REVIEW** — Possible gloss/sense mismatch (disambiguation artifact?): ni.cho.ach H5207 is glossed 'soothing' but its occurrences read 'pleasing' (32/43) and never 'soothing' — likely a disambiguation artifact  `[FA-14 · REVIEW → CA-3]`
- **WARN** — Silence is marked with the 'not-evidenced' convention. The recommended standard is the M06-style 'X of Y per tier' coverage line; this cluster differs, so silence isn't a clean queryable field.  `[FA-09 · WARN → CA-1]`
- **WARN** — Extract carries a stale/missing provenance string.  `[FA-17 · WARN → CA-2]`
- **PASS** — All findings present: 7 characteristics, 7 tier-answer sets, 7 profiles, cluster synthesis.  `[FA-01 · PASS]`
- **PASS** — Characteristic set is consistent across definitions, tier-answers and profiles (7 each).  `[FA-05 · PASS]`
- **PASS** — No characteristic key collisions in the DB.  `[FA-06 · PASS]`
- **PASS** — Every characteristic carries a definition.  `[FA-07 · PASS]`
- **PASS** — Silent-answer counts per characteristic — A:18; B:18; C:19; D:18; E:18; F:18; G:20.  `[FA-08 · PASS]`
- **PASS** — Extract verse count (999) matches the current in-scope corpus (999) exactly.  `[FA-11 · PASS]`
- **PASS** — 113 out-of-scope occurrences are documented with a set-aside reason.  `[FA-12 · PASS]`
- **PASS** — No unresolved interpretive forks flagged in the findings.  `[FA-16 · PASS]`
- **PASS** — No unsubstantiated programme-wide superlatives detected in the findings.  `[FA-23 · PASS]`

## Gate 2 — essay

- **REVIEW** — Essay covers 7/7 characteristics. Grounding: 69 of 90 substantive statements carry NO verse citation (in the statement or the next sentence). Each uncited statement is either an ungrounded analytical claim (fix) or acceptable framing/synthesis (accept) — review. Examples: "And joy is also the inner state the Bible is least sentimental about, because it insists on a q…" | "The same word for rejoicing names both the gladness of the righteous and the gloating of the cr…" | "The deepest thing this study discloses is that positive feeling, in Scripture, is never self-ju…"  `[FA-21 · REVIEW → CA-1]`
- **REVIEW** — Researcher check: confirm the essay asserts nothing the captured findings don't carry (cannot be verified mechanically).  `[FA-22 · REVIEW → CA-1]`
- **PASS** — All 16 cited verses exist in the corpus.  `[FA-18 · PASS]`
- **PASS** — No project jargon in the essay.  `[FA-20 · PASS]`
- **PASS** — No unsubstantiated superlatives in the essay.  `[FA-23 · PASS]`

## To resolve

No STOPs. 

**5 REVIEW item(s)** need your decision (record the corrective action against each).
