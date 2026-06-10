---
name: team-requirement-analysis
type: reference
description: >
  Analyze Boss requirements for a new agent team and turn them into team goals, task boundaries, output expectations, agent roles, protocols, and skill needs.
model-invocable: false
---

# Team Requirement Analysis

新团队需求分析的目标是识别“这个团队长期应该解决哪类问题”，而不是只完成 Boss 当前的一次任务。

---

# 1. 分析维度

```text
团队目标：长期解决什么问题。
适用范围：哪些输入和任务应该由该 team 处理。
不适用范围：哪些任务必须拒绝或转交。
期望输出：最终交付的格式、质量和文件。
工作流：任务应如何被拆分和调度。
角色需求：需要哪些 agents 才能形成闭环。
协议需求：哪些硬规则必须全队共享。
技能需求：哪些方法或工具应沉淀为 skills。
安全需求：数据、许可证、外部工具和执行边界。
```

---

# 2. Agent 设计原则

```text
team_lead_agent 负责总控和门禁。
专业 agent 负责明确阶段，不要职责重叠。
critic / evaluator / validator 负责质量反馈。
report_writer 负责最终交付。
```

---

# 3. 输出检查

需求分析必须能回答：

```text
为什么需要这个 team
这个 team 与现有 team 有何区别
至少需要哪些 agents
至少需要哪些 protocols
哪些 skills 可以检索复用
哪些 skills 必须本地补写
如何验证 team 可安装可用
```
