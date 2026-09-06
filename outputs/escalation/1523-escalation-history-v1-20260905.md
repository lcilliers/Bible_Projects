# Escalation deep history

## #1523 — Cluster-assignment exceptions: 772 strong(s) carry a non-T2…
type=issue source=cluster

**v1** (2026-09-05T16:25:28Z, Claude) state=raised next_action=review assigned_to=Researcher
> **short description (set this version):** Cluster-assignment exceptions: 772 strong(s) carry a non-T2…
> **comment (set this version):** reconcile()'s own exception checks, run DB-wide across every backfill-origin strong with a cluster assignment
> **context (set this version):** {"no_word": 772, "sibling_conflict": 829, "report_path": "_analytics\\Clusters\\cluster-assign-v3-20260905.md", "full_message": "Cluster-assignment exceptions: 772 strong(s) carry a non-T2 cluster with no word_registry link at all; 829 `backfill` strong(s) have an already-active or already-clustered sibling. Neither is auto-resolved \u2014 approve to acknowledge as current/known state, reject to flag for action, or revise with a comment. Full detail: _analytics\\Clusters\\cluster-assign-v3-20260905.md."}
> **tried (set this version):** reconcile()'s own exception checks, run DB-wide across every backfill-origin strong with a cluster assignment

**v2** (2026-09-05T16:34:12Z, Researcher) state=in-progress next_action=review assigned_to=Researcher
> **comment (set this version):** Keep open, not resolving now. Researcher's own view: these strongs were discovered on verses shared with other strongs -- the exception is expected to wash out naturally once those verses get analysed at the verse level, not something to resolve by registry-promotion or cluster cleanup ahead of that. Handling multi-characteristic verses (a verse carrying more than one relevant strong/theme) is one of the open questions the windows-debate work is expected to surface -- how that analysis will actually pan out isn't settled yet, so this is deliberately parked pending that, not abandoned.
