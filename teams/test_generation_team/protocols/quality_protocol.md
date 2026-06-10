---
name: quality_protocol
team: test_generation_team
required_by:
  - team_lead_agent
---

# Test Generation Quality Protocol

```text
Understand behavior before writing tests.
Map tests to public contracts, branches, failure modes and historical bugs.
Avoid brittle tests that assert implementation details unless necessary.
Each test needs purpose, setup, assertion and expected failure signal.
```

## Gates

```text
Behavior coverage < 8.5: revise.
Edge-case coverage < 8.5: revise.
Test maintainability < 8.5: revise.
Assertion quality < 8.5: revise.
Framework fit < 8.5: revise.
```
