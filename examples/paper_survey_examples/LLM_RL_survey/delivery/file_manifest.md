# 项目文件清单

> **项目**: LLM 强化学习后训练调研
> **生成日期**: 2026-06-23
> **版本**: 1.0
> **总论文数**: 280 篇

---

## 一、交付文件 (delivery/)

本目录包含最终交付的调研报告，面向技术决策者。

| 文件 | 大小 | 用途 | 目标读者 |
|------|------|------|------|
| `executive_summary.md` | ~10 KB | 2-3 页执行摘要：核心发现、关键趋势、Boss 行动建议 | 决策者，3 分钟阅读 |
| `research_survey_report.md` | ~40 KB | 完整调研报告：8 章系统覆盖方法演进、体系、团队、评估、挑战和未来方向 | 技术人员，深入阅读 |
| `file_manifest.md` | 本文件 | 项目所有文件的索引和说明 | 所有人 |

---

## 二、研究过程文件 (research/)

本目录包含调研过程中生成的所有中间文件，支撑报告的每一个结论。

### 2.1 核心文件

| 文件 | 行数 | 用途 | 生成 Agent |
|------|:---:|------|------|
| `query_plan.md` | 411 | 检索计划：7 个子问题拆解、关键词、检索式、纳入标准 | query_planning_agent |
| `paper_inventory.md` | 664 | 280 篇论文清单：标题、作者、年份、arXiv ID、核心贡献 | paper_discovery_agent |
| `lineage_map.md` | 437 | 演进脉络：五段时间线、问题-方法矩阵、关键转折点、论文影响路径 | lineage_mapping_agent |
| `lab_people_map.md` | 556 | 实验室团队：8 个工业实验室 + 8 个学术团队 + 开源社区、人才流动 | lab_people_agent |
| `method_taxonomy.md` | 803 | 方法分类：5 大训练范式、DPO 变体对比矩阵、GRPO 机制、评估方法论 | method_taxonomy_agent |
| `synthesis_insights.md` | 437 | 综合洞察：5 大热点、8 个未解决问题、4 个争议点、未来预判 | synthesis_insight_agent |
| `source_log.md` | — | 检索执行日志和来源记录 | paper_discovery_agent |
| `deep_read_notes.md` | — | 单篇论文深读笔记 | paper_deep_read_agent |
| `daily_paper_radar.md` | — | 今日论文推荐 | daily_paper_radar_agent |

### 2.2 文件之间的引用关系

```
query_plan.md (检索计划)
    │
    ▼
paper_inventory.md (280 篇论文清单) ← source_log.md
    │
    ├──→ lineage_map.md (演进脉络)
    ├──→ lab_people_map.md (实验室团队)
    ├──→ method_taxonomy.md (方法分类)
    ├──→ deep_read_notes.md (精读笔记)
    └──→ daily_paper_radar.md (今日推荐)
            │
            ▼
    synthesis_insights.md (综合洞察)
            │
            ▼
    delivery/executive_summary.md + delivery/research_survey_report.md
```

---

## 三、协议与配置 (`.opencode/`)

| 文件 | 用途 |
|------|------|
| `AGENTS.md` | 项目 Agent 团队入口和路由 |
| `protocols/delivery_protocol.md` | 交付报告的结构规范和验收标准 |
| `protocols/quality_protocol.md` | 共享质量协议：防幻觉、防编造、防摘要堆砌 |
| `protocols/skill_registry.md` | 技能注册表：可用的 skills 和能力路由 |
| `agents/*.md` | 各 Agent 的角色提示和任务分配 |
| `skills/*/SKILL.md` | 各 Skill 的工作流方法和资源 |

---

## 四、论文覆盖统计

### 4.1 按子方向分布

| 子方向 | 论文数 | 时间跨度 |
|------|:---:|------|
| Q1: SFT 基础 | 23 | 2023-2026 |
| Q2: Reward Modeling | 76 | 2023-2026 |
| Q3: PPO-RLHF | 42 | 2022-2026 |
| Q4: DPO 变体 | 80 | 2023-2026 |
| Q5: GRPO & Group-wise | 31 | 2025-2026 |
| Q6: Agentic RL | 64 | 2023-2026 |
| Q7: 评估 Benchmark | (含于以上) | 2023-2026 |
| **总计（去重）** | **280** | **2017-2026** |

### 4.2 按年份分布

| 年份 | 论文数 | 主要方向 |
|:---:|:---:|------|
| 2017-2020 | 3-5 | PPO 奠基、RLHF 概念 |
| 2021-2022 | ~10 | RLHF 范式确立 |
| 2023 | ~50 | DPO 革命、开源 RLHF、评估标准化 |
| 2024 | ~100 | DPO 变体爆发、Agent PO、PRM 兴起 |
| 2025 | ~80 | GRPO 革命、Agentic RL 爆发、理论深化 |
| 2026 (至 6 月) | ~35 | 理论统一、应用扩展、评估反思 |

### 4.3 论文地位分布

| 地位 | 数量 | 说明 |
|:--:|:---:|------|
| ★ 开创性 | 10-15 | 定义新范式（PPO, InstructGPT, DPO, Constitutional AI, DeepSeek-R1 等） |
| ▲ 代表性 | 30-40 | 体现标准方法（ORPO, SimPO, KTO, Online DPO, UltraFeedback 等） |
| ● 最新 | 80-100 | 2025-2026 前沿，影响力待验证 |
| ○ 边缘 | 140-160 | 领域应用或微小改进 |

---

## 五、数据质量声明

### 5.1 来源
- 280 篇论文通过 HuggingFace Papers API 检索（索引自 arXiv）
- 未覆盖 Anthropic/OpenAI 的非 arXiv 技术报告
- 未覆盖中文预印本平台
- Semantic Scholar API 无法访问，引用关系基于推断

### 5.2 置信度
- [确定]：多篇论文交叉验证，有定量数据支持
- [推断]：基于论文趋势、引用模式的合理推断
- [争议]：学术界存在明显分歧

### 5.3 局限
1. 2025-2026 论文多数未经过同行评审
2. 作者机构信息依赖 HuggingFace API 元数据，可能不完整
3. DeepSeek 等中国团队个人贡献者信息未公开
4. 人才流动信息基于公开新闻，可能存在滞后

### 5.4 禁止行为确认
本报告严格遵循 quality_protocol.md 的规定：
- ✅ 不编造论文、作者、机构、年份、链接、实验结果
- ✅ 不把标题相似当作相关工作
- ✅ 不把 arXiv 新论文当作已验证结论
- ✅ 不把模型自称贡献直接当成事实
- ✅ 包含局限性和反证
- ✅ 区分开源/闭源、已验证/未验证、确定/推断
- ✅ 所有关键结论可回溯到 paper_inventory.md

---

## 六、快速导航

| 你想了解 | 看这个文件 |
|----------|----------|
| 3 分钟抓重点 | `delivery/executive_summary.md` |
| 完整技术报告 | `delivery/research_survey_report.md` |
| 280 篇论文全量清单 | `research/paper_inventory.md` |
| 方法对比和公式 | `research/method_taxonomy.md` |
| 技术演进史 | `research/lineage_map.md` |
| 谁在做什么 | `research/lab_people_map.md` |
| Boss 阅读建议 | `research/synthesis_insights.md` 第 5 章 |
| 未来机会和空白 | `research/synthesis_insights.md` 第 4 章 |
| 未解决问题排序 | `research/synthesis_insights.md` 第 2 章 |

---

*文件清单生成时间: 2026-06-23 | 项目: LLM 强化学习后训练调研*
