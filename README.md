# Statistics and Data Analysis for Engineers

This repository contains the LaTeX source for *Statistics and Data Analysis
for Engineers*, a practical, Python-oriented textbook designed for the STA1
course at VIA University College.

The book follows the twelve-session STA1 curriculum. Each numbered chapter
corresponds to one taught session, while Appendix A supports the preliminary
Python and data setup material.

## Structure

- Chapters 1–4: data, probability, and probability distributions
- Chapters 5–9: sampling, estimation, tests, and analysis of variance
- Chapters 10–12: regression, categorical data, and integrated analysis
- Appendix A: Python and data setup

The visual design and LaTeX environment system are derived from the
*Mathematics for Software Engineering* book template. The statistical prose,
examples, figures, exercises, and Python material will be original to this
book.

Editorial decisions are recorded in `planning/`: the chapter/session
contract, source map, and course-wide style and notation guide are mirrored
from the STA1 project and must be updated with it when a shared decision
changes.

## Build

A current TeX distribution with `latexmk` and Biber is recommended:

```powershell
latexmk -pdf main.tex
```

The verified `main.pdf` is committed alongside the source so the course
website can link to a stable published PDF. Rebuild and visually inspect it
before every release commit that changes book content.

## Status

Chapter 1, *Data and Descriptive Statistics*, is complete as a first reviewed
draft. It includes a reproducible engineering dataset, Python figures, a
worked analysis, and exercises. The remaining chapters are being developed
and reviewed in four waves: 1–3, 4–6, 7–9, and 10–12.

## Author

Richard Brooks, VIA University College.

## Licence

Copyright © 2026 Richard Brooks. A final licence for source code and book
content will be selected before the first public content release.
