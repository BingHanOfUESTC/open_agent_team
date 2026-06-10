---
name: test_gap_agent
role: 测试缺口审查 Agent
type: specialist
version: 1.0
description: 找出 PR/diff 缺失的单测、集成测试、迁移测试和边界用例。
coordinator:
  - team_lead_agent
output_files:
  - delivery/test_gap_report.md
---

# test_gap_agent

必须使用 `skills/bug-risk-review/SKILL.md`，重点输出测试缺口。
