def enforce_k_anonymity(df, k):

    counts = df["cluster"].value_counts()

    small_clusters = counts[counts < k].index

    for c in small_clusters:

        df.loc[df["cluster"] == c, "cluster"] = -1

    return df