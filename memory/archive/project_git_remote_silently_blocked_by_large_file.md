---
name: project_git_remote_silently_blocked_by_large_file
description: A >100MB file committed to history silently blocked ALL pushes; remote fell 553 commits behind. Purged 20260713.
metadata: 
  node_type: memory
  type: project
  originSessionId: 6b56630f-0f9e-4733-abf8-f856527e68ee
---

On 2026-07-13 a `git push` failed: `outputs/archive/wa-verse-span-lexical-index-v1-20260626.json` (247 MB) had been committed in the 2026-07-09 filing-maintenance commit and exceeded GitHub's 100 MB hard limit. GitHub rejects the **entire** push if any commit in the range carries a >100 MB blob, so **every push had silently failed since**, leaving `origin/main` stuck at 2026-07-03 while local ran 553 commits ahead. The IDE's "outstanding changes to sync" count was these unpushed commits, not uncommitted edits.

**Root cause:** the existing ignore rule `outputs/wa-verse-span-lexical-index-*.json` was non-recursive, so the copy that landed in `outputs/archive/` slipped through.

**Fix (all done):** added recursive ignore `outputs/**/wa-verse-span-lexical-index-*.json`; purged the blob from all 1600 commits with `git-filter-repo --path ... --invert-paths --force` (installed via `pip install git-filter-repo`); kept the file on disk (regenerable, NAS-mirrored) untracked; re-added the `origin` remote (filter-repo drops it); force-pushed with `--force-with-lease`. Verified remote had zero unique work first (its tip tree was byte-identical to a local commit that is an ancestor of HEAD; all remote-only commits ≤2026-07-03). Backup bundle of pre-purge history saved to the session scratchpad.

**Why:** a blocked push is invisible unless you look — no error surfaces until you next push.

**How to apply:** (1) periodically check `git rev-list --count @{u}..HEAD` — a large or growing number means pushes may be blocked, not just deferred. (2) Any large/regenerable artefact must be gitignored **recursively** (`**/name-*`), because filing moves relocate files into subfolders. (3) To find offenders: `git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | awk '/^blob/ && $3>94371840'`. Related: [[reference_operational_governance_git_backup_manifest]], [[feedback_filing_is_first_class_governance]].
