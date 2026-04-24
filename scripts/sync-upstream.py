#!/usr/bin/env python3
"""Sync the Codex skill from forrestchang/andrej-karpathy-skills.

This intentionally has no third-party dependencies so it can run locally and in
GitHub Actions. It copies the upstream SKILL.md and records the exact upstream
commit in .upstream-sync.json.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

DEFAULT_REPO = "https://github.com/forrestchang/andrej-karpathy-skills.git"
DEFAULT_REF = "main"
DEFAULT_SOURCE_PATH = "skills/karpathy-guidelines/SKILL.md"
TARGET_PATH = Path("skills/karpathy-guidelines/SKILL.md")
STATE_PATH = Path(".upstream-sync.json")


def run(cmd: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def repo_root() -> Path:
    try:
        return Path(run(["git", "rev-parse", "--show-toplevel"]))
    except subprocess.CalledProcessError:
        return Path.cwd()


def validate_skill(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit(f"{path} is missing YAML frontmatter")
    try:
        _, frontmatter, body = text.split("---", 2)
    except ValueError as exc:
        raise SystemExit(f"{path} has malformed YAML frontmatter") from exc
    required = {"name:", "description:"}
    missing = [key for key in required if key not in frontmatter]
    if missing:
        raise SystemExit(f"{path} frontmatter missing: {', '.join(missing)}")
    if "#" not in body:
        raise SystemExit(f"{path} body appears empty")


def sync(repo: str, ref: str, source_path: str) -> dict[str, str]:
    root = repo_root()
    target = root / TARGET_PATH
    state = root / STATE_PATH
    with tempfile.TemporaryDirectory(prefix="karpathy-upstream-") as tmp:
        clone_dir = Path(tmp) / "upstream"
        run(["git", "clone", "--quiet", "--depth", "1", "--branch", ref, repo, str(clone_dir)])
        commit = run(["git", "rev-parse", "HEAD"], cwd=clone_dir)
        source = clone_dir / source_path
        if not source.exists():
            raise SystemExit(f"Upstream file not found: {source_path}")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        validate_skill(target)

    payload = {
        "repo": repo,
        "ref": ref,
        "source_path": source_path,
        "target_path": str(TARGET_PATH),
        "commit": commit,
    }
    state.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Codex skill from upstream repository")
    parser.add_argument("--repo", default=DEFAULT_REPO, help=f"upstream git URL (default: {DEFAULT_REPO})")
    parser.add_argument("--ref", default=DEFAULT_REF, help=f"upstream branch/tag (default: {DEFAULT_REF})")
    parser.add_argument("--source-path", default=DEFAULT_SOURCE_PATH, help=f"upstream skill file (default: {DEFAULT_SOURCE_PATH})")
    args = parser.parse_args()

    payload = sync(args.repo, args.ref, args.source_path)
    print(f"Synced {payload['source_path']} from {payload['repo']}@{payload['commit']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
