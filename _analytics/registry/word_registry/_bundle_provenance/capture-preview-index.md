# Capture Preview — Index

**Generated:** 2026-04-30 07:55 UTC
**Bundle dir:** `research\investigations\ai_question_test_bundle_20260429`

Read-only parsing of AI second-tier analysis output.  No DB writes.  Validate the per-word `parsed-capture-preview.md` files before approving capture.

## Per-word output

| Word | Folder | Analysis file | Session log | Prompts | A/P/S/N | New | Gap |
| --- | --- | --- | --- | ---: | --- | ---: | ---: |
| R064 forgiveness | R064 forgiveness | [WA-R064-second-tier-analysis-v1-2026-04-30.md](R064 forgiveness/WA-R064-second-tier-analysis-v1-2026-04-30.md) | [WA-session-log-R064-second-tier-v1-2026-04-30.md](R064 forgiveness/WA-session-log-R064-second-tier-v1-2026-04-30.md) | 189 | A=91 P=49 S=19 N=30 | 19 | 21 |
| R068 grace | R068 grace | [WA-grace-prompt-test-v1-2026-04-29.md](R068 grace/WA-grace-prompt-test-v1-2026-04-29.md) | _(none)_ | 179 | A=110 P=39 S=11 N=19 | 14 | 36 |
| R023 compassion | r023-compassion | [WA-R023-second-tier-analysis-v1-2026-04-30.md](r023-compassion/WA-R023-second-tier-analysis-v1-2026-04-30.md) | [WA-session-log-R023-second-tier-v1-2026-04-30.md](r023-compassion/WA-session-log-R023-second-tier-v1-2026-04-30.md) | 188 | A=112 P=40 S=11 N=25 | 127 | 20 |
| R030 contrition | r030 contrition | [WA-R030-second-tier-analysis-v1-2026-04-30.md](r030 contrition/WA-R030-second-tier-analysis-v1-2026-04-30.md) | [WA-session-log-R030-second-tier-v1-2026-04-30.md](r030 contrition/WA-session-log-R030-second-tier-v1-2026-04-30.md) | 189 | A=112 P=25 S=29 N=23 | 33 | 56 |
| R062 fellowship | r062 fellowship | [WA-R062-second-tier-analysis-v1-2026-04-30.md](r062 fellowship/WA-R062-second-tier-analysis-v1-2026-04-30.md) | [WA-session-log-R062-second-tier-v1-2026-04-30.md](r062 fellowship/WA-session-log-R062-second-tier-v1-2026-04-30.md) | 189 | A=93 P=54 S=13 N=29 | 31 | 35 |

## Capture-target proposal

Each per-word file's §4 enumerates the proposed DB targets and counts.  No writes occur until the researcher approves a follow-up apply script.

**Proposed targets:**
- Per-prompt response → `wa_finding_catalogue_links` linking finding ↔ v2 catalogue question (coverage = full/partial/no_finding/not_applicable from A/P/S/N)
- New finding (per-prompt or session-log §7.2) → `wa_session_b_findings` (finding_type='OBSERVATION', author='claude_ai', session_b_instruction='WA-second-tier-analysis-instruction-v1-2026-04-30.md')
- Complete-silence + partial gaps (§8.1, §8.2) → `wa_session_research_flags` (flag_code='SB_FINDING')
- Session D implications (§11) → `wa_session_research_flags` (flag_code='SD_POINTER')
- RESEARCHER_DECISION items (§9) → `wa_session_research_flags` (proposed new flag_code 'RESEARCHER_DECISION'; awaits researcher approval)