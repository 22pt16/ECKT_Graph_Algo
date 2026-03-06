from src.load_graph import load_facebook_graph
from src.generate_attributes import create_node_attributes
from src.clustering import perform_clustering
from src.kanonymity import enforce_k_anonymity
from src.generalization import generalize_attributes
from src.tcloseness import check_t_closeness
from src.evaluation import cluster_sizes, anonymity_score, information_loss
from src.visualization import plot_cluster_sizes

import networkx as nx
import pandas as pd

print("Loading graph...")

print("\nGraph Statistics:")
G = load_facebook_graph("data/facebook_combined.txt")

print("Average degree:", sum(dict(G.degree()).values())/G.number_of_nodes())
print("Clustering coefficient:", nx.average_clustering(G))


print("\nGenerating attributes...")
df = create_node_attributes(G)

print(df.columns.tolist())


print("\nRunning K means++ clustering...")
df = perform_clustering(df, k=20)


print("\nApplying k-anonymity...")
df = enforce_k_anonymity(df, k=10)


print("\nGeneralizing attributes...")
df = generalize_attributes(df)


print("\nChecking t-closeness...")
valid_clusters = check_t_closeness(
    df,
    sensitive_col="income_category",
    t=0.7
)

print("\nValid clusters:", valid_clusters)


print("\nEvaluation")

print("Cluster sizes:\n", sorted(cluster_sizes(df)))

print("Anonymity score:", anonymity_score(df))

print("Information loss:", information_loss(df))

print("\nPrivacy Summary")
print("Total clusters:", df["cluster"].nunique())
print("Clusters satisfying t-closeness:", len(valid_clusters))

df.to_csv("output/anonymized_data.csv", index=False)
print("Output saved as : output/anonymized_data.csv ")
plot_cluster_sizes(cluster_sizes(df))