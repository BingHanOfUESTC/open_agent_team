# Visual Style System

Use this skill to extract or design a PPT style system that can be encoded into `style_spec.json`.

## Style Spec Fields

```json
{
  "slide_size": "16:9",
  "theme_colors": {
    "background": "FFFFFF",
    "text": "1F2937",
    "primary": "2563EB",
    "secondary": "14B8A6",
    "accent": "F59E0B",
    "muted": "6B7280"
  },
  "fonts": {
    "title": "Arial",
    "body": "Arial",
    "caption": "Arial"
  },
  "typography": {
    "title_size": 30,
    "subtitle_size": 18,
    "body_size": 15,
    "caption_size": 9,
    "min_title_size": 20,
    "min_body_size": 10
  },
  "layout_tokens": {
    "margin_left": 0.65,
    "margin_right": 0.65,
    "header_height": 0.25,
    "footer_height": 0.28,
    "gutter": 0.28
  },
  "template_patterns": {
    "uses_header": false,
    "uses_footer": true,
    "header_text": "",
    "footer_text": ""
  },
  "layouts": {}
}
```

## Template Transfer

When a template is provided:

```text
Extract style, not content.
Preserve slide size and visual rhythm.
Reuse color/font/layout tendencies, header/footer treatment, page numbering, section-divider patterns, table/chart styling, shape fill/line habits and spacing.
Avoid using client names, copied diagrams, data, slogans or business content from the template.
```

Use `style_spec_suggestion` from the PPTX decoder as the starting point when available. Clean it manually:

```text
Keep template design colors, but map them into semantic roles: background, text, primary, secondary, accent, muted and surface.
Preserve the template's dominant font family and realistic title/body/caption size hierarchy.
Preserve reusable header/footer usage, but replace template-specific business text with generic or deck-specific text.
Preserve visual style and purpose style, not source content.
```

## No Template Design

When no template is provided:

```text
Choose style based on audience and purpose.
Use restrained color palette.
Make text hierarchy obvious.
Use consistent spacing and margins.
Design repeatable layouts: title, section, content, comparison, chart, table, closing.
```

## Rules

```text
Readable beats decorative.
Consistency beats novelty.
Use enough contrast for projection.
Leave whitespace.
Avoid layouts that require tiny text.
Avoid content boxes that force body text below 10pt.
For dense slides, split content across slides or use a two-column/grid layout instead of shrinking text.
```
