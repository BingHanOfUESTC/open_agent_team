---
name: experiment-iteration-loop
description: Use this skill when designing, running, logging, diagnosing, or iterating experiments for the selected research idea.
---

# Experiment Iteration Loop

This skill ensures experiments are decisive, logged, and honest about failures.

---

# 1. Experiment Queue

Maintain:

```text
research_workspace/experiments/experiment_queue.md
```

Use this structure:

```markdown
## EXP-<N>: <name>

- Purpose:
- Hypothesis:
- Baseline or variant:
- Config:
- Command:
- Expected duration:
- Hardware:
- Success criterion:
- Failure criterion:
- Status:
```

---

# 2. Required Experiment Types

Default order:

```text
SMOKE: environment and data sanity
BASE: baseline reproduction or minimum baseline
MAIN: proposed method
ABL: ablation that isolates the change
ROB: robustness/sensitivity if resources allow
FAIL: diagnosis for unexpected failure
```

Do not run expensive variants before baseline and smoke tests.

---

# 3. Logging

For every run, save:

```text
config
command
stdout/stderr
metric output
random seed
hardware
start/end time
git diff or file state
notes
```

Write summary to:

```text
research_workspace/09_experiment_log.md
```

Store raw logs under:

```text
research_workspace/experiments/logs/
```

---

# 4. Result Table

Maintain:

```text
research_workspace/experiments/results.csv
```

Minimum columns:

```text
experiment_id
method
dataset
split
seed
metric
value
runtime
hardware
log_path
notes
```

Figures and LaTeX tables must be generated from this file or a documented equivalent.

---

# 5. Iteration Decision

After each batch of experiments, decide:

```text
continue
debug
ablate
pivot
downgrade
stop_success
stop_negative_result
blocked
```

Record the decision and evidence in `decision_register.md`.

