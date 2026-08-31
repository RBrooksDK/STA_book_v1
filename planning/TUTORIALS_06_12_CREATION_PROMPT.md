# Creation and revision prompt for STA1 Tutorials 6--12

Use the following prompt in a coding agent that can access both repositories.

---

You are rebuilding Tutorials 6--12 for STA1, a practical, Python-oriented introductory statistics course for engineering students.

## Repositories and sources of truth

- Course site: `C:\GitHub\STA1_26`
- Theory textbook: `C:\GitHub\STA_book_v1`
- Course planning and conventions:
  - `C:\GitHub\STA1_26\planning\CHAPTER_SESSION_CONTRACT.md`
  - `C:\GitHub\STA1_26\planning\STYLE_AND_NOTATION.md`
  - `C:\GitHub\STA_book_v1\planning\CHAPTER_SESSION_CONTRACT.md`
  - `C:\GitHub\STA_book_v1\planning\STYLE_AND_NOTATION.md`

Tutorial files in scope:

- `06_Estimation_and_Confidence_Intervals/Tutorial_06.md`
- `06_Estimation_and_Confidence_Intervals/Tutorial_06_notebook.ipynb`
- `07_Hypothesis_Testing_I_Principles_and_One_Sample_Tests/Tutorial_07.md`
- `07_Hypothesis_Testing_I_Principles_and_One_Sample_Tests/Tutorial_07_notebook.ipynb`
- `08_Hypothesis_Testing_II_Comparing_Two_Groups/Tutorial_08.md`
- `08_Hypothesis_Testing_II_Comparing_Two_Groups/Tutorial_08_notebook.ipynb`
- `09_Analysis_of_Variance/Tutorial_09.md`
- `09_Analysis_of_Variance/Tutorial_09_notebook.ipynb`
- `10_Simple_Linear_Regression/Tutorial_10.md`
- `10_Simple_Linear_Regression/Tutorial_10_notebook.ipynb`
- `11_Categorical_Data_and_Chi_Square_Tests/Tutorial_11.md`
- `11_Categorical_Data_and_Chi_Square_Tests/Tutorial_11_notebook.ipynb`
- `12_Integrated_Analysis_and_Exam_Preparation/Tutorial_12.md`
- `12_Integrated_Analysis_and_Exam_Preparation/Tutorial_12_notebook.ipynb`

Before editing, inspect `git status` in both repositories and preserve all unrelated work. Read the complete current Session 06--12 `README.md` files and the complete textbook sources `chapter06.tex` through `chapter12.tex`. Do not rely only on the current local `main.pdf`, because it may be a temporary single-chapter review build.

The textbook source is authoritative for theory, terminology, notation, assumptions, distinctions, and mathematical claims. The session pages are authoritative for teaching scope and learning objectives. The existing tutorials are drafts and useful raw material, but they are not authoritative when they conflict with the textbook or the teaching design below.

Do not edit the textbook. Do not change the 12-session structure. Do not create the final-project assignment brief in this task. Do not commit, push, or deploy unless explicitly asked after instructor review.

## Course and tutorial design

STA1 is deliberately practical. The textbook is the theory layer; the tutorials are the Python and interpretation layer. SMP is the more mathematically advanced probability course. Tutorials must therefore help students perform, diagnose, interpret, and report statistical analyses without repeating long derivations or turning into exercise sheets.

Apply these principles to Tutorials 6--12:

