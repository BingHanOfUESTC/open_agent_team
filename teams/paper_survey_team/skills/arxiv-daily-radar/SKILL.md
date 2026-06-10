---
name: arxiv-daily-radar
description: Use this skill when paper_survey_team needs to find, filter, rank, and summarize the newest papers from arXiv or paper communities for a user-specified research direction and time window such as today, latest day, last 24 hours, or last 3 days.
---

# arXiv Daily Radar

This local skill defines a reproducible workflow for daily paper recommendation.

## Workflow

1. Convert the user's direction into keywords, synonyms, and arXiv categories.
2. Search arXiv by submitted date or announced date when possible.
3. Cross-check with Hugging Face Papers, OpenReview, Papers with Code, lab pages, and community discussion when available.
4. Exclude papers outside the requested window unless they are needed as background.
5. Rank papers by:
   - relevance to Boss direction
   - novelty of problem or method
   - credibility of authors/institutions
   - experimental strength
   - relation to current research frontier
   - availability of code/data
   - potential impact
6. Produce a short list with reasons, not just titles.

## Required Output

```markdown
# Daily Paper Radar

## Search Window

## Query Terms

## Candidate Papers
| Rank | Paper | Authors | Source | Date | Why It Matters | Priority |
|---|---|---|---|---|---|---|

## Top Recommendations

For each paper:
- Core problem
- Core contribution
- Method idea
- Main evidence
- Why it is worth reading today
- Caveats
- Related prior work

## Trend Signal

## Papers To Skip Or Defer
```

## Hard Rules

- Do not fabricate today's papers.
- Do not treat "new" as "important".
- If exact date filtering is unavailable, state the limitation.
- If only abstracts are available, mark the analysis as abstract-level.
- Include links whenever available.
