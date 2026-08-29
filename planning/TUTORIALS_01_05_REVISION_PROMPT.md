# Revision prompt for STA1 Tutorials 1--5

Use the following prompt in a coding agent that can access both repositories.

---

You are revising the first five Python tutorials for the practical statistics course STA1.

## Repositories and sources of truth

- Course site: `C:\GitHub\STA1_26`
- Theory textbook: `C:\GitHub\STA_book_v1`
- Tutorial files in scope:
  - `01_Data_and_Descriptive_Statistics/Tutorial_01.md`
  - `01_Data_and_Descriptive_Statistics/Tutorial_01_notebook.ipynb`
  - `02_Probability_for_Data_Analysis/Tutorial_02.md`
  - `02_Probability_for_Data_Analysis/Tutorial_02_notebook.ipynb`
  - `03_Random_Variables_and_Discrete_Distributions/Tutorial_03.md`
  - `03_Random_Variables_and_Discrete_Distributions/Tutorial_03_notebook.ipynb`
  - `04_Continuous_Distributions_in_Practice/Tutorial_04.md`
  - `04_Continuous_Distributions_in_Practice/Tutorial_04_notebook.ipynb`
  - `05_Sampling_Distributions_and_the_CLT/Tutorial_05.md`
  - `05_Sampling_Distributions_and_the_CLT/Tutorial_05_notebook.ipynb`

Before editing, inspect `git status` in both repositories and preserve all unrelated work. Read the current Session 01--05 `README.md` files and Chapters 1--5 in the textbook source. The textbook is authoritative for theory, terminology, notation, assumptions, and mathematical claims. The session pages are authoritative for the teaching scope and learning objectives. The tutorials are the practical Python layer and must not become a second theory textbook.

Do not edit the textbook. Do not change the 12-session course structure. Do not commit, push, or deploy unless explicitly asked after the revision has been reviewed.

## Overall teaching design

STA1 is a practical, Python-oriented course for engineering students. SMP is the more mathematically advanced probability course. Each STA1 tutorial should therefore be a realistic guided lab that connects a compact piece of theory to computation, visualisation, and interpretation.

Use these principles throughout Tutorials 1--5:

1. Keep enough mathematics to explain what the Python computation means, but refer to the Brooks chapter for the full theory rather than repeating long derivations.
2. Organise each tutorial as a coherent engineering investigation: question, data/model, computation, visualisation, interpretation, and limitations.
3. Keep the workload realistic for one practical part of a 2 x 45-minute session. Prefer depth and interpretation over many disconnected examples.
4. Use the existing datasets in `STA1_26/data` unless a known theoretical population is pedagogically necessary. Tutorial 5 is such a case.
5. Use `numpy.random.default_rng(2026)` for reproducible simulation. Avoid global `np.random.seed`.
6. Use vectorised NumPy operations where they improve clarity; do not hide the statistical idea inside unnecessarily advanced code.
7. Label every plot with the quantity and unit. Keep the existing visual palette where practical (`#6CA2C6` and `#FF8C00`).
8. Make students interpret every important numerical result or plot in the engineering context. A function call alone is not a statistical conclusion.
9. Distinguish model assumptions from observed facts. A QQ-plot is a diagnostic, not proof; a fitted distribution is a working model, not the data-generating truth.
10. Keep uppercase notation for random variables/statistics and lowercase for realised observations, for example (X) versus (x) and \(\bar X\) versus \(\bar x\).
11. In mathematics, parameterise the normal distribution as (N(\mu,\sigma^2)). In SciPy, explicitly state that `scale` is the standard deviation \(\sigma\), not the variance.
12. For exponential models, distinguish rate \(\lambda\) from SciPy's scale \(1/\lambda\).
13. Prefer SciPy survival functions for upper tails. For an integer-valued variable, explain precisely that
    \[
    P(X\geq k)=P(X>k-1)=\texttt{dist.sf(k-1)}.
    \]
    Do not recommend `1 - cdf(...)` as the preferred numerical method.
14. Do not add ordinary exercise sets to the tutorials; exercises live on the session pages. Short prediction questions and interpretation pauses inside a guided tutorial are welcome.
15. Keep each Markdown tutorial and its notebook semantically identical. The notebook may split the same material into executable cells, but it must not contain different claims, examples, or conclusions.

