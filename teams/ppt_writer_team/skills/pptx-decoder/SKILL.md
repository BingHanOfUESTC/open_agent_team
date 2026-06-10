# PPTX Decoder

Use this skill when the team needs to parse an existing `.pptx` file as either:

```text
1. a template whose style should be extracted, or
2. a material deck whose content should be summarized.
```

## Tool

Use:

```bash
python .opencode/skills/pptx-decoder/scripts/decode_pptx.py --input template.pptx --output template_style.json --mode template
```

or from the repository:

```bash
python teams/ppt_writer_team/skills/pptx-decoder/scripts/decode_pptx.py --input template.pptx --output template_style.json --mode template
```

## Modes

```text
template:
  Extract slide size, theme/design colors, font hierarchy, layouts, shape styles, header/footer regions, image counts and reusable visual patterns.

material:
  Extract titles, body text, notes, tables, media counts and slide-level summaries.
```

## Output

The script writes JSON with:

```text
file
mode
slide_width
slide_height
slides[]
style_summary
style_spec_suggestion
warnings[]
```

In template mode, `style_spec_suggestion` is a machine-generated starting point for `deck_spec/style_spec.json`. The template decoder or visual designer must review it before use, especially semantic color roles and any header/footer text examples.

## Rules

```text
Use template mode only for style transfer.
Do not reuse unrelated template content.
Preserve reusable design intent: colors, typography, spacing, page furniture, section-divider style, table/chart treatment and purpose-specific layout rhythm.
If python-pptx is missing, report dependency error and ask ppt_encoder_agent/team_lead_agent to install it.
```
