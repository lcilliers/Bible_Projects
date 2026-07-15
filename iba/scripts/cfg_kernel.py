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
        self.enum_values: dict[str, list] = {}   # group -> raw values (str or {value,description})
        self.recon_ids: set[str] = set()
        self.no_subject: list[str] = []          # ruling 2026-07-15 (b3) backfill

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

        # BOOTSTRAP.  The vocabularies live in the enum register like all other
        # nomenclature (researcher ruling 2026-07-15 a; the config self-hosts).
        # So the kernel reads the register FIRST, trusting only its envelope, then
        # validates everything -- the register included -- against it.  The kernel
        # still knows no vocabulary VALUE: it learns them here, at run time.
        enums = self._read(self.root / "wide" / "enums.json")
        if not enums:
            self.errors.append("wide/enums.json missing -- the register IS the vocabulary source")
            return False

        for i in enums["items"]:
            group = i["id"].split(".", 1)[1]     # enum.kind -> kind
            self.enum_ids.add(group)
            values = i.get("spec", {}).get("values", [])
            self.enum_values[group] = values
            self.vocab[f"vocab.{group}"] = {
                v["value"] if isinstance(v, dict) else v for v in values
            }
            self.items.append(("wide/enums.json", i))

        recon = self._read(self.root / "wide" / "reconciliations.json")
        if recon:
            self.recon_ids = {i["id"] for i in recon["items"]}

        # Tier B (process/) and Tier A utilities use the six facets.  Tier A wide
        # files use their own node names (modules / dependencies / module_gates).
        # Rather than hard-code every node name -- which would make the kernel know
        # about the layout, and the layout is authoring ergonomics, not architecture
        # -- treat ANY array of envelope-bearing objects as a rule list.
        paths = (sorted(self.root.glob("process/*.json"))
                 + sorted(self.root.glob("utility/*.json"))
                 + sorted(self.root.glob("wide/*.json")))
        for path in paths:
            rel = str(path.relative_to(self.root)).replace("\\", "/")
            if rel == "wide/enums.json":
                continue                      # already loaded as the vocabulary source
            if rel == "wide/reconciliations.json":
                # A DECISION REGISTER, not a rulebook.  Its items are decisions
                # ABOUT rules and deliberately do not carry the envelope (see that
                # file's meta.envelope + meta.open.envelope-exemption).  They use
                # enum.decision_status, not enum.status.  Loaded above for recon_ids.
                continue
            doc = self._read(path)
            if not doc:
                continue
            for node, value in doc.items():
                if node == "meta" or not isinstance(value, list):
                    continue
                if not any(isinstance(x, dict) and ("id" in x or MARKER_DEFAULTS in x)
                           for x in value):
                    continue                  # not a rule list (e.g. a plain string array)
                for item in expand(value):
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
        """status must agree with spec.canonical / spec.reconcile, both ways.

        RECONCILE means the value is contested: it must name the decision that
        settles it, and must not claim to be canonical.
        LIVE means it is settled: it must NOT still point at an unresolved
        reconciliation, and must not be marked non-canonical.

        The second direction matters because resolving a reconciliation is a
        STATUS FLIP -- and a flip that leaves `canonical: false` or a dangling
        `reconcile` pointer behind produces an item that reads as authoritative
        while still declaring itself contested.  Nothing else would catch it.
        """
        for src, it in self.items:
            spec = it.get("spec", {})
            status, ref = it.get("status"), f"{src}:{it.get('id')}"
            canonical, reconcile = spec.get("canonical"), spec.get("reconcile")

            if status == "RECONCILE":
                if not reconcile:
                    self.warnings.append(f"{ref} is RECONCILE but names no `spec.reconcile` decision")
                if canonical is True:
                    self.errors.append(f"{ref} is RECONCILE but claims spec.canonical=true -- contradictory")
            elif status == "LIVE":
                if canonical is False:
                    self.errors.append(
                        f"{ref} is LIVE but spec.canonical=false -- a settled rule cannot "
                        f"declare itself contested"
                    )
                if reconcile:
                    self.errors.append(
                        f"{ref} is LIVE but still points at reconcile={reconcile!r} -- "
                        f"clear the pointer when a decision is ruled, or the item reads as "
                        f"authoritative while declaring itself unsettled"
                    )

    def check_nomenclature_has_enum(self):
        """gate.cfgmaint.nomenclature-has-enum -- researcher ruling 2026-07-15 (a, b2).

        No custom nomenclature may exist in the configurator without its
        DESCRIPTION being cross-checkable in the enum register.  Every field
        whose values are drawn from a fixed set is nomenclature; its set --
        WITH a description per value -- lives in wide/enums.json and nowhere
        else.  That includes the configurator's own vocabularies: the config
        self-hosts.
        """
        for vocab in sorted({v for _, v in ENVELOPE.values() if v} |
                            {v for _, v in VALIDATION_FIELDS.values() if v}):
            group = vocab.split(".", 1)[1]          # vocab.kind -> kind
            if group not in self.enum_ids:
                self.errors.append(
                    f"NOMENCLATURE `{group}` is used as a controlled field but has no "
                    f"enum.{group} in the register (it lives in _manifest meta.vocabularies "
                    f"-- a second home). See open.cfgmaint.vocab-migration."
                )
                continue
            for value in sorted(self.vocab[vocab]):
                if not self.value_described(group, value):
                    self.errors.append(
                        f"enum.{group} value {value!r} has no description -- "
                        f"nomenclature must be cross-checkable (ruling 2026-07-15 a)"
                    )

    def value_described(self, group: str, value: str) -> bool:
        """A value is cross-checkable only if it carries a description.

        Bare-string values cannot -- which is what settles meta.open.value-metadata
        in favour of object-form values.
        """
        vals = self.enum_values.get(group, [])
        for v in vals:
            if isinstance(v, dict) and v.get("value") == value:
                return bool(v.get("description"))
            if v == value:
                return False        # bare string: present, but no description
        return False

    def check_no_duplicate_rule(self):
        """gate.cfgmaint.no-duplicate-rule -- researcher ruling 2026-07-15 (b3).

        The same TYPE of rule about the same ITEM must not live in two
        configurations.  (kind, subject) is the identity; a second rule of the
        same kind about the same subject must CITE the first, not restate it.

        Different kinds about one subject are correct -- a principle stating a
        rule and a gate enforcing it share a subject by design.
        """
        seen = collections.defaultdict(list)
        for src, it in self.items:
            subject = it.get("subject")
            if not subject:
                self.no_subject.append(f"{src}:{it.get('id')}")
                continue
            seen[(it.get("kind"), subject)].append(f"{src}:{it['id']}")
        for (kind, subject), where in sorted(seen.items()):
            if len(where) > 1:
                self.errors.append(
                    f"DUPLICATE RULE: kind={kind} subject={subject!r} defined in "
                    f"{len(where)} places -- {', '.join(where)}. One must cite the other."
                )

    def run(self):
        self.check_envelope()
        self.check_ids_unique()
        self.check_references()
        self.check_reconcile_canonical()
        self.check_nomenclature_has_enum()
        self.check_no_duplicate_rule()


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
        print("VALID -- every item passes the envelope, nomenclature and duplication checks")

    if k.no_subject:
        print(f"\nBACKFILL -- {len(k.no_subject)} item(s) carry no `subject` "
              f"(field added 2026-07-15 per ruling b3).")
        print(f"  Until backfilled, no-duplicate-rule covers only "
              f"{len(k.items) - len(k.no_subject)}/{len(k.items)} items -- the "
              f"duplication check is PARTIAL, not clean.")

    if k.warnings:
        # group repeated warning shapes so a systemic gap reads as one line
        groups = collections.Counter(
            w.split(" cites ")[0].split(":")[0] if " cites " in w else w.split(" -- ")[0]
            for w in k.warnings
        )
        print(f"\n{len(k.warnings)} warning(s):")
        for w in k.warnings:
            print(f"  WARN    {w}")

    if k.reconcile:
        print(f"\n{len(k.reconcile)} RECONCILE item(s) -- study modules depending on these refuse to run.")
        print("  (run with --blocked for the list)")
    return 1 if k.errors else 0


if __name__ == "__main__":
    sys.exit(main())
