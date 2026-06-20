# Image Asset Prep

Use this skill when a PPT needs real images from Boss-provided materials or public search results. For video search/linking, use it together with `media-asset-sourcing`.

## Purpose

Prepare image assets before PPTX rendering so the encoder can insert concrete local files instead of leaving placeholders or asking the author to download images manually.

## Tool

```bash
python teams/ppt_writer_team/skills/image-asset-prep/scripts/prepare_images.py \
  --scan-dir source_materials \
  --output-dir materials/images \
  --aspect-ratio 16:9 \
  --width 1600 \
  --height 900
```

For selected URLs or local files:

```bash
python teams/ppt_writer_team/skills/image-asset-prep/scripts/prepare_images.py \
  --input local/photo.jpg \
  --url https://example.com/image.jpg \
  --output-dir materials/images \
  --aspect-ratio 4:3
```

For a curated manifest:

```bash
python teams/ppt_writer_team/skills/image-asset-prep/scripts/prepare_images.py \
  --manifest materials/image_requests.json \
  --output-dir materials/images
```

## Manifest Shape

```json
[
  {
    "id": "hero_product",
    "source": "downloads/product.jpg",
    "alt": "Product in use",
    "aspect_ratio": "16:9",
    "fit": "cover"
  },
  {
    "id": "market_chart_photo",
    "url": "https://example.com/photo.jpg",
    "alt": "Storefront image",
    "aspect_ratio": "4:3"
  }
]
```

## Outputs

```text
materials/images/raw/
materials/images/processed/
materials/images/image_manifest.json
```

`image_manifest.json` contains `id`, original source, processed local path, dimensions, aspect ratio and alt/caption metadata. `deck_spec.json` should reference the processed local path or the image id from this manifest.

When preparing thumbnails for videos, save them under:

```text
materials/media/thumbnails/
```

and record them in `materials/media/media_manifest.json`.

## Rules

```text
Prefer images from Boss-provided material when available.
When using public web images, save the image into materials/images/raw/ and record the source URL.
Never leave final slides with "download image" instructions.
Crop/resize before rendering so image boxes are visually full and do not contain avoidable empty margins.
Use cover crop for hero/photo slots and contain only when the full image must remain visible.
Do not use images whose source or rights are unclear for external-facing decks without review.
```
