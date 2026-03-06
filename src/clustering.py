import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist


def perform_clustering(df, k):

    features = df[[
        "age",
        "gender",
        "location",
        "income_numeric"
    ]].values

    print("min cluster k = ", k)

    model = KMeans(
        n_clusters=k,
        init="k-means++",
        random_state=42
    )

    model.fit(features)

    centroids = model.cluster_centers_

    dist_matrix = cdist(features, centroids)

    n = features.shape[0]

    pairs = []

    for i in range(n):
        for j in range(k):
            pairs.append((dist_matrix[i][j], i, j))

    pairs.sort(key=lambda x: x[0])

    assigned = np.full(n, -1)

    for dist, node, cluster in pairs:

        if assigned[node] == -1:
            assigned[node] = cluster

    df["cluster"] = assigned

    return df