1. Build each tutorial as one coherent engineering investigation: question, observational units and design, data audit, descriptive evidence, justified method, computation, diagnostics, interpretation, limitations, and conclusion.
2. Keep the practical workload realistic for approximately 60--90 minutes. Prefer one case studied carefully over several disconnected demonstrations.
3. Refer students to the corresponding Brooks chapter for full theory. Retain only the formulas needed to understand the Python results.
4. Begin method choice with the statistical question, target population, observational unit, variable types, and data structure. Never select a test merely because a software function is available.
5. Treat independence, representative sampling, random assignment, pairing, clustering, and time order as design questions. A histogram, QQ-plot, or normality test cannot establish independence or representativeness.
6. Distinguish observed facts from model assumptions. Diagnostics reveal discrepancies; they do not certify that a model is true.
7. Report effect magnitude in engineering units whenever possible. A small p-value is not a measure of effect size or practical importance.
8. Report estimates and suitable confidence intervals alongside tests. Do not reduce an analysis to a reject/fail-to-reject decision.
9. Define comparison order and one-sided or two-sided direction before viewing the result. Keep that order consistent in code, tables, intervals, and prose.
10. Use precise p-value language. A p-value is the probability, conditional on the null hypothesis and the model assumptions, of obtaining the observed test statistic or one more extreme in the direction specified by the alternative. It is not `P(H0 | data)` and not the probability that the result occurred "by chance."
11. Use "fail to reject" rather than "accept" the null hypothesis. A non-significant result does not prove equality or no effect.
12. Distinguish statistical significance, practical significance, and causal interpretation. Causal language requires a design that supports it.
13. Use uppercase notation for random variables and statistics and lowercase for realised values, for example `X` versus `x` and `\bar X` versus `\bar x`.
14. Use the textbook's parameterisations and naming consistently. Retain units in tables, plots, estimates, and conclusions.
15. Use `numpy.random.default_rng(2026)` for every new simulation or generated dataset. Avoid global `np.random.seed` and unexplained randomness.
16. Prefer clear NumPy, pandas, Matplotlib, SciPy, and statsmodels code. Do not hide the statistical reasoning in unnecessarily advanced code.
17. Label every plot with the measured quantity and unit. Use the existing visual palette where practical: VIA blue `#6CA2C6` and orange `#FF8C00`.
18. A software summary is evidence to interpret, not a conclusion. Extract, label, and explain the important estimate, standard error, interval, statistic, degrees of freedom, and p-value.
19. Do not add ordinary exercise sets. Short prediction questions, interpretation pauses, and small "before running this cell" prompts are welcome inside a guided lab.
20. Keep each Markdown tutorial and notebook semantically identical. The notebook may split material into cells and contain executed outputs, but it must not contain different data, claims, examples, or conclusions.
21. Use `tools/md_to_notebook.py` where appropriate so the Markdown tutorial remains the maintainable source, then execute and validate the generated notebook.
22. Do not use absolute local data paths. Data must resolve when running from the repository root and when opening the notebook from its session directory.
23. Do not introduce proofs. The practical material may explain formulas but should not duplicate the book's theoretical development.
24. Do not repeat claims that `n=30` is a universal adequacy threshold or that a formal normality test is a mechanical pass/fail gate.

## Fixed final-project constraints

Tutorial 12 must prepare students for a final group project with these fixed requirements. Do not silently change, weaken, or add to them:

- Submission deadline: **June 1**.
- Group size: **2--4 students**.
- Any deviation from the group-size rule must be discussed with **R. Brooks before the final session, Session 12**.
- Workload: **25 hours per student**.
- Submission format: **one Jupyter notebook**.
- Explanations, reasoning, interpretation, and conclusions must be written in notebook Markdown cells; Python must be placed in code cells.
- Every code cell must be executed before submission so all relevant output, tables, and figures are visible.
- The analysis must include at least **three statistical methods from three different sessions or textbook chapters**, excluding Chapter/Session 12.
- Every selected method must answer a stated question and contribute to one coherent engineering investigation. The requirement must not be met by attaching unrelated tests to the same notebook.
- The project must comply with the analysis principles in **Brooks, Chapter 12** and **Tutorial 12**.
- The project is discussed during the exam. It is not graded separately, but it contributes to the overall course grade.
- The same assessment principle applies to all six assignments: they are not separately graded, but form part of the overall exam basis and grade.

These rules should shape Tutorial 12 and its planning checklist. Do not write the detailed project brief, assessment rubric, or submission page yet; that will be a separate task.

## Required work by tutorial

### Tutorial 6 -- Estimation and confidence intervals

Revision level: substantial.

Use Chapter 6 as the source of truth. The tutorial should move from a point estimate to standard error, interval precision, repeated-sampling coverage, and a responsible engineering interpretation.

Required content:

