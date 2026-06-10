---
name: quality_protocol
team: bug_triage_team
required_by:
  - team_lead_agent
---

# Bug Triage Quality Protocol

```text
Separate observed facts from hypotheses.
Preserve exact error messages, versions, environment and reproduction steps.
Trace stack frames to relevant code and configs.
Prefer minimal reproduction over broad speculation.
Every fix option needs verification.
```

## Gates

```text
Evidence capture < 9.0: revise.
Reproduction clarity < 8.5: revise.
Hypothesis plausibility < 8.5: revise.
Code-context fit < 8.5: revise.
Verification strength < 8.5: revise.
```
