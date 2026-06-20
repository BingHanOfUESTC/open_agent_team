---
name: reproducible-code-data-setup
description: Use this skill when downloading repositories, preparing datasets, checking licenses, creating environments, running smoke tests, or preparing reproducible research code.
---

# Reproducible Code Data Setup

This skill controls the handoff from idea to runnable research artifact.

---

# 1. Source Intake

Before using external code or data, record:

```text
name
URL
local path
commit/tag/version
license
download date
intended use
security notes
```

Write it to:

```text
research_workspace/06_code_data_manifest.md
```

Do not run installer scripts from unknown repositories before reading them.

---

# 2. Safety Review

Check for:

```text
credential access
network exfiltration
destructive filesystem operations
hidden downloads
opaque binaries
postinstall hooks
unbounded subprocess spawning
license incompatibility
dataset terms that prohibit the intended use
```

If risk is unclear, isolate in a container or do static review only.

---

# 3. Environment Contract

Create one of:

```text
environment.yml
requirements.txt
pyproject.toml
Dockerfile
setup_notes.md
```

Record:

```text
OS
Python version
CUDA/ROCm/CPU status
GPU model and memory
package manager
exact install commands
known incompatibilities
```

---

# 4. Smoke Tests

Run the cheapest possible checks first:

```text
import test
CLI help command
unit test subset
dataset sample load
one batch forward pass
one batch train step
metric computation on tiny output
```

Only after smoke tests pass should full experiments begin.

---

# 5. Patch Discipline

When modifying third-party code:

```text
keep changes minimal
prefer config switches over invasive edits
document every modified file
preserve upstream license headers
separate baseline from new method
make experiment commands reproducible
```

