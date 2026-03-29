def check_t_closeness(df, sensitive_col, t):

    global_dist = df[sensitive_col].value_counts(normalize=True)

    valid_clusters = []

    for cluster in df["cluster"].unique():
        

        subset = df[df["cluster"] == cluster]

        cluster_dist = subset[sensitive_col].value_counts(normalize=True)

        # align distributions
        aligned = global_dist.index.union(cluster_dist.index)

        g = global_dist.reindex(aligned, fill_value=0)
        c = cluster_dist.reindex(aligned, fill_value=0)

        
        diff = (g - c).abs().max()

        if diff <= t:
            
            valid_clusters.append(cluster)
        print("Global distribution:", global_dist.to_dict())
        print("Cluster", cluster, "diff =", diff)

    valid_clusters = [int(c) for c in valid_clusters]    
    return valid_clusters