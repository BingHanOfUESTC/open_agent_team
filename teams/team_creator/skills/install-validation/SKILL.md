---
name: install-validation
type: workflow
description: >
  Validate that a generated team can be installed by the local agent_team installer into an OpenCode .opencode directory.
model-invocable: false
---

# Install Validation

团队创建完成前，必须验证安装器能识别它。

---

# 1. 必跑检查

```text
目录存在：<team_name>/
agents/ 存在
protocols/ 存在
README.md 存在
agents/team_lead_agent.md 存在
protocols/quality_protocol.md 存在
protocols/delivery_protocol.md 存在
skills/ 中每个 skill 有 SKILL.md
agents/ 下没有 protocol 文件
```

---

# 2. 安装器 dry-run

```bash
agent_team install --name <team_name> --path /tmp/<test_project> --dry-run
```

必须记录：

```text
Agents 数量
Protocols 数量
Skills 数量
退出码
错误信息
```

---

# 3. 通过条件

```text
dry-run 退出码为 0
Agents 数量符合架构设计
Protocols 数量不为 0
安装器没有把 protocols 识别为 agents
```
