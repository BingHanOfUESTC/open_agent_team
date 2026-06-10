---
name: output-evaluation-rubric
type: reference
description: >
  Build and apply evaluation rubrics for generated outputs against Boss expectations without treating reference outputs as text to copy.
model-invocable: false
---

# Output Evaluation Rubric

评价的目标是判断结果是否达到 Boss 期望，而不是鼓励模型复制参考输出。

---

# 1. 评价维度

默认维度：

```text
任务完成度
期望输出匹配度
结构完整度
事实或逻辑可靠性
可读性
风格适配
可复用技能贡献度
污染风险控制
```

Boss 给出特定评价标准时，优先使用 Boss 标准，同时保留污染风险控制。

---

# 2. P0 / P1 / P2

```text
P0：不改不能通过，例如任务没完成、结构错误、污染风险高、核心事实错。
P1：明显影响质量，例如表达不稳、结构缺口、部分标准未满足。
P2：可优化项，例如局部措辞、细节丰富度、次要格式。
```

---

# 3. 失败归因

每个失败项必须归因：

```text
skill 缺口：当前 skills 没有提供必要方法。
skill 污染：skills 过拟合参考输出或任务专属信息。
执行偏差：skills 足够，但执行时没有遵守。
输入不足：Boss 信息不足，无法可靠完成。
评价冲突：Boss 标准之间存在冲突。
```

---

# 4. 评分要求

```text
必须给分项分
必须给综合分
必须解释扣分原因
必须给下一轮动作建议
不得只说“接近预期”
不得因文本相似而忽略泛化性
```
