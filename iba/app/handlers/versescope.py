"""versescope handler -- work package `verse-scope`, step verse_scope.resolve (#2228).

The scope resolver: any request -> the collection of verses, as a JSON file under
verse_scope.output_dir (versioned and archived by lib/filingkit). The logic is in lib/versescope.py;
the handler merges the command-line selectors with an optional request file (-File), writes the
file and turns a ScopeError into the routed condition 'refused' (cfg_on_fail: report-continue).
Read-only: no table is written."""
from __future__ import annotations

import datetime
import json
import pathlib

from ..lib import filingkit
from ..lib import versescope as vs
from .base import Ctx, Outcome, fail, ok


def resolve(ctx: Ctx) -> Outcome:
    params = dict(ctx.params)
    label = (params.pop("Label", None) or "verse-scope").strip()
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
        request = vs.normalise_request(params, file_request)
        out = vs.resolve(ctx.cfg, request)
    except vs.ScopeError as exc:
        return fail("refused", str(exc))
    out = {"label": label, "run_id": ctx.run_id,
           "resolved_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), **out}
    path = filingkit.versioned_path(ctx.cfg, label, out_dir=ctx.cfg.required_setting("verse_scope.output_dir"),
                                    ext="json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    lines = [f"{s['kind']} {s['value']}{(' (' + s['item'] + ')') if s.get('item') else ''}: {s['verses']} verse(s)"
             for s in out["selectors"]]
    if "only_strong" in out:
        lines.append(f"only_strong {', '.join(x['code'] for x in out['only_strong']['strongs'])}: "
                     f"{out['only_strong']['verses_dropped']} verse(s) dropped")
    c = out["counts"]
    return ok(f"-> {path.as_posix()}\n  " + "\n  ".join(lines)
              + f"\n  {c['verses']} verse(s); {c['not_resolved']} not resolved", path=str(path))
