---
name: research-lineage-mapper
description: Use this skill when paper_survey_team needs to map a research direction into influential paper paths, lab/team/person trajectories, problem definitions, method lineages, benchmark evolution, unresolved problems, and future directions.
---

# Research Lineage Mapper

This local skill turns paper collections into a research trajectory.

## Core Questions

For any direction, answer:

```text
What problem was originally defined?
Which papers changed the problem definition?
Which methods became dominant?
Which labs or teams repeatedly contributed?
Which benchmarks shaped progress?
Which assumptions remain fragile?
What is still unsolved?
Where is the direction likely to go?
```

## Mapping Axes

Use at least four axes:

```text
Time: early work -> transition -> current frontier
Problem: task definition -> objective -> evaluation
Method: algorithm/model/data/training/inference route
People: labs, PIs, students, companies, open-source communities
```

## Report Artifacts

```markdown
# Research Lineage Map

## Timeline
| Period | Key Question | Representative Papers | Main Shift |
|---|---|---|---|

## Problem-Method Matrix
| Problem Definition | Method Family | Representative Papers | Strength | Limitation |
|---|---|---|---|---|

## Lab And People Map
| Lab/Team | Key People | Representative Contributions | Evidence |
|---|---|---|---|

## Benchmark Evolution
| Benchmark/Data | What It Measures | What It Misses | Related Papers |
|---|---|---|---|

## Open Problems

## Future Directions
```

## Hard Rules

- Do not invent advisor/student relationships.
- Mark inferred relationships as inference.
- Do not overstate impact from a single paper.
- Distinguish influential, representative, recent, and speculative papers.
