---
name: delivery_protocol
role: 技能自进化最终交付协议
type: shared_protocol
version: 1.0
description: 规定技能自进化团队的交付结构、验收标准和禁止交付内容。
applies_to:
  - team_lead_agent
  - iteration_controller_agent
  - report_writer_agent
---

# Delivery Protocol / 技能自进化最终交付协议

---

# 1. 最终交付

```text
delivery/final_result.md
delivery/skills_manifest.md
delivery/evolution_report.md
delivery/contamination_report.md
```

---

# 2. final_result.md

必须包含：

```text
最终任务结果
使用的 skill 版本
是否达到通过分
残留风险
```

---

# 3. skills_manifest.md

必须包含：

```text
最终 skills 清单
每个 skill 的用途
每个 skill 的输入输出
每个 skill 的泛化边界
每个 skill 的污染审查结论
```

---

# 4. evolution_report.md

必须包含：

```text
Boss 任务摘要
技能拆分逻辑
每轮 skill 版本变化
每轮执行结果
每轮评价分数
失败归因和修正动作
最终是否通过
```

---

# 5. contamination_report.md

必须包含：

```text
参考输出隔离说明
被禁止进入 skill 的内容清单
每轮污染审查结论
残留污染风险
```

---

# 6. 验收标准

```text
iteration_status.md 决策为 pass_to_delivery 或 stop_at_limit_with_boss_approval
最终 skills 已通过污染审查
最终结果已有评价分数
未达标时已明确标注
```
