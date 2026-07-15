"""
cfg_apply.py — the configurator-maintenance utility's WRITE PATH.

THE SOLE WRITE PATH TO THE CONFIGURATOR (cfgmaint.sole-write-path).
Hand-editing the seed is what this replaces.

Why it exists
─────────────
Until 2026-07-15 every change to the configurator was a hand-edit: an ad-hoc
script mutated the JSON, and the kernel ran AFTERWARDS.  That is the exact
inverse of cfgmaint.load-lifecycle, which says:

    read -> SELF-VALIDATE -> (invalid? REJECT, NOTHING WRITTEN) -> write -> version -> audit

Writing first and checking later means invalid config reaches disk and is only
removed if someone notices.  It did, three times in one session -- including a
shell-quoting bug that silently emptied enum descriptions and which the kernel
PASSED, because a mangled string is still a string.

This tool inverts it: the edit runs against a STAGING COPY, the kernel gates the
staging copy, and the live config is touched only if staging validates.

    stage -> apply -> validate -> [reject | commit]

Commit also does what a hand-edit never did: bumps config_version, syncs the
manifest's file list, writes per-file hashes (without which a version pin is a
label, not evidence -- ent.cfg.version), and appends an audited change record
with who/when/why (cfgmaint.audit-every-change; rationale is REQUIRED).

Usage
─────
    python iba/scripts/cfg_apply.py --check
        Validate the live config. Read-only. Also runs the gates the kernel
        alone does not: seed-declared, hash parity.

    python iba/scripts/cfg_apply.py --edit path/to/edit.py --why "reason"
        Stage, apply the edit, validate, and commit only if valid.
        The edit script runs with cwd = the staging config root.

    python iba/scripts/cfg_apply.py --edit path/to/edit.py --why "..." --dry-run
        Everything except the commit. Shows the diff and the verdict.

    python iba/scripts/cfg_apply.py --sync --why "reason"
        No edit -- just reconcile the manifest (files + hashes) and version.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config"
KERNEL = ROOT / "scripts" / "cfg_kernel.py"
CHANGELOG = CONFIG / "_change_log.jsonl"


# ── helpers ──────────────────────────────────────────────────────────────────
def seed_files(root: pathlib.Path) -> list[pathlib.Path]:
    """Every seed file the loader would read. Excludes archive/ and the log."""
    return sorted(
        p for p in root.rglob("*.json")
        if "archive" not in p.parts and p.name != "_change_log.jsonl"
    )


def file_hash(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def rel(p: pathlib.Path, root: pathlib.Path) -> str:
    return str(p.relative_to(root)).replace("\\", "/")


def load_items(root: pathlib.Path) -> dict[str, dict]:
    """Every rule, by id -- so a change can be diffed at ITEM level, not line level."""
    out: dict[str, dict] = {}
    for p in seed_files(root):
        try:
            doc = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for node, value in doc.items():
            if node == "meta" or not isinstance(value, list):
                continue
            for item in value:
                if isinstance(item, dict) and "id" in item:
                    out[item["id"]] = item
    return out


def run_kernel(root: pathlib.Path) -> tuple[bool, str]:
    r = subprocess.run(
        [sys.executable, str(KERNEL), "--config", str(root)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    return r.returncode == 0, (r.stdout or "") + (r.stderr or "")


# ── gate.cfgmaint.seed-declared -- declared LIVE, never implemented ──────────
def check_seed_declared(root: pathlib.Path) -> list[str]:
    """Every file under config/ is declared in _manifest, and every declared
    file exists.  BOTH directions: an undeclared file is a silent gap; a
    declared-but-missing file is a silent hole.  Same failure class.

    'pending' entries are declared-and-not-yet-authored -- legitimate, not holes.
    """
    errs: list[str] = []
    man = json.loads((root / "_manifest.json").read_text(encoding="utf-8"))
    sections = man.get("sections", {})
    declared: dict[str, str] = {}

    def walk(node):
        if isinstance(node, dict):
            if "file" in node:
                declared[node["file"]] = node.get("status", "")
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk({k: v for k, v in sections.items() if k != "deleted"})
    # `deleted` declares files that were RETIRED (dissolved into other files).
    # They are recorded, not missing -- omitting them would lose the supersession,
    # and counting them as declared would demand they exist. Neither.
    retired = {d["file"] for d in sections.get("deleted", []) if isinstance(d, dict) and "file" in d}
    actual = {p.name for p in seed_files(root)}
    for f in sorted(retired & actual):
        errs.append(f"{f!r} is declared RETIRED but still exists -- a superseded file "
                    f"left in place is a confident wrong answer where someone will find it")

    for f in sorted(actual - set(declared)):
        errs.append(f"UNDECLARED seed file {f!r} -- config must not grow silently "
                    f"(gate.cfgmaint.seed-declared)")
    for f, status in sorted(declared.items()):
        if f not in actual and "pending" not in status.lower():
            errs.append(f"DECLARED but MISSING: {f!r} (status={status!r})")
    return errs


def check_hashes(root: pathlib.Path) -> list[str]:
    """A version pin without hashes is a label, not evidence (ent.cfg.version)."""
    man = json.loads((root / "_manifest.json").read_text(encoding="utf-8"))
    if not man.get("file_hashes"):
        return ["NO PER-FILE HASHES -- 'the config that ran' is an assumption, not a "
                "record (ent.cfg.version: 'they are not optional')"]
    errs = []
    for p in seed_files(root):
        r = rel(p, root)
        if r == "_manifest.json":
            continue
        if man["file_hashes"].get(r) != file_hash(p):
            errs.append(f"HASH MISMATCH {r} -- the file changed outside this utility")
    return errs


# ── the lifecycle ────────────────────────────────────────────────────────────
def stage() -> pathlib.Path:
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="cfg_stage_"))
    dst = tmp / "config"
    shutil.copytree(CONFIG, dst)
    return dst


def diff_items(before: dict, after: dict) -> dict:
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    changed = sorted(i for i in set(before) & set(after)
                     if json.dumps(before[i], sort_keys=True) != json.dumps(after[i], sort_keys=True))
    return {"added": added, "removed": removed, "changed": changed}


def bump(version: str) -> str:
    a, b, *rest = version.split("-")[0].split(".")
    return f"{a}.{b}.{int(rest[0]) + 1}" if rest else f"{a}.{int(b) + 1}.0"


def sync_manifest(root: pathlib.Path, new_version: str, why: str, when: str) -> None:
    p = root / "_manifest.json"
    man = json.loads(p.read_text(encoding="utf-8"))
    man["config_version"] = new_version
    man["last_change"] = {"version": new_version, "at": when, "why": why,
                          "by": "cfg_apply.py (the sole write path)"}
    # hashes last: the manifest's own hash would otherwise chase itself
    man["file_hashes"] = {}
    p.write_text(json.dumps(man, indent=2, ensure_ascii=False), encoding="utf-8")
    man["file_hashes"] = {rel(f, root): file_hash(f) for f in seed_files(root)
                          if rel(f, root) != "_manifest.json"}
    p.write_text(json.dumps(man, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate the live config, read-only")
    ap.add_argument("--edit", help="python script to apply (runs with cwd = staging config root)")
    ap.add_argument("--sync", action="store_true", help="reconcile manifest files + hashes only")
    ap.add_argument("--why", help="rationale -- REQUIRED for any write (cfgmaint.audit-every-change)")
    ap.add_argument("--dry-run", action="store_true", help="stage + validate, never commit")
    a = ap.parse_args()

    if a.check:
        ok, out = run_kernel(CONFIG)
        print(out.rstrip())
        extra = check_seed_declared(CONFIG) + check_hashes(CONFIG)
        print("\n-- gates the kernel alone does not run --")
        if extra:
            print(f"{len(extra)} FAILURE(S):")
            for e in extra:
                print(f"  ERROR   {e}")
        else:
            print("  seed-declared + hash parity: PASS")
        return 0 if (ok and not extra) else 1

    if not (a.edit or a.sync):
        ap.error("nothing to do -- pass --check, --edit or --sync")
    if not a.why:
        ap.error("--why is REQUIRED. A change with no recorded rationale is "
                 "indistinguishable from a default someone typed "
                 "(cfgmaint.audit-every-change: rationale_required).")

    when = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    before = load_items(CONFIG)
    live_man = json.loads((CONFIG / "_manifest.json").read_text(encoding="utf-8"))
    old_version = live_man["config_version"]
    new_version = bump(old_version)

    # ── 1. STAGE ────────────────────────────────────────────────────────────
    st = stage()
    print(f"[stage]    {st}")

    # ── 2. APPLY ────────────────────────────────────────────────────────────
    if a.edit:
        r = subprocess.run([sys.executable, str(pathlib.Path(a.edit).resolve())],
                           cwd=str(st), capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        print((r.stdout or "").rstrip())
        if r.returncode != 0:
            print("[REJECT]   the edit script failed -- live config untouched", file=sys.stderr)
            print((r.stderr or "").rstrip(), file=sys.stderr)
            shutil.rmtree(st.parent, ignore_errors=True)
            return 1

    sync_manifest(st, new_version, a.why, when)

    # ── 3. VALIDATE (before anything touches live) ──────────────────────────
    ok, out = run_kernel(st)
    extra = check_seed_declared(st) + check_hashes(st)
    if not ok or extra:
        print(out.rstrip())
        for e in extra:
            print(f"  ERROR   {e}")
        print("\n[REJECT]   staging is INVALID -- LIVE CONFIG UNTOUCHED, nothing written.")
        print("           This is the lifecycle working: bad config never reached disk.")
        shutil.rmtree(st.parent, ignore_errors=True)
        return 1

    # ── 4. DIFF ─────────────────────────────────────────────────────────────
    d = diff_items(before, load_items(st))
    print(f"[validate] PASS")
    print(f"[diff]     +{len(d['added'])} added  ~{len(d['changed'])} changed  "
          f"-{len(d['removed'])} removed")
    for k, sym in (("added", "+"), ("changed", "~"), ("removed", "-")):
        for i in d[k][:12]:
            print(f"             {sym} {i}")
        if len(d[k]) > 12:
            print(f"             … {len(d[k]) - 12} more")

    if a.dry_run:
        print(f"[dry-run]  would bump {old_version} -> {new_version}; nothing written")
        shutil.rmtree(st.parent, ignore_errors=True)
        return 0

    # ── 5. COMMIT + AUDIT ───────────────────────────────────────────────────
    for p in seed_files(st):
        dst = CONFIG / rel(p, st)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst)
    with CHANGELOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "version": new_version, "at": when, "why": a.why,
            "by": "cfg_apply.py", "edit": a.edit, **d,
        }, ensure_ascii=False) + "\n")
    shutil.rmtree(st.parent, ignore_errors=True)
    print(f"[commit]   {old_version} -> {new_version}  (audited in _change_log.jsonl)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
