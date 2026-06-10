---
name: skill-architecture-patterns
description: Use this skill when designing the structure of a new agent skill, choosing skill name, folder layout, freedom level, references/scripts/assets split, dependencies, validation plan, and gotchas before writing SKILL.md.
---

# Skill Architecture Patterns

## Naming

Use lowercase hyphen-case. Prefer action or capability names:

```text
good: pptx-deck-generation
good: api-change-review
bad: SkillForMakingBeautifulOutputs
```

## Freedom Level

```text
High freedom: heuristic workflows, writing, research, broad review.
Medium freedom: preferred patterns with configurable steps.
Low freedom: fragile operations, file formats, APIs, scripts, compliance checks.
```

## File Structure

```text
skill-name/
  SKILL.md
  references/     optional: long docs, schemas, examples
  scripts/        optional: deterministic or repeated operations
  assets/         optional: templates, images, starter files
```

Do not add README, changelog, install guide, or unrelated docs inside a skill package.

## Architecture Output

```markdown
# Skill Architecture

## Skill Name
## Description Draft
## Freedom Level
## Folder Structure
## SKILL.md Contents
## References
## Scripts
## Assets
## Validation Cases
## Gotchas
```
