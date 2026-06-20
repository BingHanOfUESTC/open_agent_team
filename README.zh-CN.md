<p align="center">
  <img src="docs/images/project_logo.png" alt="Open Agent Team logo" width="720">
</p>


<h1 align="center">Open Agent Team</h1>

<p align="center">
  为 OpenCode 准备的一键安装 multi-agent 团队库。选一个团队，安装到项目里，然后从 <code>@team_lead_agent</code> 开始协作。
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="#快速开始">快速开始</a> | <a href="#ppt-writer-演示案例">PPT Demo</a> | <a href="#内置团队">内置团队</a> | <a href="#你会得到什么">你会得到什么</a>
</p>

---

Open Agent Team 是一个可复用的 multi-agent team 仓库。每个 team 都包含角色提示词、共享质量协议、交付标准和可选 skills，用来完成一个完整工作流。

项目目标很直接：让复杂 multi-agent 协作变成一次安装、直接使用。

```text
选择团队 -> 安装到项目 -> 打开 OpenCode -> 让 @team_lead_agent 开始工作
```

## 为什么值得下载

- **一条命令安装**：把完整 agent team 安装进任意 OpenCode 项目。
- **交付件完整**：不是零散聊天记录，而是按团队标准生成可交付文件。
- **流程可靠**：质量协议覆盖来源追踪、审查返修、交付验收和最终整理。
- **团队可复用**：可以使用内置团队，也可以注册自己的本地团队。
- **OpenCode 原生结构**：自动写入 `.opencode/agents`、`protocols`、`skills`、`AGENTS.md` 和 `opencode.json`。

## 快速开始

在本仓库根目录执行：

```bash
python -m pip install -e .
agent_team list
```

把一个团队安装到你的项目：

```bash
agent_team install --name ppt_writer_team --path /path/to/your/project
```

用 OpenCode 打开该项目，然后输入：

```text
@team_lead_agent 请根据 ./materials 里的资料生成一份 15 页投资人演示 PPT。
```

安装后会生成：

```text
/path/to/your/project/.opencode/
  AGENTS.md
  opencode.json
  agents/
  protocols/
  skills/
```

## 你会得到什么

### 可编辑 PPT，而不是图片版幻灯片

`ppt_writer_team` 可以把文档、表格、PDF、PPT 模板、笔记和公开资料整理成完整 PowerPoint 交付包：

- `delivery/final_deck.pptx`：可编辑 `.pptx`，不是静态图片。
- `delivery/speaker_notes.md`：演讲备注和讲稿。
- `delivery/source_trace.md`：关键事实和数据的来源追踪。
- `deck_spec/deck_spec.json`：结构化页面方案，方便审查和重新生成。

如果你提供现成 PPT 模板，团队可以提取版式、字体、色彩和视觉风格，但不会复用无关内容。

#### PPT Writer 演示案例

<p align="center">
  <a href="https://github.com/user-attachments/assets/e2bdfb2f-3d30-41da-bff0-ea122c7426d6">
    <img src="docs/images/ppt_writer_team_cover.png"
         alt="Watch ppt_writer_team demo"
         width="400">
  </a>
</p>


<p align="center">
  <strong>▶ 点击图片观看 ppt_writer_team 演示视频</strong>
</p>

仓库中也内置了两套完整输入/输出示例，位于 [examples/ppt_writer_examples](examples/ppt_writer_examples/)：

| 示例 | 输入 prompt | 可编辑 PPT | 讲稿备注 | 来源追踪 | 执行摘要 |
| --- | --- | --- | --- | --- | --- |
| 英文梵高艺术史 PPT | [prompt_input1.txt](examples/ppt_writer_examples/prompt_input1.txt) | [final_deck.pptx](examples/ppt_writer_examples/delivery1/final_deck.pptx) | [speaker_notes.md](examples/ppt_writer_examples/delivery1/speaker_notes.md) | [source_trace.md](examples/ppt_writer_examples/delivery1/source_trace.md) | [executive_summary.md](examples/ppt_writer_examples/delivery1/executive_summary.md) |
| 中文梵高艺术史 PPT | [prompt_input2.txt](examples/ppt_writer_examples/prompt_input2.txt) | [final_deck.pptx](examples/ppt_writer_examples/delivery2/final_deck.pptx) | [speaker_notes.md](examples/ppt_writer_examples/delivery2/speaker_notes.md) | [source_trace.md](examples/ppt_writer_examples/delivery2/source_trace.md) | [executive_summary.md](examples/ppt_writer_examples/delivery2/executive_summary.md) |

这两个案例展示了 `ppt_writer_team` 的目标交付形态：可编辑 PPT、可直接讲解的讲稿、执行摘要，以及便于审查可信度的来源追踪文件。

### 方便筛选阅读的论文调研

`paper_survey_team` 面向方向综述、每日论文雷达和单篇论文深读：

- 输出可排序、可筛选的论文列表，并说明每篇为什么重要；
- 整理作者、机构、年份、链接、主题、推荐优先级；
- 梳理方法脉络、benchmark 演进、关键实验室、代表人物和未解决问题；
- 单篇论文深读覆盖背景、贡献、方法、实验、局限和延伸阅读。

