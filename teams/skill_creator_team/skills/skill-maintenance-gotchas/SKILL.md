---
name: skill-maintenance-gotchas
description: Use this skill when reviewing or maintaining an agent skill after creation, especially to add gotchas from failures, check over-triggering or under-triggering, assess action-at-a-distance conflicts with other skills, and plan future iterations.
---

# Skill Maintenance Gotchas

## Maintenance Review

Check:

```text
What failures would make this skill worse over time?
Where might the skill over-trigger?
Where might it under-trigger?
Which existing skills overlap with it?
What gotchas should be added after first real use?
What should become a script if repeated?
What should move to references if SKILL.md grows?
```

## Gotchas Format

```markdown
## Gotcha: <short name>

Symptom:
Cause:
What to do:
Validation:
```

## Action At A Distance

New skills can affect routing for existing skills. Always check:

```text
similar names
similar descriptions
overlapping trigger phrases
shared tools or file types
broader descriptions that may steal traffic
```

## Maintenance Output

```markdown
# Gotchas And Risks

## Initial Gotchas
## Over-Trigger Risks
## Under-Trigger Risks
## Skill Conflicts
## Future Iterations
```
