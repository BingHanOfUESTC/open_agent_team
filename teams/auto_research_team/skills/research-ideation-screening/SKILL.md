---
name: research-ideation-screening
description: Use this skill when generating, screening, ranking, or selecting research ideas from literature gaps and experimental constraints.
---

# Research Ideation Screening

This skill prevents vague novelty claims. An idea is only useful if it is tied to evidence, implementable under constraints, and falsifiable by an experiment.

---

# 1. Idea Generation Lenses

Generate candidates using at least five lenses:

```text
failure case repair
metric-target mismatch
data efficiency
compute efficiency
robustness and distribution shift
architecture simplification
training objective change
evaluation protocol improvement
tooling or reproducibility gap
negative result worth documenting
```

Avoid ideas that only rename existing methods.

---

# 2. Idea Card

Write each candidate in:

```text
research_workspace/ideas/idea_<N>.md
```

Template:

```markdown
# Idea <N>: <title>

- Gap:
- Evidence:
- Hypothesis:
- Method sketch:
- Minimal implementation:
- Baseline:
- Dataset/benchmark:
- Primary metric:
- Ablation:
- Expected failure mode:
- Resource estimate:
- Novelty risk:
- License/data risk:
- Stop condition:
```

---

# 3. Screening Matrix

Maintain:

```text
research_workspace/ideas/screening_matrix.md
```

Score 1-5:

```text
evidence strength
novelty
implementation simplicity
evaluation clarity
resource fit
expected impact
risk containment
paper-worthiness
```

Select the idea with the best combination of evidence, feasibility, and falsifiability, not the most impressive wording.

---

# 4. Red-Team Questions

Before committing to an idea, answer:

```text
Has this already been done?
Can a small experiment disprove it?
Is the baseline fair?
Would a null result still teach something?
Can the implementation be isolated?
Can results be plotted in one clear table or figure?
What would make us abandon the idea?
```

If these cannot be answered, return to literature mapping or scope refinement.

