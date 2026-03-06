def cluster_sizes(df):

    return df["cluster"].value_counts()

def anonymity_score(df):

    return df["cluster"].value_counts().mean()