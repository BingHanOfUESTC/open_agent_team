# Skill Creator Team / Skill 定制生成团队

`skill_creator_team` 是一套根据用户问题、任务场景和可选期望结果，定制生成可复用 agent skills 的 multi-agent team。

目标：

> Boss 给出一个反复出现的问题、工作流、工具使用场景，或同时给出期望输出样例后，团队负责分析真正需要沉淀的可泛化能力，设计 skill 边界和文件结构，生成 `SKILL.md` 与必要的 references/scripts/assets，并通过路由、结构、污染和验证用例审查，交付可安装、可维护、可迭代的 skill。

这套团队不是“把用户需求改写成一个长提示词”。它的定位是：

```text
把一次问题背后的复用能力抽象成 skill
让 description 服务模型路由，而不是写给人类看的宣传摘要
用 progressive disclosure 控制上下文成本
把脆弱、重复、可验证的步骤沉淀为 scripts 或模板
用 gotchas、正负例和验证任务驱动维护
避免把用户样例答案、专属实体或一次性结论写进 skill
```

---

# 1. 默认定位

```text
目标：根据用户问题或期望结果创建可复用 skill
适用：研究、写作、代码、数据处理、文件生成、工具集成、审查流程、内部工作流等可复用任务
默认输出：generated_skills/<skill_name>/SKILL.md
可选输出：references/、scripts/、assets/、validation_report.md、maintenance_notes.md
Boss 职责：给出问题、使用场景、期望输出、禁区、目标平台或安装位置
团队职责：需求分析、skill 架构、skill 编写、渐进加载设计、验证审查和交付说明
```

---

# 2. 组织架构

```text
Boss
│
└── @team_lead_agent
    ├── @requirement_analysis_agent
    ├── @skill_architect_agent
    ├── @skill_author_agent
    ├── @progressive_disclosure_agent
    ├── @validation_agent
    ├── @maintenance_reviewer_agent
    └── @report_writer_agent
```

---

# 3. Agent 职责

```text
agents/team_lead_agent.md                 总控。调度需求分析、架构设计、skill 编写、验证和交付。
agents/requirement_analysis_agent.md      从用户问题和期望输出中提炼触发场景、复用价值、输入输出和禁区。
agents/skill_architect_agent.md           设计 skill 类型、边界、文件夹结构、资源拆分、自由度和依赖。
agents/skill_author_agent.md              编写 SKILL.md、frontmatter、核心流程、gotchas 和必要资源。
agents/progressive_disclosure_agent.md    审查上下文成本，决定哪些内容留在 SKILL.md，哪些放入 references/scripts/assets。
agents/validation_agent.md                设计正例、负例、结构检查、路由检查和最小可执行验证。
agents/maintenance_reviewer_agent.md      评估可维护性、gotchas、版本迭代方式、对其他 skills 的影响。
agents/report_writer_agent.md             交付 skill 包、使用说明、验证报告和维护建议。
protocols/quality_protocol.md             团队共享质量协议。
protocols/delivery_protocol.md            最终交付协议。
protocols/skill_registry.md               内置 skills 与能力路由。
```

---

# 4. 内置 Skills

```text
skills/skill-requirement-analysis/        从问题和期望结果提炼触发条件、复用场景和验收标准。
skills/skill-architecture-patterns/       选择 skill 类型、自由度、文件结构和资源拆分方式。
skills/skill-authoring-workflow/          编写 SKILL.md、description、body、gotchas 和资源导航。
skills/progressive-disclosure-design/     设计 metadata -> SKILL.md -> references/scripts/assets 的渐进加载。
skills/skill-validation-and-evaluation/   设计正负例、结构验证、路由验证和质量评分。
skills/skill-maintenance-gotchas/         维护 gotchas、变更记录、冲突风险和后续迭代建议。
```

---

# 5. Boss Input 模板

```markdown
# Boss Input

## 想创建的 skill
一句话描述。示例：让 agent 能稳定生成可编辑 PPT；让 agent 能审查某类 API 变更。

## 用户问题或典型任务
贴出真实用户问题、重复出现的工作流、工具使用场景或失败案例。

## 期望输出
可选。可以给目标结果、示例输出、评分标准或交付格式。

## 使用环境
可选。Codex / Claude Code / OpenCode / 内部 agent；是否有本地脚本、API、文件模板。

## 可复用范围
这个 skill 应该适用于哪些任务，不应该适用于哪些任务。

## 禁区
示例：不要硬编码样例答案；不要把客户私有数据写入 skill；不要依赖不可复现网页。

## 验证要求
可选。希望提供正例、负例、dry-run、脚本校验或真实任务验证。
```

---

# 6. 默认流程

```text
1. Team Lead 建立 00_boss_brief.md
2. Requirement Analysis 输出 01_skill_requirements.md
3. Skill Architect 输出 02_skill_architecture.md
4. Skill Author 生成 generated_skills/<skill_name>/SKILL.md 和必要资源
5. Progressive Disclosure Agent 审查上下文成本和资源拆分
6. Validation Agent 生成 validation/validation_cases.md 并运行结构检查
7. Maintenance Reviewer 输出 maintenance/gotchas_and_risks.md
8. 必要时返修 skill
9. Report Writer 交付 delivery/skill_creation_report.md
```

---

# 7. 强制边界

```text
不得把用户给出的期望答案原样写进 skill
不得把一次性任务结果伪装成通用方法
不得让 SKILL.md 变成长篇教程或 README
不得在 description 里写泛泛总结，必须写触发条件和适用场景
不得无验证用例就声称 skill 可用
不得把所有细节塞进 SKILL.md；长内容必须拆到 references/scripts/assets
不得创建与任务无关的辅助文档污染 skill 包
```

---

# 8. 默认交付

```text
generated_skills/<skill_name>/SKILL.md
generated_skills/<skill_name>/references/      可选
generated_skills/<skill_name>/scripts/         可选
generated_skills/<skill_name>/assets/          可选
validation/validation_cases.md
validation/validation_report.md
maintenance/gotchas_and_risks.md
delivery/skill_creation_report.md
```
