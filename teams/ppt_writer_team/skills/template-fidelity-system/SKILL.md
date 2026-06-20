---
name: template-fidelity-system
description: Use this skill when Boss provides a PPT/PPTX template and expects the new deck to follow that template's layout, fonts, backgrounds, master rhythm, and page patterns rather than merely taking loose visual inspiration.
---

# Template Fidelity System

This skill makes template use strict by default. A supplied template is not a mood board. It is the design contract for the generated deck unless Boss explicitly asks for redesign.

## Fidelity Modes

```text
strict: keep template dimensions, background, fonts, margins, page furniture, layout slots, and component style as closely as possible.
adaptive: keep the template system, but add new layouts only when the template lacks the required page type.
inspiration_only: use the template as loose reference only when Boss explicitly requests redesign.
```

Default to `strict` when a template is provided.

## Required Outputs

Create:

```text
template/template_fidelity_plan.md
deck_spec/style_spec.json
```

`style_spec.json` should include:

```json
{
  "template_pptx": "path/to/template.pptx",
  "template_fidelity": {
    "mode": "strict",
    "preserve_background": true,
    "preserve_master": true,
    "preserve_header_footer": true,
    "allow_new_layouts": false
  },
  "layouts": {
    "content": {
      "source_template_slide": 3,
      "slots": [
        {"role": "headline", "x": 0.7, "y": 0.5, "w": 11.8, "h": 0.6},
        {"role": "body", "x": 0.8, "y": 1.35, "w": 5.4, "h": 4.9},
        {"role": "visual", "x": 6.7, "y": 1.35, "w": 5.7, "h": 4.9}
      ]
    }
  }
}
```

Use inches for slot coordinates.

## Template Analysis Checklist

Record:

```text
slide size and aspect ratio
dominant background per page type
font family and title/body/caption sizes
margin grid and gutters
headline placement
body/content slots
image slots and crop style
chart/table styling
section divider pattern
page number, footer, logo, date, confidentiality marks
decorative shapes that are part of the template identity
```

## Design Rules

```text
Use template slots before inventing new ones.
Keep the same background treatment for matching page types.
Keep font family and hierarchy unless unreadable or unavailable.
Keep page furniture in the same positions.
Keep chart/table colors and stroke habits aligned with the template.
Replace template business text with current deck content.
Do not copy unrelated customer names, data, slogans, charts, or confidential text.
```

## Fidelity Gate

Before encoding:

```text
Each slide has a template page type or explicit exception.
Each slide uses template-compatible slot geometry.
style_spec references the template path when available.
No global color/font/background replacement has occurred without Boss request.
New layouts, if any, are explained in template_fidelity_plan.md.
```

