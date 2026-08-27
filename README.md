# Statistics and Data Analysis for Engineers

This repository contains the LaTeX source for *Statistics and Data Analysis
for Engineers*, a theory-oriented textbook for engineering students and
practitioners.

The book develops a coherent progression from descriptive statistics and
probability to statistical inference and integrated data analysis.

## Structure

- Chapters 1–4: data, probability, and probability distributions
- Chapters 5–9: sampling, estimation, tests, and analysis of variance
- Chapters 10–12: regression, categorical data, and integrated analysis

The book combines statistical explanations, definitions, results, derivations,
figures, and worked engineering examples using formulas. Python, tutorials,
and exercises are provided separately on the course website so the textbook
can remain focused on theory and mathematical understanding.

Editorial decisions and source provenance are recorded in `planning/`.

## Build

A current TeX distribution with `latexmk` and Biber is recommended:

```powershell
latexmk -pdf main.tex
```

The verified `main.pdf` is committed alongside the source as the published
edition. Rebuild and visually inspect it before every release commit that
changes book content.

## Status

Chapters 1 and 2 are complete as first reviewed theory drafts with worked
engineering examples. The remaining chapters are being developed
and reviewed in four waves: 1–3, 4–6, 7–9, and 10–12.

## Author

Richard Brooks, VIA University College.

## Licence

Copyright © 2026 Richard Brooks. A final licence for source code and book
content will be selected before the first public content release.
