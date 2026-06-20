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

Use recursive search when the field is unclear:

```text
breadth pass: collect diverse candidate papers
depth pass: follow citations, authors, code links, benchmarks
gap pass: search directly for failure modes and limitations
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
why_relevant
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
```

---

# 4. Citation Verification

Before final report:

```text
1. Every cited paper must appear in paper_inventory.tsv.
2. Every BibTeX entry must have a source URL or DOI/arXiv ID.
3. Claims about results must point to a paper section, table, figure, or experiment log.
4. If only metadata/abstract was read, mark it and avoid detailed claims.
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

