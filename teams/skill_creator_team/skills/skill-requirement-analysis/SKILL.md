---
name: skill-requirement-analysis
description: Use this skill when creating a new agent skill from a user problem, repeated workflow, expected output, examples, or failure cases; extract trigger conditions, reusable capability, inputs, outputs, constraints, evaluation criteria, and contamination risks before authoring the skill.
---

# Skill Requirement Analysis

Use this before writing any SKILL.md.

## Workflow

1. Restate the user problem in one paragraph.
2. Identify the repeated task pattern behind the request.
3. Separate reusable method from one-off content.
4. Define trigger conditions and non-trigger conditions.
5. Capture inputs, outputs, tools, file types, and environment assumptions.
6. Extract evaluation criteria from the expected result.
7. Record privacy, copyright, security, and sample-answer contamination risks.

## Output Shape

```markdown
# Skill Requirements

## Problem
## Reusable Capability
## Trigger Conditions
## Non-Trigger Conditions
## Inputs
## Outputs
## Tools / Environment
## Evaluation Criteria
## Risks And Forbidden Content
## Open Questions
```

## Gotchas

- Do not mistake a desired final answer for reusable skill content.
- Do not create a skill if the task is purely one-off and unlikely to recur.
- If examples are provided, use them for evaluation and failure-mode extraction, not memorization.
