---
name: delivery_protocol
role: Team Creator 最终交付协议
type: shared_protocol
version: 1.0
description: 规定 team_creator 创建新团队时的最终交付结构、验收标准和禁止交付内容。
applies_to:
  - team_lead_agent
  - installation_validator_agent
  - report_writer_agent
---

# Delivery Protocol / Team Creator 最终交付协议

---

# 1. 最终交付目标

必须交付：

```text
<new_team_name>/
delivery/team_creation_report.md
delivery/skill_sources_report.md
delivery/security_review_report.md
delivery/install_validation_report.md
```

---

# 2. 新团队必须包含

```text
README.md
agents/team_lead_agent.md
protocols/quality_protocol.md
protocols/delivery_protocol.md
protocols/skill_registry.md
skills/
```

---

# 3. 安装验证

必须运行或要求执行：

```bash
agent_team install --name <new_team_name> --path /tmp/<test_project> --dry-run
```

验证输出必须记录：

```text
Agents 数量
Protocols 数量
Skills 数量
是否出现错误
```

---

# 4. 报告要求

`team_creation_report.md` 必须包含：

```text
Boss 需求摘要
新团队结构
agent 职责清单
protocol 职责清单
skill 路由
安装命令
```

`skill_sources_report.md` 必须包含：

```text
候选 skills
集成 skills
拒绝 skills
来源 URL
许可证
修改说明
```

`security_review_report.md` 必须包含：

```text
安全审查维度
风险项
处理动作
最终结论
```

`install_validation_report.md` 必须包含：

```text
目录检查
dry-run 输出
阻断问题
是否可安装
```

---

# 5. 禁止交付

```text
只有设计，没有文件
只有 agents，没有 protocols
有 protocols 但放错目录
有 skills 但无来源和审查
安装器无法识别新 team
```
