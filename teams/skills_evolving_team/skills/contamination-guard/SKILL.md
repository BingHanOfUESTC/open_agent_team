---
name: contamination-guard
type: reference
description: >
  Detect and prevent contamination of skills by Boss-provided target outputs, reference answers, examples, task-specific entities, and overfit structures.
model-invocable: false
---

# Contamination Guard

Skill 污染指：把本次任务的参考输出、样例答案、专属实体、专属结论或过拟合结构写进 skill，导致 skill 失去泛化能力。

---

# 1. 高风险污染

```text
参考输出原文进入 skill
样例答案改写后进入 skill
本次任务专属实体进入 skill
本次任务专属结论进入 skill
skill 的模板字段和参考输出一一对应且无泛化理由
skill 名称绑定本次任务实体
```

高风险必须阻断。

---

# 2. 中风险过拟合

```text
示例过于接近 Boss 样例
检查表只适用于本次任务
输出格式过度模仿参考输出
把评价标准写成固定答案结构
```

中风险必须改写成抽象方法。

---

# 3. 低风险措辞

```text
局部词汇与 Boss 描述相近
泛化示例不够抽象
某些约束表达不够清楚
```

低风险可条件通过，但必须记录。

---

# 4. 隔离原则

```text
Boss 期望输出：可用于 evaluation，不可进入 skill。
Boss 参考答案：可用于差距比对，不可进入 skill。
Boss 格式偏好：可抽象为输出约束，但不能复制样例内容。
Boss 禁区：可以进入 skill 的禁止内容和安全边界。
```

---

# 5. 审查输出

```text
污染结论：通过 / 条件通过 / 不通过
高风险项
中风险项
低风险项
必须删除或改写项
允许保留项
是否允许执行
```
