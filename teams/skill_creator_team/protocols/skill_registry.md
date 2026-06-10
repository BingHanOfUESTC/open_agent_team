---
name: skill_registry
role: Skill 创建能力路由表
type: protocol
version: 1.0
description: 记录 skill_creator_team 可用 skills、调用场景、方法来源和边界。
---

# Skill Registry / Skill 创建能力路由表

## 1. 方法来源

本团队实践以下公开方法原则：

```text
Claude Code skill lessons:
  - skill 是文件夹，不只是 markdown
  - description 服务模型路由
  - gotchas 高价值
  - progressive disclosure 管理上下文成本
  - scripts 帮助 agent 不重复造轮子

Perplexity skill design notes:
  - eval 先于 skill 生成
  - 避免把给人看的 README 写成 skill
  - 正负例路由测试和维护 gotchas 很重要
  - 新 skill 可能影响其他 skill，要审查 action at a distance

Codex local skill-creator guide:
  - concise is key
  - 按任务脆弱度设置自由度
  - references/scripts/assets 渐进加载
  - 不创建无关辅助文档
```

若 Boss 提供额外文章摘录或内部规范，必须作为 evidence 写入 `00_boss_brief.md`，不得无来源扩展。

## 2. 内置 Skills

```text
skills/skill-requirement-analysis/
  用途：分析用户问题、期望输出、触发条件、复用价值和禁区。

skills/skill-architecture-patterns/
  用途：决定 skill 类型、自由度、文件结构、资源拆分和依赖。

skills/skill-authoring-workflow/
  用途：编写 SKILL.md、description、body、gotchas、资源导航和 frontmatter。

skills/progressive-disclosure-design/
  用途：审查上下文成本，把长内容拆到 references/scripts/assets。

skills/skill-validation-and-evaluation/
  用途：设计验证案例、结构检查、路由检查和评分报告。

skills/skill-maintenance-gotchas/
  用途：维护 gotchas、风险、冲突影响和后续迭代建议。
```

## 3. 能力路由

```text
需求不清：skill-requirement-analysis
需要设计文件结构：skill-architecture-patterns
需要写 SKILL.md：skill-authoring-workflow
内容太长或上下文太重：progressive-disclosure-design
需要验收或测试：skill-validation-and-evaluation
需要维护建议或失败模式：skill-maintenance-gotchas
```
