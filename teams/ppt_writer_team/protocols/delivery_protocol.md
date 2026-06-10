---
name: delivery_protocol
team: ppt_writer_team
required_by:
  - team_lead_agent
---

# PPT Writer Team Delivery Protocol

## 1. 必须交付文件

```text
delivery/final_deck.pptx
delivery/executive_summary.md
delivery/speaker_notes.md
delivery/source_trace.md
deck_spec/deck_spec.json
deck_spec/style_spec.json
deck_spec/content_outline.md
reviews/deck_review.md
```

## 2. 条件交付文件

```text
materials/material_inventory.md
materials/evidence_table.md
materials/images/image_manifest.json
research/search_plan.md
research/source_pack.md
template/template_style_report.md
encoding/encoding_report.md
encoding/decoder_report.md
revisions/revision_plan.md
revisions/change_log.md
```

## 3. final_deck.pptx 要求

```text
必须可被 PowerPoint、Keynote 或 LibreOffice Impress 打开。
页面内容必须尽量可编辑。
不得只交付截图版幻灯片。
必须保留 speaker notes，至少在 speaker_notes.md 中完整交付。
必须与 deck_spec.json 的页面顺序一致。
图片页面必须插入本地 prepared image，不得只保留图片下载说明或空占位符。
```

## 4. executive_summary.md 要求

```text
PPT 目标
受众
页数
核心叙事
关键结论
素材来源概述
模板/视觉风格说明
未覆盖或低置信度信息
```

## 5. source_trace.md 要求

```text
每个关键事实对应来源文件、页码、sheet、段落或 URL。
搜索资料必须记录标题、URL、访问日期和用途。
外部图片必须记录图片来源 URL、权利/许可风险和本地 processed_path。
无法核实的信息必须标注为未使用或低置信度。
```

## 6. 不允许交付

```text
只有大纲，没有 PPTX。
只有 PDF，没有 PPTX。
只有图片版 PPTX。
只有 deck_spec.json，没有渲染。
需要图片却让作者手动下载或插入。
使用模板 PPT 的无关原内容充数。
没有来源追踪的事实密集型 PPT。
```
