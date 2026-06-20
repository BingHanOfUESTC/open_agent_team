---
name: latex-paper-artifact
description: Use this skill when producing the final arXiv-style LaTeX paper, BibTeX, figures, tables, reproducibility statement, appendix, and artifact manifest.
---

# LaTeX Paper Artifact

This skill turns the research process into a paper-style deliverable and a reproducible artifact package.

---

# 1. Paper Directory

Create:

```text
research_workspace/reports/paper/main.tex
research_workspace/reports/paper/references.bib
research_workspace/reports/paper/figures/
research_workspace/reports/paper/tables/
research_workspace/reports/paper/scripts/
```

Use a compact arXiv-style `article` layout unless Boss specifies a venue template.

---

# 2. Required Sections

`main.tex` must include:

```text
abstract
introduction
related work
method
experiments
conclusion
```

Recommended:

```text
limitations
reproducibility statement
ethics or broader impact when relevant
appendix
```

---

# 3. Claim Discipline

For every core claim, identify its backing:

```text
literature evidence card
experiment id
result table row
figure script
documented limitation
```

Do not write:

```text
state-of-the-art
significant improvement
robustly outperforms
proves
```

unless the experiment design and evidence actually support the claim.

---

# 4. Figures and Tables

Generate plots from scripts:

```text
research_workspace/reports/paper/scripts/make_<figure>.py
```

Every figure/table caption should state:

```text
what is measured
dataset/split
number of seeds if available
source file or experiment id
main takeaway
```

---

# 5. Compilation and Delivery

Try:

```bash
latexmk -pdf main.tex
```

or a locally available equivalent. If LaTeX is unavailable, record the missing tool and still deliver source files.

Final delivery must include:

```text
paper source path
PDF path or compile failure reason
BibTeX source
figure scripts
artifact manifest
reproduction guide
known limitations
```

