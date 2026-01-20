import pandas as pd

def make_performance_table(df, typical_range):
    return df.groupby("course_level")["performance_score"].agg(
        Students="count",
        Average="mean",
        Lowest="min",
        Highest="max",
        Typical_Range=typical_range
    )

def make_aptitude_table(df, typical_range):
    return df.groupby("course_level")["aptitude_score"].agg(
        Students="count",
        Average="mean",
        Lowest="min",
        Highest="max",
        Typical_Range=typical_range
    )
