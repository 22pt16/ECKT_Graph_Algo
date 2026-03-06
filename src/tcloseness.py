def check_t_closeness(df, sensitive_col, t):

    global_dist = df[sensitive_col].value_counts(normalize=True)

    valid_clusters = []

    for cluster in df["cluster"].unique():

        subset = df[df["cluster"] == cluster]

        dist = subset[sensitive_col].value_counts(normalize=True)

        diff = abs(global_dist - dist).fillna(0).sum()

        if diff <= t:

            valid_clusters.append(cluster)

    return valid_clusters