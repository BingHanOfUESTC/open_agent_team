---
name: skill-authoring-workflow
description: Use this skill when writing or updating SKILL.md for an agent skill, including model-facing frontmatter description, concise body instructions, workflow steps, resource navigation, gotchas, and self-checks.
---

# Skill Authoring Workflow

## Required SKILL.md Anatomy

```markdown
---
name: skill-name
description: Use this skill when ...
---

# Skill Title

## When To Use
## Workflow
## Inputs
## Outputs
## Gotchas
## References / Scripts / Assets
## Self-Check
```

## Description Rules

The description is for model routing. Include:

```text
task trigger
user phrases or scenarios
file types or tool contexts if relevant
boundaries that avoid over-triggering
```

Avoid human marketing language.

## Body Rules

```text
Keep only essential procedural knowledge.
Assume the model already knows common reasoning and writing.
Use concise examples.
Move long details to references.
Move repeated code to scripts.
Move templates/assets to assets.
```

## Gotchas

- Gotchas should be concrete failure modes, not vague warnings.
- Prefer “When X happens, do Y” over broad principles.
- If the skill depends on setup, say exactly what to ask or inspect.
