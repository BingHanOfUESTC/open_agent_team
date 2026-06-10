---
name: delivery_protocol
role: Skill 创建交付协议
type: protocol
version: 1.0
description: 规定 skill_creator_team 的交付结构、必备文件和验收标准。
---

# Delivery Protocol / Skill 创建交付协议

## 1. 必备交付文件

```text
00_boss_brief.md
01_skill_requirements.md
02_skill_architecture.md
generated_skills/<skill_name>/SKILL.md
validation/validation_cases.md
validation/validation_report.md
maintenance/gotchas_and_risks.md
delivery/skill_creation_report.md
```

## 2. 可选交付文件

```text
generated_skills/<skill_name>/references/*.md
generated_skills/<skill_name>/scripts/*
generated_skills/<skill_name>/assets/*
generated_skills/<skill_name>/agents/openai.yaml
delivery/install_notes.md
```

## 3. skill_creation_report.md 必须包含

```text
skill 名称
触发场景
适用范围与不适用范围
文件结构
设计理由
验证结果摘要
主要 gotchas
后续维护建议
```

## 4. 交付验收

```text
SKILL.md 有 name 和 description frontmatter
description 包含明确触发条件
SKILL.md body 不超过必要长度，长细节已拆分
references/scripts/assets 只在有真实需要时出现
validation_cases.md 包含正例和负例
validation_report.md 写明 pass / conditional_pass / fail
gotchas_and_risks.md 记录至少 3 个易错点或维护风险
```
