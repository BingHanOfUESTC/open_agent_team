---
name: research-depth-control
description: Use this skill when auto_research_team needs deeper literature coverage, more citations in paper writing, stronger related-work synthesis, or a gate that prevents shallow research from reaching ideation or LaTeX.
---

# Research Depth Control

This skill raises the research-depth floor for auto research tasks. Use it together with `literature-evidence-mapping` before ideation, before experiment planning, and again before final paper writing.

---

# 1. Depth Targets

Default targets unless Boss narrows the scope:

```text
candidate papers: 30-60
included papers: 15-30
deep-read papers: 8-12
baseline/source papers: 3-6
recent papers: at least 5 from the last 24 months when the field is active
negative/limitation papers: at least 3
code/data/benchmark sources: at least 5 combined
```

For small or niche fields, record why the target cannot be met and list the exact searches that were exhausted.

---

# 2. Four-Pass Search

Run and log four distinct passes:

```text
breadth pass: broad field terms, surveys, benchmark papers, classic baselines
depth pass: citation chasing from top papers, authors, labs, official repos
gap pass: limitations, failure modes, robustness, negative results, open problems
recency pass: latest 6-24 month papers from arXiv/OpenReview/venue pages/Papers With Code
```

Each pass must record:

```text
query
source/index
date searched
number of hits screened
inclusion/exclusion rationale
new papers added
```

Do not stop after a single search engine or a single query phrasing.

---

# 3. Source Stratification

The final paper set should cover these buckets where applicable:

```text
foundational work
strong baseline methods
most recent frontier methods
benchmark/dataset/evaluation papers
reproducibility or implementation sources
failure/limitation/negative evidence
adjacent methods that solve a similar bottleneck
```

If one bucket is empty, explain whether it is irrelevant or still an evidence gap.

---

# 4. Evidence Density Gate

Before idea selection, require:

```text
at least 15 included papers or a documented niche-field exception
at least 8 deep-read evidence cards
at least 3 papers tied to the chosen benchmark/dataset
at least 3 explicit limitations or open problems cited from papers
at least 2 reusable baselines or implementation references
```

Before paper writing, require:

```text
Related Work cites at least 12 papers for a normal ML/CS research report
Introduction cites at least 4 papers spanning motivation, gap, and baseline context
Method cites all directly reused algorithmic components
Experiments cites dataset, metric, benchmark, and baseline sources
Every paragraph in Related Work has at least one citation
Every non-obvious prior-work claim is backed by a BibTeX key in references.bib
```

If the work is a short internal report, Boss may lower the citation target, but the lowered target must be written in `research_workspace/research_state.md`.

---

# 5. Citation Coverage Map

Create:

```text
research_workspace/literature/citation_coverage.md
```

Use this structure:

```markdown
# Citation Coverage

## Coverage Summary
| Bucket | Target | Actual | Status |
|---|---:|---:|---|

## Section Coverage
| Paper Section | Claims Needing Citations | Citation Keys | Missing |
|---|---|---|---|

## Under-Cited Areas

## Papers Excluded From Citation
```

`latex_report_agent` must consult this file before finalizing `main.tex`.

---

# 6. Claim Ledger

Create:

```text
research_workspace/literature/claim_ledger.md
```

Every claim that may enter the paper must be recorded as:

```markdown
## Claim <N>: <short claim>

- Type: background | related_work | method | experiment | limitation
- Support: paper card id, section/table/figure, or experiment id
- Confidence: high | medium | low
- Allowed wording:
- Forbidden wording:
- Citation key or artifact path:
```

Do not use unsupported claims in the final paper.