- Distinguish estimator from realised estimate and introduce bias briefly and practically. Bias is important, but it must not dominate this course.
- Build a t interval for one population mean when sigma is unknown. Show the estimate, sample SD, standard error, critical value, margin of error, and interval before verifying with SciPy.
- Mention the z interval only in the setting where population sigma is genuinely known. Do not use z merely because the sample is large.
- Use a vectorised repeated-sampling simulation from a known model to illustrate 95% coverage. Keep the parameter fixed and vary the interval from sample to sample.
- State precisely that 95% describes the long-run coverage of the procedure, not a 0.95 probability assigned to the parameter after observing one interval.
- Show how interval width changes with sample size, confidence level, and variability. Do not imply that more data repair bias, dependence, or invalid measurement.
- Construct an interval for one population proportion using the Wilson interval as the practical default. The Wald interval may be shown briefly to demonstrate why it can fail near 0 or 1 or with small samples, but it must not be presented as the recommended interval.
- Use a method-consistent tool such as `statsmodels.stats.proportion.proportion_confint(..., method="wilson")`, or implement and verify the Wilson formula transparently.
- Retain a short bootstrap percentile interval as a computational extension. Explain that bootstrap resampling approximates sampling variation from the observed sample; it does not create new information or repair a biased sample.
- Clearly distinguish a confidence interval for a population mean from the variation of individual observations.
- End with a compact report containing the estimate, interval, population, units, assumptions, practical context, and limitations.

Do not let the bootstrap replace the core t and Wilson procedures. Use one principal dataset and one coherent engineering context.

### Tutorial 7 -- Hypothesis testing I: principles and one-sample tests

Revision level: substantial.

Use Chapter 7 as the source of truth. This tutorial must make the logic and interpretation of testing clearer than the current draft.

Required content:

- Begin with a real specification or decision threshold and write `H0` and `H1` in notation and contextual language.
- Distinguish a two-sided departure from a one-sided engineering concern. Fix the alternative before examining the sample result.
- Compute a one-sample t statistic manually from the estimate and standard error, then verify it with `scipy.stats.ttest_1samp` using `alternative=` explicitly.
- Include a visual or computational illustration of the p-value as a tail probability under the null model. The prose and formula must condition on `H0` and the model assumptions.
- Report the observed mean, difference from the null value, confidence interval, t statistic, degrees of freedom, p-value, and practical threshold together.
- Demonstrate the matching decision between a two-sided t test and t confidence interval.
- Include an assumption workflow: data/design audit, a plot of observations, a QQ-plot, and a formal normality assessment such as Shapiro--Wilk. Explain that the formal test is supplementary, may have low power in small samples or detect immaterial departures in large samples, and does not test independence.
- Do not use a chi-square test as the normality test. Chapter 7's QQ-plot and Shapiro--Wilk/Anderson--Darling discussion is the relevant source.
- Include one population-proportion question. Demonstrate the exact binomial test where discreteness or small counts matter and the score/Wilson approach for an adequate large-sample setting. Do not mix an exact test with a Wilson interval and claim exact test-interval duality.
- Explain type I error, type II error, and power briefly through the decision context or a compact simulation, without turning the tutorial into a power-analysis chapter.
- End with the Chapter 7 reporting order: target population and parameter, hypotheses and direction, design and sample size, estimate and interval, statistic/df/p-value, decision, effect magnitude, practical consequence, and limitations.

Remove every statement that treats the p-value as `P(H0 | data)`, says the null is accepted, or interprets non-significance as equality.

### Tutorial 8 -- Hypothesis testing II: comparing two groups

Revision level: major rebuild.

Use Chapter 8 as the source of truth. The relationship between the observations must determine the method.

Required content:

- Start by identifying observational units and deciding whether the comparison is independent or paired. Two columns do not by themselves establish either design.
- Distinguish random sampling from random assignment and state what the design supports: sample description, population generalisation, association, or causation.
- For two independent quantitative groups, use Welch's procedure as the default. Do not run a preliminary Levene test to decide automatically between pooled and Welch analyses.
- Report the ordered mean difference in original units with a Welch confidence interval, test statistic, Welch--Satterthwaite degrees of freedom, and p-value.
- For paired measurements, compute the within-pair differences explicitly, plot or summarise them, and show that the paired t procedure is a one-sample analysis of those differences. Report a confidence interval for the mean paired difference.
- Explain why pairing unrelated observations is invalid and why analysing genuine pairs as independent discards design information.
- Include a comparison of two independent proportions. A natural option is to derive an SLA-failure indicator from the two independent response-time samples, provided the threshold is justified before inspecting the results.
- For the proportion comparison, report the absolute risk/proportion difference and interval. Add relative risk when useful and label it correctly. Do not confuse an odds ratio with a relative risk.
- Prefer unstandardised differences in milliseconds, kWh, percentage points, or other engineering units. Cohen's d may be an optional supplement but must not replace the raw difference and its interval.
- Do not test each group separately and compare significance decisions. Test or estimate the group difference directly.
- End with the six-step analysis order from Chapter 8 and separate statistical evidence from practical importance.

