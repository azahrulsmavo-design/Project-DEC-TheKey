import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv("data/student_combined_data.csv")

    sns.set(style="darkgrid")
    order = ["Advanced", "Intermediate", "Foundation"]

    df["course_level"] = pd.Categorical(df["course_level"], categories=order, ordered=True)

    perf_stats = df.groupby("course_level", observed=False)["performance_score"].agg(["mean", "std"]).reindex(order)
    apt_stats  = df.groupby("course_level", observed=False)["aptitude_score"].agg(["mean", "std"]).reindex(order)

    r = df["performance_score"].corr(df["aptitude_score"])

    fig, axes = plt.subplots(3, 3, figsize=(16, 9), constrained_layout=True)

    sns.boxplot(data=df, x="course_level", y="performance_score", order=order, ax=axes[0,0])
    axes[0,0].set_title("Performance Score Distribution by Course Level")

    sns.boxplot(data=df, x="course_level", y="aptitude_score", order=order, ax=axes[0,1])
    axes[0,1].set_title("Aptitude Score Distribution by Course Level")

    sns.violinplot(data=df, x="course_level", y="performance_score", order=order, inner="box", ax=axes[0,2])
    axes[0,2].set_title("Performance Score Distribution (Violin Plot)")

    sns.violinplot(data=df, x="course_level", y="aptitude_score", order=order, inner="box", ax=axes[1,0])
    axes[1,0].set_title("Aptitude Distribution (Violin Plot)")

    axes[1,1].bar(order, perf_stats["mean"].values)
    axes[1,1].errorbar(order, perf_stats["mean"].values, yerr=perf_stats["std"].values, fmt="none", capsize=5)
    axes[1,1].set_title("Mean Performance Score by Level (with SD)")
    axes[1,1].tick_params(axis="x", rotation=30)

    axes[1,2].bar(order, apt_stats["mean"].values)
    axes[1,2].errorbar(order, apt_stats["mean"].values, yerr=apt_stats["std"].values, fmt="none", capsize=5)
    axes[1,2].set_title("Mean Aptitude Score by Level (with SD)")
    axes[1,2].tick_params(axis="x", rotation=30)

    sns.scatterplot(data=df, x="performance_score", y="aptitude_score", hue="course_level", hue_order=order, ax=axes[2,0])
    sns.regplot(data=df, x="performance_score", y="aptitude_score", scatter=False, ax=axes[2,0], line_kws={"linestyle":"--"})
    axes[2,0].set_title(f"Performance vs Aptitude Score (r = {r:.3f})")
    axes[2,0].legend(title="Course Level", loc="upper left", fontsize=7, title_fontsize=8)

    for lvl in order:
        sns.histplot(df.loc[df["course_level"] == lvl, "performance_score"],
                     bins=12, alpha=0.35, ax=axes[2,1], label=lvl)
    axes[2,1].set_title("Performance Score Histogram by Level")
    axes[2,1].legend(fontsize=7)

    for lvl in order:
        sns.histplot(df.loc[df["course_level"] == lvl, "aptitude_score"],
                     bins=12, alpha=0.35, ax=axes[2,2], label=lvl)
    axes[2,2].set_title("Aptitude Score Histogram by Level")
    axes[2,2].legend(fontsize=7)

    for ax in axes.ravel():
        ax.title.set_fontsize(10)
        ax.xaxis.label.set_size(9)
        ax.yaxis.label.set_size(9)
        ax.tick_params(labelsize=8)

    plt.savefig("assets/visual_comparison.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
