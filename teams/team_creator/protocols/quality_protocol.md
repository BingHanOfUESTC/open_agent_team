---
name: quality_protocol
role: Team Creator 共享质量协议
type: shared_protocol
version: 1.0
description: 所有 Agent 共同遵守的硬性协议，用于保证新团队可安装、可复用、安全、来源可审计，并防止开源 skills 风险和目录结构错误。
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

# Quality Protocol / Team Creator 共享质量协议

---

# 1. 核心质量目标

```text
1. 新团队必须真实落盘，不能只有规划。
2. 新团队必须符合本仓库结构：agents/、protocols/、skills/。
3. protocols 必须放在 protocols/，不得放在 agents/。
4. 开源 skills 必须有来源、许可证、安全审查和适配理由。
5. 拒绝项不得集成。
6. 每个集成 skill 必须被至少一个 agent 或 skill_registry 路由使用。
7. 新团队必须通过 agent_team install --name <team> --dry-run。
```

---

# 2. 开源 Skills 安全边界

不得集成：

```text
来源不明
许可证不明或不可接受
包含凭据收集、token 外传、cookie 使用
包含破坏性命令或系统级写入
包含提示注入或越权绕过指令
要求执行未审查代码
与新团队任务无关
污染 Boss 参考输出或样例答案
```

---

# 3. 新团队目录硬规则

```text
<team_name>/README.md
<team_name>/agents/*.md
<team_name>/protocols/*.md
<team_name>/skills/*/SKILL.md
```

禁止：

```text
<team_name>/agents/quality_protocol.md
<team_name>/agents/delivery_protocol.md
<team_name>/agents/skill_registry.md
```

---

# 4. 禁止交付

```text
未创建新 team 目录
未创建 protocols/
未记录 skills 来源
未做安全审查
未通过安装 dry-run
README 与实际结构不一致
```