Use the existing response-time data if they support a coherent independent, paired, and binary comparison. Do not introduce a second unrelated dataset merely to add another function call.

### Tutorial 9 -- Analysis of variance

Revision level: substantial.

Use Chapter 9 as the source of truth. Build one coherent supplier or process comparison around a quantitative response and one categorical factor.

Required content:

- Explain why a collection of unadjusted pairwise t tests is a poor default for three or more groups.
- State the global hypotheses correctly: all population means are equal versus at least one differs.
- Begin with group sample sizes, means, SDs, and a labelled boxplot or point-based group plot.
- Fit a one-way model and show a readable ANOVA table with sums of squares, degrees of freedom, mean squares, F statistic, and p-value. Connect F to between-group relative to within-group variation without repeating the full derivation.
- Treat independence and study design as primary assumptions. Diagnose approximate within-group error shape and common spread using group plots, residual plots, and a QQ-plot of residuals, not a QQ-plot of the pooled raw response.
- Do not use a preliminary variance test as an automatic switch. Discuss sample sizes, group spreads, design, and plots together.
- Use classical one-way ANOVA when the common-variance model is credible. Mention or demonstrate Welch's one-way ANOVA as the practical alternative when independent groups have materially unequal variances.
- Do not combine Welch's ANOVA automatically with ordinary Tukey intervals. If unequal-variance pairwise follow-up is included, use a compatible approach such as Games--Howell and verify library support.
- After a relevant significant classical omnibus test, use Tukey HSD to identify pairwise differences with multiplicity-adjusted p-values and simultaneous confidence intervals.
- Calculate and interpret eta-squared as a descriptive effect magnitude. Do not interpret it as causation or the probability that the factor determines an observation.
- Report group differences in original engineering units and state explicitly that a non-significant pairwise result does not establish equal means.
- End with the seven-step Chapter 9 analysis order and a compact engineering conclusion.

Use one main dataset. Remove the second disconnected example unless it serves a clearly labelled, short robustness comparison.

### Tutorial 10 -- Simple linear regression from a statistical perspective

Revision level: complete conceptual rebuild.

Use Chapter 10 as the source of truth. This is a statistics tutorial, not a machine-learning tutorial and not a linear-algebra tutorial.

Required content:

- Remove scikit-learn, train/test splitting, prediction-model comparison, and machine-learning framing from the tutorial.
- Use statsmodels for fitting, inference, diagnostics, confidence intervals, and prediction intervals.
- Begin with the engineering question and a scatterplot. Identify the quantitative response, quantitative predictor, observational unit, target population, and observed predictor range.
- State the conditional-mean model `Y = beta0 + beta1 x + epsilon` and explain fitted values and residuals in context.
- Interpret the slope in response units per predictor unit. Interpret the intercept only when `x=0` is meaningful and supported by the observed range.
- Explain Pearson correlation carefully: direction and strength of linear association, range from -1 to 1, sensitivity to outliers and nonlinearity, no universal threshold for "strong," and no causal interpretation from correlation alone.
- Explain the coefficient of determination carefully: the fraction of observed squared response variation around the sample mean accounted for by the fitted line. It is not the probability that the model is correct, not causation, and not a universal measure of prediction quality.
- Verify that `R^2 = r^2` for simple linear regression with an intercept and explain the conditions under which that identity applies.
- Report the least-squares line, residual standard deviation, slope estimate, standard error, confidence interval, t statistic, and p-value.
- Include residual-versus-fitted, residual-versus-order, and QQ-plots. Examine possible outliers, leverage, and influence. An influential observation should be investigated, not automatically deleted.
- Distinguish linearity, constant spread, normal error approximation, and independence. Residual plots do not establish representative sampling or causality.
- At a meaningful `x0` within the observed range, report both a confidence interval for the mean response and a wider prediction interval for one new observation.
- Explain extrapolation and do not predict outside the observed range without a defensible engineering model.
- End with the eight-step statistical regression workflow from Chapter 10 and a compact report that combines slope, uncertainty, R-squared, residual variation, diagnostics, prediction, and limitations.

Use `energy_load.csv` as the principal case if suitable. Remove reliance on `Calculating_metrics.md` unless every claim in it has been checked against Chapter 10. Do not retain it merely as a substitute for the textbook.

