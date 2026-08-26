"""Reproduce the calculations and base-rate figure in Chapter 2."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "figure"


def main() -> None:
    p_defect = 0.02
    sensitivity = 0.95
    false_positive_rate = 0.08
    p_flag = sensitivity * p_defect + false_positive_rate * (1 - p_defect)
    ppv_at_example = sensitivity * p_defect / p_flag

    n = 10_000
    n_defective = round(n * p_defect)
    n_good = n - n_defective
    tp = round(n_defective * sensitivity)
    fn = n_defective - tp
    fp = round(n_good * false_positive_rate)
    tn = n_good - fp
    table = pd.DataFrame(
        {"flagged": [tp, fp], "not_flagged": [fn, tn]},
        index=["defective", "good"],
    )
    table["total"] = table.sum(axis=1)
    table.loc["total"] = table.sum(axis=0)
    print(table)
    print(f"\nP(flag) = {p_flag:.4f}")
    print(f"P(defect | flag) = {ppv_at_example:.6f}")

    rng = np.random.default_rng(2026)
    defective = rng.random(100_000) < p_defect
    flagged = np.where(
        defective,
        rng.random(100_000) < sensitivity,
        rng.random(100_000) < false_positive_rate,
    )
    print(f"Simulated P(defect | flag) = {defective[flagged].mean():.6f}")

    base_rates = np.linspace(0.001, 0.20, 300)
    ppv = sensitivity * base_rates / (
        sensitivity * base_rates
        + false_positive_rate * (1 - base_rates)
    )
    plt.rcParams.update(
        {"font.size": 10, "axes.spines.top": False, "axes.spines.right": False}
    )
    fig, ax = plt.subplots(figsize=(8.2, 4.4), constrained_layout=True)
    ax.plot(base_rates, ppv, color="#6ca2c6", linewidth=2.2)
    ax.scatter(
        [p_defect],
        [ppv_at_example],
        color="#ee7f38",
        s=55,
        zorder=3,
        label="Worked example",
    )
    ax.axvline(p_defect, color="#253746", linestyle="--", linewidth=1)
    ax.set(
        xlabel="Defect base rate",
        ylabel="Positive predictive value",
        xlim=(0, 0.20),
        ylim=(0, 0.80),
    )
    ax.xaxis.set_major_formatter(lambda value, _: f"{100 * value:.0f}%")
    ax.yaxis.set_major_formatter(lambda value, _: f"{100 * value:.0f}%")
    ax.legend(frameon=False)
    fig.savefig(FIGURE / "chapter02_base_rate.pdf", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
