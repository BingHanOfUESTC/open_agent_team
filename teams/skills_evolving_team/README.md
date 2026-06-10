# Skills Evolving Team / 技能自进化团队

`skills_evolving_team` 是一套面向“按 Boss 目标自动设计、生成、执行、评价并迭代 skills”的 multi-agent team。

目标：

> Boss 给出任务、期望输出、评价标准和迭代上限后，团队先分析要达成这种输出需要哪些可泛化技能，再创建或更新这些技能，随后使用技能执行任务生成结果，并将结果与 Boss 期望输出和评价标准比对，持续迭代到通过分或达到迭代上限。

这套团队不是一次性提示词调参器，也不是把 Boss 样例答案塞进 skill 的记忆器。它的定位是：

```text
把一次任务背后的可复用能力抽象出来
把 skills 写成方法、流程、检查表和能力边界
用版本化执行结果和评价结果驱动 skill 迭代
严格禁止把 Boss 给出的目标输出、参考答案、样例文本原样写入 skill
最终交付任务结果、技能清单、迭代记录和污染风险报告
```

---

# 1. 默认定位

```text
目标：自动拆分、创建、验证和迭代可泛化 skills
适用：写作、研究、分析、产品设计、报告生成、评审流程、数据整理等可流程化任务
默认迭代上限：3 轮
默认通过分：8.5 / 10
Boss 职责：给出任务、期望输出、禁区、评价标准和迭代上限
团队职责：分析能力缺口、设计 skills、执行任务、评价结果、迭代修正、交付结果
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
    ├── @contamination_guard_agent
    ├── @execution_agent
    ├── @evaluator_agent
    ├── @iteration_controller_agent
    └── @report_writer_agent
```

---

# 3. 每个 Agent 的职责

```text
agents/team_lead_agent.md              总控。接收 Boss 输入，调度技能拆分、创建、执行、评价和迭代。
agents/requirement_analysis_agent.md  分析 Boss 任务、期望输出、评价标准、禁区和可泛化能力需求。
agents/skill_architect_agent.md       将能力需求拆成技能体系、技能边界、调用顺序和验收标准。
agents/skill_author_agent.md          编写或更新 skills，确保是可泛化方法而不是样例记忆。
agents/contamination_guard_agent.md   审查 skills 是否泄漏 Boss 参考输出、样例答案或任务专属内容。
agents/execution_agent.md             使用当前 skills 执行 Boss 任务，生成候选结果。
agents/evaluator_agent.md             按 Boss 期望输出和评价标准，对候选结果打分和指出差距。
agents/iteration_controller_agent.md  维护版本化迭代状态，决定继续修 skill / 继续执行 / 通过 / 到达上限。
agents/report_writer_agent.md         交付最终结果、技能清单、评价记录、迭代记录和污染风险报告。
protocols/quality_protocol.md            团队共享质量协议。
protocols/delivery_protocol.md           最终交付协议。
protocols/skill_registry.md              内置 skills 与能力路由。
```

---

# 4. 内置 Skills

```text
skills/skill-decomposition-framework/   将目标输出拆解成可泛化技能、能力边界和调用链。
skills/generalizable-skill-authoring/   编写可复用、不污染、不记忆样例答案的 SKILL.md。
skills/output-evaluation-rubric/        构建评分表、差距分析和通过/返修判断。
skills/contamination-guard/             检查 skill 是否被 Boss 样例、参考答案、专属输出污染。
skills/iteration-workflow/              版本化技能迭代、执行结果迭代和状态机。
```

---

# 5. Boss Input 模板

```markdown
# Boss Input

## 任务
描述希望团队最终完成什么。

## 期望输出
描述输出格式、质量、结构、风格、评价标准。可以给参考输出，但参考输出只能用于评价，不得写入 skills。

## 评价标准
可选。示例：准确性、结构完整度、可读性、复用性、风格一致性、数据可靠性。

## 迭代上限
可选。默认 3 轮。

## 通过分
可选。默认 8.5 / 10。

## 禁区
可选。示例：不要把参考答案写进 skill，不要硬编码本次任务，不要依赖不可复现来源。
```

---

# 6. 默认流程

```text
1. Producer 建立 Boss brief、通过分和迭代上限
2. Requirement Analysis 分析目标输出需要的能力
3. Skill Architect 设计技能拆分、技能边界和调用顺序
4. Skill Author 生成或更新 skills/draft_skills_vNN/
5. Contamination Guard 审查技能污染风险
6. Execution Agent 使用当前 skills 执行任务，生成 outputs/result_vNN.md
7. Evaluator 对 result_vNN 打分，输出 evaluations/evaluation_vNN.md
8. Iteration Controller 判断通过、继续改 skill、继续改执行结果或停止
9. 未通过则循环 3-8
10. Report Writer 交付最终结果和技能进化报告
```

---

# 7. 强制边界

```text
Boss 给出的参考输出只能进入 evaluation，不得进入 skill 正文
skill 只能写可复用的方法、流程、检查表、输入输出约定和失败模式
不得把本次任务的专属实体、结论、样例段落、答案结构硬编码进 skill
不得因为结果凑近参考输出就牺牲 skill 泛化性
不得无评价记录直接交付最终结果
不得无污染审查直接启用新 skill
```

---

# 8. 默认交付

```text
delivery/final_result.md
delivery/skills_manifest.md
delivery/evolution_report.md
delivery/contamination_report.md
iteration_status.md
```