### Tutorial 11 -- Categorical data and chi-square tests

Revision level: major rebuild.

Use Chapter 11 as the source of truth. The tutorial should show how observed counts, expected counts, residual patterns, and effect magnitude combine into a categorical analysis.

Required content:

- Distinguish categorical counts from quantitative measurements. Use counts, not a table containing only percentages, in the chi-square calculation.
- Include a goodness-of-fit question against specified category probabilities. Make category order and expected counts explicit.
- Include a contingency-table analysis and explain the design distinction between independence and homogeneity. The Pearson calculation may be the same, but the sampling design and interpretation differ.
- Calculate or display expected counts and degrees of freedom. If probabilities or model parameters were estimated from the same data, adjust the degrees of freedom correctly or avoid that example.
- Explain the Pearson chi-square statistic as a sum of non-negative cell contributions.
- Report observed counts together with relevant conditional proportions so the practical pattern is visible.
- Calculate Pearson residuals and adjusted residuals, label rows and columns, and use a readable table or heatmap to identify the cells driving the global result.
- Calculate Cramer's V as an effect magnitude and interpret it cautiously. Do not present a universal cutoff as an engineering decision rule.
- Check sparse expected counts. Pool categories only when the combined category is substantively meaningful and not chosen after seeing an inconvenient result.
- Include a short computational alternative for sparse tables, such as a seeded Monte Carlo/permutation assessment under the appropriate null model or Fisher's exact test for a compatible 2-by-2 design. Do not let this extension dominate the tutorial.
- State explicitly that chi-square goodness of fit on binned continuous observations is not the preferred normality assessment in this course. QQ-plots and the formal methods introduced in Chapter 7 retain the continuous information.
- A significant table result is not a root-cause analysis and does not by itself establish causation.
- End with the nine-step categorical workflow from Chapter 11 and a report containing the global test, expected-count adequacy, conditional proportions, residual pattern, Cramer's V, and design limitations.

Use `defect_types.csv` as the principal case if suitable. Keep the goodness-of-fit example compact and connected to the same engineering setting.

### Tutorial 12 -- Planning and reporting an integrated statistical analysis

Revision level: complete rebuild.

Use Chapter 12 as the direct conceptual structure. Introduce no new statistical method. This tutorial is the bridge from individual methods to the final group project.

Replace the current recycled thickness analysis with one new, coherent engineering case. Prefer a reproducibly generated synthetic dataset that supports a single decision and at least three meaningful subquestions from three different Sessions/Chapters 1--11. Do not combine unrelated existing datasets.

A suitable design is an integrated system-performance dataset with one independent row per benchmark run and variables such as:

- unique run identifier;
- system or configuration group;
- a quantitative operating-load predictor;
- a quantitative performance or energy response;
- a second quantitative outcome relevant to the same decision; and
- a categorical reliability or incident outcome.

If this design is used, add its generation transparently to `tools/generate_datasets.py`, use `numpy.random.default_rng(2026)`, save the dataset under `data/`, and update `data/generation_log.json`. State clearly in the tutorial that the data are synthetic and describe the simulated study design. Do not expose hidden "true answers" as if students would know them in a real analysis.

The integrated case must demonstrate the Chapter 12 workflow:

1. formulate one engineering decision and translate it into explicit statistical questions;
2. identify the target population, observational unit, variables, units, and practical thresholds;
3. audit provenance, identifiers, missingness, ranges, category coding, dependence, and measurement comparability;
4. distinguish primary questions from exploratory questions before displaying inferential results;
5. use descriptive summaries and plots before formal methods;
6. select at least three methods because each answers a stated subquestion, not merely to reach a required count;
7. state assumptions and diagnostics for each method;
8. report estimates, confidence intervals, test statistics, degrees of freedom, p-values, effect magnitudes, and relevant plots without dumping raw software output;
9. integrate the separate results into one evidence-based engineering recommendation;
10. distinguish statistical evidence, practical importance, association, causation, and scope of generalisation; and
11. state specific limitations and what additional evidence would reduce the important uncertainty.

The three-method example should model the project requirement while remaining manageable. A coherent combination might be one-way ANOVA for a performance comparison, simple linear regression for an operating relationship, and a chi-square analysis for a reliability pattern. This is a suggested design, not a licence to force those methods onto unsuitable data.

Add a reusable project-planning table or Markdown template containing at least:

