---
name: skill_registry
role: 高质量短篇小说团队技能注册表
type: shared_registry
version: 1.0
description: 记录 story_team 可直接使用的内置 skills、能力路由、来源和缺口处理方式。
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

# Skill Registry / 技能注册表

---

# 1. 本团队已内置 Skills

本团队的可直接使用 skills 放在：

```text
teams/story_team/skills/
```

当前已内置：

```text
skills/story-architecture/
  来源：git clone https://github.com/haowjy/creative-writing-skills.git 后抽取 skills/story-architecture。
  用途：故事结构、因果、节奏、铺垫与回收。

skills/scene-construction/
  来源：同上。
  用途：场景进入、对话、节奏、转场。

skills/prose-writing/
  来源：同上。
  用途：叙述距离、自由间接引语、句子节奏、感官落地、人物内心。

skills/prose-critique/
  来源：同上。
  用途：结构、人物、声音、语言、连续性等维度的批评方法。

skills/writing-principles/
  来源：同上。
  用途：通用写作原则和反 AI 腔提醒。

skills/originality-safety-guard/
  来源：本地封装。
  用途：真实人物、新闻、历史、知名作品撞名和借梗审查。

skills/narrative-hook-engine/
  来源：本地新增。
  用途：第一段、第一页、前三页阅读钩子和开篇返修。

skills/character-pressure-lab/
  来源：本地新增。
  用途：人物 Want/Need/Lie/Cost、关系筹码、选择代价和人物可信度返修。

skills/scene-tension-engine/
  来源：本地新增。
  用途：场景欲望、阻力、权力变化、因果推进和场景删改判断。

skills/reader-impact-test/
  来源：本地新增。
  用途：模拟真实读者阅读留存、跳读点、记忆点和结尾余震测试。

skills/revision-workflow/
  来源：本地新增。
  用途：版本化审稿、返修计划、change_log、复评门禁和迭代状态机。

skills/style-voice-calibration/
  来源：本地新增。
  用途：叙述距离、句式节奏、角色声音区分和去 AI 平滑。

skills/exemplar-prose-calibration/
  来源：从 Boss 提供的 /Users/ai_bing/projects/multi_agents/novel_examples 样例中提炼的泛化写作校准规则。
  用途：中文类型小说质感、叙述声音、章节钩子、反 AI 腔、机械句式清理和样例污染边界。

skills/revision-routing/
  来源：本地新增。
  用途：将 critic/reader 的返修意见按 L0-L5 分层派给正确 agent，避免所有问题默认返给 editor。

skills/revision-compliance-gate/
  来源：本地新增。
  用途：复评前逐条验收返修是否真实执行，防止只做表面润色或用“已优化”糊弄。
```

---

# 2. 能力路由

```text
故事结构和场景设计：
  使用 skills/story-architecture/SKILL.md、skills/scene-construction/SKILL.md、skills/scene-tension-engine/SKILL.md。

开头抓力和前三页阅读动力：
  使用 skills/narrative-hook-engine/SKILL.md、skills/reader-impact-test/SKILL.md。

人物压力、关系筹码和声音：
  使用 skills/character-pressure-lab/SKILL.md、skills/style-voice-calibration/SKILL.md。

正文写作和语言打磨：
  使用 skills/prose-writing/SKILL.md、skills/writing-principles/SKILL.md、skills/style-voice-calibration/SKILL.md、skills/exemplar-prose-calibration/SKILL.md。

锐利批评和返修诊断：
  使用 skills/prose-critique/SKILL.md、skills/reader-impact-test/SKILL.md、skills/revision-workflow/SKILL.md、skills/exemplar-prose-calibration/SKILL.md。

版本化迭代控制：
  使用 skills/revision-workflow/SKILL.md，由 iteration_controller_agent 维护 iteration_status.md。

返修派单和遵从度验收：
  使用 skills/revision-routing/SKILL.md、skills/revision-compliance-gate/SKILL.md。

原创性、撞名、真实人物新闻历史避让：
  使用 skills/originality-safety-guard/SKILL.md。
```

---

# 3. 缺口处理

如果需要新增风格、类型、地域、职业、历史、技术或文化准确性 skill：

```text
优先寻找可 git clone 且带 SKILL.md 的可靠来源
抽取到 teams/story_team/skills/
记录来源和用途
不得只在文档里推荐安装
不得把无法复现来源伪装成已安装 skill
```
