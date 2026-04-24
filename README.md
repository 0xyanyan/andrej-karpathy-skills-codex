# Andrej Karpathy Skills for Codex

Codex-compatible packaging for [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills).

This repo keeps the upstream `karpathy-guidelines` skill in Codex's installable skill layout:

```text
skills/karpathy-guidelines/SKILL.md
skills/karpathy-guidelines/agents/openai.yaml
```

## Install in Codex

Install directly from GitHub with Codex's skill installer:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo no-later-cn/andrej-karpathy-skills-codex \
  --path skills/karpathy-guidelines
```

Then restart Codex so the new skill is discovered.

Use it explicitly when you want the guardrails:

```text
Use $karpathy-guidelines while implementing this change.
```

## Sync from upstream

The source of truth is Forrest Chang's upstream repository. To pull updates into this Codex package:

```bash
python3 scripts/sync-upstream.py
git diff
git add skills/karpathy-guidelines/SKILL.md .upstream-sync.json
git commit -m "Sync Karpathy guidelines from upstream"
git push
```

A scheduled GitHub Actions workflow also runs the same sync script and opens/updates a PR when upstream changes.

## Attribution

The guideline content is derived from [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills), which is published under the MIT license. This repository only adds Codex packaging, install metadata, and sync automation.
