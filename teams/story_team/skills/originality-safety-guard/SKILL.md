---
name: originality-safety-guard
description: Use this skill when checking creative fiction for originality, name safety, public figure misuse, historical figure misuse, news-event overfitting, recognizable plot borrowing, IP-like names, and high-risk homage. Trigger before drafting and before final delivery for story_team.
---

# Originality Safety Guard

This local skill protects `story_team` from lazy borrowing, accidental
recognizable references, public figure misuse, and high-risk derivative work.

## Core Rule

Keep the theme. Replace the traceable specifics.

The story may explore grief, ambition, corruption, revenge, fame, poverty,
technology, power, faith, memory, or any other human subject. It must not
reuse identifiable real people, real news chains, famous fictional names, or
recognizable plot skeletons as shortcuts.

## Checkpoints

Run this at three points:

1. Concept stage: before the team commits to premise.
2. Outline stage: before drafting.
3. Final stage: before delivery.

## High-Risk Content

Flag and replace:

```text
Real public figures, ancient or modern
Real historical figures and famous rulers, ministers, generals, revolutionaries
Real news victims, criminals, celebrities, companies, schools, hospitals, disasters, court cases
Names strongly associated with famous novels, films, games, anime, comics, web novels
Factions, places, artifacts, spells, organizations, or titles that resemble known IP
Plot structures whose sequence of distinctive beats maps closely to a famous work
Settings that preserve enough detail to identify a real scandal, case, accident, or tragedy
```

## Allowed Transformation

When a story needs realism or historical texture:

```text
Change names
Change location
Change period
Change profession mix
Change event order
Change motive
Change outcome
Remove exact dates, numbers, institutions, and signature details
Invent fictional civic, corporate, religious, or family structures
```

## Report Format

```markdown
# Originality Safety Report

## Verdict
Pass / Conditional Pass / Fail

## High-Risk Items
| Item | Risk | Why It Matters | Required Fix |
|---|---|---|---|

## Medium-Risk Items
| Item | Risk | Suggested Fix |
|---|---|---|

## Name Review
| Name | Type | Risk Level | Action |
|---|---|---|---|

## Plot Similarity Review
| Beat | Similarity Risk | Action |
|---|---|---|

## Final Gate
Allowed into final draft: Yes / No
```

## Hard Gate

If any high-risk item remains unresolved, the final answer must not claim the
story is ready. Send it back to concept, outline, or revision depending on
where the risk lives.
