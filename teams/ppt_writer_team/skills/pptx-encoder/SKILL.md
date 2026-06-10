# PPTX Encoder

Use this skill when the team must render `deck_spec.json` and `style_spec.json` into a real editable `.pptx`.

## Tool

Use:

```bash
python .opencode/skills/pptx-encoder/scripts/render_deck.py \
  --deck-spec deck_spec/deck_spec.json \
  --style-spec deck_spec/style_spec.json \
  --output delivery/final_deck.pptx \
  --report encoding/encoding_report.md
```

or from the repository:

```bash
python teams/ppt_writer_team/skills/pptx-encoder/scripts/render_deck.py \
  --deck-spec deck_spec/deck_spec.json \
  --style-spec deck_spec/style_spec.json \
  --output delivery/final_deck.pptx \
  --report encoding/encoding_report.md
```

## Supported Elements

```text
text
bullets
callout
table
image_placeholder
image
chart_placeholder
divider
footer/source note
speaker notes
```

## Style Spec Support

The renderer reads these optional fields from `style_spec.json`:

```text
typography: title/subtitle/body/caption sizes and minimum readable sizes.
layout_tokens: margins, gutters, header height and footer height.
template_patterns: reusable header/footer behavior and deck-specific header/footer text.
theme_colors: background, text, primary, secondary, accent, muted and surface.
```

The renderer dynamically reduces text size within configured minimums and distributes multiple elements across the available content area. If a slide still needs unreadably small text, revise `deck_spec.json` by splitting content across slides instead of forcing more text into one slide.

## Image Elements

Use prepared local image assets:

```json
{
  "type": "image",
  "image_path": "materials/images/processed/hero-product-1600x900.jpg",
  "caption": "Optional short caption"
}
```

`image_placeholder` can also include `image_path`; if the file exists, the renderer inserts the image. If the path is missing, it renders a placeholder and records a warning.

## deck_spec Minimal Shape

```json
{
  "title": "Deck title",
  "slides": [
    {
      "layout": "title",
      "headline": "A clear claim",
      "elements": [],
      "speaker_notes": "What the presenter should say.",
      "source_notes": []
    }
  ]
}
```

## Rules

```text
Generate editable PowerPoint text and shapes.
Never render the whole page as one image.
Preserve deck_spec as the source of truth.
Report unsupported element types instead of silently dropping them.
Use the template style system from style_spec before falling back to defaults.
Insert prepared local images directly when deck_spec provides image_path/processed_path.
```
