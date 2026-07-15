"""
cfg_kernel.py — the envelope-validator KERNEL for the IBA configurator.

THIS IS THE ONE PERMITTED PIECE OF HARD-CODING IN THE APPLICATION.

Why it must be code and not config: a validator that reads its rules from the
store it is checking cannot detect that store being corrupt -- it would corrupt
its own checks and report itself sound.  So the kernel is fixed, minimal, and
versioned with the app.  See config/utility/config-maintenance.json ->
meta.the_bootstrap_paradox and cfgmaint.kernel-is-the-only-hardcoding.

THE BOUNDARY (testable, and the point of the whole design):
    The kernel knows the ENVELOPE and nothing else.
    If it ever needs to know about a dimension, a gate, a genre, or a
    vocabulary VALUE, that knowledge is in the wrong place.

It reads the vocabularies from _manifest.json meta.vocabularies at run time --
it does not carry them.  It only knows that an envelope HAS a `governs`, and
that `governs` must be drawn from whatever vocabulary the manifest declares.

Read-only.  Never writes.  Exit 0 = valid, 1 = invalid (load would be rejected).

Usage:
    python iba/scripts/cfg_kernel.py                    # validate the whole config
    python iba/scripts/cfg_kernel.py --config PATH      # a different config root
    python iba/scripts/cfg_kernel.py --blocked          # list RECONCILE items + what they block
    python iba/scripts/cfg_kernel.py --json             # machine-readable result
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import sys

# ── The envelope.  The only hard-coded knowledge in the application. ──────────
# Field -> (required, vocabulary key in _manifest meta.vocabularies or None)
ENVELOPE = {
    "id": (True, None),
    "governs": (True, "vocab.governs"),  # list-valued
    "kind": (True, "vocab.kind"),
    "status": (True, "vocab.status"),
    "version": (True, None),
    "authority": (True, None),
    "reference": (True, None),
    "intent": (True, None),
    "satisfaction": (False, None),  # not-applicable on definitional kinds
    "validation": (False, None),    # ditto -- see meta.open.definitional-kinds
    "spec": (True, None),
}
VALIDATION_FIELDS = {
    "axis": (True, "vocab.axis"),
    "severity": (True, "vocab.severity"),
    "enforcement": (True, "vocab.enforcement"),
    "check": (True, None),
    "enum": (False, None),  # resolved against the enum register, not a vocabulary
}
FACETS = ["process", "entities", "output", "validation", "naming", "filing"]

# Authoring conveniences, not rules.  `_envelope_defaults` appearing as an array
# element sets defaults for every item AFTER it in that same array (so 18
# dimensions need not repeat governs/kind/status/version/authority/reference).
# The kernel MERGES them -- an item always overrides a default.  Once loaded to
# the DB every rule row carries its full envelope; defaults do not survive.
MARKER_DEFAULTS = "_envelope_defaults"
MARKER_COMMENT = "_comment"


def expand(raw_items: list[dict]) -> list[dict]:
    """Apply `_envelope_defaults` markers positionally; drop comments."""
    out, defaults = [], {}
    for item in raw_items:
        if MARKER_DEFAULTS in item:
            defaults = item[MARKER_DEFAULTS]
            continue
        if MARKER_COMMENT in item:
            continue
        out.append({**defaults, **item})
    return out


class Kernel:
    def __init__(self, root: pathlib.Path):
        self.root = root
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.items: list[tuple[str, dict]] = []   # (source file, item)
        self.reconcile: list[tuple[str, dict]] = []
        self.vocab: dict[str, set[str]] = {}
        self.enum_ids: set[str] = set()
        self.recon_ids: set[str] = set()

    # ── load ─────────────────────────────────────────────────────────────────
    def _read(self, path: pathlib.Path):
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            self.errors.append(f"{path.relative_to(self.root)}: UNPARSEABLE -- {e}")
            return None

    def load(self) -> bool:
        man = self._read(self.root / "_manifest.json")
        if not man:
            return False
        for name, body in man["meta"]["vocabularies"].items():
            self.vocab[name] = {v["value"] for v in body["values"]}

        enums = self._read(self.root / "wide" / "enums.json")
        if enums:
            # an enum's CODE is its id; validation.enum cites the bare group name
            self.enum_ids = {i["id"].split(".", 1)[1] for i in enums["items"]}
            for i in enums["items"]:
                self.items.append(("wide/enums.json", i))

        recon = self._read(self.root / "wide" / "reconciliations.json")
        if recon:
            self.recon_ids = {i["id"] for i in recon["items"]}

        for path in sorted(self.root.glob("process/*.json")) + sorted(
            self.root.glob("utility/*.json")
        ):
            doc = self._read(path)
            if not doc:
                continue
            rel = str(path.relative_to(self.root)).replace("\\", "/")
            for facet in FACETS:
                for item in expand(doc.get(facet, [])):
                    self.items.append((rel, item))
        return not self.errors

    # ── checks ───────────────────────────────────────────────────────────────
    def check_envelope(self):
        """gate.cfgmaint.envelope-complete"""
        for src, it in self.items:
            ref = f"{src}:{it.get('id', '<NO ID>')}"
            for field, (required, vocab) in ENVELOPE.items():
                if field not in it:
                    if required:
                        self.warnings.append(f"{ref} missing envelope field `{field}`")
                    continue
                if not vocab:
                    continue
                values = it[field] if isinstance(it[field], list) else [it[field]]
                for v in values:
                    if v not in self.vocab[vocab]:
                        self.errors.append(f"{ref} {field}={v!r} not in {vocab}")

            val = it.get("validation")
            if not val:
                continue
            for field, (required, vocab) in VALIDATION_FIELDS.items():
                if field not in val:
                    if required:
                        self.errors.append(f"{ref} validation missing `{field}`")
                    continue
                if vocab and val[field] not in self.vocab[vocab]:
                    self.errors.append(
                        f"{ref} validation.{field}={val[field]!r} not in {vocab}"
                    )

            if it.get("status") == "RECONCILE":
                self.reconcile.append((src, it))

    def check_ids_unique(self):
        """gate.cfgmaint.id-unique -- ids are frozen at mint and globally unique"""
        seen = collections.Counter(it.get("id") for _, it in self.items)
        for i, c in seen.items():
            if c > 1:
                self.errors.append(f"id {i!r} declared {c} times -- ids must be globally unique")

    def check_references(self):
        """gate.cfgmaint.references-resolve"""
        ids = {it.get("id") for _, it in self.items}
        for src, it in self.items:
            ref = f"{src}:{it.get('id')}"
            spec = it.get("spec", {})

            enum_ref = it.get("validation", {}).get("enum") or spec.get("enum")
            if enum_ref and enum_ref not in self.enum_ids:
                self.errors.append(f"{ref} enum={enum_ref!r} not in the enum register")

            r = spec.get("reconcile")
            if r and r.startswith("recon.") and r not in self.recon_ids:
                self.errors.append(f"{ref} reconcile={r!r} not in reconciliations.json")

            # `cites` is what makes "reference, never restate" (layout v2 §2.3)
            # enforceable: a citation that does not resolve means a rule was
            # paraphrased instead of cited.
            for c in spec.get("cites", []):
                if c not in ids:
                    self.warnings.append(f"{ref} cites {c!r} -- unresolved (not yet authored?)")
            for c in (spec.get("implements"), it.get("implements")):
                if c and c not in ids:
                    self.warnings.append(f"{ref} implements {c!r} -- unresolved")

    def check_reconcile_canonical(self):
        """A RECONCILE item must name the decision that settles it."""
        for src, it in self.reconcile:
            spec = it.get("spec", {})
            if not spec.get("reconcile"):
                self.warnings.append(
                    f"{src}:{it['id']} is RECONCILE but names no `spec.reconcile` decision"
                )

    def run(self):
        self.check_envelope()
        self.check_ids_unique()
        self.check_references()
        self.check_reconcile_canonical()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    here = pathlib.Path(__file__).resolve().parent.parent
    ap.add_argument("--config", default=str(here / "config"), help="config root")
    ap.add_argument("--blocked", action="store_true", help="list RECONCILE items and what they block")
    ap.add_argument("--json", action="store_true", help="machine-readable result")
    args = ap.parse_args()

    k = Kernel(pathlib.Path(args.config))
    if not k.load():
        print("LOAD FAILED -- config unreadable:", file=sys.stderr)
        for e in k.errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    k.run()

    by_kind = collections.Counter(it.get("kind") for _, it in k.items)
    by_status = collections.Counter(it.get("status") for _, it in k.items)
    by_governs = collections.Counter(g for _, it in k.items for g in it.get("governs", []))

    if args.json:
        print(json.dumps({
            "valid": not k.errors,
            "items": len(k.items),
            "errors": k.errors,
            "warnings": k.warnings,
            "reconcile": [i["id"] for _, i in k.reconcile],
            "by_kind": dict(by_kind),
            "by_status": dict(by_status),
        }, indent=2))
        return 0 if not k.errors else 1

    if args.blocked:
        print(f"RECONCILE items -- the loader refuses to run study modules on these ({len(k.reconcile)}):\n")
        by_file = collections.defaultdict(list)
        for src, it in k.reconcile:
            by_file[src].append(it)
        for src, items in sorted(by_file.items()):
            print(f"  {src}")
            for it in items:
                d = it.get("spec", {}).get("reconcile", "-- no decision named --")
                print(f"     {it['id']:42} -> {d}")
        return 0

    print(f"IBA configurator -- kernel check\n{'=' * 60}")
    print(f"config root : {args.config}")
    print(f"items       : {len(k.items)}")
    print(f"by kind     : {', '.join(f'{v} {kk}' for kk, v in sorted(by_kind.items(), key=lambda x: -x[1]))}")
    print(f"by status   : {', '.join(f'{v} {s}' for s, v in by_status.most_common())}")
    print(f"by governs  : {', '.join(f'{v} {g}' for g, v in by_governs.most_common(8))}")
    print()
    if k.errors:
        print(f"INVALID -- {len(k.errors)} error(s). A load would be REJECTED; nothing written.")
        for e in k.errors:
            print(f"  ERROR   {e}")
    else:
        print("ENVELOPE VALID -- every item validates against _manifest.json meta.vocabularies")
    if k.warnings:
        print(f"\n{len(k.warnings)} warning(s):")
        for w in k.warnings:
            print(f"  WARN    {w}")
    if k.reconcile:
        print(f"\n{len(k.reconcile)} RECONCILE item(s) -- study modules depending on these refuse to run.")
        print("  (run with --blocked for the list)")
    return 1 if k.errors else 0


if __name__ == "__main__":
    sys.exit(main())
