---
name: skill_registry
role: 技能自进化团队技能注册表
type: shared_registry
version: 1.0
description: 记录 skills_evolving_team 可使用的内置 skills 和能力路由。
applies_to:
  - team_lead_agent
  - requirement_analysis_agent
  - skill_architect_agent
  - skill_author_agent
  - contamination_guard_agent
  - execution_agent
  - evaluator_agent
  - iteration_controller_agent
  - report_writer_agent
---

# Skill Registry / 技能注册表

---

# 1. 内置 Skills

```text
skills/skill-decomposition-framework/
  用途：将 Boss 目标输出拆解为可泛化能力、技能边界和调用链。

skills/generalizable-skill-authoring/
  用途：编写可复用、不污染、不记忆样例答案的 SKILL.md。

skills/output-evaluation-rubric/
  用途：构建评分表、差距分析、失败归因和通过/返修判断。

skills/contamination-guard/
  用途：检查 skill 是否被 Boss 参考输出、样例答案或任务专属内容污染。

skills/iteration-workflow/
  用途：维护版本化技能迭代、执行结果迭代和状态机。
```

---

# 2. 能力路由

```text
需求分析：
  使用 skills/skill-decomposition-framework/SKILL.md 和 skills/contamination-guard/SKILL.md。

技能架构：
  使用 skills/skill-decomposition-framework/SKILL.md 和 skills/generalizable-skill-authoring/SKILL.md。

技能编写：
  使用 skills/generalizable-skill-authoring/SKILL.md 和 skills/contamination-guard/SKILL.md。

污染审查：
  使用 skills/contamination-guard/SKILL.md。

输出评价：
  使用 skills/output-evaluation-rubric/SKILL.md。

迭代控制：
  使用 skills/iteration-workflow/SKILL.md。
```
