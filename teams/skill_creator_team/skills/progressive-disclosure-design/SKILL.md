---
name: progressive-disclosure-design
description: Use this skill when reducing context cost in an agent skill by deciding what belongs in metadata, SKILL.md body, references, scripts, assets, or validation files; trigger when SKILL.md is too long, too detailed, or mixes multiple variants.
---

# Progressive Disclosure Design

A skill should load information in layers:

```text
metadata: name + description for routing
SKILL.md: essential workflow and resource map
references: detailed docs loaded only when needed
scripts: deterministic operations and repeated code
assets: templates or files used in output
```

## Review Checklist

```text
Can description route correctly without reading the body?
Does SKILL.md stay focused on core workflow?
Are long examples, schemas, APIs, and policy details in references?
Are fragile repeated operations implemented as scripts?
Are templates or starter files in assets?
Does SKILL.md clearly tell the agent when to load each resource?
```

## Refactor Patterns

```text
Multiple domains -> references/<domain>.md
Multiple frameworks -> references/<framework>.md
Repeated code -> scripts/<operation>.py
Output template -> assets/<template>
Large examples -> references/examples.md
```

## Gotchas

- Do not hide mandatory rules in references unless SKILL.md tells the agent to read them.
- Do not split so deeply that navigation becomes its own task.
- Keep references one level deep unless there is a strong reason.
