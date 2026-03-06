def enforce_k_anonymity(df, k):

    counts = df["cluster"].value_counts()

    small_clusters = counts[counts < k].index
    largest_cluster = counts.idxmax()

    for c in small_clusters:
        df.loc[df["cluster"] == c, "cluster"] = largest_cluster
    print("K anonymity k: ",k)
    return df