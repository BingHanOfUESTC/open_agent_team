---
name: skill-decomposition-framework
type: reference
description: >
  Decompose a desired output into reusable skill capabilities, skill boundaries, input/output contracts, and execution order. Use before authoring skills.
model-invocable: false
---

# Skill Decomposition Framework

技能拆解的目标不是为当前任务写更多提示词，而是找出“未来类似任务也会用到的能力”。

---

# 1. 拆解维度

从 Boss 期望输出中抽象：

```text
内容能力：需要理解、分析、生成或校验什么内容。
结构能力：输出需要什么组织方式、层级和顺序。
风格能力：语气、密度、读者对象和表达约束。
流程能力：需要先做什么、后做什么、如何迭代。
评价能力：什么算好，什么算失败，如何打分。
安全能力：哪些内容不能写入 skill，哪些风险必须审查。
```

---

# 2. 可泛化能力判断

一个能力适合写成 skill，当它满足：

```text
可在多个类似任务中复用
可描述为方法、步骤、检查表或失败模式
不依赖本次任务的专属实体或结论
不需要记住 Boss 的参考输出
能被执行结果验证
```

不适合写成 skill：

```text
只服务本次任务的答案片段
Boss 样例输出的固定结构复制
一次性格式偏好
不可复现的数据或隐含知识
```

---

# 3. 技能边界

每个 skill 必须定义：

```text
它解决什么问题
它不解决什么问题
它需要哪些输入
它产出什么中间件或结果
它何时被调用
它如何被评价
```

---

# 4. 拆分粒度

过粗的问题：

```text
一个 skill 包含分析、生成、评价、返修全部逻辑
难以定位失败原因
```

过细的问题：

```text
每个小格式都拆一个 skill
skill 只能服务当前任务
调用成本高但泛化收益低
```

推荐粒度：一个 skill 对应一类稳定能力。
