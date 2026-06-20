---
name: media-asset-sourcing
description: Use this skill when PPT slides need external images, screenshots, logos, product photos, stock-like visuals, diagrams, or videos that must be downloaded, inserted, or linked with source and rights tracking.
---

# Media Asset Sourcing

This skill turns media needs into local PPT-ready assets and source-traced video links.

## Search Plan

Create:

```text
materials/media/media_search_plan.md
```

For each needed visual:

```text
slide id
visual purpose
preferred media type: photo | screenshot | logo | chart | icon | video | thumbnail
query terms
preferred sources
rights requirement
fallback plan
```

## Source Preference

Prefer:

```text
Boss-provided media
official product/company/project pages
press kits and media kits
openly licensed repositories
Wikimedia Commons with license review
Unsplash/Pexels/Pixabay for generic photos when license permits
official YouTube/Vimeo/Bilibili pages for video links
dataset/benchmark/project pages for technical screenshots
```

Avoid:

```text
random reposted images
watermarked stock previews
unknown-license social media uploads
unrelated decorative photos
AI-generated images unless Boss accepts them
video mirrors from unofficial accounts
```

## Download and Prepare

Images:

```text
download/copy to materials/images/raw/
crop/resize to materials/images/processed/
record source URL, license/risk, alt text, caption, slide use
reference processed_path in deck_spec
```

Videos:

```text
download only when allowed and practical
otherwise use official video_url
prepare thumbnail_path when possible
record duration, source URL, title, rights risk, and recommended slide
reference video_path or video_url + thumbnail_path in deck_spec
```

## Manifest

Create:

```text
materials/media/media_manifest.json
```

Shape:

```json
{
  "images": [
    {
      "id": "hero_image",
      "processed_path": "materials/images/processed/hero.jpg",
      "source_url": "https://example.com/image",
      "license": "unknown | public-domain | cc-by | owned | permitted",
      "rights_risk": "low | medium | high",
      "alt": "Short alt text",
      "recommended_slide": "S03"
    }
  ],
  "videos": [
    {
      "id": "product_demo_video",
      "title": "Product demo",
      "video_url": "https://example.com/video",
      "video_path": "",
      "thumbnail_path": "materials/media/thumbnails/product_demo.jpg",
      "source_url": "https://example.com/video",
      "rights_risk": "low",
      "recommended_slide": "S08",
      "insert_mode": "link_card"
    }
  ]
}
```

## Deck Spec Elements

Image:

```json
{
  "type": "image",
  "image_path": "materials/images/processed/hero.jpg",
  "caption": "Source: ..."
}
```

Video link:

```json
{
  "type": "video_link",
  "title": "Watch the product demo",
  "video_url": "https://example.com/video",
  "thumbnail_path": "materials/media/thumbnails/product_demo.jpg",
  "caption": "Official demo video"
}
```

## Rules

```text
Do not leave image/video placeholders in final PPT when a media asset was requested.
Every external media item must have source and rights-risk metadata.
When video embedding is unsupported, use a thumbnail plus clickable URL.
Media must support the slide message; decorative filler is a failure.
```
