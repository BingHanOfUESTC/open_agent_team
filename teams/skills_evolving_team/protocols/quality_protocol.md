---
name: quality_protocol
role: 技能自进化共享质量协议
type: shared_protocol
version: 1.0
description: 所有 Agent 共同遵守的硬性协议，用于防止 skill 污染、任务过拟合、无评价交付和形式化迭代。
applies_to:
  - team_lead_agent
  - requirement_analysis_agent
  - skill_architect_agent
  - skill_author_agent
  - contamination_guard_agent
  - execution_agent
  - evaluator_agent
  - iteration_controller_agent
  - report_writer_agent
---

# Quality Protocol / 技能自进化共享质量协议

本协议高于任何局部 agent 习惯。

---

# 1. 核心目标

```text
1. 技能可泛化：skill 必须表达方法，而不是记忆本次答案。
2. 污染可审计：Boss 参考输出只能用于评价，不能进入 skill。
3. 执行可复现：每轮必须记录使用的 skill 版本和执行日志。
4. 评价可追踪：每轮必须有分项评分、P0/P1/P2 和失败归因。
5. 迭代真实发生：未通过时必须产生新 skill 版本或新执行结果。
6. 交付不粉饰：到达上限未通过时不得声称通过。
```

---

# 2. 允许进入 skill 的内容

```text
通用方法
流程步骤
输入输出约定
评价检查表
失败模式
抽象示例
跨任务适用的原则
```

---

# 3. 禁止进入 skill 的内容

```text
Boss 参考输出原文
Boss 样例答案的改写版本
本次任务专属实体
本次任务专属结论
为贴合样例而硬编码的结构
不可复用的领域细节
```

---

# 4. 必须维护的文件

```text
00_boss_brief.md
01_requirement_analysis.md
02_skill_architecture.md
generated_skills/vNN/
contamination/skill_audit_vNN.md
outputs/result_vNN.md
outputs/execution_log_vNN.md
evaluations/evaluation_vNN.md
iteration_status.md
delivery/final_result.md
delivery/skills_manifest.md
delivery/evolution_report.md
delivery/contamination_report.md
```

---

# 5. 禁止交付

```text
没有污染审查的 skills
没有执行日志的结果
没有评价分数的结果
没有 iteration_status 的交付
评价未通过却伪称通过
把 Boss 参考输出写入 skill 的交付
```
