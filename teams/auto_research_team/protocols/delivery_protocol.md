---
name: delivery_protocol
role: 自动科研团队最终交付协议
type: shared_protocol
version: 1.0
description: 规定自动科研任务的交付目录、必备文件、LaTeX 报告结构、复现说明和验收标准。
applies_to:
  - team_lead_agent
  - latex_report_agent
  - artifact_delivery_agent
---

# Delivery Protocol / 自动科研团队最终交付协议

---

# 1. 最终交付目标

默认最终交付是一套完整研究包，不是一份孤立报告。

必须交付：

```text
research_workspace/00_boss_brief.md
research_workspace/01_research_scope.md
research_workspace/02_literature_inventory.md
research_workspace/literature/search_plan.md
research_workspace/literature/paper_inventory.tsv
research_workspace/literature/citation_coverage.md
research_workspace/literature/claim_ledger.md
research_workspace/literature/gap_map.md
research_workspace/literature/cards/
research_workspace/03_deep_read_notes.md
research_workspace/04_gap_and_ideas.md
research_workspace/05_research_plan.md
research_workspace/06_code_data_manifest.md
research_workspace/07_environment_log.md
research_workspace/08_implementation_notes.md
research_workspace/09_experiment_log.md
research_workspace/10_result_analysis.md
research_workspace/reports/paper/main.tex
research_workspace/delivery/artifact_manifest.md
research_workspace/delivery/reproduction_guide.md
```

若成功编译 LaTeX，还应交付：

```text
research_workspace/reports/final_research_report.pdf
```

---

# 2. LaTeX 论文结构

`reports/paper/main.tex` 应采用接近 arXiv 主流论文的排版，优先使用简洁 article 或 conference-like 模板。

必须包含：

```text
\begin{abstract}
\section{Introduction}
\section{Related Work}
\section{Method}
\section{Experiments}
\section{Conclusion}
\bibliography 或 thebibliography
```

图表要求：

```text
图放入 reports/paper/figures/
表放入 reports/paper/tables/ 或直接由 LaTeX 表格生成
绘图脚本放入 scripts/ 或 reports/paper/scripts/
图表 caption 必须说明数据来源
```

---

# 3. 交付清单

`delivery/artifact_manifest.md` 必须列出：

```text
研究 idea
研究计划
代码路径
数据路径或下载说明
环境路径或创建命令
实验配置
实验日志
结果表格
图表脚本
LaTeX 源码
PDF 路径
复现指南
已知限制
许可证说明
```

---

# 4. 验收标准

交付包必须满足：

```text
Boss 能看懂研究问题、idea、计划、实现、实验和结论。
Boss 能按 reproduction guide 找到代码入口和实验入口。
论文报告中的核心结论能回溯到实验或文献证据。
论文报告的引用覆盖满足 depth targets，或明确记录已批准/合理的降级原因。
没有把失败实验隐藏起来。
没有把未完整验证的结论包装成强结论。
代码、数据、模型和第三方仓库来源清楚。
```
