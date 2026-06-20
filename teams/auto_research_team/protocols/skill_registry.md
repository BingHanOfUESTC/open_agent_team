---
name: skill_registry
role: 自动科研团队能力路由协议
type: shared_protocol
version: 1.0
description: 记录自动科研任务中应优先使用的内置、系统和外部能力，以及缺失能力时的降级方式。
applies_to:
  - team_lead_agent
  - literature_discovery_agent
  - repo_data_agent
  - environment_agent
  - experiment_runner_agent
  - latex_report_agent
---

# Skill Registry / 自动科研团队能力路由协议

---

# 1. 内置 Skills

```text
skills/autoresearch-orchestration/
  用于 team_lead_agent 的全流程调度。采用“内层实验优化 + 外层证据综合”的双循环，避免只线性跑一次。

skills/literature-evidence-mapping/
  用于 literature_discovery_agent、paper_deep_read_agent、gap_idea_agent。建立 evidence cards、citation ledger 和 gap map。

skills/research-ideation-screening/
  用于 gap_idea_agent、research_plan_agent。把候选 idea 按新颖性、可实现性、可证伪性、资源成本和失败风险排序。

skills/reproducible-code-data-setup/
  用于 repo_data_agent、environment_agent、implementation_agent。处理代码/数据/环境准备、许可证、安全检查和 smoke test。

skills/experiment-iteration-loop/
  用于 experiment_runner_agent、result_analysis_agent。管理 baseline、main、ablation、robustness、失败诊断和迭代决策。

skills/latex-paper-artifact/
  用于 latex_report_agent、artifact_delivery_agent。生成 LaTeX 论文、BibTeX、图表脚本、复现声明和最终 artifact manifest。
```

---

# 2. 开源参考来源

本 team 的 skills 借鉴以下公开项目的工作流思想，但本目录中的 skill 文本为本项目原生整理，不直接复制外部实现：

```text
Orchestra-Research/AI-Research-SKILLs
  借鉴点：autoresearch 中央编排、ideation、ML paper writing、academic plotting、citation verification、完整 idea-to-paper 生命周期。

SamuelSchmidgall/AgentLaboratory
  借鉴点：Literature Review -> Experimentation -> Report Writing 三阶段，以及 arXiv、Hugging Face、Python、LaTeX 工具链组合。

SakanaAI/AI-Scientist
  借鉴点：自动 idea、实验、论文生成的端到端框架，以及对 LLM 生成代码执行风险的安全提醒。

aiming-lab/AutoResearchClaw
  借鉴点：idea-to-paper、自进化、多 agent 协作、citation verification 和人机协作审查。

dzhng/deep-research
  借鉴点：递归检索、breadth/depth 参数、从 learnings 生成下一轮 research directions。

K-Dense-AI/scientific-agent-skills
  借鉴点：面向具体科学任务的可组合 skills 和数据库/工具路由。
```

---

# 3. 能力路由

```text
论文检索：优先使用 arXiv、Semantic Scholar、OpenReview、ACL Anthology、Papers With Code、Google Scholar 可访问页面和官方项目页。
代码检索：优先使用论文官方仓库、作者主页、Papers With Code 链接和组织级 GitHub。
数据检索：优先使用数据集官方页、Hugging Face Datasets、Kaggle、OpenML、官方 benchmark 页面。
环境搭建：优先复用仓库 requirements、environment.yml、pyproject.toml、Dockerfile 或 Boss 指定环境。
实验运行：优先使用项目原生命令；若缺失，补写最小可复现实验脚本。
绘图制表：优先使用 Python 脚本从原始结果生成 figures/tables。
LaTeX 报告：优先生成可本地编译的 main.tex、references.bib 和 figures。
```

---

# 4. 缺失能力降级

```text
无法联网：使用 Boss 提供材料和本地缓存，标注检索缺口。
无法下载数据：使用公开小样本、mock-free smoke test 或说明阻塞原因。
无 GPU：优先 CPU smoke test、小模型、小数据、短 epoch 或只复现评测脚本。
无 LaTeX 编译器：交付 main.tex、bib、figures 和编译命令，明确未生成 PDF。
仓库无运行说明：先做静态审查，再建立最小环境和 smoke test。
许可证不清：不得使用为正式实现依赖，只能列为参考线索。
```

---

# 5. 记录要求

每次使用外部资源都必须记录：

```text
名称
URL 或本地路径
版本、commit、tag 或下载日期
许可证
用途
风险或限制
```
