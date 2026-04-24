# Andrej Karpathy Skills for Codex

[English README](README.md)

这是 [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills) 的 Codex 可用版本。

本仓库把上游的 `karpathy-guidelines` skill 重新整理为 Codex 可安装的目录结构，让 Codex 用户可以直接从 GitHub 安装，也方便后续同步上游更新。

```text
skills/karpathy-guidelines/SKILL.md
skills/karpathy-guidelines/agents/openai.yaml
```

## 出处与致谢

- **原始 skill 仓库：** [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills)
- **原始灵感：** 上游 skill 中引用的 Andrej Karpathy 关于 LLM 写代码常见问题的观察。
- **许可证：** MIT，沿用上游 skill 元数据。

本仓库只增加了 Codex 包装、Codex UI 元数据、安装说明和上游同步自动化。skill 的核心 guideline 内容仍然来自 Forrest Chang 的上游仓库。

## 这个 skill 可以做什么

`karpathy-guidelines` 是一个面向编码代理的行为准则 skill。适合在写代码、代码审查、调试、重构时使用，用来减少 LLM 写代码时常见的问题。

它会提醒 Codex：

- 先思考，再改代码；
- 主动暴露假设、歧义和不确定性；
- 优先选择最简单可工作的实现；
- 做小而精准的修改，不扩大范围；
- 避免过度抽象、过度设计和没有被要求的功能；
- 在实现前定义可验证的成功标准；
- 用测试或具体检查来验证结果。

## 优点

这个 skill 适合希望 Codex 更像谨慎资深工程师一样工作的场景：

- **减少过度工程化：** 避免提前抽象、无意义配置和 speculative features。
- **diff 更小：** 鼓励只修改与用户需求直接相关的代码。
- **推理更透明：** 明确说明假设、取舍和不确定点。
- **验证更扎实：** 把模糊任务转成可以检查、可以测试的目标。
- **重构更安全：** 避免顺手改无关代码，降低引入回归的风险。

## 在 Codex 中安装

使用 Codex 自带的 skill installer 从 GitHub 安装：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo 0xyanyan/andrej-karpathy-skills-codex \
  --path skills/karpathy-guidelines
```

安装后重启 Codex，让 Codex 重新发现新 skill。

## 使用方法

当你希望 Codex 更严格地遵守这些编码准则时，显式调用：

```text
Use $karpathy-guidelines while implementing this change.
```

示例：

```text
Use $karpathy-guidelines to fix this bug with the smallest safe diff and add a regression test.
```

```text
Use $karpathy-guidelines to review this refactor plan and point out over-engineering risks.
```

```text
Use $karpathy-guidelines while simplifying this module. Do not change behavior.
```

也可以用中文描述任务，同时保留 `$karpathy-guidelines` 触发词：

```text
请使用 $karpathy-guidelines 修复这个 bug，要求改动尽量小，并补一个回归测试。
```

## 同步上游更新

上游 Forrest Chang 的仓库仍是 guideline 内容的来源。手动同步方式：

```bash
python3 scripts/sync-upstream.py
git diff
git add skills/karpathy-guidelines/SKILL.md .upstream-sync.json
git commit -m "Sync Karpathy guidelines from upstream"
git push
```

仓库里也配置了 GitHub Actions：每天自动检查上游，如果发现变化，会自动创建或更新一个同步 PR，方便 review 后合并。
