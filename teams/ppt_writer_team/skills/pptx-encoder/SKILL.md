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
video_link
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
template_pptx: optional path to Boss-provided template. When present, renderer uses it as the base presentation where possible.
template_fidelity: preserve_background/preserve_master/header_footer flags.
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

## Video Elements

Prefer local video embedding only when the runtime supports it. Otherwise use clickable video cards:

```json
{
  "type": "video_link",
  "title": "Watch demo",
  "video_url": "https://example.com/video",
  "thumbnail_path": "materials/media/thumbnails/demo.jpg",
  "caption": "Official demo video"
}
```

The renderer inserts a thumbnail when available and adds a clickable URL card. This is the default fallback for videos because PowerPoint video embedding support varies across runtimes.

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
When style_spec includes template_pptx, generate from that template base and preserve master/background behavior where possible.
For video needs, insert a local video when supported or a clickable thumbnail/link card.
```
