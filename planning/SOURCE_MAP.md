# Source map: *Statistics and Data Analysis for Engineers*

## Purpose

This is the editorial source map shared by the STA1 website and the planned textbook *Statistics and Data Analysis for Engineers*. It records what each chapter/session must cover, where the reusable material lives, and which sources are used only for verification or inspiration.

The book and course site must not drift apart. A scope change is first recorded here and in `planning/CHAPTER_SESSION_CONTRACT.md`, then applied to both artifacts.

## Authority and reuse

Use sources in this order:

1. The official STA1 course description and approved learning outcomes.
2. The frozen chapter/session contract in this repository.
3. Correct statistical theory, cross-checked against Ross and another authoritative source where necessary.
4. Brooks-authored material in `MSE_book_v2`, `STA_26`, `SMP1_25`, and `STA1_26`.
5. Newly written theoretical explanations, derivations, worked examples, tutorial material, assignments, and project material.

Ross is a scope and verification source. Do not copy its prose, figures, examples, or exercises. Brooks-authored material may be revised and reused, but it must still be checked for correctness, notation, level, and fit with the new course.

Existing STA1 tutorials and notebooks are inputs, not curriculum authorities.
They may be reorganised, replaced, or rewritten when the MSE book, another
Brooks-authored example, or a newly designed example gives a clearer and more
correct learning progression. The final tutorial must follow the reviewed
textbook chapter and session contract, not constrain them.

## Structural correspondence

| Course item | Textbook item |
| --- | --- |
| Session 01 | Chapter 1 — Data and Descriptive Statistics |
| Session 02 | Chapter 2 — Probability for Data Analysis |
| Session 03 | Chapter 3 — Random Variables and Discrete Distributions |
| Session 04 | Chapter 4 — Continuous Distributions in Practice |
| Session 05 | Chapter 5 — Sampling Distributions and the Central Limit Theorem |
| Session 06 | Chapter 6 — Estimation and Confidence Intervals |
| Session 07 | Chapter 7 — Hypothesis Testing I: Principles and One-Sample Tests |
| Session 08 | Chapter 8 — Hypothesis Testing II: Comparing Two Groups |
| Session 09 | Chapter 9 — Analysis of Variance |
| Session 10 | Chapter 10 — Simple Linear Regression |
| Session 11 | Chapter 11 — Categorical Data and Chi-Square Tests |
| Session 12 | Chapter 12 — Integrated Statistical Analysis and Exam Preparation |

## Chapter sources

### Website self-study 00 — Python and Data Setup

- **STA1:** `00_Getting_Started_with_Python_and_Data/README.md`, `pages/conventions.md`, `pages/datasets.md`
- **Purpose:** environment setup, reproducibility, data paths, core packages, notebook and reporting workflow
- **Boundary:** installation and programming details belong on the website and are not part of the textbook

### Chapter 1 — Data and Descriptive Statistics

