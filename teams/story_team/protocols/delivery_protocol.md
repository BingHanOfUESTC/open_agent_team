---
name: delivery_protocol
role: 高质量短篇小说最终交付协议
type: shared_protocol
version: 1.0
description: 规定短篇小说团队的最终交付结构、必备文件、验收标准和禁止交付内容。
applies_to:
  - team_lead_agent
  - final_editor_agent
  - critic_agent
  - reader_impact_agent
  - iteration_controller_agent
  - originality_guard_agent
---

# Delivery Protocol / 高质量短篇小说最终交付协议

---

# 1. 最终交付目标

默认最终交付不是创意说明，而是一篇完整可读的短篇小说。

必须包含：

```text
delivery/final_story.md
delivery/executive_summary.md
delivery/creative_process_report.md
```

正式任务还应包含：

```text
00_boss_brief.md
01_concept_options.md
02_story_bible.md
03_scene_outline.md
04_draft_story.md
05_critic_review.md
06_revision_plan.md
07_originality_report.md
iteration_status.md
drafts/draft_v*.md
reviews/critic_v*.md
reviews/reader_impact_v*.md
revisions/revision_plan_v*_to_v*.md
revisions/change_log_v*_to_v*.md
```

---

# 2. final_story.md 要求

必须包含：

```text
标题
完整正文
无大纲残留
无批注残留
无模板占位符
无未解释的格式断裂
```

---

# 3. executive_summary.md 要求

必须简要说明：

```text
题材
篇幅
核心看点
最终审美判断
是否经过 critic 返修
最终迭代轮数和是否达到目标分
原创性审查结论
```

---

# 4. creative_process_report.md 要求

必须包含：

```text
选定概念
人物与结构选择
锐评摘要
读者冲击测试摘要
返修摘要
版本迭代记录
原创性审查摘要
残留风险
```

---

# 5. 验收标准

一篇短篇只有满足以下条件才可交付：

```text
故事完整
第一段有阅读抓力
主角有明确欲望和代价
关键场景有因果推进
结尾有余味
语言没有明显 AI 腔
critic 至少完成一轮评价
reader_impact_agent 至少完成一轮阅读留存测试
必要返修已执行
iteration_status.md 决策为 pass_to_final_editor，或 stop_at_limit_with_boss_approval
原创性审查通过或条件通过且风险已处理
```

---

# 6. 禁止交付

不得交付：

```text
未完成正文
只写开头或样章
带真实名人历史新闻误用风险的稿件
疑似套用知名作品剧情或人名的稿件
critic 明确不通过但未返修的稿件
没有版本化复评链路的稿件
iteration_status.md 未放行的稿件
```
