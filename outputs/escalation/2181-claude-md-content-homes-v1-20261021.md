# #2181: Where each part of the old CLAUDE.md now lives (v1, 2026-10-21)

Escalation #2181 (option B of the #2179 review; an element of the IBA app reset, #2177). CLAUDE.md
is cut to a short entry file: pointers only, as the control map requires (`cfg_control_home`,
kind `session_entry`, #2180). Before the cut, every rule it held was checked for a home in
config. Rules with no home were added (migration
`iba/app/migration/claude_md_rules_to_config_v1_20261021.py`, run
`DEVMODE-2181-CLAUDE-MD-RULES-20261021`).

**The old file, whole, is history:** `archive/docs/claude-md-history-to-20261021.md` (703 lines).
Read it only deliberately, to see a past state. It is not a source for how things are now.

## Banners (old lines 1–345)

| Old content | Now lives in |
|---|---|
| Authoritative source: `C:\Bible_study_projects` only | `cfg_behaviour_rule` 83 `authoritative-source-only` (**new**) |
| Study on hold (2026-10-19) | `cfg_setting governance.study_status` (**new**, printed at start); reason on #2172 |
| `AskUserQuestion` banned | `cfg_behaviour_rule` 16; `.claude/settings.json` permissions.deny |
| IBA app session start: run `Start-Iba.ps1`; start at USER-GUIDE; rules are `cfg_*` rows, changed through Propose | `.claude/commands/start-project.md`; `governance.rules_must_be_config_driven`; GOVERNANCE.md §3A; USER-GUIDE.md |
| Base layer moved to IBA; §4/§5/§7/§8 superseded | `governance.scope_iba_db`; history |
| `bible_research.db` prose-only | `governance.scope_research_db`; GOVERNANCE.md §81 |
| Fan-out replaces cluster-by-cluster analysis; strands; focused capture; `ib_node` principle | `cfg_behaviour_rule` 84 `fan-out-progressive-strands` (**new**) |
| Prose is the researcher's; narrative drafts are files written on instruction | `cfg_behaviour_rule` 85 `prose-only-on-instruction` (**new**) |
| Essay regenerated as *Inner Being in Operation*; adjust original to new; each strand updates the chapters and records the weave in the register; chapter table is the authority | `cfg_behaviour_rule` 86 `narrative-reset-and-weave-record` (**new**); 76; 78 |
| Voice: first person, personal, direct, easy to read, no project terms | the style guide `narrative.inner_being_style_guide_path` §3 (named by rule 86) |
| Chapter text: Held sections, ESV check, science later, Spirit in 13.1, Jesus in Ch 13 | `cfg_behaviour_rule` 87 `narrative-chapter-text-rules` (**new**) |
| Weave, don't fit; every observation placed; strand woven by activity; key characteristic gets a Ch 10 sub-chapter | `cfg_behaviour_rule` 88 `weave-not-fit` (**new**); 79 |
| Change of character | `cfg_behaviour_rule` 89 `change-of-character-recorded` (**new**) |
| Open threads register: in the escalation table; Match before every unit pull; Raise at ledger approval | `cfg_behaviour_rule` 74 (Match before every pull **added**) |
| No re-tagging | `cfg_behaviour_rule` 70 |
| Each strand checks its M47 verses for dropped placements (#1979) | `cfg_behaviour_rule` 93 `strand-checks-its-m47-verses` (**new**) |
| Read each verse in its whole passage, no framework; narration probes, explores figurative speech | `cfg_behaviour_rule` 91 `narration-probes-not-restates` (**new**); 73 |
| No unnecessary holding | `cfg_behaviour_rule` 92 `no-unnecessary-holding` (**new**) |
| Read by role; read outward; never close on "not X" | `cfg_behaviour_rule` 73 |
| Routing to Ch 13 (A/B/C); no correction pass | `cfg_behaviour_rule` 72 |
| The claims register keeps the narrative honest; reconcile a concept's claims when a chapter is touched | `cfg_behaviour_rule` 77 |
| Threads are networks of handles, cleared by cluster work | `cfg_behaviour_rule` 74 |
| Let Scripture speak | `cfg_behaviour_rule` 69 |
| Weaving carries meaning (#1930) | `cfg_behaviour_rule` 90 `weaving-carries-meaning` (**new**) |
| Writing standard (style guide path) | `cfg_setting narrative.inner_being_style_guide_path`; rule 69 |
| Scan glosses across all codes before reading a theme | `cfg_behaviour_rule` 94 `strand-pull-scans-glosses-across-codes` (**new**) |
| Verse sets only through the raw layer, never an inline STEP call | `cfg_behaviour_rule` 95 `verse-sets-only-through-raw-layer` (**new**) |
| Strand queue and per-strand progress (M25, fear, anger, M64, M18, M72, M09, M08, flesh and body, M07) | study state: the strand escalations (#1963, #1978, #1986, #1993, #1998, #2148, #2156, #2162, #2171) and threads; the old text is history |
| Strand-specific scope rulings (M72 scope, flesh and body scope, poor/needy dimensions) | the strand's own escalation history and its cluster folder files |
| July/June method banners (verse-first lexical, cycle authority, method reset) | history (they describe the pre-fan-out pipeline) |

## Sections §1–§14 (old lines 346–703)

| Old section | Now lives in |
|---|---|
| §1 What this project is | CLAUDE.md (one paragraph); `iba/app/CHARTER.md` |
| §2 Directory map | history (stale: `Sessions-v2/`, `engine/`); the control map's folder kinds |
| §3 Schema v3.33.0 (`bible_research.db`) | history; `cfg_table`/`cfg_column` and `iba/config/DBSchema/DBSchema.json` |
| §4–§8 Engine, STEP client, scripts, pipeline, data flow | history (provenance only since 2026-08-17) |
| §9 Interaction protocols | `cfg_behaviour_rule` 17–24 (class `chat`) |
| §10 Document architecture, programme state 2026-06-14 | history |
| §11 Common operations | history (mostly retired commands); current tools in USER-GUIDE.md |
| §12 Git | `cfg_behaviour_rule` 26; `governance.session_log_triggers_commit`; `governance.no_direct_github_publish`; `.claude/commands/session-close.md` (commit message form); `.gitignore` |
| §13 Environment | USER-GUIDE.md §1 (Python, STEP); `backup.*` settings (NAS backups) |
| §14 Controlled vocabulary (`bible_research.db`) | history; `cfg_enum` |

## Other places that pointed at CLAUDE.md, repointed

- `.claude/commands/start-project.md`: the conflicts line, and the study-hold condition (now `governance.study_status`)
- `.claude/commands/session-close.md`: the pre-authorisation line
- `.claude/commands/developer-mode.md`: the list of rules that still apply
- `iba/app/ps/Start-Iba.ps1`: its description
- `cfg_behaviour_rule` `enforced_by` texts that said "delivered by CLAUDE.md": 3 rows restated
- `iba/app/lib/cfgquality.py`:
  - the delivery check now verifies once that the start routine delivers every active rule (`init.py` → `lib/compliance.py`), not per row against CLAUDE.md or memory
  - the governance-setting orphan check now reads `lib/compliance.py` too; 51 false orphans, unseen since #2173, cleared
