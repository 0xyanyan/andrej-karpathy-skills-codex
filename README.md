# Andrej Karpathy Skills for Codex

[English README](README.en.md)

这是 [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills) 的 Codex 可用版本。

本仓库把上游的 `karpathy-guidelines` skill 重新整理为 Codex 可安装的目录结构，让 Codex 用户可以直接从 GitHub 安装、分享给他人使用，并通过自动化流程跟随上游更新。

```text
skills/karpathy-guidelines/SKILL.md
skills/karpathy-guidelines/agents/openai.yaml
```

## 出处与致谢

- **原始 skill 仓库：** [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills)
- **原始灵感：** 上游 skill 中引用的 Andrej Karpathy 关于 LLM 写代码常见问题的观察。
- **许可证：** MIT，沿用上游 skill 元数据。

本仓库只增加了 Codex 包装、Codex UI 元数据、安装说明、中文文档和上游同步自动化。skill 的核心 guideline 内容仍然来自 Forrest Chang 的上游仓库。

## 这个 skill 是什么

`karpathy-guidelines` 是一个面向 Codex / AI 编码代理的“行为准则”skill。它不是某个框架的代码模板，也不是一个会生成特定文件的工具，而是一组用来约束 AI 写代码方式的工程习惯。

它的目标是让 Codex 在处理代码任务时更谨慎、更简洁、更可验证，减少常见的 LLM 编码问题，例如：

- 没弄清需求就开始大改；
- 为简单问题写复杂抽象；
- 顺手重构无关代码；
- 添加用户没有要求的功能；
- 不说明假设和风险；
- 没有测试或验证就声称完成。

## 它可以做什么

启用 `$karpathy-guidelines` 后，它会提醒 Codex 在编码任务中遵循这些原则：

1. **先思考再改代码**
   - 明确任务目标；
   - 识别假设、歧义和风险；
   - 如果有更简单的方案，优先指出并采用。

2. **简单优先**
   - 用能解决问题的最小实现；
   - 不为了“以后可能用到”而提前抽象；
   - 不添加没有被要求的配置、扩展点或功能。

3. **精准修改**
   - 只修改和任务直接相关的代码；
   - 匹配项目现有风格；
   - 不借机格式化、重构或清理无关文件。

4. **目标驱动执行**
   - 把“修一下”“优化一下”这类模糊任务转成可验证目标；
   - 优先补回归测试或验证步骤；
   - 运行检查后再报告完成。

## 优点

这个 skill 特别适合希望 Codex 更像“谨慎的资深工程师”而不是“过度热心的代码生成器”时使用。

- **减少过度工程化**：避免把小 bug 修成大重构。
- **降低回归风险**：鼓励最小改动和明确验证。
- **代码 diff 更小**：更容易 review，也更容易回滚。
- **推理更透明**：会主动说明假设、取舍和不确定点。
- **更适合真实项目协作**：不会随意改动无关文件或引入额外复杂度。
- **提升任务完成质量**：把实现和验证绑定起来，而不是只“看起来完成”。

## 适合的使用场景

### 1. 修 bug

当你希望 Codex 先定位原因、补回归测试、再做最小修复时使用。

```text
请使用 $karpathy-guidelines 修复登录失败的问题。要求先找到原因，尽量做最小改动，并补一个回归测试。
```

适合避免：为了修一个 bug 顺手重构整个登录模块。

### 2. 小功能开发

当你要加一个明确的小功能，但不希望 Codex 自动扩展需求时使用。

```text
Use $karpathy-guidelines to add email format validation to the signup form. Keep the implementation minimal and reuse existing validation patterns.
```

适合避免：额外引入新的表单库、验证框架或复杂配置。

### 3. 重构或清理代码

当你希望 Codex 保持行为不变，只做局部简化时使用。

```text
请使用 $karpathy-guidelines 简化这个模块。不要改变现有行为，不要顺手改无关代码。先说明验证方式。
```

适合避免：把“简化一个函数”变成跨模块重写。

### 4. Code review

当你希望 Codex 审查 PR 或 diff 中是否存在过度设计、范围膨胀、验证不足时使用。

```text
Use $karpathy-guidelines to review this diff. Focus on over-engineering, unrelated changes, missing assumptions, and missing tests.
```

适合发现：不必要抽象、无关格式化、测试缺口、隐藏假设。

### 5. 计划实现方案

当你还没开始写代码，希望先让 Codex 给出最小可验证实现计划时使用。

```text
请使用 $karpathy-guidelines 为这个需求制定实现计划：只给最小可行方案、需要改哪些文件、如何验证，不要设计未来扩展。
```

适合避免：还没写代码就设计复杂架构。

### 6. 处理不明确需求

当需求存在多种解释，希望 Codex 不要直接猜测时使用。

```text
Use $karpathy-guidelines to analyze this request. If there are multiple interpretations, list them first and recommend the simplest safe path.
```

适合避免：AI 静默选择一个解释并写错方向。

## 不太适合的场景

这个 skill 会让 Codex 偏谨慎、偏保守，因此不一定适合所有任务。

不太适合：

- 快速头脑风暴，需要大量发散想法；
- 原型探索，允许大范围试错；
- 用户明确要求大规模重构或重新设计；
- 非代码类创意写作任务。

如果任务非常简单，也可以不用它，避免额外流程感。

## 在 Codex 中安装

使用 Codex 自带的 skill installer 从 GitHub 安装：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo 0xyanyan/andrej-karpathy-skills-codex \
  --path skills/karpathy-guidelines
```

安装后重启 Codex，让 Codex 重新发现新 skill。

## 使用方法

最简单的方式是在任务中显式写出 `$karpathy-guidelines`：

```text
Use $karpathy-guidelines while implementing this change.
```

中文任务也可以保留 `$karpathy-guidelines` 触发词：

```text
请使用 $karpathy-guidelines 修复这个 bug，要求改动尽量小，并补一个回归测试。
```

### 更多使用示例

#### 示例：最小修复

```text
Use $karpathy-guidelines to fix the failing test. Do not refactor unrelated code. Explain the root cause and run the relevant test afterward.
```

#### 示例：避免过度设计

```text
请使用 $karpathy-guidelines 实现这个小功能。不要引入新依赖，不要做未来扩展，只实现当前需求并说明验证方式。
```

#### 示例：安全重构

```text
Use $karpathy-guidelines to refactor this file for readability. Preserve behavior, keep the diff small, and run the existing test suite.
```

#### 示例：审查 AI 生成代码

```text
请使用 $karpathy-guidelines 审查这段 AI 生成的代码，重点看是否过度抽象、是否改了无关逻辑、是否缺少测试。
```

#### 示例：需求澄清

```text
Use $karpathy-guidelines to inspect this feature request. Before coding, list assumptions, ambiguous points, and the smallest verifiable implementation plan.
```

#### 示例：提交前检查

```text
请使用 $karpathy-guidelines 检查当前 diff：每一处修改是否都能对应到需求？有没有无关改动？验证是否足够？
```

## 推荐工作流

一个常见的使用方式：

```text
请使用 $karpathy-guidelines 完成这个任务：
1. 先说明你理解的目标和成功标准；
2. 找到需要修改的最小代码范围；
3. 实现最小改动；
4. 运行相关测试或检查；
5. 最后说明修改了什么、如何验证、还有什么风险。
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