- engineering objective and intended decision;
- target population and observational unit;
- dataset source and study design;
- primary and secondary statistical questions;
- for each selected method: session/chapter, parameter or effect, variables, reason for selection, assumptions, diagnostics, and expected output;
- practical threshold or decision criterion;
- missing-data and unusual-observation plan;
- distinction between planned and exploratory analyses;
- integrated reporting structure; and
- limitations and reproducibility checks.

Add a final-project readiness checklist that reflects the fixed constraints exactly:

- deadline June 1;
- 2--4 students, with deviations discussed with R. Brooks before Session 12;
- 25 hours per student;
- one Jupyter notebook;
- Markdown cells for explanations and code cells for Python;
- every code cell executed and outputs visible;
- at least three statistical methods from three different Sessions/Chapters 1--11;
- compliance with Brooks Chapter 12 and Tutorial 12;
- one coherent investigation rather than disconnected analyses; and
- readiness to discuss the project during the exam as part of the overall course grade.

The tutorial itself should remain a guided worked example, not the final-project brief and not a solution template that dictates student topics. It should teach a transferable analysis process while preserving the students' freedom to choose their own engineering question and dataset.

## Narrow session-page corrections

The task is primarily to rebuild tutorials. Make only narrowly necessary corrections to Session 06--12 `README.md` files when a page directly contradicts the textbook or revised tutorial. Examples include:

- replacing a Wald interval presented as the practical default with Wilson terminology;
- removing an instruction to use Levene's test as an automatic pooled-versus-Welch selector;
- removing machine-learning framing from Session 10 if present;
- ensuring Session 12 links Brooks Chapter 12 and the revised Tutorial 12; and
- removing outdated statements that conflict with the fixed project constraints.

Do not rewrite the session plans, learning objectives, navigation, or folder structure without a demonstrated need. Report every session-page change separately.

## Notebook construction and execution

For every tutorial:

1. Treat the `.md` file as the maintainable tutorial source.
2. Generate or synchronise the corresponding notebook with `tools/md_to_notebook.py`.
3. Execute the notebook from a clean kernel in an environment compatible with the course setup.
4. Save execution counts and all relevant outputs in the notebook.
5. Confirm that no code cell has an error output, stale output, hidden dependency on a previous kernel state, or an absolute path.
6. Confirm that a top-to-bottom run produces the reported values and plots.
7. Ensure Markdown formulas render correctly in Jupyter and MkDocs.
8. Keep outputs concise. Do not print thousands of simulated values or unreadable full data frames.
9. Verify notebook JSON after execution.
10. Check that the notebook works both from the repository root and when opened from its session directory.

Use only packages already appropriate for the course: NumPy, pandas, Matplotlib, SciPy, and statsmodels. Do not add a new package unless it is necessary, lightweight, available in the course environment, and documented. Scikit-learn is specifically out of scope for Tutorial 10.

## Validation requirements

Before handing back the work:

- execute Tutorials 6--12 from clean kernels;
- validate every notebook as JSON;
- run the relevant MkDocs build check;
- inspect every rendered plot for labels, units, clipping, and legibility in light and dark themes where relevant;
- check that all notebook links from Session 06--12 work;
- confirm all reported numerical values against executed outputs;
- search Tutorials 6--12 for incorrect p-value interpretations, `accept H0`, automatic causal claims, automatic outlier deletion, universal normality cutoffs, and unqualified `n=30` rules;
- search for any use of the Wald proportion interval as the practical default;
- search for any preliminary Levene-test decision rule selecting pooled versus Welch analysis;
- search Tutorial 10 for remaining scikit-learn, train/test, or machine-learning content;
- search Tutorial 11 for chi-square normality testing;
- verify that Tutorial 12 contains no new statistical method and that its three methods answer three explicit, coherent questions;
- verify that the final-project readiness checklist reproduces every fixed project constraint exactly; and
- inspect `git diff --check` and `git status` without altering unrelated work.

## Deliverable

Return:

1. a concise list of files changed;
2. a tutorial-by-tutorial summary of the pedagogical and statistical changes;
3. the datasets created or changed and how they were generated reproducibly;
4. the notebook execution and MkDocs validation commands and outcomes;
5. a list of any session-page corrections;
6. confirmation that every code cell is executed and all outputs are visible; and
7. any remaining choice that genuinely requires an instructor decision.

Do not commit, push, deploy, or create the final-project assignment brief. Leave the revised Tutorials 6--12 ready for instructor review.

---
