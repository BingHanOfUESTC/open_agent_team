---
name: skill_registry
team: ppt_writer_team
required_by:
  - team_lead_agent
---

# PPT Writer Team Skill Registry

## 1. 素材理解

```text
skills/document-material-ingestion/SKILL.md
```

用于 doc/docx、xls/xlsx/csv、pdf、ppt/pptx、txt、markdown 等素材的读取策略、摘要、证据表和置信度标注。

## 2. 公开资料搜索

```text
skills/web-research-briefing/SKILL.md
```

当 Boss 没有提供素材，或素材不足以支撑 PPT 目标时使用。

## 3. 图片与视频资产准备

```text
skills/image-asset-prep/SKILL.md
skills/media-asset-sourcing/SKILL.md
```

用于从素材目录或搜索结果下载/复制图片到 `materials/images/raw/`，裁剪 resize 到 `materials/images/processed/`，生成 `materials/images/image_manifest.json` 供 `deck_spec.json` 引用；同时筛选视频，准备本地视频或缩略图+链接，生成 `materials/media/media_manifest.json`。

## 4. PPT 模板解析

```text
skills/pptx-decoder/SKILL.md
skills/template-fidelity-system/SKILL.md
```

用于解析 `.pptx` 的 slide size、主题色、字体、版式、文本框、图片、形状、备注、背景、母版节奏和 slot geometry。有模板时默认严格遵从模板系统，不复用无关业务内容。

## 5. PPT 生成

```text
skills/pptx-encoder/SKILL.md
```

用于把 `deck_spec/deck_spec.json` 和 `deck_spec/style_spec.json` 渲染为可编辑 `.pptx`。

## 6. 故事线设计

```text
skills/presentation-storyline-design/SKILL.md
```

用于定义受众、目标、叙事主线、章节结构、页面节奏和决策路径。

## 7. 页面文案

```text
skills/slide-copywriting/SKILL.md
```

用于每页 headline、body、callout、chart title、speaker notes 和 source note。

## 8. 视觉系统

```text
skills/visual-style-system/SKILL.md
```

用于从模板迁移风格，或在无模板时自建字体、颜色、版式、图表和图标风格。
有模板时必须配合 `template-fidelity-system`，优先保持模板布局、字体、背景和页眉页脚；无模板时才进行开放式创新设计。

## 9. 质量评审

```text
skills/deck-quality-review/SKILL.md
```

用于内容、结构、视觉、来源、可编辑性和编码完整性审查。