它的目标不是堆摘要，而是帮你快速判断“哪些论文值得先读”。

### 工程团队能产出可执行结果

工程相关团队会生成可落地的文件：

- 按严重程度排序的 code review findings；
- test plan、unit tests、integration tests、edge cases；
- bug triage report、复现计划、根因假设、修复选项和验证计划；
- 架构图谱、ADR 风格设计说明、API/data model 方案和实施路线图。

## 内置团队

| Team | 适合做什么 | 典型交付件 |
| --- | --- | --- |
| `auto_research_team` | 从研究主题自动推进到可复现代码、实验和论文式报告 | 研究计划、代码/数据清单、实验日志、结果分析、LaTeX 报告 |
| `ppt_writer_team` | 从素材、模板和公开资料生成可编辑 PPT | `.pptx`、讲稿、来源追踪、deck spec |
| `paper_survey_team` | 文献综述、论文雷达、单篇论文深读 | 论文列表、调研报告、脉络图、阅读路线 |
| `paper_writing_team` | 论文写作、related work、返修、rebuttal | 论文段落、文献综合、审稿意见、rebuttal 策略 |
| `grant_proposal_team` | 基金/项目申请书 | proposal、specific aims、预算说明、合规清单 |
| `story_team` | 高质量短篇小说创作与返修 | 终稿、锐评、返修记录 |
| `course_creator_team` | 课程和教学包设计 | syllabus、lesson plans、作业、题库、教师讲稿 |
| `business_plan_team` | 商业计划书和 pitch narrative | business plan、pitch narrative、财务假设、风险表 |
| `job_application_team` | 简历、求职信、outreach、面试准备 | 定制简历、cover letter、LinkedIn outreach、interview prep |
| `code_review_team` | 以问题为先的代码审查 | review findings、风险摘要、测试缺口、修复建议 |
| `test_generation_team` | 根据代码、bug 或需求设计测试 | test plan、unit tests、integration tests、edge cases |
| `bug_triage_team` | 日志、报错、issue 根因分析 | triage report、复现计划、根因假设、验证计划 |
| `codebase_onboarding_team` | 快速理解陌生代码仓库 | onboarding guide、architecture map、key files、quickstart |
| `software_architect_team` | 从需求到架构设计 | 需求拆解、架构方案、API/data model、roadmap |
| `iphone_app_team` | iPhone App 产品、设计和工程交接 | 产品范围、信息架构、设计系统、iOS 架构、QA handoff |
| `skill_creator_team` | 根据用户问题、期望输出和工作流样例创建可复用 skill | generated skill、验证用例、gotchas、维护报告 |
| `skills_evolving_team` | skill 设计、评估和迭代 | reusable skills、评估 rubric、迭代报告 |
| `team_creator` | 创建新的可安装 agent team | 新 team 目录、agents、protocols、skills、验证报告 |

查看团队列表：

```bash
agent_team list
agent_team list --verbose
agent_team list --json
```

## 安装选项

安装到当前目录：

```bash
agent_team install --name code_review_team
```

只预览，不写文件：

```bash
agent_team install --name code_review_team --path /path/to/project --dry-run
```

清理已生成的 OpenCode team 文件后重新安装：

```bash
agent_team install --name code_review_team --path /path/to/project --clean
```

`--clean` 会删除生成的 `.opencode/agents`、`.opencode/protocols` 和 `.opencode/skills`，但保留 `.opencode` 里的其他文件。

## 工作方式

大多数团队结构如下：

```text
teams/<team_name>/
  README.md
  agents/
    team_lead_agent.md
    *_agent.md
  protocols/
    quality_protocol.md
    delivery_protocol.md
    skill_registry.md
  skills/
    <skill_name>/
      SKILL.md
```

安装时会复制到：

```text
agents/*.md      -> .opencode/agents/
protocols/*.md   -> .opencode/protocols/
skills/*         -> .opencode/skills/
```

安装器还会写入 `.opencode/AGENTS.md` 并合并 `.opencode/opencode.json`，让 OpenCode 自动加载团队规则。

## 添加自己的团队

创建团队目录：

```text
my_team/
  README.md
  agents/team_lead_agent.md
  protocols/quality_protocol.md
  protocols/delivery_protocol.md
  protocols/skill_registry.md
  skills/
```

注册并安装：

```bash
agent_team add --name my_team --path /path/to/my_team
agent_team install --name my_team --path /path/to/project
```

之后可以更新或删除：

```bash
agent_team update --name my_team --path /new/path/to/my_team
agent_team remove --name my_team
```

## 可靠性交付原则

- 每个 team 默认由 `team_lead_agent` 负责调度。
- `protocols` 定义强制质量规则和交付规则。
- `skills` 提供具体任务方法和脚本能力。
- 交付件有明确文件名和结构，方便审查、返修、重新生成和移交。
- 资料密集型团队强调来源追踪和 evidence cards，避免无依据结论。

## 许可证与第三方声明

本项目使用 MIT License，见 [LICENSE](LICENSE)。

部分内置 skills 改编自第三方开源仓库，仍受其原始许可证约束。来源和许可证见 [NOTICE](NOTICE) 与 [THIRD_PARTY_LICENSES](THIRD_PARTY_LICENSES/)。
