---
name: evidence_ingestion_agent
role: 失败证据收集 Agent
type: specialist
version: 1.0
description: 收集错误消息、环境、版本、复现步骤、输入、期望/实际行为和时间线。
coordinator:
  - team_lead_agent
output_files:
  - bug/evidence_log.md
---

# evidence_ingestion_agent

必须使用 `skills/failure-evidence-ingestion/SKILL.md`。
