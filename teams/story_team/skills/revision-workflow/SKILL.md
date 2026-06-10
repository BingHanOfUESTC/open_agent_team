---
name: revision-workflow
type: workflow
description: >
  Versioned fiction revision workflow. Use when coordinating critique-revision loops, applying review findings, proving that changes were actually made, and deciding whether a draft has passed or needs another revision.
model-invocable: false
---

# Revision Workflow

返修不是写 todo。返修是产生一个更强的新稿，并用复评证明它解决了旧稿的问题。

---

# 1. 固定循环

```text
draft_vNN
critic_vNN
reader_impact_vNN
revision_plan_vNN_to_vNN+1
change_log_vNN_to_vNN+1
draft_vNN+1
critic_vNN+1
reader_impact_vNN+1
iteration_status update
```

循环直到通过或达到上限。

---

# 2. 返修计划必须可验证

每条返修计划必须包含：

```text
对应 review finding
影响位置
采取动作：删除 / 合并 / 重写 / 移动 / 新增 / 压缩
预期改善的评分维度
验证方式
```

---

# 3. change_log 必须证明真实修改

change_log 不写“已优化”。必须写：

```text
旧稿问题
新稿改法
涉及段落或场景
为什么这个改法比旧稿更有压力、更可信或更有余味
残留风险
```

---

# 4. 禁止伪返修

```text
只同义改写句子，但结构问题仍在
只新增解释，试图说服读者相信人物
只把 critic 的话复制进计划，没有输出完整新稿
只润色语言，不处理 P0 动机、结构、开头问题
新稿没有复评就进入终稿
```

---

# 5. 复评重点

复评不是重新夸一遍。必须检查：

```text
上一轮 P0 是否消失
新稿是否产生新的 P0
分数是否真实上升
开头、人物、结构、语言、余震是否达到门槛
reader impact 的流失点是否减少
```
