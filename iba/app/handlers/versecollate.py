"""versecollate handler -- work package `verse-collate`, step verse_collate.collate (#2228 tools 3-5).

Resolves the scope (the same selectors as Verse-Scope.ps1, or -File) and collates what is known and what is
missing for every verse in it; writes <label>-<YYYYMMDD>.json (the record) and .md (the summary) under
verse_collate.output_dir, versioned by lib/filingkit. A scope or guard refusal is the routed condition
'refused'. Read-only on the tables. The logic is in lib/versecollate.py."""
from __future__ import annotations

import datetime
import json
import pathlib

from ..lib import filingkit
from ..lib import versecollate as vc
from ..lib import versescope as vs
from .base import Ctx, Outcome, fail, ok

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]


def collate(ctx: Ctx) -> Outcome:
    params = dict(ctx.params)
    label = (params.pop("Label", None) or "verse-collate").strip()
    file_request = None
    if params.get("File"):
        f = pathlib.Path(params.pop("File"))
        if not f.is_file():
            return fail("refused", f"request file not found: {f.as_posix()}")
        try:
            file_request = {k.lower(): v for k, v in json.loads(f.read_text(encoding="utf-8")).items()}
        except (ValueError, AttributeError) as exc:
            return fail("refused", f"request file {f.as_posix()} is not a JSON object: {exc}")
    try:
        out = vc.collate(ctx.cfg, vs.normalise_request(params, file_request), PROJECT_ROOT)
    except (vs.ScopeError, vc.CollateError) as exc:
        return fail("refused", str(exc))
    out = {"label": label, "run_id": ctx.run_id,
           "collated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), **out}
    folder = ctx.cfg.required_setting("verse_collate.output_dir")
    pj = filingkit.versioned_path(ctx.cfg, label, out_dir=folder, ext="json")
    pm = filingkit.versioned_path(ctx.cfg, label, out_dir=folder, ext="md")
    pj.parent.mkdir(parents=True, exist_ok=True)
    pj.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    pm.write_text("\n".join(vc.markdown(out, label)) + "\n", encoding="utf-8")
    c, g = out["counts"], out["gaps"]
    return ok(f"-> {pm.as_posix()}\n  -> {pj.as_posix()}\n  {c['verses']} verse(s), {c['with_a_gap']} with a gap: "
              + ", ".join(f"{k} {v}" for k, v in g.items() if v) + f" ({c['seconds']}s)", path=str(pm))
