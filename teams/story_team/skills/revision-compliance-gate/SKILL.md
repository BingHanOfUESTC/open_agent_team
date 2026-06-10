---
name: revision-compliance-gate
type: reference
description: >
  Verify whether a revised fiction draft actually complied with critic and
  reader feedback. Use after revision output and before critic re-review.
model-invocable: false
---

# Revision Compliance Gate / 返修遵从度门禁

本门禁不评价“文笔是否变好”，只判断：返修是否真实执行了上一轮 P0/P1。

---

# 1. 输入

```text
reviews/critic_vNN.md
reviews/reader_impact_vNN.md
revisions/revision_routing_vNN_to_vNN+1.md
revisions/revision_plan_vNN_to_vNN+1.md
revisions/change_log_vNN_to_vNN+1.md
drafts/draft_vNN.md
drafts/draft_vNN+1.md
```

---

# 2. 验收表格式

```markdown
# Revision Compliance Report: draft_vNN+1

## Verdict
pass / partial / fail

| issue_id | 层级 | 上轮问题 | 要求改动 | 声称改动 | 文本证据 | 是否解决 | 备注 |
|---|---|---|---|---|---|---|---|
```

---

# 3. 判定规则

```text
fail：任一 P0 未定位回应，或声称重写但文本只做表面润色。
partial：P0 已处理但 P1 大量未处理，或产生新的明显结构/人物问题。
pass：所有 P0 有真实文本改动，核心 P1 有对应处理，change_log 可追踪。
```

以下情况直接 fail：

```text
没有 routing table。
没有 change_log。
change_log 只写“已优化/已润色/已增强”。
需要更新事实源但未更新 story bible/scene outline。
需要重写段落但只改了形容词和句子顺序。
复评前没有生成完整新稿。
```

---

# 4. 输出后动作

```text
pass：允许 critic_agent 和 reader_impact_agent 复评。
partial：允许复评但必须标记残留问题，iteration_controller 默认 continue。
fail：不得进入复评，退回对应责任 agent 重新返修。
```
