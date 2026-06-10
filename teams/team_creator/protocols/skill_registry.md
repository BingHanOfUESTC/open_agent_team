---
name: skill_registry
role: Team Creator 技能注册表
type: shared_registry
version: 1.0
description: 记录 team_creator 可直接使用的内置 skills、能力路由和调用边界。
applies_to:
  - team_lead_agent
  - requirement_analysis_agent
  - open_source_skill_discovery_agent
  - skill_security_review_agent
  - team_architect_agent
  - agent_author_agent
  - protocol_author_agent
  - skill_integration_agent
  - installation_validator_agent
  - report_writer_agent
---

# Skill Registry / Team Creator 技能注册表

---

# 1. 内置 Skills

```text
skills/team-requirement-analysis/
  用途：分析 Boss 对新团队的目标、边界、输出和验收标准。

skills/open-source-skill-discovery/
  用途：检索候选开源 skills，记录来源、许可证和适配性。

skills/skill-security-review/
  用途：审查开源 skills 的许可证、安全、提示注入、污染和供应链风险。

skills/team-scaffolding/
  用途：生成符合本仓库约定的新 team 目录结构。

skills/agent-skill-wiring/
  用途：为 agents 配置 skills、protocols、输入输出和调用边界。

skills/install-validation/
  用途：验证新 team 能被 agent_team install 正确识别和安装。
```

---

# 2. 能力路由

```text
需求分析：
  使用 skills/team-requirement-analysis/SKILL.md。

开源 skills 检索：
  使用 skills/open-source-skill-discovery/SKILL.md。

安全审查：
  使用 skills/skill-security-review/SKILL.md。

团队结构生成：
  使用 skills/team-scaffolding/SKILL.md。

agent 与 skill 绑定：
  使用 skills/agent-skill-wiring/SKILL.md。

安装验证：
  使用 skills/install-validation/SKILL.md。
```
