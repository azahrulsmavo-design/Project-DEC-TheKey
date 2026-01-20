import pandas as pd
import numpy as np
from scipy.stats import f_oneway
import statsmodels.api as sm
from statsmodels.formula.api import ols

df = pd.read_csv("data/student_combined_data.csv")

advanced = df.loc[df["course_level"] == "Advanced", "performance_score"]
intermediate = df.loc[df["course_level"] == "Intermediate", "performance_score"]
foundation = df.loc[df["course_level"] == "Foundation", "performance_score"]

def format_p(p):
    if p < 0.001:
        return "p < 0.001"
    else:
        return f"p = {p:.3f}"

def cohens_d(x, y):
    nx, ny = len(x), len(y)
    pooled_std = np.sqrt(
        ((nx - 1)*x.var(ddof=1) + (ny - 1)*y.var(ddof=1)) / (nx + ny - 2)
    )
    return (x.mean() - y.mean()) / pooled_std

f_statistic, p_value = f_oneway(advanced, intermediate, foundation)
print("One-Way ANOVA Test for Performance Scores across Course Levels")
print(f"F-Statistic: {f_statistic:.2f}")
print(f"P-Value: {format_p(p_value)}")
print()
if p_value < 0.05:
    print("Result: Significant differences exist between course levels.")
else:
    print("Result: No significant differences between course levels.")
print()

advanced = df.loc[df["course_level"] == "Advanced", "aptitude_score"]  
intermediate = df.loc[df["course_level"] == "Intermediate", "aptitude_score"]
foundation = df.loc[df["course_level"] == "Foundation", "aptitude_score"]
f_statistic, p_value = f_oneway(advanced, intermediate, foundation)
print("One-Way ANOVA Test for Aptitude Scores across Course Levels")
print(f"F-Statistic: {f_statistic:.2f}")
print(f"P-Value: {format_p(p_value)}")
print()
if p_value < 0.05:
    print("Result: Significant differences exist between course levels.")
else:
    print("Result: No significant differences between course levels.")
print()
print()
print()

print("ANOVA Table for Performance Scores")
model = ols("performance_score ~ C(course_level)", data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)
ss_between = anova_table.loc["C(course_level)", "sum_sq"]
ss_total = ss_between + anova_table.loc["Residual", "sum_sq"]

eta_squared = ss_between / ss_total
print(f"Eta Squared (η²): {eta_squared:.3f}")

print("ANOVA table for aptitude scores")
model = ols("aptitude_score ~ C(course_level)", data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
ss_between = anova_table.loc["C(course_level)", "sum_sq"]
ss_total = ss_between + anova_table.loc["Residual", "sum_sq"]
eta_squared = ss_between / ss_total
print(f"Eta Squared (η²): {eta_squared:.3f}")


print("--- Cohen's d for Performance Scores ---")
adv_perf = df.loc[df["course_level"] == "Advanced", "performance_score"]
intm_perf = df.loc[df["course_level"] == "Intermediate", "performance_score"]
found_perf = df.loc[df["course_level"] == "Foundation", "performance_score"]

print("Advanced vs Intermediate:", cohens_d(adv_perf, intm_perf))
print("Intermediate vs Foundation:", cohens_d(intm_perf, found_perf))
print("Advanced vs Foundation:", cohens_d(adv_perf, found_perf))
print()

print("--- Cohen's d for Aptitude Scores ---")
adv_apt = df.loc[df["course_level"] == "Advanced", "aptitude_score"]
intm_apt = df.loc[df["course_level"] == "Intermediate", "aptitude_score"]
found_apt = df.loc[df["course_level"] == "Foundation", "aptitude_score"]

print("Advanced vs Intermediate:", cohens_d(adv_apt, intm_apt))
print("Intermediate vs Foundation:", cohens_d(intm_apt, found_apt))
print("Advanced vs Foundation:", cohens_d(adv_apt, found_apt))
