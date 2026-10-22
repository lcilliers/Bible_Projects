# File naming & location governance — adoption plan (v1)

> Escalation #863. Scope per the researcher: *"make sure that the governance rules of IBA include
> the GLOBAL FILE rules and filing and folder rules... All I want is that it is properly done and I
> can find things when I look for it."* This is a **plan for the researcher's decision**, not a
> build — nothing here is implemented. Grounded in a live trace already done this session
> (`iba/app/reports/file-versioning-config-trace-20260826.md`) and a full read of
> `docs/file-organisation-rules.md` (553 lines, the source document named in #863's own raise).

## 1. The actual shape of the gap

`docs/file-organisation-rules.md` is not one rule — it's two very different kinds of content mixed
together, and they need different treatment:

**(a) General, timeless principles** — apply to any file, in any folder, from any era of the
project:
- §2.1 naming shape: lowercase, hyphens, compact `YYYYMMDD` dates, `-v{n}` version suffix (no
  leading zero), zero-padded numeric ids.
- §2.3 / §2.3a: the snapshot-vs-living-document distinction — a snapshot gets filename versioning
  (`-v{n}-{date}`, same-day bumps, prior versions archived, only the latest stays live); a living
  document gets one stable filename with version tracked in its own metadata + git, never archived
  copies.
- §4 / §4.1: archiving triggers and the stale-document policy (archived, never deleted; findable
  again via the manifest).
- §5: the five Claude Code obligations (determine folder before writing, archive superseded
  versions, never leave files at a folder root, etc.).

**(b) Artefact-specific patterns tied to a *particular methodology*** — §2.2's per-type filename
templates (`wa-{NNN}-{word}-sessionb-observations-v{n}-{date}.md` etc.) and most of §3's
folder-by-folder rules (`Sessions/Session_B/09_Analysis_output_logs/`, dimension review folders,
verse-context batch folders...). These aren't general rules — they're the filing convention *for
one specific research methodology*, and CLAUDE.md's own top banner records that methodology has
been superseded **multiple times** since this document was last touched (2026-06-27): the
verse-first/term-driven method (2026-07-02), the characteristic→role→lexical cycle (2026-07-08),
the "Characteristics → Movements" reset (2026-06-25, which the file itself predates in its most
recent update), and the base-layer move to IBA (2026-08-15/17). Some of what §3 describes
(`Sessions/Session_B/*`, dimension-review folders) is explicitly marked legacy/read-only inside the
very same document. Treating (b) as live, adoptable governance would mean encoding rules nobody is
actually following as if they were current policy — the opposite of "properly done."

**This is why nothing has been adopted for (b) at all**, and why the two narrow mechanisms that
*do* exist (`report.version_on_regenerate`, `governance.oneoff_*`) both only implement fragments of
**(a)**, scoped to IBA's own report-writing code — never wired to anything else in the project, IBA
or main-project side (confirmed self-implicating finding: every report *this session's own #857
investigation* produced was hand-typed imitating the pattern, never actually calling the mechanism
that enforces it).

## 2. What this plan proposes adopting now

Only **(a)** — the general principles. Concretely:

1. **New `cfg_behaviour_class` row: `filing`.** Checked live — none of the five existing classes
   (`chat`, `terminal`, `sqlite`, `documentation`, `llm_output`) cover "where a file goes / how it's
   named / when it's archived." `documentation` is about single-authority content *referencing*
   (pointer vs copy), a different concern entirely. `governance.operational_behaviour_control`
   already anticipates exactly this ("and any further class identified"). Authoritative doc: this
   plan's build record, or a rewritten `docs/file-organisation-rules.md` §1/§2.1/§2.3/§2.3a/§4/§5
   scoped to drop the methodology-specific parts.
2. **`cfg_behaviour_rule` rows under `filing`**, one per general principle in §1(a) above — naming
   shape, snapshot-vs-living distinction, archiving triggers, the five obligations. Each a real,
   checkable rule, not prose.
3. **A shared utility, generalising `oneoff_path()`** — call it `filingkit.versioned_path()` or
   similar — implementing the naming/versioning/archiving rule for **any** caller project-wide, not
   just `iba/app/reports/`. `oneoff_path()`'s own logic (same-day `-v{n}` bump, archive-before-write,
   collision handling) is already a correct implementation of §2.3 — this generalises it rather than
   inventing new machinery, and gives every future report/output-writer (IBA or main-project side) a
   single function to call instead of hand-imitating the shape.
4. **A `configmaint.validate` check**: find writes that hand-imitate the naming pattern via
   `Write`/`path.write_text()` without calling the shared utility (the same class of gap this
   session's own reports just fell into) — flags it, doesn't block it, matching the advisory-finding
   pattern already used elsewhere in `configmaint.validate`.

## 3. What this plan does NOT propose (flagged, not silently dropped)

- **No attempt to encode §2.2/§3's methodology-specific patterns as live rules.** They describe how
  filing *used to* work under superseded methods. If any of it should be formally retired rather
  than left as ambiguous legacy prose, that's a documentation-cleanup decision for the researcher,
  separate from this plan.
- **No bulk retrofit of existing misfiled files.** "Filing is in a real mess" (researcher, verbatim)
  is a real, separate problem from whether the *rule* is config-driven going forward. Fixing the
  rule first, then cleaning up historical mess against a rule that's actually enforced, is the
  right order — a bulk cleanup run *before* the rule exists would just create new mess by a
  different, equally ungoverned convention.
- **No location-governance table (a `cfg_folder_purpose` or similar) covering every project
  folder.** The project's own structure has moved at least three times in the period this document
  covers (`Sessions` → `Sessions-v2` → `verse-analysis` → IBA). A location-governance mechanism
  needs to name only **currently active** folders (`Sessions-v2/`, `iba/docs/`, `iba/app/reports/`,
  `outputs/`, `research/investigations/`, `Workflow/methodology/`, `Logs/`, and IBA's own
  `governance.*_dir` settings already in place) — a full table is a second-phase decision, once the
  researcher confirms which folders are actually still live.

## 4. Open questions for the researcher

1. Does the scope in §2 (general naming/versioning/archiving, project-wide, via one shared utility)
   match what "properly done" means here, or is more/less wanted?
2. Should `docs/file-organisation-rules.md` itself be rewritten to drop the superseded §2.2/§3
   methodology-specific content (kept in git history, not lost) once the general rules move to
   `cfg_*`, so the live doc doesn't keep presenting dead patterns as current?
3. Is a bulk historical-mess cleanup wanted as a *separate*, later item once this rule exists and is
   enforced — or should current-folder location governance (§3's "not proposed" item) be pulled
   into this same round instead of deferred?

Approve scope, and I'll build §2 next round (design → propose → build → verify, same cycle as
`#833`/`#836`), same as any other IBA module.
