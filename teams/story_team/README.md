# Story Team / 高质量短篇小说创作团队

`story_team` 是一套面向 Boss 私人使用的短篇小说 multi-agent team。

目标很明确：

> Boss 给出题材、偏好、禁区和篇幅，团队负责构思、人物、结构、正文、锐评、返修、原创性审查和终稿交付，最终交付一篇完整、抓人、有人味儿、读完有余震的短篇小说。

这套团队不是“生成一篇看起来像小说的文字”。它的定位是：

```text
让短篇从第一段就有阅读抓力
让人物不是设定容器，而是有欲望、有软肋、有选择代价的人
让情节不是事件流水账，而是因果推进、转折有效、结尾有回声
让语言避开 AI 腔、模板腔、故作文学腔
用版本化锐评、读者冲击测试、真实改稿和复评逼近高质量成稿
严格禁止乱用真实名人、新闻事件、历史人物和知名作品剧情/人名
```

---

# 1. 默认定位

```text
目标：完整短篇小说
默认规模：3000-8000 字
扩展规模：8000-15000 字
默认交付：delivery/final_story.md
可选交付：delivery/creative_process_report.md
Boss 职责：给出题材、偏好、禁区，最终阅读和取舍
团队职责：完成创作、批评、返修、原创性审查和最终交付
```

短篇团队优先追求：

```text
强开头
少人物
单一核心矛盾
高密度场景
强情绪线
克制设定解释
结尾回声
读后难忘
```

---

# 2. 最终组织架构

```text
Boss
│
└── @team_lead_agent
    ├── @concept_architect_agent
    ├── @character_voice_agent
    ├── @plot_scene_agent
    ├── @writer_agent
    ├── @critic_agent
    ├── @reader_impact_agent
    ├── @revision_router_agent
    ├── @revision_agent
    ├── @revision_compliance_agent
    ├── @iteration_controller_agent
    ├── @originality_guard_agent
    └── @final_editor_agent
```

---

# 3. 每个 Agent 的职责

```text
agents/team_lead_agent.md             总控。接收 Boss 输入，调度全流程，执行返修门禁，整理最终交付。
agents/concept_architect_agent.md    提炼题材、核心矛盾、叙事承诺、独特性和读者钩子。
agents/character_voice_agent.md      设计人物欲望、伤口、秘密、关系张力、语气和视角。
agents/plot_scene_agent.md           设计短篇结构、关键场景、因果推进、反转和结尾回声。
agents/writer_agent.md               生产正文初稿，执行高密度短篇写作，不用模板腔。
agents/critic_agent.md               豆瓣式锐利批评，打分、指出失败处、强制返修。
agents/reader_impact_agent.md        模拟真实读者阅读留存、跳读点、记忆点和结尾余震。
agents/revision_router_agent.md      将返修意见按 L0-L5 分层派单，确保世界观/人物/结构问题回到正确上游。
agents/revision_agent.md             根据批评意见重写、压缩、增补和局部结构返修。
agents/revision_compliance_agent.md  复评前逐条验收返修是否真实执行，阻断表面润色。
agents/iteration_controller_agent.md 维护版本化审稿状态机，决定继续返修、放行终稿或到达上限。
agents/originality_guard_agent.md    检查真实人物/新闻/历史真名误用、知名作品撞名、借梗和高识别度剧情。
agents/final_editor_agent.md         终稿编辑，统一语言、节奏、格式，交付完整故事。
protocols/quality_protocol.md           团队共享质量协议。
protocols/delivery_protocol.md          最终交付协议。
protocols/skill_registry.md             内置 skills 与能力路由。
```

---

# 3.1 内置 Skills

本团队已带可直接使用的 skills：

```text
skills/story-architecture/        从 haowjy/creative-writing-skills 克隆后抽取。
skills/scene-construction/        从 haowjy/creative-writing-skills 克隆后抽取。
skills/prose-writing/             从 haowjy/creative-writing-skills 克隆后抽取。
skills/prose-critique/            从 haowjy/creative-writing-skills 克隆后抽取。
skills/writing-principles/        从 haowjy/creative-writing-skills 克隆后抽取。
skills/originality-safety-guard/  本地封装，用于原创性、撞名、借梗和真实人物新闻历史避让。
skills/narrative-hook-engine/     本地新增，用于第一段、第一页和前三页阅读抓力。
skills/character-pressure-lab/    本地新增，用于人物欲望、关系筹码、选择代价和可信度。
skills/scene-tension-engine/      本地新增，用于场景压力、权力变化、因果推进和删改判断。
skills/reader-impact-test/        本地新增，用于阅读留存、跳读点、记忆点和结尾余震测试。
skills/revision-workflow/         本地新增，用于版本化返修、change_log、复评门禁和迭代状态机。
skills/style-voice-calibration/   本地新增，用于叙述距离、角色声音区分和去 AI 平滑。
skills/exemplar-prose-calibration/ 本地新增，用于从 Boss 小说样例提炼中文类型小说质感、叙述声音、反 AI 腔和样例污染边界。
skills/revision-routing/          本地新增，用于返修问题分层、责任 agent 派单和事实源更新要求。
skills/revision-compliance-gate/  本地新增，用于复评前检查返修遵从度，防止“已优化”式无效返修。
```

