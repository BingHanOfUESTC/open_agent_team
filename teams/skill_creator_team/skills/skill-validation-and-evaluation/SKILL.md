---
name: skill-validation-and-evaluation
description: Use this skill when validating a newly created or updated agent skill with structure checks, routing positive and negative examples, contamination checks, progressive disclosure review, and quality scoring before delivery.
---

# Skill Validation And Evaluation

## Required Validation

```text
Structure check: SKILL.md exists, has YAML frontmatter, name, description.
Routing check: 2+ positive examples should trigger the skill.
Negative routing check: 1+ example should not trigger the skill.
Content check: workflow, inputs, outputs, gotchas, resources.
Contamination check: no copied expected answer, private data, or one-off conclusion.
Progressive disclosure check: no unnecessary long content in SKILL.md.
```

## Validation Cases Format

```markdown
# Validation Cases

## Positive Case 1
User request:
Expected trigger reason:

## Positive Case 2
User request:
Expected trigger reason:

## Negative Case
User request:
Why it should not trigger:
```

## Scoring

Use 0-10:

```text
8.5-10: pass
7.0-8.4: conditional_pass with required fixes
<7.0: fail
```

## Script

Use `scripts/validate_skill.py <skill_dir>` for basic structure validation.
