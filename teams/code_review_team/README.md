# Code Review Team

`code_review_team` reviews a diff, pull request or repository slice for bugs, security risks, performance issues, maintainability and test gaps.

Use `@team_lead_agent` as the entry point.

## Long Context Handling

For large diffs or repositories, select context around changed files, callers, tests, configs and public contracts. Do not review by reading unrelated files.

## Default Delivery

```text
delivery/review_findings.md
delivery/risk_summary.md
delivery/test_gap_report.md
delivery/suggested_fixes.md
```
