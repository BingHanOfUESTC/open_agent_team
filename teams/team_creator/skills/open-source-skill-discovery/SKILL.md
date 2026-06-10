---
name: open-source-skill-discovery
type: reference
description: >
  Discover open-source skills and related reusable prompt/tool assets, recording source, license, relevance, maintenance, and integration risks.
model-invocable: false
---

# Open Source Skill Discovery

开源 skills 检索的目标是寻找可复用能力，不是随便复制代码或 prompt。

---

# 1. 检索来源

优先：

```text
带 SKILL.md 的开源技能仓库
可信 agent / prompt / tool 项目
有明确许可证的 GitHub 仓库
官方或高质量社区维护的 reusable workflows
```

谨慎：

```text
无许可证仓库
个人 gist
没有维护记录的项目
需要密钥或外部服务的工具
```

---

# 2. 候选记录字段

```text
名称
URL
作者或组织
许可证
最近更新情况
是否包含代码
是否需要网络/API/密钥
能力摘要
与新团队的相关性
初步安全风险
建议处理方式
```

---

# 3. 筛选原则

```text
相关性不足，拒绝。
许可证不明，拒绝或仅参考。
含危险命令，拒绝。
含可复用方法但格式不适配，改写后集成。
只提供领域知识但无技能结构，可作为参考，不直接复制。
```
