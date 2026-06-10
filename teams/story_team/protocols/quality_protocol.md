---
name: quality_protocol
role: 高质量短篇小说共享质量协议
type: shared_protocol
version: 1.0
description: 所有 Agent 共同遵守的硬性协议，用于防止短篇创作中的 AI 腔、弱开头、人物空心、结构松散、结尾无余味、真实人物新闻历史误用、知名作品撞名和借梗。
applies_to:
  - team_lead_agent
  - concept_architect_agent
  - character_voice_agent
  - plot_scene_agent
  - writer_agent
  - critic_agent
  - reader_impact_agent
  - revision_agent
  - iteration_controller_agent
  - originality_guard_agent
  - final_editor_agent
---

# Quality Protocol / 高质量短篇小说共享质量协议

本协议高于任何局部 agent 习惯。任何产出若与本协议冲突，以本协议为准。

---

# 1. 核心目标

```text
1. 强开头：第一段必须提供异常、冲突、声音或不可忽视的细节。
2. 人物可信：人物必须有欲望、恐惧、代价和选择。
3. 结构紧：每个场景必须改变局势、关系或读者理解。
4. 语言有人味儿：避免 AI 腔、模板句、抽象形容词堆砌和故作深沉。
5. 结尾有余震：结尾必须留下情绪、意义或悖论的回声，而不是说明答案。
6. 批评返修闭环：锐评必须导致版本化真实修改，而不是形式化记录或 todo。
7. 原创性安全：禁止真实人物新闻历史误用、知名作品撞名、借梗和套壳。
```

---

# 2. 必须维护的事实源

```text
00_boss_brief.md
01_concept_options.md
02_story_bible.md
03_scene_outline.md
05_critic_review.md
06_revision_plan.md
07_originality_report.md
iteration_status.md
drafts/draft_v00.md
reviews/critic_v00.md
reviews/reader_impact_v00.md
revisions/revision_plan_v00_to_v01.md
revisions/change_log_v00_to_v01.md
revisions/revision_routing_v00_to_v01.md
reviews/revision_compliance_v01.md
delivery/final_story.md
```

---

# 3. 原创性硬规则

默认禁止：

```text
真实古今中外名人姓名
真实历史人物姓名
真实新闻人物姓名
真实案件、灾难、热点新闻的高识别度细节链
知名小说、影视、动漫、游戏、网文中的人名、地名、组织名、设定名
知名作品高识别度剧情结构
同人化、套壳化、致敬化的偷懒
```

如果题材需要现实感或历史感，必须：

```text
架空人物
架空地点
改写事件结构
替换身份组合
删除可识别细节链
保留主题，不保留原型
```

---

# 4. AI 腔与样本文学质感门禁

高风险表达：

```text
他意识到
这一刻，他终于明白
仿佛有什么东西
某种难以言说的
空气凝固了
命运的齿轮
不是……而是……
既熟悉又陌生
```

出现时不一定全删，但必须判断是否真实服务语境。若只是模板反应，必须替换。

必须使用 `skills/exemplar-prose-calibration/SKILL.md` 做进一步校准：

```text
AI 腔的本质是用抽象总结替代具体经验。
“不是……而是……”类机械对照句，短篇全文最好为 0，最多 1 处且必须有具体语义功能。
“他意识到 / 终于明白 / 某种难以言说 / 空气凝固 / 命运的齿轮”等模板句累计超过 2 处，必须专项返修。
段尾不得连续升华主题；优先停在物件、行为、未说完的话、状态变化或新问题上。
不得要求“写得像”Boss 样例，不得复制样例人物名、设定名、桥段链或专属世界观组合。
```

正文必须建立明确叙述声音，而不是中性说明腔：

```text
POV 有偏见、有误判、有注意力重点
人物声音能通过句长、词汇、回避方式和紧张反应区分
信息释放通过行动、对话、误判和代价完成
每个关键场景有可复述的具体记忆点
```

---

# 5. 批评返修门禁

```text
默认 critic 综合分 < 8.5：继续返修，除非 Boss 指定更低目标或达到迭代上限
开头抓力 < 8.5：重写开头
人物可信度 < 8.0：重写人物动机、对话或关键选择
结构与因果 < 8.0：重排或重写关键场景
语言品质 < 8.0：清理模板句、重复句式和抽象废话
情绪余震 < 8.0：重写结尾或补强前文回声
reader_impact_agent 有 P0 阅读流失点：继续返修
原创性审查未通过：不得交付终稿
```

# 6. 版本化迭代硬规则

正式任务必须遵循：

```text
每一版正文必须有 drafts/draft_vNN.md
每一版必须有 reviews/critic_vNN.md 和 reviews/reader_impact_vNN.md
每一轮返修必须有 revision_plan 和 change_log
每一轮返修前必须有 revision_routing，明确 P0/P1 的层级、责任 agent、必改事实源和验收标准
每一轮返修后、复评前必须有 revision_compliance，逐条验收 P0/P1 是否真实修改
新稿必须经过复评，不能用上一轮评分代表新稿
iteration_status.md 必须记录当前决策：continue / ready_for_originality_review / pass_to_final_editor / stop_at_limit / stop_at_limit_with_boss_approval
```

以下情况不得进入终稿：

```text
只有返修计划，没有新稿
只有新稿，没有 change_log
只有 change_log，没有 revision_routing
revision_compliance 为 fail
只有 critic 评价，没有 reader impact 测试
没有 iteration_status.md
iteration_status.md 未允许进入 final_editor_agent
```

---

# 7. 禁止交付

不得以下列内容冒充完成：

```text
只有大纲，没有正文
只有片段，没有完整故事
只有漂亮句子，没有人物选择
只有反转，没有铺垫
只有概念，没有场景
只有批评记录，没有返修稿
原创性风险未清除
```
