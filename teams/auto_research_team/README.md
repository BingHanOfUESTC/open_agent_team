# Auto Research Team / 自动科研闭环团队

`auto_research_team` 是一套面向开放式研究任务的 multi-agent team。

目标：

> Boss 只给出研究内容和研究目标后，团队自动完成前沿调研、问题定位、idea 生成、研究计划、代码与数据准备、环境搭建、实验验证、迭代分析和 LaTeX 论文式报告交付。

入口保持与其他团队一致：

```text
@team_lead_agent
```

---

# 1. 默认定位

```text
输入：研究主题、研究目标、可选硬件/环境/时间预算/目标 venue。
输出：完整研究包，包括 idea、研究计划、代码实现、实验记录、结果分析、LaTeX 报告和交付清单。
默认工作区：research_workspace/
默认报告：reports/paper/main.tex + 编译产物。
默认原则：可追溯、可复现、尊重许可证、实验结果不造假。
```

---

# 2. 组织架构

```text
Boss
│
└── @team_lead_agent
    ├── @research_scoping_agent
    ├── @literature_discovery_agent
    ├── @paper_deep_read_agent
    ├── @gap_idea_agent
    ├── @research_plan_agent
    ├── @repo_data_agent
    ├── @environment_agent
    ├── @implementation_agent
    ├── @experiment_runner_agent
    ├── @result_analysis_agent
    ├── @latex_report_agent
    └── @artifact_delivery_agent
```

---

# 3. 每个 Agent 的职责

```text
agents/team_lead_agent.md             总控。接收 Boss brief，调度全流程，维护研究状态和最终交付。
agents/research_scoping_agent.md      明确研究问题、评价目标、约束、硬件环境和验收标准。
agents/literature_discovery_agent.md  检索前沿论文、代码、数据集、benchmark 和 leaderboards。
agents/paper_deep_read_agent.md       深读关键论文，抽取方法、假设、实验设置、结果和局限。
agents/gap_idea_agent.md              基于证据提出可验证改进点、创新假设和风险。
agents/research_plan_agent.md         制定研究计划、实验矩阵、里程碑、资源预算和停止条件。
agents/repo_data_agent.md             下载/整理合规代码与数据，记录来源、许可证、版本和校验信息。
agents/environment_agent.md           搭建或复用 Boss 指定环境，记录依赖、硬件、命令和复现步骤。
agents/implementation_agent.md        实现算法或模型改动，保持代码可读、可测试、可回滚。
agents/experiment_runner_agent.md     运行训练/验证/消融实验，记录配置、日志、随机种子和失败原因。
agents/result_analysis_agent.md       分析结果、统计显著性、误差案例、资源消耗和迭代建议。
agents/latex_report_agent.md          写作 arXiv 风格 LaTeX 报告，生成图表并插入论文。
agents/artifact_delivery_agent.md     汇总 idea、计划、代码、实验、报告、复现说明和交付清单。
protocols/quality_protocol.md         事实、复现、安全、许可证和实验诚信协议。
protocols/delivery_protocol.md        最终交付结构、文件清单和验收标准。
protocols/skill_registry.md           可用能力和外部工具路由说明。
```

---

# 4. 内置 Skills

这些 skills 是为本 team 原生整理的轻量能力模块，借鉴开源 auto-research 项目的工作流设计，但不复制外部实现。

```text
skills/autoresearch-orchestration/       双循环自动科研编排：内层实验优化，外层证据综合和交付。
skills/literature-evidence-mapping/      文献检索、证据卡、引用核验和研究脉络映射。
skills/research-depth-control/           控制调研深度、文献覆盖、深读配额和论文引用密度。
skills/research-ideation-screening/      从文献 gap 生成候选 idea，并按可验证性和风险筛选。
skills/reproducible-code-data-setup/     代码、数据、环境、许可证和安全准备流程。
skills/experiment-iteration-loop/        baseline、main、ablation、robustness 和失败诊断实验循环。
skills/latex-paper-artifact/             arXiv 风格 LaTeX、BibTeX、图表脚本和复现声明交付。
```

参考来源包括：

```text
Orchestra-Research/AI-Research-SKILLs
SamuelSchmidgall/AgentLaboratory
SakanaAI/AI-Scientist
aiming-lab/AutoResearchClaw
dzhng/deep-research
K-Dense-AI/scientific-agent-skills
```

---

# 5. Boss Input 模板

```markdown
# Boss Input

## 研究内容
例如：提升小样本医学图像分割、多智能体强化学习信用分配、长上下文 RAG 评测等。

## 研究目标
例如：提出可验证算法改进，在公开 benchmark 上验证，并产出 arXiv 风格论文报告。

## 约束
可选。时间预算、GPU/CPU/内存、目标框架、目标数据集、禁止来源、许可证要求。

## 指定环境
可选。conda/env/docker/已有 repo/已有数据路径/集群命令。

## 目标交付
可选。论文、代码、实验表格、复现实验脚本、PPT、技术报告。
```

---

# 6. 默认工作流

```text
1. 建立 research_workspace/00_boss_brief.md
2. 明确研究范围、约束、硬件和验收标准
3. 按 breadth/depth/gap/recency 四轮检索前沿论文、代码、数据集和 benchmark
4. 深读关键工作并建立 evidence cards、claim ledger 和 citation coverage map
5. 推理待改进点，提出 2-4 个候选 idea
6. 选择主 idea，写研究计划和实验矩阵
7. 下载合规代码和数据，搭建环境
8. 实现算法或模型改动
9. 运行 smoke test、baseline、main、ablation 和 robustness 实验
10. 分析结果并根据证据迭代
11. 生成图表和 LaTeX arXiv 风格报告
12. 交付完整研究包和复现说明
```

---

# 7. 强制边界

```text
不得编造论文、结果、日志、数据集、引用或训练成功。
不得绕过数据集、代码或模型许可证。
不得下载或运行来源不明的高风险脚本。
不得把未验证 idea 写成已证明贡献。
不得只交付论文文本而没有代码、实验记录和复现说明。
不得在硬件不足时假装完成训练；必须降级为小规模验证或明确阻塞。
```

---

# 8. 默认交付

```text
research_workspace/
  00_boss_brief.md
  01_research_scope.md
  02_literature_inventory.md
  literature/search_plan.md
  literature/paper_inventory.tsv
  literature/citation_coverage.md
  literature/claim_ledger.md
  literature/gap_map.md
  literature/cards/
  03_deep_read_notes.md
  04_gap_and_ideas.md
  05_research_plan.md
  06_code_data_manifest.md
  07_environment_log.md
  08_implementation_notes.md
  09_experiment_log.md
  10_result_analysis.md
  reports/paper/main.tex
  reports/paper/figures/
  reports/paper/tables/
  reports/final_research_report.pdf
  delivery/artifact_manifest.md
  delivery/reproduction_guide.md
```
