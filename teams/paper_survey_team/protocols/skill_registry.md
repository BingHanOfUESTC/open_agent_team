---
name: skill_registry
role: 科研调研团队技能注册表
type: shared_registry
version: 1.0
description: 记录 paper_survey_team 可直接使用的内置 skills、能力路由、来源和缺口处理方式。
applies_to:
  - team_lead_agent
  - query_planning_agent
  - paper_discovery_agent
  - lineage_mapping_agent
  - lab_people_agent
  - method_taxonomy_agent
  - paper_deep_read_agent
  - daily_paper_radar_agent
  - synthesis_insight_agent
  - report_writer_agent
---

# Skill Registry / 技能注册表

---

# 1. 本团队已内置 Skills

本团队的可直接使用 skills 放在：

```text
teams/paper_survey_team/skills/
```

当前已内置：

```text
skills/huggingface-papers/
  来源：git clone https://github.com/huggingface/skills.git 后抽取。
  用途：Hugging Face Papers 与 arXiv 论文解析、元数据和 markdown 内容获取。

skills/arxiv/
  来源：git clone https://github.com/NousResearch/hermes-agent.git 后抽取 skills/research/arxiv。
  用途：通过 arXiv API 搜索论文、按作者/分类/ID 检索、生成基础元数据。

skills/systematic-literature-review/
  来源：git clone https://github.com/bytedance/deer-flow.git 后抽取。
  用途：系统性文献综述、论文检索、结构化元数据抽取和主题综合。

skills/academic-paper-review/
  来源：同上。
  用途：单篇论文审阅、贡献、方法、实验和局限分析。

skills/deep-research/
  来源：同上。
  用途：跨来源深度调研和综合报告。

skills/arxiv-daily-radar/
  来源：本地封装。
  用途：今日/最近 24 小时 arXiv 论文推荐流程。

skills/research-lineage-mapper/
  来源：本地封装。
  用途：关键论文路径、实验室团队、人员和方法脉络映射。
```

---

# 2. 能力路由

```text
方向综述和系统性文献调研：
  使用 skills/systematic-literature-review/SKILL.md 和 skills/deep-research/SKILL.md。

arXiv / Hugging Face Papers 单篇解析：
  使用 skills/arxiv/SKILL.md 和 skills/huggingface-papers/SKILL.md。

单篇论文深读：
  使用 skills/academic-paper-review/SKILL.md。

今日论文推荐：
  使用 skills/arxiv-daily-radar/SKILL.md、skills/arxiv/SKILL.md 和 skills/huggingface-papers/SKILL.md。

论文路径、实验室、团队、人员和方法脉络：
  使用 skills/research-lineage-mapper/SKILL.md。
```

---

# 3. 缺口处理

如果需要新增特定领域数据库、会议、代码复现、专利、临床试验或实验数据 skill：

```text
优先寻找可 git clone 且带 SKILL.md 的可靠来源
抽取到 teams/paper_survey_team/skills/
记录来源和用途
不得只在文档里推荐安装
不得把无法复现来源伪装成已安装 skill
```
