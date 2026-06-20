---
name: autoresearch-orchestration
description: Use this skill when auto_research_team needs to manage an end-to-end research lifecycle from Boss brief to literature, idea, implementation, experiments, synthesis, and LaTeX delivery. Trigger for open-ended research tasks, autonomous research loops, idea-to-paper workflows, or long-running experiment iteration.
---

# Autoresearch Orchestration

This skill gives `auto_research_team` a durable control loop. It is inspired by open-source auto-research systems, but the operating procedure here is specific to this repository.

Use it when the task is larger than a single literature review or code change.

---

# 1. Workspace Contract

Create or update:

```text
research_workspace/research_state.md
research_workspace/research_log.md
research_workspace/findings.md
research_workspace/decision_register.md
research_workspace/to_boss.md
```

`research_state.md` tracks the current stage:

```text
scope
literature
idea
plan
code_data
environment
implementation
experiment
analysis
paper
delivery
blocked
```

`findings.md` is persistent memory. Never bury lessons only in chat.

---

# 2. Two-Loop Operation

Outer synthesis loop:

```text
1. collect evidence
2. update gap map
3. revise idea
4. revise experiment plan
5. decide whether to continue, pivot, or stop
```

Inner experiment loop:

```text
1. choose smallest decisive experiment
2. run smoke test
3. run baseline
4. run main variant
5. run ablation or diagnostic
6. update results table
```

The team must not jump to paper writing until both loops have produced traceable evidence or a clearly documented negative result.

---

# 3. Decision Register

Every major decision must be written as:

```markdown
## Decision <N>: <short title>

- Date:
- Owner:
- Options considered:
- Evidence:
- Decision:
- Risk:
- Reversal condition:
```

Use this for selecting papers, rejecting datasets, choosing the main idea, changing baseline, stopping training, or downgrading experiments.

---

# 4. Boss Escalation

Escalate only when progress requires Boss input:

```text
data license requires approval
paid API or paid compute is required
private dataset credentials are missing
hardware is insufficient for all meaningful validation
research objective conflicts with safety or license constraints
```

Otherwise make a conservative assumption, record it, and continue.

---

# 5. Done Criteria

The loop is complete only when:

```text
research question is explicit
literature evidence is traceable
idea is tied to a gap
code/data/environment status is known
experiments or valid downgrades are logged
result analysis states supported and unsupported claims
LaTeX report compiles or failure is recorded
artifact manifest and reproduction guide exist
```

