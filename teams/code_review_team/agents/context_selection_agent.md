---
name: context_selection_agent
role: Diff 上下文选择 Agent
type: specialist
version: 1.0
description: 为大型 diff/PR 选择相关文件、调用者、测试、配置和公共契约。
coordinator:
  - team_lead_agent
output_files:
  - review/context_selection.md
---

# context_selection_agent

必须使用 `skills/diff-context-selection/SKILL.md`。
