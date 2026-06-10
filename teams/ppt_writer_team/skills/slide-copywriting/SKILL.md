# Slide Copywriting

Use this skill when writing slide headlines, bullets, labels, callouts, captions, speaker notes and source notes.

## Headline Rules

```text
Write the takeaway, not the topic.
Prefer specific verbs and numbers when supported.
Avoid vague titles such as "Overview", "Background", "Analysis".
Keep headlines short enough to fit.
```

## Body Rules

```text
Use 3-5 bullets at most for standard content slides.
Keep bullets parallel.
Use exact units and dates for numbers.
Move nuance into speaker notes.
Do not paste paragraphs from source material.
```

## Visual Intent Rules

```text
For charts, state the question the chart answers.
For tables, state what comparison matters.
For diagrams, state the relationship or flow.
For timelines, state the change or sequence.
```

## deck_spec Element Examples

```json
{
  "type": "text",
  "role": "body",
  "text": ["Point one", "Point two"]
}
```

```json
{
  "type": "image",
  "image_path": "materials/images/processed/hero-product-1600x900.jpg",
  "alt": "Product in use",
  "caption": "Optional short caption",
  "source": "materials/images/image_manifest.json#hero_product"
}
```

```json
{
  "type": "chart_placeholder",
  "chart_type": "bar",
  "title": "Revenue growth is concentrated in two segments",
  "data_source": "materials/evidence_table.md#E12"
}
```

## Rules

```text
Every factual claim needs a source note.
Do not overfill slides.
Do not use slogans when evidence is required.
Do not make unsupported causal claims.
For image slides, reference prepared local image_path values from materials/images/image_manifest.json.
Do not write "download image", "insert image manually" or unresolved image instructions in final deck_spec.
```
