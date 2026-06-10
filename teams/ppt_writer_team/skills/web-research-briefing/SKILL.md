# Web Research Briefing

Use this skill when Boss provides no material, or when provided material is insufficient for the requested PPT.

## Research Plan

Create a search plan before collecting facts:

```text
decision / communication goal
key questions
priority source types
queries
exclusion rules
freshness requirements
```

## Source Priority

```text
1. Official primary sources: company, regulator, government, standards body, university, project owner.
2. Original publications: papers, reports, filings, datasets.
3. Reputable secondary sources: recognized media or analyst summaries.
4. Low-confidence web content only for leads, not final claims.
```

## Source Pack Schema

```text
| id | title | url | publisher | date | accessed | key facts | planned use | confidence |
```

## Image Source Pack

When public images are needed:

```text
Prefer official pages, press/media kits, product pages, project pages, Wikimedia/CC sources or user-approved sources.
Record image page URL, direct image URL when available, publisher/owner, license or rights note, accessed date and intended slide use.
Pass approved image URLs to image_asset_agent for download into materials/images/raw/.
```

## Rules

```text
Do not fabricate URLs.
Do not use a single weak source for a central claim.
Record access date for web sources.
Mark facts as uncertain when sources conflict.
Keep copyrighted text summarized, not copied.
Do not use unclear-rights images for external-facing decks without explicit review.
```

## Output Files

```text
research/search_plan.md
research/source_pack.md
research/research_gaps.md
```
