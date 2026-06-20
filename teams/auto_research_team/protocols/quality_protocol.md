---
name: quality_protocol
role: 自动科研团队共享质量协议
type: shared_protocol
version: 1.0
description: 规定自动科研闭环中的事实、引用、代码、数据、环境、实验、许可证、安全和报告质量要求。
applies_to:
  - team_lead_agent
  - research_scoping_agent
  - literature_discovery_agent
  - paper_deep_read_agent
  - gap_idea_agent
  - research_plan_agent
  - repo_data_agent
  - environment_agent
  - implementation_agent
  - experiment_runner_agent
  - result_analysis_agent
  - latex_report_agent
  - artifact_delivery_agent
---

# Quality Protocol / 自动科研团队共享质量协议

本协议高于任何局部 agent 习惯。任何产出若与本协议冲突，以本协议为准。

---

# 1. 核心原则

```text
事实可追溯：论文、代码、数据、指标、结果都必须有来源或本地路径。
实验可复现：记录环境、硬件、依赖、命令、配置、随机种子和输出位置。
结果不造假：训练失败、指标不提升、硬件不足必须如实记录。
许可证合规：代码、模型、数据和图表必须记录许可证与使用限制。
安全优先：不得运行来源不明、破坏性、窃取凭据或越权访问的脚本。
假设分离：把事实、作者主张、团队推断和实验结论明确区分。
成本透明：记录 GPU/CPU/内存/时间消耗和可行的降级方案。
```

---

# 2. 禁止行为

```text
不得编造论文、引用、DOI、arXiv ID、作者、代码仓库或数据集。
不得编造实验日志、指标、图表、训练轮数或错误分析。
不得把 arXiv 新论文当成已被社区验证的结论。
不得绕过数据集条款、模型权重许可或代码许可证。
不得把下载的第三方代码混入实现而不记录来源。
不得在没有 smoke test 的情况下宣称环境搭建成功。
不得在没有 baseline 的情况下宣称改进有效，除非 Boss 明确只要原型验证。
不得在文献覆盖不足时直接进入论文写作，除非写明范围降级和检索缺口。
不得用只读摘要的论文支撑方法细节、实验结果对比或强局限结论。
```

---

# 3. 证据分级

```text
A：本地复现实验日志、脚本、配置和原始输出。
B：论文正文、官方代码仓库、官方数据集文档、benchmark 官方页面。
C：作者博客、issue、release notes、公开演讲或第三方复现。
D：社区讨论、排行榜截图、未核验转载。
```

核心结论优先使用 A/B 级证据。C/D 级证据只能作为背景或线索，必须标注置信度。

文献深度底线：

```text
默认筛选 30-60 篇候选论文。
默认纳入 15-30 篇相关论文。
默认深读 8-12 篇关键论文。
默认 Related Work 至少引用 12 篇论文。
主动研究方向默认包含近 24 个月最新工作，除非该领域更新很慢。
达不到数量时必须记录 niche-field exception、搜索来源、查询词和缺口。
```

---

# 4. 实验质量底线

正式实验至少记录：

```text
任务和数据划分
baseline 配置
main idea 配置
评价指标
随机种子
硬件信息
依赖版本
启动命令
日志路径
原始输出路径
失败原因
```

资源不足时允许降级为：

```text
小样本 smoke test
单 batch overfit test
短 epoch sanity check
公开结果再分析
算法复杂度或消融设计
```

但必须在报告中明确“未完成完整训练/验证”。

---

# 5. LaTeX 报告质量

报告必须包含：

```text
abstract
introduction
related work
method
experiment
conclusion
references
```

推荐包含：

```text
limitations
reproducibility statement
appendix
```

报告中每个主要图表必须能追溯到生成脚本、数据文件或实验日志。

报告引用要求：

```text
Introduction 至少覆盖问题背景、主流 baseline、研究 gap 和 benchmark。
Related Work 每段至少有一个 citation key，且不能只是论文列表。
Method 引用所有复用、改写或对比的算法组件。
Experiments 引用数据集、benchmark、metric、baseline 和公开结果来源。
每个 references.bib 条目必须出现在 paper_inventory.tsv 或 evidence card 中。
```
