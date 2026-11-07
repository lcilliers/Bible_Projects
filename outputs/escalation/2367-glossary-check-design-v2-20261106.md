# #2367 glossary currency check: where the glossary is, and what remains

Replaces v1 (archived), whose main finding was wrong: I looked only in `iba.db` and `Workflow/Catalogue`, and concluded the glossary had no home. The config says where it is; I did not read it first (governance.past_precedent_investigation_signals_missing_config, B:34).

## Where the config puts it (checked live 2026-11-06)

| source | what it says |
|---|---|
| `cfg_behaviour_rule` 13 (sqlite.dont-assume-which-database) | `bible_research.db` holds prose only, the programme and glossary prose; `iba.db` holds process control, base data and analysis |
| `cfg_prose` `prose.book_stage_map` / `prose.book_output_dir` | book "Word Index and Glossary", working files in `Workflow/Glossary` |
| `cfg_control_home` kind `study_method` | the glossary is the authority for the programme and inner-being definitions, through `cfg_prose_concept` pointers |
| `cfg_prose_concept` | 6 pointers (glossary_role, characteristic, operation, m_code_cluster, t2, t3) naming glossary entries by `prose_section` id |
| `cfg_setting glossary.currency_check` | the 7 terms the controlled values point to; the check is build B10 |
| process | `iba/app/ps/Prose.ps1` (`-Step Search`, `ExportChapter`, `ImportChapter`, `SetStatus`, `ApplyPatch`): edits go as supersede patches |

## The live glossary: `database/bible_research.db`, table `prose_section`

- Section types `glossary_programme` (85 rows) and `glossary_contentious` (2); 78 are draft, 9 archived. All 7 terms of `glossary.currency_check` are there (ids 1043, 1046, 1047, 1048, 1066, 1069, 1089) and the pointers' ids match. Every entry is status `draft`, not approved; T2 and T3 were last updated 2026-09-05, the rest have no update date.
- `role` is in the contentious glossary, awaiting you (as `cfg_prose_concept` already says).
- Surface terminology: entries exist for `surface`, `word`, `family`, `family root`. A search of headings and bodies for the new cycle terms found: base form 1 hit, inflection 2, collection 1, subgroup 2, concept 3, derivation 0, surface group 0. Hits in a body are not a definition; I have not read them.

## What remains (nothing to choose about where)

1. **Draft the new surface terms** as glossary entries, through Prose.ps1 as supersede patches for your approval: base (base form), inflection, derivation, collection, surface group (behaviour, being, inner_being_state, other), subgroup, concept and concept domain. Definitions come from how the cycle uses them (the surface_term enums and the AI prompts), drafted for you to correct.
2. **The check (B10)**: a read of `bible_research.db prose_section` by heading for each term in `glossary.currency_check` plus the surface terms, reported as an advisory finding in `Config-Maintenance.ps1 -Step Validate`: missing, archived, or draft-only. This is a code change and a second database read, so its design comes to you first (B:105).

## Entries drafted (step 1 done)

Eight draft entries (base, inflection, derivation, surface group, subgroup, collection, concept, concept domain) are in `outputs/escalation/2367-glossary-surface-term-entries-v1-20261106.md` for your correction. The patch `archive/patches/wa-prose-glossary-surface-terms-v1-20261106.json` passed `Prose.ps1 -Step ApplyPatch -DryRun` (8 inserts into section type `glossary_programme`, status draft). Not applied.

## Design of the check (step 2)

- **Where:** a new quality-check function in `iba/app/lib/cfgquality.py`, called from `configmaint.validate` beside the other advisory checks, so it appears in section 0 of the config report and escalates only when new (as #2357 does today). No new script.
- **What it reads:** `database/bible_research.db`, table `prose_section` joined to `prose_section_type` where the code starts with `glossary`, read-only; the terms to look for are the list in `cfg_setting glossary.currency_check` (the 7 today, plus the 8 new surface terms added to that list once their entries exist).
- **What it reports (advisory finding per term):** no active entry with that heading; the only entry is `archived`; or the entry is still `draft` (all 87 today, so this would flag every term until you approve them; I suggest reporting draft separately and not as a failure, or it will be noise).
- **Controlled values:** a second list, also in config, of the controlled values whose meaning must be in the glossary: the `cfg_prose_concept` pointers are checked that their `prose_section` id still exists and has the heading they name.
- **Code and config changes this needs:** the function in `cfgquality.py` (and its entry in `cfgreport.py` section 0), the new terms added to `glossary.currency_check` through `configmaint.propose`, and a BUILD.md entry (governance.build_md_on_code_change).

## To approve

1. Apply the 8 entries after your corrections (Prose.ps1 ApplyPatch).
2. The check as designed above, with the one choice: report a draft-only entry as an advisory finding, or leave draft out of the check.

| decision | note |
|---|---|
| apply entries: yes / correct first | |
| draft-only entry: flag / do not flag | |
