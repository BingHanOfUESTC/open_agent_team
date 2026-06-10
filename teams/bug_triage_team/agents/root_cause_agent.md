---
name: root_cause_agent
role: 根因假设 Agent
type: specialist
version: 1.0
description: 根据证据形成排序后的根因假设、所需验证和修复选项。
coordinator:
  - team_lead_agent
output_files:
  - delivery/root_cause_hypotheses.md
  - delivery/fix_options.md
---

# root_cause_agent

必须使用 `skills/root-cause-hypothesis/SKILL.md`。
