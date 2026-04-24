# Andrej Karpathy Skills for Codex

[中文 README](README.md)

Codex-compatible packaging for [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills).

This repository republishes the upstream `karpathy-guidelines` skill in Codex's installable skill layout, so Codex users can install it directly from GitHub and keep it synchronized with upstream changes.

```text
skills/karpathy-guidelines/SKILL.md
skills/karpathy-guidelines/agents/openai.yaml
```

## Source and attribution

- **Original skill repository:** [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills)
- **Original idea:** Andrej Karpathy's observations about common LLM coding pitfalls, linked from the upstream skill.
- **License:** MIT, following the upstream skill metadata.

This repo only adds Codex packaging, Codex UI metadata, installation instructions, and upstream sync automation. The guideline content remains sourced from Forrest Chang's upstream repository.

## What this skill does

`karpathy-guidelines` is a behavioral guardrail skill for coding agents. Use it when writing, reviewing, debugging, or refactoring code to reduce common LLM coding mistakes.

It nudges Codex to:

- think before changing code;
- surface assumptions and ambiguity instead of hiding them;
- prefer the simplest working implementation;
- make surgical, request-scoped edits;
- avoid speculative abstractions and unasked-for features;
- define success criteria before implementation;
- verify the result with tests or concrete checks.

## Why use it

This skill is useful when you want Codex to behave more like a careful senior engineer:

- **Less over-engineering:** discourages premature abstractions and unnecessary configurability.
- **Smaller diffs:** pushes for minimal, traceable changes.
- **Clearer reasoning:** makes assumptions, tradeoffs, and uncertainty explicit.
- **Better verification:** turns vague tasks into checkable goals and testable outcomes.
- **Safer refactors:** avoids touching unrelated code or cleaning up outside the requested scope.

## Install in Codex

Install directly from GitHub with Codex's skill installer:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo 0xyanyan/andrej-karpathy-skills-codex \
  --path skills/karpathy-guidelines
```

Then restart Codex so the new skill is discovered.

## Usage

Invoke it explicitly when you want stricter coding guardrails:

```text
Use $karpathy-guidelines while implementing this change.
```

Example prompts:

```text
Use $karpathy-guidelines to fix this bug with the smallest safe diff and add a regression test.
```

```text
Use $karpathy-guidelines to review this refactor plan and point out over-engineering risks.
```

```text
Use $karpathy-guidelines while simplifying this module. Do not change behavior.
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

A scheduled GitHub Actions workflow also runs the same sync script and opens or updates a PR when upstream changes.
