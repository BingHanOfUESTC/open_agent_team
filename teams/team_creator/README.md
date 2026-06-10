# Team Creator / Agent Team 创建团队

`team_creator` 是一套负责根据 Boss 需求自动创建新 multi-agent team 的团队。

目标：

> Boss 给出想要的新团队用途、任务边界、期望输出和禁区后，团队自动分析应该配置哪些 agents、protocols 和 skills；检索相关开源 skills；进行安全、许可证、污染和适配性审查；把合格 skills 集成进新团队；为每个 agent 配备必要 skills；最后在当前项目中生成完整新 team，并通过安装器验证。

这套团队不是“写几个 agent 名字”的规划器，而是：

```text
把 Boss 需求变成可安装的新团队目录
把团队结构、职责、协议、技能路由一次性配齐
自动检索开源 skills，但必须安全审查和适配审查
只集成与任务相关、来源可追踪、许可证可接受的 skills
不得把 Boss 的期望输出或参考答案硬编码进 skills
生成后必须能被 agent_team install 安装到 OpenCode 项目
```

---

# 1. 默认定位

```text
目标：创建一个新的可安装 agent team
输出位置：当前仓库根目录下 <new_team_name>/
默认结构：README.md + agents/ + protocols/ + skills/
默认验证：agent_team install --name <new_team_name> --dry-run
Boss 职责：给出新团队目标、期望输出、偏好、禁区、是否允许联网检索开源 skills
团队职责：设计、检索、审查、集成、生成、验证和交付新 team
```

---

# 2. 组织架构

```text
Boss
│
└── @team_lead_agent
    ├── @requirement_analysis_agent
    ├── @open_source_skill_discovery_agent
    ├── @skill_security_review_agent
    ├── @team_architect_agent
    ├── @agent_author_agent
    ├── @protocol_author_agent
    ├── @skill_integration_agent
    ├── @installation_validator_agent
    └── @report_writer_agent
```

---

# 3. 每个 Agent 的职责

```text
agents/team_lead_agent.md                    总控。接收 Boss 需求，调度团队创建全流程。
agents/requirement_analysis_agent.md        分析新团队目标、任务边界、输出要求、禁区和能力缺口。
agents/open_source_skill_discovery_agent.md 检索候选开源 skills，记录来源、用途、许可证和适配理由。
agents/skill_security_review_agent.md       审查候选 skills 的许可证、来源可信度、代码安全、提示注入和污染风险。
agents/team_architect_agent.md              设计新团队 agents、protocols、skills、调度流程和交付结构。
agents/agent_author_agent.md                编写新团队 agent prompt，明确职责、输入输出、skills 调用和门禁。
agents/protocol_author_agent.md             编写新团队 quality/delivery/skill_registry 等共享协议。
agents/skill_integration_agent.md           集成审查通过的开源 skills，并补写本地 skills。
agents/installation_validator_agent.md      验证新团队目录结构和 agent_team install dry-run。
agents/report_writer_agent.md               交付创建报告、技能来源报告、安全审查报告和安装说明。
protocols/quality_protocol.md               团队共享质量协议。
protocols/delivery_protocol.md              最终交付协议。
protocols/skill_registry.md                 内置 skills 与能力路由。
```

---

# 4. 内置 Skills

```text
skills/team-requirement-analysis/       分析 Boss 新团队需求、边界和验收标准。
skills/open-source-skill-discovery/     检索和筛选开源 skills，记录来源、许可证和适配性。
skills/skill-security-review/           审查开源 skills 的安全、许可证、污染和供应链风险。
skills/team-scaffolding/                生成符合本仓库约定的新 team 目录结构。
skills/agent-skill-wiring/              为 agents 配置 skills、protocols 和输入输出边界。
skills/install-validation/              验证新 team 能被 agent_team install 正确安装。
```

---

# 5. Boss Input 模板

```markdown
# Boss Input

## 新团队名称
示例：legal_research_team / podcast_team / data_cleaning_team。

## 团队目标
描述这个 team 要长期解决什么类型的问题。

## 期望输出
描述新 team 最终运行时应该交付什么。

## 适用范围
可选。这个 team 应该处理哪些任务。

## 禁区
可选。哪些任务、来源、风格、行为或风险必须禁止。

## 开源 skills 检索
允许 / 不允许。默认允许，但必须做安全审查。

## 许可证要求
可选。默认只接受可在本项目中合理复用且来源可追踪的内容。

## 迭代上限
可选。默认 2 轮架构修订。
```

---

# 6. 默认流程

```text
1. Producer 建立 Boss brief
2. Requirement Analysis 分析新团队目标和能力需求
3. Open Source Skill Discovery 检索候选开源 skills
4. Skill Security Review 审查候选 skills
5. Team Architect 设计新团队结构、agents、protocols、skills 路由
6. Agent Author 编写 agents/*.md
7. Protocol Author 编写 protocols/*.md
8. Skill Integration 集成审查通过的 skills，补写本地 skills
9. Installation Validator 运行 agent_team install --name <new_team> --dry-run
10. Report Writer 交付创建报告和使用说明
```

---

# 7. 强制边界

```text
不得集成来源不明或许可证不可接受的开源 skills
不得集成含恶意命令、凭据窃取、破坏性操作或提示注入的 skills
不得把 Boss 的参考输出、样例答案或专属任务结果写进 skills
不得只写规划文档而不创建实际 team 目录
不得跳过安装验证
不得让 protocols 放入 agents/；必须放入 protocols/
```

---

# 8. 默认交付

```text
<new_team_name>/
delivery/team_creation_report.md
delivery/skill_sources_report.md
delivery/security_review_report.md
delivery/install_validation_report.md
```
