---
name: iteration-workflow
type: workflow
description: >
  Versioned workflow for evolving skills, executing tasks, evaluating outputs, and deciding whether to continue or stop.
model-invocable: false
---

# Iteration Workflow

技能自进化必须有版本链。没有版本链，就无法判断改进来自 skill、执行还是偶然输出。

---

# 1. 固定循环

```text
requirement_analysis
skill_architecture_vNN
generated_skills_vNN
contamination_audit_vNN
execution_result_vNN
evaluation_vNN
iteration_status
```

未通过时，根据失败归因选择：

```text
改 skill architecture
改 generated skills
重新执行
请求 Boss 澄清
达到上限停止
```

---

# 2. 版本规则

```text
generated_skills/v00/
generated_skills/v01/
outputs/result_v00.md
outputs/result_v01.md
evaluations/evaluation_v00.md
evaluations/evaluation_v01.md
contamination/skill_audit_v00.md
contamination/skill_audit_v01.md
```

不得覆盖旧版本。

---

# 3. 决策规则

继续改 skill：

```text
skill 缺口导致 P0
skill 污染导致不通过
多轮执行都失败在同一能力点
```

继续执行：

```text
skill 足够，但 execution_agent 没遵守
结果局部偏差，不需要改 skill
```

请求 Boss 澄清：

```text
评价标准冲突
关键输入缺失
期望输出不可判定
```

---

# 4. 禁止伪迭代

```text
只改评价措辞，不改 skill 或结果
只改结果，不记录执行偏差
只改 skill，不重新执行和评价
把达到上限说成通过
```
