# File Manifest: LLM 研究调研报告 — 交付文件清单

> **项目**: project0623v1 — 大语言模型（LLM）关键论文系统梳理 (2017–2026)
> **生成日期**: 2026-06-23
> **交付版本**: v1.0

---

## 交付文件（delivery/）

| 文件 | 路径 | 行数 | 用途 |
|------|------|------|------|
| 执行摘要 | `delivery/executive_summary.md` | ~110 | 2000 字以内的核心结论，面向 5 分钟快速阅读 |
| 正式调研报告 | `delivery/research_survey_report.md` | ~400 | 六章完整报告：背景、历史、团队、方法、未来、参考文献 |
| 文件清单 | `delivery/file_manifest.md` | 本文 | 所有交付和中间文件的路径、行数、用途索引 |

---

## 中间研究文件（research/）

| 文件 | 路径 | 行数 | 用途 | 生成者 |
|------|------|------|------|--------|
| 检索计划 | `research/query_plan.md` | 607 | 定义 8 个子问题、关键词、检索式、纳入/排除标准 | query_planning_agent |
| 论文清单 | `research/paper_inventory.md` | 164 | 65+ 篇核心论文的标题、作者、机构、arXiv ID、摘要关键点 | paper_discovery_agent |
| 发展轨迹 | `research/lineage_map.md` | 985 | 分阶段时间线、主干演进图、影响力路径、Benchmark 演进 | lineage_mapping_agent |
| 实验室与人员 | `research/lab_people_map.md` | 579 | 10 家工业实验室 + 学术关键人物 + 人才流动路径 | lab_people_agent |
| 方法分类 | `research/method_taxonomy.md` | 658 | 7 个方法维度（架构/预训练/Scaling/对齐/推理/效率/知识）分类体系 | method_taxonomy_agent |
| 综合洞察 | `research/synthesis_insights.md` | 683 | 十大突破、范式转变、未解问题、争议分析、研究方向推荐 | synthesis_insight_agent |
| 来源日志 | `research/source_log.md` | 237 | 逐次检索记录、错误重试、未覆盖论文清单 | paper_discovery_agent |

---

## 质量自检

交付前已确认以下事项：

- [x] **论文真实性**：所有 60+ 篇论文均来自 arXiv API、Hugging Face Papers API 或官方技术报告，未编造任何论文、作者、机构或实验结果
- [x] **来源可追溯**：关键结论均可回溯到 paper_inventory.md 中的具体编号和 arXiv ID
- [x] **引文格式**：报告中使用 [论文编号] 或 (Author, Year) + arXiv 链接格式
- [x] **非摘要堆砌**：报告以"发展脉络"而非"论文列表"方式组织，体现演进逻辑
- [x] **局限性标注**：未解问题、争议和方法局限均在正文中标注
- [x] **推断标注**：不确定的人员关系、未来方向预测等已标注"推断"或"据公开报道"
- [x] **未编造引用**：所有引用链路（论文→paper_inventory→source_log）可被完整回溯
- [x] **不混淆事实与观点**：事实陈述均关联到具体论文；综合分析和趋势判断明确标注为推断
- [x] **方法脉络清晰**：方法分类按"问题定义→方法解决→方法演化"组织，非按标题罗列
- [x] **中文报告，英文标题**：报告正文为中文，论文标题保留英文原文

---

## 使用建议

| 阅读场景 | 推荐文件 | 预计时间 |
|---------|---------|---------|
| 快速了解全局 | `executive_summary.md` | 8 分钟 |
| 深入理解发展脉络 | `research_survey_report.md` 第二章 | 25 分钟 |
| 理解技术方法分类 | `research_survey_report.md` 第四章 + `method_taxonomy.md` | 30 分钟 |
| 识别研究机会 | `research_survey_report.md` 第五章 + `synthesis_insights.md` | 20 分钟 |
| 了解实验室和人才 | `research_survey_report.md` 第三章 + `lab_people_map.md` | 15 分钟 |
| 完整研读 | 全部 delivery + research 文件 | 3-4 小时 |