以后新增写作能力时，优先把可用 skill 放入 `teams/story_team/skills/`，不要只在文档里推荐安装。

---

# 4. Boss Input 标准模板

最小可用模板：

```markdown
# Boss Input

## 题材
一句话即可。

## 期望气质
示例：悬疑 / 都市 / 科幻 / 奇幻 / 现实主义 / 温柔但刺痛 / 黑色幽默 / 冷峻。

## 篇幅
可选。默认 3000-8000 字。

## 偏好
可选。

## 禁区
可选。
```

推荐模板：

```markdown
# Boss Input

## 题材
一个县城殡葬店老板收到一单来自未来的预约。

## 期望气质
悬疑、克制、带一点荒诞现实感，结尾要有余震。

## 篇幅
6000 字左右。

## 偏好
不要大段解释，人物要像真实生活里的人。

## 禁区
不要真实新闻原型，不要直接使用历史人物，不要套用知名小说剧情。
```

---

# 5. 创作迭代机制

默认流程：

```text
1. Producer 锁定任务边界和禁区
2. Concept Architect 提供 2-3 个高潜力方向
3. Producer 选择最强方向
4. Character Voice 建立人物与声音
5. Plot Scene 设计结构和关键场景
6. Originality Guard 先审查设定与命名
7. Writer 生产 drafts/draft_v00.md
8. Critic 输出 reviews/critic_v00.md
9. Reader Impact 输出 reviews/reader_impact_v00.md
10. Iteration Controller 更新 iteration_status.md
11. 未达标时 Revision Router 输出 revision_routing，先把 L2-L5 问题派回对应上游事实源
12. Revision 基于 routing table 输出 revision_plan、change_log 和 drafts/draft_v01.md
13. Revision Compliance 逐条验收 P0/P1 是否真实修改
14. compliance 通过或部分通过后，Critic + Reader Impact 对新版本复评
15. 循环 10-14，直到达到目标分或 Boss 指定迭代上限
16. Originality Guard 终审最新通过稿
17. Iteration Controller 在原创性通过后放行终稿
18. Final Editor 在 pass_to_final_editor 或 stop_at_limit_with_boss_approval 状态下交付
```

返修门槛：

```text
默认目标综合分 < 8.5：继续返修，除非 Boss 指定更低目标或达到迭代上限
开头抓力 < 8.5：必须重写开头或前三页
人物可信度 < 8.0：必须重写人物动机、关系筹码与关键对话
结构与因果 < 8.0：必须重写或合并关键场景
语言品质 < 8.0：必须清理模板腔、解释腔和单调句式
读者冲击测试有 P0 流失点：必须继续返修
原创性风险未过：不得交付
```

版本化产物：

```text
drafts/draft_v00.md
reviews/critic_v00.md
reviews/reader_impact_v00.md
revisions/revision_plan_v00_to_v01.md
revisions/change_log_v00_to_v01.md
drafts/draft_v01.md
iteration_status.md
```

禁止把“已列出返修 todo”当作完成。每一轮返修必须有完整新稿、change_log 和复评。

---

# 6. 强制禁区

团队不得：

```text
直接使用古今中外真实名人姓名作为角色
直接复刻真实新闻事件
直接使用真实历史人物、真实朝代核心事件和著名史事结构
借用知名小说、影视、游戏、动漫、网文的人名、地名、组织名、设定名
复刻知名作品高识别度剧情结构
使用“致敬”“化用”“同人感”来掩盖借用
用名言、典故、热梗、真实事件堆砌文学感
```

如果 Boss 明确要求历史或新闻感，也必须：

```text
架空人物
架空地点
改写事件结构
去除可识别原型
保留主题，不保留真实细节链
```

---

# 7. 推荐理念

短篇小说不是缩短的长篇。它应当像一枚钉子：

```text
开头钉住读者
中段拧紧矛盾
结尾留下刺
```

最终报告和正文必须做到：

```text
故事完整
人物可感
场景有质感
语言不油
转折不廉价
结尾不解释过度
读完还有余味
```
