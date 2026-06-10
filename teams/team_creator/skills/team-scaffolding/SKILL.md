---
name: team-scaffolding
type: workflow
description: >
  Create a repository-native team folder with README.md, agents/, protocols/, and skills/ using the project conventions expected by the agent_team installer.
model-invocable: false
---

# Team Scaffolding

新团队必须符合本仓库结构，才能被安装器识别。

---

# 1. 标准结构

```text
<team_name>/
  README.md
  agents/
    team_lead_agent.md
    *_agent.md
  protocols/
    quality_protocol.md
    delivery_protocol.md
    skill_registry.md
  skills/
    <skill_name>/
      SKILL.md
```

---

# 2. README 必须包含

```text
团队目标
默认定位
组织架构
每个 agent 职责
内置 skills
Boss input 模板
默认流程
强制边界
默认交付
```

---

# 3. Agent 文件必须包含

```text
YAML front matter
name
role
type
version
description
input_files
output_files
coordinator
正文职责说明
必用 skills
禁止行为
```

---

# 4. Protocol 文件必须放在 protocols/

禁止放在：

```text
agents/quality_protocol.md
agents/delivery_protocol.md
agents/skill_registry.md
```
