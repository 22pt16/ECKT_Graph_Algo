import numpy as np

def cluster_sizes(df):

    return df["cluster"].value_counts().tolist()


def anonymity_score(df):

    return df["cluster"].value_counts().mean()


def information_loss(df):

    original_var = df["income_numeric"].var()

    cluster_var = df.groupby("cluster")["income_numeric"].var().mean()

    return cluster_var / original_var