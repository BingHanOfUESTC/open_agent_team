---
name: agent-skill-wiring
type: reference
description: >
  Wire agents to relevant skills, protocols, inputs, outputs, and quality gates so a generated team has usable routing instead of isolated files.
model-invocable: false
---

# Agent Skill Wiring

一个 team 不是文件堆。每个 agent 都必须知道何时使用哪些 skills，产出什么文件，交给谁。

---

# 1. Wiring 要素

每个 agent 必须明确：

```text
上游输入
下游输出
必须遵守的 protocols
必须使用的 skills
可选 skills
质量门禁
禁止行为
下游 agent
```

---

# 2. Skill Registry 要求

`protocols/skill_registry.md` 必须包含：

```text
skills 清单
每个 skill 来源
每个 skill 用途
能力路由
缺口处理
```

---

# 3. 检查

```text
每个 skill 是否至少被一个 agent 使用
每个 agent 是否至少有一个清晰职责
是否存在职责重复的 agent
是否存在没有质量门禁的关键路径
是否存在未被 protocol 约束的高风险行为
```