- **STA1:** `01_Data_and_Descriptive_Statistics/README.md`, `Tutorial_01.md`, dataset `sensor_thickness.csv`
- **MSE:** `MSE_book_v2/chapter06.tex`
- **Old STA:** `01_Repetition_af_sandsynlighedsteori_og_stokastiske_variable/Tutorial_1.md`
- **Session notes:** [STA 01](https://drive.google.com/file/d/1D20cFjJA9CmBZQGu_rESr4u4jqoc_x7a/view?usp=sharing), used selectively
- **Ross check:** 1.2–1.4 and 2.1–2.3
- **Core:** populations and samples; data types; summaries; sample versus population variance; histograms, boxplots, scatterplots, shape and outliers
- **Reuse decision:** the textbook chapter is a direct reuse of `MSE_book_v2/chapter06.tex`, including its tables, graphs, grouped-data treatment, ogives, computational variance formula, coefficient of variation, normal and skewed data, outlier detection, and boxplots
- **Draft status:** complete theory-first textbook chapter; statistical software is mentioned only as the normal practical tool for producing summaries and plots, while all code remains tutorial-only
- **Editorial departures from MSE Chapter 6:** removes the Law of Large Numbers and empirical-rule material; retains a descriptive introduction to normal data and the normal curve, with the mathematical model deferred by cross-reference to Chapter 4; adapts only chapter labels, STA colour names, transitions to later chapters, and minor wording needed for this standalone book
- **Reference convention:** all internal references use `\autoref` so the complete phrase, such as `Figure 1.5`, is clickable

### Chapter 2 — Probability for Data Analysis

- **STA1:** `02_Probability_for_Data_Analysis/README.md`, `Tutorial_02.md`
- **MSE:** `MSE_book_v2/chapter04.tex` and `chapter05.tex` are the canonical source and are reused directly
- **Session notes:** [STA 01](https://drive.google.com/file/d/1D20cFjJA9CmBZQGu_rESr4u4jqoc_x7a/view?usp=sharing), [SMP 01](https://drive.google.com/file/d/1oqEy7sINksGCfdytv_O8qIZ0FoVEyWjz/view?usp=drive_link)
- **Ross check:** 3.1–3.4 and 3.6–3.8
- **Core:** random experiments, sample spaces and events; basic probability; joint events and set operations; conditional probability; multiplication and total probability rules; independence; and Bayes' theorem
- **Boundary:** no standalone combinatorics catalogue; joint-distribution theory remains in SMP1
- **Draft status:** complete theory-first chapter copied from the relevant MSE material; Python remains tutorial-only
- **Editorial departures from MSE Chapters 4–5:** adds an original chapter introduction motivated by the Monty Hall problem and Bayes' theorem; omits the whole `Counting Principles` section; renames the opening section to `Random Experiments, Sample Spaces, and Events`; adapts named examples to the STA-book title convention; uses `\autoref` for complete clickable references; and replaces the single Python-file context with an equivalent JavaScript-file context to preserve the theory-only policy
- **Section order:** 2.1 Random Experiments, Sample Spaces, and Events; 2.2 Basic Probability; 2.3 Probability of Joint Events and Set Operations; 2.4 Conditional Probability; 2.5 Multiplication and Total Probability Rules; 2.6 Independence; 2.7 Bayes' Theorem

### Chapter 3 — Random Variables and Discrete Distributions

- **STA1:** `03_Random_Variables_and_Discrete_Distributions/README.md`, `Tutorial_03.md`, dataset `packet_loss.csv`
- **Old STA:** sessions 02–03 and their tutorials
- **Session notes:** [STA 02](https://drive.google.com/file/d/1azFhbhkKSIiLboKuxTlyhh-41jYMtbRm/view?usp=sharing), [STA 03](https://drive.google.com/file/d/1laRKIxHLa2DBjmzVMQuKyc6vilaPrFNx/view?usp=sharing), [SMP 02](https://drive.google.com/file/d/1LJ8Nu0D1PLLB1FF1jTsLK50HGLhl1EtG/view?usp=sharing)
- **Ross check:** 4.1–4.2, 4.4, 4.6, 5.1–5.2; optional parts of 5.3
- **Core:** random variables, PMF, CDF, expectation, variance, Bernoulli, binomial and Poisson; statistical software is mentioned generically for numerical evaluation, while SciPy and simulation remain tutorial-only on the course website
- **Boundary:** geometric, negative binomial and hypergeometric are enrichment; no MGFs or multivariate theory
- **Draft status:** complete theory-first textbook chapter, including its concluding synthesis and transition to continuous models
- **Example coverage so far:** components and inspection cost, cybersecurity alerts and rare incidents, production defects and panel flaws, software packet loss and service failures, supply-chain delays and urgent orders, structural fastener tests, climate exceedances and flood warnings, and mechanical sampling without replacement

### Chapter 4 — Continuous Distributions in Practice

- **STA1:** `04_Continuous_Distributions_in_Practice/README.md`, `Tutorial_04.md`, datasets `response_times.csv` and `component_lifetimes.csv`
- **Old STA:** sessions 04–05 and their tutorials
- **Session notes:** [STA 04](https://drive.google.com/file/d/1hfivT-AFbsnR9CxJeff-K2dTC7MC-HPZ/view?usp=sharing), [STA 05](https://drive.google.com/file/d/1qTGWWIihQLTLNe0e-0nUwGIbpkH7XWkS/view?usp=sharing), [SMP 03](https://drive.google.com/file/d/1-MKzwovM7uHrSUQ_XBe1NczVT2ssdbKd/view?usp=sharing)
- **Ross check:** 4.2, selected results from 4.4 and 4.6, and 5.4–5.6
- **Core:** continuous support, PDF, CDF, survival function, quantiles, uniform, normal and exponential models, standardisation, cumulative standard normal tables, the empirical rule, memorylessness, the practical Poisson-count/exponential-waiting-time connection, model choice and QQ-plots
- **Boundary:** calculus is limited to the three conceptual integral forms needed to interpret a density: total area, interval probability, and accumulated CDF area; students do not integrate densities by hand, and continuous-moment integrals and their derivations are omitted
- **Draft status:** complete theory-first textbook chapter in five sections; Python remains tutorial-only
- **Example coverage:** measurement resolution, maintenance time, supply-chain delivery windows, calibration error, machined shaft diameters, voltage thresholds, standard normal table lookups, server-request waiting times, electronic-component lifetimes, network traffic and response-time QQ diagnostics

### Chapter 5 — Sampling Distributions and the Central Limit Theorem

- **STA1:** `05_Sampling_Distributions_and_the_CLT/README.md`, `Tutorial_05.md`
- **Old STA:** session 06 and its tutorial
- **Session notes:** [STA 06](https://drive.google.com/file/d/1YQHZe0Ukj0Jkhn3vTrjLkFKJfVwcWUOg/view?usp=sharing)
- **Ross check:** 6.1–6.3 and selected parts of 6.4–6.5
- **Core:** i.i.d. random samples; statistics as random variables; population, observed-sample and sampling distributions; exact and approximate sampling distributions of the mean; standard error; sums and sample proportions; the law of large numbers; the central limit theorem; the sample variance; and the normal-population results leading through chi-square to Student's (t)
- **Boundary:** no proofs, moment-generating functions, finite-population correction, technical convergence theory, bootstrap methods, or software code; simulation belongs in the tutorial and is used to illustrate rather than justify assumptions
- **Critical checks:** write the sample-mean distribution as `N(mu, sigma^2/n)`, distinguish exact normal sampling from a CLT approximation, never claim that the CLT makes raw data normal, and do not use a universal `n >= 30` rule
- **Draft status:** complete theory-first chapter in four sections; Chapter 5 is the active isolated PDF build
- **Example coverage:** production sampling, exact discrete repeated sampling, plate thickness, vibration precision, cyber-alert proportions, skewed server response times, road-salt capacity, process variance, and battery capacity

### Chapter 6 — Estimation and Confidence Intervals

- **STA1:** `06_Estimation_and_Confidence_Intervals/README.md`, `Tutorial_06.md`
- **Old STA:** session 07 and its tutorial
- **Session notes:** [STA 07](https://drive.google.com/file/d/1HV1sbPdtBIYqaGUiHVdnnVXospCYBhAK/view?usp=sharing), [SMP 06](https://drive.google.com/file/d/1EFr1Pz5E2lyVtgxd2Lwj9O4SdvcyXw_x/view?usp=sharing)
- **Ross check:** 7.1, 7.3 and 7.5; defer 7.4 to Chapter 8
- **Core:** estimator versus estimate; bias and precision; confidence level, margin of error, and repeated-sampling coverage; z- and t-intervals for one population mean; sample-size planning; Wald and Wilson intervals for one population proportion; and responsible interpretation
- **Boundary:** no proofs, maximum likelihood, Bayesian intervals, intervals for a variance, prediction intervals, or two-sample intervals; no software code in the textbook
- **Enrichment:** bootstrap resampling is introduced conceptually at the end of the chapter and implemented only in the practical tutorial
- **Critical checks:** the parameter is fixed while the interval procedure is random; a realised 95% interval is not assigned probability 0.95; Wilson is the practical default for proportions while Wald is retained to explain the normal approximation
- **Draft status:** complete theory-first chapter in five sections; Chapter 6 is the active isolated PDF build
- **Example coverage:** service monitoring, sensor calibration, combined sensor readings, laboratory coverage, concrete strength, parallel-computing speedup, vibration-study planning, authentication alerts, rare manufacturing defects, and energy reduction

### Chapter 7 — Hypothesis Testing I

- **STA1:** `07_Hypothesis_Testing_I_Principles_and_One_Sample_Tests/README.md`, `Tutorial_07.md`
- **Old STA:** one-sample portions of session 08 and `Tutorial_8.md`
- **Session notes:** [STA 08](https://drive.google.com/file/d/1Ji4laf6gU06-unx-QhclQupT4u9OePUA/view?usp=sharing), [SMP 07](https://drive.google.com/file/d/1sIXa8DCVkjguV8dHwXPTtPZiQKLZsc-o/view?usp=sharing)
- **Ross check:** 8.1–8.3 and the one-sample part of 8.6
- **Core:** hypotheses, one- and two-sided alternatives, alpha, test statistics, p-values, type I/II errors, intuitive power, one-sample z/t tests, formal normality assessment using Shapiro--Wilk together with Q--Q plots and Anderson--Darling as an alternative, score and exact binomial tests for one proportion, confidence-interval/test duality, and practical versus statistical significance
- **Boundary:** no proofs, software code, formal power-curve calculations, equivalence testing, Bayesian hypothesis probabilities, two-sample methods, or multiple-testing procedures; those topics are either outside scope or developed later
- **Critical language:** never define a p-value as `P(H0 | data)`; use “fail to reject,” not “accept”; report effect magnitude and a matching confidence interval where useful; and distinguish the nominal alpha level from the possibly smaller realised size of a discrete exact test
- **Draft status:** complete theory-first chapter in five sections; Chapter 7 is the active isolated PDF build
- **Example coverage:** structural fasteners, process design and sampling validity, sensor calibration, cybersecurity incident response, laboratory concentration, machining tolerances, server response time, automated production inspection, safety-interlock failures, and climate-sensor calibration

### Chapter 8 — Hypothesis Testing II

- **Draft status:** complete theory-first chapter in five sections; Chapters 5
  and 8 are the active review build
- **STA1:** `08_Hypothesis_Testing_II_Comparing_Two_Groups/README.md`, `Tutorial_08.md`, dataset `response_times.csv`
- **Old STA:** two-sample and paired portions of session 08 and `Tutorial_8.md`
- **Session notes:** [STA 08](https://drive.google.com/file/d/1Ji4laf6gU06-unx-QhclQupT4u9OePUA/view?usp=sharing), [SMP 07](https://drive.google.com/file/d/1sIXa8DCVkjguV8dHwXPTtPZiQKLZsc-o/view?usp=sharing)
- **Ross check:** 7.4, 8.4 and the two-sample part of 8.6
- **Core:** study-design expansion, observational versus randomised comparisons,
  independent versus paired designs, Welch t-test, paired t-test, independent
  two-proportion inference, confidence intervals and effect measures
- **Design rule:** determine the sampling design before selecting a Python function
- **Boundary:** no proofs, software code, standalone variance tests, paired
  binary procedures, equivalence testing, or multiple-group comparisons

### Chapter 9 — Analysis of Variance

- **STA1:** `09_Analysis_of_Variance/README.md`, `Tutorial_09.md`, datasets `resin_impurities.xlsx` and `scope_filter_intensity.xlsx`
- **Old STA:** `10_Variansanalyse_ANOVA/README.md` and tutorial/site exercises
- **Ross check:** 10.1–10.3
- **Core:** family-wise type I error, one-way ANOVA, between/within variation, F-statistic, assumptions, diagnostics and Tukey HSD
- **New work:** the old course has no separate session-notes PDF; this chapter requires substantial new prose, examples, and figures
- **Boundary:** no two-way ANOVA or interactions in core STA1

### Chapter 10 — Simple Linear Regression

- **STA1:** `10_Simple_Linear_Regression/README.md`, `Tutorial_10.md`, `Calculating_metrics.md`, dataset `energy_load.csv`
- **Old STA:** session 09 and `Tutorial_9.md`
- **Old SMP:** session 08 and `Calculating_metrics.md`
- **Session notes:** [STA 09](https://drive.google.com/file/d/155VOAnrutze7091LObcAhAcnau__uBl1/view?usp=sharing), [SMP 08](https://drive.google.com/file/d/1N_hUEd6Hwn93dVtaSWHsFqe9N47E2WRg/view?usp=sharing)
- **Ross check:** 9.1–9.2 and 9.4–9.6
- **Core:** study design and scatterplots, least squares, coefficient interpretation, residual standard deviation, correlation, R-squared, slope inference, residual diagnostics, conceptual leverage and influence, and confidence versus prediction intervals
- **Python:** Statsmodels for estimation, inference and diagnostics; machine-learning workflows and scikit-learn are outside the core chapter and session

### Chapter 11 — Categorical Data and Chi-Square Tests

- **STA1:** `11_Categorical_Data_and_Chi_Square_Tests/README.md`, `Tutorial_11.md`, dataset `defect_types.csv`
- **Old STA:** `10_Goodness_of_fit_og_analyse_af_kategoriske_data/README.md` and tutorial/site exercises
- **Ross check:** 11.1–11.4
- **Core:** counts and conditional proportions; fully specified and
  estimated-parameter goodness of fit; pooling and Monte Carlo assessment;
  independence versus homogeneity; expected counts and degrees of freedom;
  Pearson and adjusted standardised residuals; Cramer's V; and sparse-table
  alternatives; explicitly connect squared standardised count discrepancies
  with the chi-square distribution introduced for sample variance
- **New work:** there is no separate old session-notes PDF; create a coherent textbook narrative and original engineering examples

### Chapter 12 — Integrated Statistical Analysis and Exam Preparation

- **STA1:** `12_Integrated_Analysis_and_Exam_Preparation/README.md`, `Tutorial_12.md`, `pages/assignments.md`, `pages/project.md`
- **Inputs:** selected datasets and examples from Chapters 1–11
- **Core:** question, data audit, visualisation, method choice, assumptions, estimates, uncertainty, conclusion and recommendation
- **Boundary:** exam instructions stay on the course site; the book chapter teaches a reusable workflow

## SMP material outside STA1 core

- [SMP multivariate notes](https://drive.google.com/file/d/1oUHWdzQZa62bTqsmLe_eRts7OpOEhFgJ/view?usp=sharing) may support intuitive covariance/correlation explanations.
- Stochastic processes, Markov chains, joint densities, transformations and MGFs are not STA1 textbook chapters.
- Calculus-heavy derivations from SMP must not migrate into the practical STA1 treatment.

## Required per-chapter source package

Before drafting a chapter, record:

- official learning outcome and session outcome;
- primary Brooks-authored sources;
- Ross verification sections;
- dataset, units, provenance and licence;
- definitions and results to include;
- tutorial-only Python functions and conventions, kept outside the textbook;
- worked engineering example;
- assignment/project connection;
- known gaps and disputed points;
- completed mathematical, computational and copyright checks.

## Known gaps

1. ANOVA and categorical analysis require the most new textbook writing.
2. Old hypothesis-testing material must be divided cleanly between Chapters 7 and 8.
3. MSE probability Chapters 4–5 are reused directly, with only the counting-principles section omitted and the agreed house-style adaptations applied.
4. Continuous-distribution explanations must be rewritten without manual integration.
5. The assessment pages intentionally remain placeholders until the six assignments and group project are designed.
6. Every reused example must be checked for units, assumptions, notation, licensing, and alignment with the theory-first textbook style; Python belongs in tutorials.
