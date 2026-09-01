"""catalogue handlers — thin dispatcher adapter over `iba.app.lib.cataloguewrite`.

Registers `obs_catalogue.update` as the `catalogue-update` work package. Escalation #1007.
"""

from __future__ import annotations

import json

from .base import Ctx, Outcome, ok, fail
from ..lib import cataloguewrite


def update(ctx: Ctx) -> Outcome:
    p = ctx.params
    if not p.get("ObsId"):
        return fail("bad-params", "update needs -ObsId")
    if not p.get("Set"):
        return fail("bad-params", "update needs -Set (JSON object of column:value pairs)")
    try:
        obs_id = int(p["ObsId"])
    except ValueError:
        return fail("bad-params", f"-ObsId must be an integer, got {p['ObsId']!r}")
    try:
        set_ = json.loads(p["Set"])
    except json.JSONDecodeError as e:
        return fail("bad-params", f"-Set is not valid JSON: {e}")
    if not isinstance(set_, dict):
        return fail("bad-params", f"-Set must be a JSON object, got {type(set_).__name__}")

    try:
        result = cataloguewrite.run_update(ctx.cfg, obs_id, set_)
    except ValueError as e:
        return fail("bad-params", str(e))

    changed_cols = sorted(result["changed"])
    return ok(f"obs_id={obs_id}: updated {len(changed_cols)} column(s) ({', '.join(changed_cols)})",
              **result)
