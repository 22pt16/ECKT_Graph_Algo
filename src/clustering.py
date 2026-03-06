from sklearn.cluster import KMeans

def perform_clustering(df, k):

    features = df[["age","gender","location"]]

    model = KMeans(
        n_clusters=k,
        init="k-means++",
        random_state=42
    )

    df["cluster"] = model.fit_predict(features)

    return df