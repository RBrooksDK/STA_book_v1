"""Reproduce the numerical summaries and figures in Chapter 1."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGURE = ROOT / "figure"


def main() -> None:
    df = pd.read_csv(DATA / "sensor_thickness.csv")
    x = df["thickness_um"]

    q1, q3 = x.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    summary = pd.Series({"n": x.count(), "mean": x.mean(), "median": x.median(), "sample_variance": x.var(ddof=1), "sample_sd": x.std(ddof=1), "minimum": x.min(), "q1": q1, "q3": q3, "maximum": x.max(), "iqr": iqr, "lower_fence": lower, "upper_fence": upper})
    print(summary.to_string())
    print("\nFlagged observations:")
    print(df.loc[(x < lower) | (x > upper), ["sample_id", "line", "thickness_um"]].to_string(index=False))
    print("\nSample SD check:", np.std(x, ddof=1))

    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    blue = "#6ca2c6"
    orange = "#ee7f38"

    fig, axes = plt.subplots(2, 1, figsize=(8.2, 5.5), gridspec_kw={"height_ratios": [3, 1]}, constrained_layout=True)
    axes[0].hist(x, bins="fd", color=blue, edgecolor="white")
    axes[0].axvline(x.mean(), color=orange, linewidth=1.8, label="Mean")
    axes[0].axvline(x.median(), color="#253746", linestyle="--", linewidth=1.5, label="Median")
    axes[0].set(xlabel="Thickness (micrometres)", ylabel="Count")
    axes[0].legend(frameon=False)
    axes[1].boxplot(x, vert=False, patch_artist=True, boxprops={"facecolor": blue, "alpha": 0.75}, medianprops={"color": orange, "linewidth": 1.8})
    axes[1].set(xlabel="Thickness (micrometres)", yticks=[])
    fig.savefig(FIGURE / "chapter01_distribution.pdf", bbox_inches="tight")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.2, 4.1), constrained_layout=True)
    colours = {"A": blue, "B": orange}
    for line, group in df.groupby("line"):
        ax.scatter(group["sample_id"], group["thickness_um"], label=f"Line {line}", color=colours[line], s=22, alpha=0.82)
    ax.axhline(250, color="#253746", linestyle="--", linewidth=1, label="250 micrometres")
    ax.set(xlabel="Collection order (sample ID)", ylabel="Thickness (micrometres)")
    ax.legend(frameon=False, ncol=3)
    fig.savefig(FIGURE / "chapter01_order.pdf", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