## Required revisions by tutorial

### Tutorial 1 -- Data and descriptive statistics

Revision level: moderate.

Keep the plate-thickness case and `sensor_thickness.csv`. Preserve the focus on description rather than inference, but make the tutorial answer all parts of its own opening question.

- Retain mean, median, sample standard deviation, quartiles, IQR, histogram, and boxplot.
- Add a compact groupwise summary for production lines A and B, including at least `n`, mean, median, sample SD, and IQR.
- Add an index/run plot of `thickness_um` against `sample_id`, preferably distinguishing the production line and showing the 250 micrometre target. This is needed because both the session page and tutorial text promise that students will inspect possible drift.
- Explain that the `1.5 x IQR` rule identifies potential outliers; it is not an automatic deletion rule.
- Briefly note that software packages can use different quartile conventions. State which pandas convention is being used rather than implying that every hand calculation must produce an identical quartile.
- Keep the `ddof=1` distinction, but phrase it contextually: use the sample standard deviation when the observed data are treated as a sample. Do not claim that every standard deviation calculation in all circumstances must use `n-1`.
- End with a defensible descriptive conclusion. Do not infer a line effect or process change from the plots.
- Update the forward reference so that a two-line inferential comparison points primarily to Session 08; Session 09 is for ANOVA with more than two groups.

### Tutorial 2 -- Probability for data analysis

Revision level: light. Preserve the current automated-inspection case and most of its structure; it is already the strongest of the five tutorials.

- Retain the event definitions, four-cell contingency table, natural frequencies, independence versus mutual exclusivity, total probability, Bayes' theorem, base-rate curve, improved false-positive-rate scenario, and seeded simulation check.
- Keep the distinction between expected/model-based counts and observed data explicit.
- Tighten duplicated theory where the textbook already gives the full explanation, but do not remove the denominators and verbal interpretations that make conditional probability practical.
- Verify every calculated probability and ensure complements, intersections, and conditioning are labelled consistently.
- Keep the main engineering conclusion: sensitivity is not positive predictive value, and a flag is evidence rather than proof.
- Preserve a few embedded prediction/interpretation questions, but do not expand this into a separate exercise sheet.

### Tutorial 3 -- Random variables and discrete distributions

Revision level: moderate.

Keep the packet-loss/binomial and rack-fault/Poisson cases, but improve the connection between the models, SciPy, and their assumptions.

- Retain the distinction between (X) and (x), PMF and CDF, Bernoulli, binomial, and Poisson.
- Replace upper-tail calculations such as `1 - binom.cdf(4, n, p)` with `binom.sf(4, n, p)`, and replace `1 - poisson.cdf(2, mu=lam)` with `poisson.sf(2, mu=lam)`.
- Correct the explanatory text: SciPy's `sf(k)` is (P(X>k)), so `sf(k-1)` gives (P(X\geq k)). Explain that `sf` is normally preferable to subtracting a CDF from 1 in a far tail.
- Show at least one useful `ppf` computation, for example the smallest count below which a stated percentage of packet-loss outcomes falls.
- Consider a two-panel PMF/CDF visualisation if it remains readable and fits the session workload.
- State and revisit the model assumptions: fixed (n), constant (p), and independence for a binomial model; a stable rate and an appropriate count window for a Poisson model.
- Treat the empirical loss rate in `packet_loss.csv` as an estimate, not as proof that the binomial assumptions hold.
- Keep combinatorics limited to explaining the binomial coefficient.

### Tutorial 4 -- Continuous distributions in practice

Revision level: moderate to substantial.

The current tutorial covers normal and exponential models well but omits the uniform distribution even though it is in the session objectives.

