---
name: quality_protocol
role: Skill 创建共享质量协议
type: protocol
version: 1.0
description: 所有 Agent 共同遵守的硬性协议，用于保证生成的 skill 可触发、可复用、低上下文成本、可验证、可维护。
---

# Quality Protocol / Skill 创建共享质量协议

## 1. 质量目标

生成的 skill 必须满足：

```text
触发清晰：description 能让模型准确判断何时使用
内容精简：SKILL.md 只保留必要流程和导航
结构完整：frontmatter、body、可选 references/scripts/assets 合理组织
边界明确：说明适用任务、不适用任务、输入输出和禁区
可验证：至少包含正例、负例、结构检查和质量评分
可维护：gotchas 能随失败案例追加，不破坏其他 skills
无污染：不记忆用户样例答案、不泄漏私有数据、不硬编码一次性结论
```

## 2. 必须实践的设计原则

```text
description 写给模型路由，不写成人类宣传语
gotchas 是高价值内容，必须从失败模式或易错点提炼
progressive disclosure 优先：metadata -> SKILL.md -> references/scripts/assets
脚本用于脆弱、重复、可确定验证的步骤
不要 railroading：保留合理自由度，除非任务脆弱或高风险
验证先于自信交付：没有 validation_report，不得说 skill 已可用
```

## 3. 禁止行为

```text
把用户期望输出原文塞进 skill
把具体客户名、项目名、答案、结论写成通用规则
把所有背景资料放进 SKILL.md
创建 README、INSTALLATION、CHANGELOG 等非必要文件放进 skill 包
description 只写“用于某某任务”而没有触发场景
没有负例就判断路由准确
没有 gotchas 或 failure modes 就交付复杂 skill
```

## 4. 通过门槛

交付前必须同时通过：

```text
Skill structure check: pass
Routing description check: pass
Progressive disclosure check: pass
Contamination check: pass
Validation cases: 至少 2 个正例 + 1 个负例
Maintenance review: pass 或 conditional_pass
```
