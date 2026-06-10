---
name: quality_protocol
team: code_review_team
required_by:
  - team_lead_agent
---

# Code Review Quality Protocol

```text
Findings first. No praise padding.
Every finding needs file/line or code evidence.
Prioritize correctness, security, data loss, compatibility and missing tests.
Do not invent behavior not supported by code.
Distinguish confirmed bug, plausible risk and style preference.
```

## Gates

```text
Evidence quality < 9.0: revise.
Bug relevance < 8.5: revise.
Security coverage < 8.0: revise.
Test gap coverage < 8.5: revise.
Actionability < 8.5: revise.
```
