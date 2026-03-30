from scipy.stats import wasserstein_distance
def enforce_t_closeness(df, sensitive_col, t):

    global_dist = df[sensitive_col].value_counts(normalize=True)

    def get_distribution(subset):
        dist = subset[sensitive_col].value_counts(normalize=True)
        aligned = global_dist.index.union(dist.index)
        g = global_dist.reindex(aligned, fill_value=0)
        c = dist.reindex(aligned, fill_value=0)
        return g, c

    changed = True

    while changed:
        changed = False
        clusters = df["cluster"].unique()

        for cluster in clusters:

            subset = df[df["cluster"] == cluster]
            g, c = get_distribution(subset)

            # diff = (g - c).abs().max()
            diff = wasserstein_distance(g,c)

            
            if diff > t:

                # Find best cluster to merge with
                best_cluster = None
                best_diff = float("inf")

                for other in clusters:
                    if other == cluster:
                        continue

                    combined = df[
                        (df["cluster"] == cluster) |
                        (df["cluster"] == other)
                    ]

                    g2, c2 = get_distribution(combined)
                    new_diff = (g2 - c2).abs().max()

                    if new_diff < best_diff:
                        best_diff = new_diff
                        best_cluster = other

                # Merge cluster into best cluster
                df.loc[df["cluster"] == cluster, "cluster"] = best_cluster

                print(f"Merging cluster {cluster} → {best_cluster}")

                changed = True
                break   # restart loop after change

    # Final valid clusters
    valid_clusters = []

    for cluster in df["cluster"].unique():
        subset = df[df["cluster"] == cluster]
        g, c = get_distribution(subset)
        diff = (g - c).abs().max()

        if diff <= t:
            valid_clusters.append(cluster)

    return df, valid_clusters