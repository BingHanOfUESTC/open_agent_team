# Survey Agent / 科研调研与论文雷达团队

`paper_survey_team` 是一套面向 Boss 私人使用的科研调研 multi-agent team。

目标很明确：

> Boss 给出研究方向、关键词、今日论文推荐需求或具体论文，团队自动搜集论文、实验室、团队、人员、方法路线和社区动态，交付一份结构严谨、引用清楚、能看出发展轨迹和未来问题的科研调研报告。

这套团队不是“论文摘要堆叠器”。它的定位是：

```text
把研究方向拆成问题定义、方法演进、关键论文、实验室团队、代表人物和未解问题
把今日论文推荐做成可筛选、可排序、可解释的研究雷达
把单篇论文深读做成背景、贡献、方法、实验、局限、衍生问题和延伸阅读的完整分析
把“影响力路径”和“问题-方法脉络”同时讲清楚
所有关键结论必须有论文、作者、机构、年份或来源支撑
```

---

# 1. 默认定位

```text
目标：科研方向综述、今日论文推荐、单篇论文深读
适用：AI、机器学习、系统、机器人、生命科学、材料、物理、社会科学等可通过论文和公开资料调研的方向
默认来源：arXiv、Semantic Scholar、Google Scholar、OpenReview、ACL Anthology、Papers with Code、Hugging Face Papers、会议官网、实验室主页、作者主页
Boss 职责：给出方向、偏好、领域边界和报告深度
团队职责：搜集、筛选、引用、综合、脉络化、报告交付
```

---

# 2. 最终组织架构

```text
Boss
│
└── @team_lead_agent
    ├── @query_planning_agent
    ├── @paper_discovery_agent
    ├── @lineage_mapping_agent
    ├── @lab_people_agent
    ├── @method_taxonomy_agent
    ├── @paper_deep_read_agent
    ├── @daily_paper_radar_agent
    ├── @synthesis_insight_agent
    └── @report_writer_agent
```

---

# 3. 每个 Agent 的职责

```text
agents/team_lead_agent.md             总控。识别任务类型，调度综述、今日推荐或单篇深读流程。
agents/query_planning_agent.md       将 Boss 输入拆成关键词、同义词、领域边界、检索式和筛选标准。
agents/paper_discovery_agent.md      搜集论文、元数据、引用线索、代码和社区讨论。
agents/lineage_mapping_agent.md      梳理影响力论文路径、问题定义演进和方法发展轨迹。
agents/lab_people_agent.md           梳理关键实验室、团队、作者、师承合作网络和代表贡献。
agents/method_taxonomy_agent.md      按问题定义和解决方法组织技术路线、评价指标和实验范式。
agents/paper_deep_read_agent.md      对单篇论文做背景、贡献、方法、实验、局限和延伸阅读分析。
agents/daily_paper_radar_agent.md    按今日/最近一天窗口搜罗新论文，排序推荐最值得关注的论文。
agents/synthesis_insight_agent.md    综合洞察研究重点、未解问题、争议、机会和未来方向。
agents/report_writer_agent.md        生成方向综述、今日论文推荐或单篇深读交付报告。
protocols/quality_protocol.md           团队共享质量协议。
protocols/delivery_protocol.md          最终交付协议。
protocols/skill_registry.md             内置 skills 与能力路由。
```

---

# 3.1 内置 Skills

本团队已带可直接使用的 skills：

```text
skills/huggingface-papers/             从 huggingface/skills 克隆后抽取。
skills/arxiv/                          从 NousResearch/hermes-agent 克隆后抽取。
skills/systematic-literature-review/   从 bytedance/deer-flow 克隆后抽取。
skills/academic-paper-review/          从 bytedance/deer-flow 克隆后抽取。
skills/deep-research/                  从 bytedance/deer-flow 克隆后抽取。
skills/arxiv-daily-radar/              本地封装，负责今日 arXiv 论文雷达流程。
skills/research-lineage-mapper/        本地封装，负责论文路径、实验室团队和人员脉络映射。
```

---

# 4. Boss Input 标准模板

## 4.1 方向综述

```markdown
# Boss Input

## 任务类型
方向综述

## 研究方向
示例：多模态大模型中的视觉 grounding。

## 领域边界
可选。示例：只看 2020 年以来 AI/ML 论文，偏模型和 benchmark，不看医学应用。

## 报告深度
简版 / 标准 / 深度。

## 特别关注
可选。示例：关键实验室、代表人物、未解决问题、未来方向。
```

## 4.2 今日论文推荐

```markdown
# Boss Input

## 任务类型
今日论文推荐

## 研究方向
示例：LLM agents、test-time scaling、robot foundation models。

## 时间窗口
最新一天 / 最近 24 小时 / 最近 3 天。

## 来源
arXiv / Hugging Face Papers / OpenReview / Papers with Code / 社区热点。

## 推荐数量
示例：Top 5 / Top 10。
```

## 4.3 单篇论文深读

```markdown
# Boss Input

## 任务类型
单篇论文深读

## 论文
arXiv URL / PDF URL / DOI / 标题 / 论文文本。

## 关注点
背景 / 方法 / 实验 / 复现 / 局限 / 相关论文 / 可延展问题。
```

---

# 5. 默认交付

```text
方向综述：
  发展轨迹、关键论文路径、实验室团队、代表人物、问题定义和方法脉络、未解问题、未来方向、推荐阅读路线。

今日论文推荐：
  今日最值得关注论文列表、核心要点、为什么重要、与已有工作的关系、是否值得深读、推荐优先级。

单篇论文深读：
  问题背景、核心贡献、方法论、实验结果、局限性、衍生问题、深入阅读论文列表。
```

---

# 6. 强制边界

团队不得：

```text
编造论文、作者、机构、引用量或实验结果
把摘要复述冒充深度理解
只按标题推荐论文
把社区热度当学术质量
忽略负结果、局限和适用边界
给出没有来源的实验室和人员关系
```

---

# 7. 报告理念

科研调研报告必须回答：

```text
这个方向试图解决什么问题
为什么这个问题重要
早期工作怎么定义问题
关键突破来自哪些论文和团队
方法路线如何演进
现在最强或最有代表性的解决方案是什么
还卡在哪里
未来可能往哪里走
今天有哪些新论文值得读
```
