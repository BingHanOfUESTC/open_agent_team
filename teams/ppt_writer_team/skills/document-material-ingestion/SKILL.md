# Document Material Ingestion

Use this skill when the team must turn Boss-provided mixed-format documents into PPT-ready facts, arguments, data tables, and source traces.

## Inputs

```text
Boss brief
File paths
Target audience
PPT goal
Required slides or topics
```

## Supported Strategy

```text
doc/docx:
  Extract heading structure, paragraphs, tables, executive conclusions, definitions.

xls/xlsx/csv:
  Extract workbook/sheet names, table ranges, fields, time periods, metrics, units, missing values.

pdf:
  Extract page-level text, headings, tables if possible, figure captions, referenced numbers.

ppt/pptx:
  If material deck: extract slide titles, body, notes, charts, tables.
  If template deck: route to template_decoder_agent and do not use content as source claims.

image files:
  Inventory jpg/jpeg/png/webp/bmp/tiff assets with path, apparent topic, dimensions if available and suggested slide use.

txt/md:
  Extract headings, lists, tables, quoted blocks, code blocks, links.
```

## Evidence Table Schema

```text
| id | claim_or_data | source_file | location | confidence | suggested_slide_use |
```

## Rules

```text
Keep source position whenever possible.
Preserve units, dates, denominator, geography, sample size and assumptions.
Separate facts from interpretation.
Mark unreadable files explicitly.
Never invent data to fill missing tables.
```

## Output Files

```text
materials/material_inventory.md
materials/evidence_table.md
materials/data_tables.md
materials/images/image_manifest.json when image assets are prepared
```