- Retain CDF, SF, PPF, the normal response-time model, the exponential lifetime model, and the QQ-plot.
- Add one short, natural uniform-model example. A good choice is a sensor rounding error uniformly distributed over a fixed interval or a waiting time uniformly distributed within a polling cycle. Show the SciPy parameterisation `uniform(loc=a, scale=b-a)` and compute one interval or tail probability.
- Add an explicit (z)-score computation and connect it to `norm.cdf` or `norm.sf`. Make clear that software replaces table lookup without changing the standardisation concept.
- Keep `norm(loc=mu, scale=sigma)` and `expon(scale=1/rate)` explicit.
- When parameters are estimated from `response_times.csv` or `component_lifetimes.csv`, describe the resulting probabilities as model-based estimates.
- Remove the opening reference to log-transformed response times unless the tutorial actually investigates a log transformation. Do not introduce an unused modelling branch.
- Ensure the QQ-plot is interpreted as evidence about model adequacy, not as a pass/fail normality certificate.
- Retain the course boundary: students interpret density and cumulative area but do not integrate densities by hand.

### Tutorial 5 -- Sampling distributions and the CLT

Revision level: major rebuild.

The current tutorial repeatedly samples with replacement from the observed sensor dataset. That is bootstrap-style resampling, which conflates a bootstrap distribution with the theoretical repeated-sampling experiment used to introduce the CLT. Bootstrap belongs later as an estimation method. Rebuild Tutorial 5 around a known population model.

Use a clearly right-skewed population, preferably an exponential population with specified mean and standard deviation, and simulate independent samples directly from that model.

The rebuilt tutorial must include:

1. A visual comparison of the population/individual-observation distribution and sampling distributions of \(\bar X\) for several sample sizes, such as (n=1,4,25). Do not present (n=30) as a universal threshold.
2. A vectorised repeated-sampling simulation with a fixed generator and enough repetitions for stable plots, for example 10,000--20,000 repetitions.
3. A summary table for each (n) comparing:
   - the population mean \(\mu\);
   - the empirical mean of the simulated sample means;
   - the theoretical standard error \(\sigma/\sqrt n\);
   - the empirical standard deviation of the simulated sample means.
4. A normal curve overlay where it is pedagogically useful, labelled as a CLT approximation for the non-normal population.
5. A separate, short illustration of the law of large numbers, such as a cumulative mean along one growing sequence. Explicitly distinguish this concentration idea from the CLT's statement about the distribution of standardised sample means across repeated samples.
6. One practical probability calculation for a sample mean. Compare the normal approximation with the simulated proportion and interpret any discrepancy.
7. A clear distinction between these cases:
   - a normal population gives \(\bar X\sim N(\mu,\sigma^2/n)\) exactly for every (n);
   - a non-normal i.i.d. population gives \(\bar X\approx N(\mu,\sigma^2/n)\) only as a CLT approximation whose quality depends on the population and (n).
8. Explicit warnings that the CLT does not make the raw observations normal, repair dependence or drift, or justify a non-representative sample.

Do not use bootstrap resampling in this tutorial. Do not introduce confidence intervals or hypothesis tests early. Do not overload the practical tutorial with chi-square or Student's (t); the textbook supplies that theoretical bridge and the later sessions will use it.

## One minimal session-page correction

After revising Tutorial 5, make one narrowly scoped correction in `05_Sampling_Distributions_and_the_CLT/README.md`: for a non-normal population under the CLT, use

\[
\bar X\approx N(\mu,\sigma^2/n),
\]

not `\sim`. Reserve `\sim` for the exact normal-population result. Do not otherwise rewrite the session pages.

## Notebook and validation requirements

For every tutorial:

- Update both the `.md` file and the corresponding `.ipynb`.
- Execute the notebook from a clean kernel in an environment compatible with the course setup.
- Ensure the notebook has no error outputs, stale outputs, hidden dependency on a previous cell state, or absolute local paths.
- Verify that data lookup works when run from the repository root and when the notebook is opened from its session directory.
- Use only course-level packages already used by the site: NumPy, pandas, Matplotlib, and SciPy.
- Validate notebook JSON and run the relevant MkDocs build check.
- Check that formulas render in both MkDocs and Jupyter.
- Confirm that all reported numerical conclusions match the executed output.
- Search for and remove inconsistent normal notation, inaccurate CDF/SF statements, unqualified causal/inferential claims, and any claim that (n=30) is a universal CLT rule.

## Deliverable

Return:

1. a concise list of files changed;
2. a short summary of the pedagogical changes to each tutorial;
3. the commands/checks used for notebook execution and MkDocs validation;
4. any remaining issue that needs an instructor decision.

Do not commit, push, or deploy. Leave the revised files ready for instructor review.

---
