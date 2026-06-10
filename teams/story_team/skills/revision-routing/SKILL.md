---
name: revision-routing
type: reference
description: >
  Route fiction revision feedback to the correct upstream or downstream agent
  instead of sending every problem to the editor. Use after critic and reader
  reports, before revision planning.
model-invocable: false
---

# Revision Routing / 返修分层派单

返修意见不得默认返给 editor。Editor 只负责表达层、局部节奏和语言润色；凡涉及故事事实、人物动机、结构、世界观、伏笔和规则的修改，必须先回到对应事实源和上游 agent。

---

# 1. 问题层级

```text
L0 文面问题
错字、病句、重复句式、AI 腔、段落节奏、对话自然度。
责任 agent：editor/final_editor/revision_agent。

L1 场景执行问题
某场没冲突、没有筹码变化、信息释放太直白、场景结尾没钩子。
责任 agent：plot_scene_agent + writer_agent + revision_agent。

L2 人物动机问题
行为不可信、选择代价不够、人物声音错位、关系张力不足。
责任 agent：character_voice_agent + writer_agent + revision_agent。

L3 故事结构问题
主线推进弱、反转无铺垫、场景顺序错、伏笔没回收、高潮不成立。
责任 agent：concept_architect_agent/plot_scene_agent + writer_agent。

L4 世界观/规则问题
规则自相矛盾、设定无法支撑冲突、关键限制缺失、事实源不一致。
责任 agent：concept_architect_agent/plot_scene_agent/originality_guard_agent，必要时更新 story bible 和 scene outline。

L5 项目方向问题
题材承诺错、核心卖点不吸引人、整体气质偏离 Boss brief。
责任 agent：team_lead_agent + concept_architect_agent，可能回到概念阶段。
```

---

# 2. 路由表格式

每轮返修前必须输出：

```markdown
# Revision Routing Table: draft_vNN

| issue_id | 来源 | 层级 | 影响范围 | 责任 agent | 必改事实源 | 下游重写文件 | 验收标准 |
|---|---|---|---|---|---|---|---|
```

字段要求：

```text
issue_id：沿用 critic/reader 的 P0/P1 编号。
来源：critic_vNN / reader_impact_vNN。
层级：L0-L5。
影响范围：段落、场景、全篇结构、人物关系、世界观规则等。
责任 agent：不能只写 revision_agent，必须写真正的上游责任方。
必改事实源：02_story_bible.md、03_scene_outline.md 等；纯文面问题可写“无”。
下游重写文件：drafts/draft_vNN+1.md 或具体章节。
验收标准：必须是可验证文本结果，不是“更好看”。
```

---

# 3. 强制原则

```text
Editor 只能改“如何表达”，不能改“故事事实”。
涉及人物为什么行动，必须回到 character_voice_agent。
涉及事件是否发生、顺序和因果，必须回到 plot_scene_agent。
涉及世界规则、空间规则、伏笔事实，必须更新 story bible/scene outline。
涉及核心承诺错误，必须由 team_lead_agent 拉回 concept_architect_agent。
```

没有 routing table 的返修，不得进入 revision_agent。
