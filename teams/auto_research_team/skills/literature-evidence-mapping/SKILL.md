---
name: literature-evidence-mapping
description: Use this skill when discovering papers, mapping related work, reading papers deeply, checking citations, or building evidence cards for an auto research task.
---

# Literature Evidence Mapping

This skill turns search results into research-grade evidence. It should be used before ideation and again before final paper writing.

---

# 1. Search Plan

Write:

```text
research_workspace/literature/search_plan.md
```

Include:

```text
research question
inclusion criteria
exclusion criteria
search queries
venues and indexes
date window
target benchmark or dataset names
```

Use recursive search when the field is unclear or the first pass returns shallow coverage:

```text
breadth pass: collect diverse candidate papers
depth pass: follow citations, authors, code links, benchmarks
gap pass: search directly for failure modes and limitations
recency pass: search the latest arXiv/OpenReview/venue/Papers With Code entries
```

Default depth floor:

```text
screen 30-60 candidate papers
include 15-30 relevant papers
deep-read 8-12 key papers
collect at least 5 recent papers from the last 24 months when available
collect at least 3 limitation/negative-result sources
```

---

# 2. Paper Inventory

Maintain:

```text
research_workspace/literature/paper_inventory.tsv
```

Columns:

```text
id
canonical_key
title
authors
year
venue
url
code_url
data_url
task
method_family
benchmark
result_claim
evidence_level
source_pass
why_relevant
limitations_signal
status
```

Status values:

```text
candidate
included
excluded
deep_read
baseline_source
idea_source
citation_only
```

---

# 3. Evidence Card

For every key paper, write a card under:

```text
research_workspace/literature/cards/<paper_id>.md
```

Template:

```markdown
# <paper title>

- Citation:
- Source URL:
- Code/Data:
- Problem:
- Method:
- Key assumptions:
- Experiments:
- Reported results:
- Limitations stated by authors:
- Limitations inferred by team:
- Relevance to current research:
- What can be reused:
- What should not be assumed:
- Citation key:
- Paper section/table/figure anchors:
- Related-work bucket:
- Claims allowed in paper:
- Claims not supported:
```

Deep-read cards must come from full paper text whenever possible. If only abstract or metadata was available, mark the card as `abstract_only` and do not use it for method details, result comparisons, or limitations beyond the abstract text.

---

# 4. Citation Verification

Before final report:

```text
1. Every cited paper must appear in paper_inventory.tsv.
2. Every BibTeX entry must have a source URL or DOI/arXiv ID.
3. Claims about results must point to a paper section, table, figure, or experiment log.
4. If only metadata/abstract was read, mark it and avoid detailed claims.
5. Related Work should cite at least 12 papers unless Boss explicitly requests a short report or the field is too narrow.
6. Each Related Work paragraph needs at least one citation.
7. The paper must cite dataset, benchmark, metric, and reused implementation sources where applicable.
```

Never invent missing BibTeX. If metadata is incomplete, use a placeholder note in the report draft and resolve before final delivery.

---

# 5. Gap Map

Write:

```text
research_workspace/literature/gap_map.md
```

Organize by:

```text
problem gap
method gap
data gap
evaluation gap
efficiency gap
robustness gap
reproducibility gap
```

Each gap must cite evidence and include a possible experiment.

Also write:

```text
research_workspace/literature/citation_coverage.md
research_workspace/literature/claim_ledger.md
```

Use `citation_coverage.md` to track whether the final paper has enough references by section and topic bucket. Use `claim_ledger.md` to prevent unsupported claims from entering the paper.
