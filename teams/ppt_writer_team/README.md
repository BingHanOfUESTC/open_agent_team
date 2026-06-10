# PPT Writer Team / 可编辑 PPT 写作与生成团队

`ppt_writer_team` 是一套面向可编辑 PowerPoint 交付的 multi-agent team。

它接收 Boss 给定的多格式素材和可选 PPT 模板，完成素材理解、信息架构、叙事设计、页面文案、视觉风格迁移、PPT 编码生成、质量审查和返修。如果 Boss 没有提供素材，团队会先形成搜索计划并收集公开资料，再完成 PPT 写作和生成。

---

# 1. 默认定位

```text
目标：生成可编辑 .pptx，而不是静态图片或 PDF
默认规模：10-25 页
输入素材：doc/docx、xls/xlsx/csv、pdf、ppt/pptx、txt、markdown、网页资料等
模板输入：可选。若提供现成 PPT，只提取风格样式，不复用具体内容
默认交付：delivery/final_deck.pptx
辅助交付：deck_spec/deck_spec.json、delivery/speaker_notes.md、delivery/source_trace.md
```

---

# 2. 组织架构

```text
Boss
│
└── @team_lead_agent
    ├── @material_ingestion_agent
    ├── @research_agent
    ├── @image_asset_agent
    ├── @template_decoder_agent
    ├── @deck_architect_agent
    ├── @slide_writer_agent
    ├── @visual_designer_agent
    ├── @ppt_encoder_agent
    ├── @deck_reviewer_agent
    └── @revision_agent
```

---

# 3. Agent 职责

```text
agents/team_lead_agent.md          总控。判断输入缺口，调度素材理解、搜索、设计、写作、生成与返修。
agents/material_ingestion_agent.md 解析 Boss 提供的多格式素材，产出可追溯素材摘要和证据表。
agents/research_agent.md           当素材不足或为空时，制定搜索计划并整理公开资料。
agents/image_asset_agent.md        收集、下载、裁剪和 resize PPT 图片资产，输出可引用图片 manifest。
agents/template_decoder_agent.md   解析 Boss 给定 PPT 模板，只提取版式、字体、色彩、母版和视觉风格。
agents/deck_architect_agent.md     设计受众、目标、故事线、章节结构和页面清单。
agents/slide_writer_agent.md       写每页标题、正文、图表意图、讲稿备注和来源引用。
agents/visual_designer_agent.md    设计或迁移视觉系统，定义页面布局、配色、图表风格和信息层级。
agents/ppt_encoder_agent.md        将 deck spec 渲染为可编辑 .pptx，并输出生成报告。
agents/deck_reviewer_agent.md      审查逻辑、准确性、可读性、风格一致性和可编辑性。
agents/revision_agent.md           根据审查意见改 deck spec 并触发重新编码。
```

---

# 4. 内置 Skills

```text
skills/document-material-ingestion/      多格式素材读取、摘要、证据追踪策略
skills/web-research-briefing/            无素材或素材不足时的搜索与资料整理策略
skills/image-asset-prep/                 图片下载/复制、裁剪、resize 和 manifest 生成
skills/pptx-decoder/                     解析 PPTX 模板和已有 PPT 内容的 Python 工具
skills/pptx-encoder/                     从 deck_spec.json 生成可编辑 PPTX 的 Python 工具
skills/presentation-storyline-design/    PPT 故事线、章节结构和页面节奏设计
skills/slide-copywriting/                页面标题、要点、讲稿备注和图表文案写作
skills/visual-style-system/              模板风格迁移和无模板视觉系统设计
skills/deck-quality-review/              PPT 质量审查、返修门禁和可编辑性检查
```

---

# 5. Boss Input 模板

```markdown
# Boss Input

## PPT 目标
这份 PPT 要说服谁、解释什么、达成什么决策。

## 受众
示例：投资人 / 管理层 / 客户 / 学术评审 / 内部团队。

## 素材路径
可选。列出 docx、xlsx、pdf、pptx、txt、md 等文件路径。

## PPT 模板路径
可选。若提供，只提取风格，不复用具体内容。

## 页数与语言
示例：15 页，中文，商务简洁。

## 必须包含
可选。关键观点、数据、章节、图表或页面。

## 禁区
可选。不能使用的说法、不能外推的数据、不能出现的视觉风格。
```

---

# 6. 默认流程

```text
1. Team Lead 建立 Boss brief、输入缺口和交付目标
2. Material Ingestion 解析已有素材
3. 若素材为空或不足，Research Agent 搜索并形成 source pack
4. 若页面需要图片，Image Asset Agent 从素材或搜索结果准备 materials/images/image_manifest.json
5. 若提供 PPT 模板，Template Decoder 提取风格；若未提供，Visual Designer 自建风格系统
6. Deck Architect 设计故事线、章节和 slide list
7. Slide Writer 写每页文案、图表意图、图片引用、speaker notes 和来源引用
8. Visual Designer 形成 layout/style spec
9. PPT Encoder 生成 editable final_deck.pptx
10. Deck Reviewer 审查准确性、逻辑、视觉、可编辑性
11. 不通过则 Revision 修改 deck spec 并重新编码
12. 达标后交付 delivery/final_deck.pptx 和辅助文档
```

---

# 7. 交付标准

```text
必须交付可编辑 .pptx
正文、标题、图表标签、备注应是可编辑文本
不得只交付图片版 PPT
每页必须有明确目的，不得堆素材
数据和事实必须能追溯到素材或搜索来源
模板 PPT 只迁移风格，不复制无关内容
无模板时必须给出自洽视觉系统
需要图片的页面必须引用本地 prepared image，不得要求作者手动下载插入
```
