---
name: generalizable-skill-authoring
type: reference
description: >
  Author reusable SKILL.md files that encode methods rather than task-specific answers. Use when creating or revising generated skills.
model-invocable: false
---

# Generalizable Skill Authoring

好的 skill 是可复用能力，不是本次任务的答案缓存。

---

# 1. SKILL.md 基本结构

```text
YAML front matter
能力目标
适用场景
输入要求
输出要求
方法步骤
质量检查
失败模式
禁止内容
```

---

# 2. 写作原则

```text
写方法，不写答案。
写判断标准，不写参考输出。
写抽象流程，不写本次任务实体。
写失败模式，不写对某个样例的补丁。
写可迁移的检查表，不写一次性格式。
```

---

# 3. 示例使用规则

允许：

```text
抽象示例
占位符示例
跨领域小例子
反例模式
```

禁止：

```text
Boss 参考输出原句
Boss 样例答案改写
本次任务专属名称
本次任务专属结论
为了贴近样例而固定字段顺序
```

---

# 4. 泛化性自检

写完 skill 后检查：

```text
换一个同类任务，这个 skill 还成立吗？
删除 Boss 参考输出后，这个 skill 还能被理解吗？
是否出现本次任务独有实体？
是否把评价答案写成了生成规则？
失败时能定位是 skill 问题还是执行问题吗？
```
