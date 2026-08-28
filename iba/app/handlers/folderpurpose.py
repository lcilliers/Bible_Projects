"""folderpurpose handlers — thin dispatcher adapters over lib/folderpurpose.py.

Escalation #971. Work package `folder-purpose`, 5 steps: seed (Method A), crosscheck (Method B),
set/list/show (Method C, the table editor).
"""

from __future__ import annotations

from .base import Ctx, Outcome, ok, fail
from ..lib import folderpurpose as fp_mod


def folder_purpose_seed(ctx: Ctx) -> Outcome:
    """Method A — full reconciliation against the live tree."""
    summary = fp_mod.seed_from_scan(ctx.cfg)
    return ok(f"folder_purpose seeded: {summary['total_on_disk']} folders on disk "
             f"({summary['new']} new, {summary['refreshed']} refreshed, "
             f"{summary['marked_deleted']} marked deleted)", **summary)


def folder_purpose_crosscheck(ctx: Ctx) -> Outcome:
    """Method B — sync governed_by_setting from live cfg_setting values, pre-fill type/status
    where unambiguous, report the operations-needs-a-setting invariant's anomalies."""
    summary = fp_mod.cross_check_settings(ctx.cfg)
    n_anom = (len(summary["anomaly_operations_without_setting"])
             + len(summary["anomaly_setting_without_folder_row"]))
    return ok(f"cross-check: {summary['governed_by_setting_updated']} governed_by_setting "
             f"updated, {summary['type_status_prefilled']} type/status pre-filled, "
             f"{n_anom} anomaly(ies)", **summary)


def folder_purpose_set(ctx: Ctx) -> Outcome:
    """Method C — hand-set type/status/usage_description for one folder."""
    folder_path = ctx.params.get("FolderPath")
    if not folder_path:
        return fail("missing-folder-path", "folderpurpose.set requires -FolderPath")
    type_ = ctx.params.get("Type") or None
    status = ctx.params.get("Status") or None
    usage_description = ctx.params.get("UsageDescription") or None
    try:
        row = fp_mod.set_purpose(ctx.cfg, folder_path, type_, status, usage_description)
    except ValueError as e:
        return fail("invalid-set", str(e))
    return ok(f"{folder_path}: type={row['type']} status={row['status']}", **row)


def folder_purpose_list(ctx: Ctx) -> Outcome:
    """Method C — list rows, optionally filtered by -Type/-Status/-TopLevelRoot."""
    rows = fp_mod.list_rows(ctx.cfg, ctx.params.get("Type") or None,
                            ctx.params.get("Status") or None,
                            ctx.params.get("TopLevelRoot") or None)
    return ok(f"{len(rows)} row(s)", count=len(rows), rows=rows)


def folder_purpose_autoassess(ctx: Ctx) -> Outcome:
    """Method D — fills type/status wherever determinable, leaves the rest for Method C."""
    summary = fp_mod.auto_assess(ctx.cfg)
    n_uncertain = len(summary["left_uncertain"])
    msg = f"{summary['assessed']} row(s) assessed"
    if n_uncertain:
        msg += f", {n_uncertain} left uncertain (genuinely ambiguous, needs Method C)"
    return ok(msg, **summary)


def folder_purpose_show(ctx: Ctx) -> Outcome:
    """Method C — show one folder's full row."""
    folder_path = ctx.params.get("FolderPath")
    if not folder_path:
        return fail("missing-folder-path", "folderpurpose.show requires -FolderPath")
    row = fp_mod.show(ctx.cfg, folder_path)
    if row is None:
        return fail("not-found", f"no folder_purpose row for {folder_path!r}")
    return ok(f"{folder_path}: type={row['type']} status={row['status']}", **row)
