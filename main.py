# =========================
# Imports
# =========================
from src.load_graph import load_facebook_graph
from src.generate_attributes import create_node_attributes
from src.clustering import perform_clustering, show_distance_matrix
from src.kanonymity import enforce_k_anonymity
from src.generalization import generalize_attributes
from src.tcloseness import enforce_t_closeness
from src.evaluation import cluster_sizes, anonymity_score, information_loss
from src.visualization import plot_cluster_sizes, plot_cluster_distribution

import networkx as nx
import pandas as pd
import time
import os


# =========================
# PARAMETERS 
# =========================
K = 5                  # k-anonymity level
T = 0.7                 # t-closeness threshold
NUM_CLUSTERS = 30      # number of clusters


# =========================
# START TIMER
# =========================
start_time = time.time()


# =========================
# LOAD GRAPH
# =========================
print("Loading graph...")

G = load_facebook_graph("data/facebook_combined.txt")

print("\nGraph Statistics:")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())
print("Average degree:", sum(dict(G.degree()).values()) / G.number_of_nodes())
print("Clustering coefficient:", nx.average_clustering(G))


# =========================
# GENERATE ATTRIBUTES
# =========================
print("\nGenerating attributes...")
df = create_node_attributes(G)
print("Attributes:", df.columns.tolist())


# =========================
# CLUSTERING
# =========================
print("\nRunning K-means++ clustering...")
df = perform_clustering(df, k=NUM_CLUSTERS)

show_distance_matrix(df)


# =========================
# K-ANONYMITY
# =========================
print("\nApplying k-anonymity...")
df = enforce_k_anonymity(df, k=K)
print("\nGeneralizing attributes...")
df = generalize_attributes(df)


# =========================
# T-CLOSENESS
# =========================
print("\nChecking t-closeness...")
valid_clusters = enforce_t_closeness(
    df,
    sensitive_col="income_category",
    t=T
)

total_clusters = df["cluster"].nunique()

print("\nValid clusters:", valid_clusters)
print("Clusters satisfying t-closeness:", len(valid_clusters))
print("Clusters violating t-closeness:", total_clusters - len(valid_clusters))
print("t-closeness satisfaction (%):", round(len(valid_clusters) / total_clusters * 100, 2))


# =========================
# EVALUATION METRICS
# =========================
print("\nEvaluation Metrics")

print(f"Chosen parameters → k: {K}, t: {T}, clusters: {NUM_CLUSTERS}")

sizes = cluster_sizes(df)

print("\nCluster sizes:", sorted(sizes))

print("\nDegree of Anonymization (DA):")
print("Min DA:", min(sizes))
print("Avg DA:", sum(sizes) / len(sizes))
print("Max DA:", max(sizes))

il = information_loss(df)
print("\nInformation Loss (IL):", il)


# =========================
# EXECUTION TIME
# =========================
end_time = time.time()
execution_time = round(end_time - start_time, 4)

print("\nExecution Time:", execution_time, "seconds")


# =========================
# SAVE OUTPUT
# =========================
os.makedirs("output", exist_ok=True)

df.to_csv("output/anonymized_data.csv", index=False)
print("\nOutput saved → output/anonymized_data.csv")


# =========================
# SAVE SUMMARY METRICS
# =========================
summary = {
    "nodes": G.number_of_nodes(),
    "edges": G.number_of_edges(),
    "clusters": total_clusters,
    "k": K,
    "t": T,
    "degree_of_anonymity": round(anonymity_score(df), 3),
    "t_closeness_percent": round(len(valid_clusters) / total_clusters * 100, 2),
    "information_loss": round(il,6),
    "execution_time_sec": execution_time
}
cols = ["nodes", "edges", "clusters", "k", "t", "degree_of_anonymity", " t_closeness_percent", "information_loss", "execution_time_sec"]
summary_df = pd.DataFrame([summary])
summary_df.columns = cols

file_path = "output/summary_metrics.csv"

if os.path.exists(file_path):
    summary_df.to_csv(file_path, mode='a', header=False, index=False)
else:
    summary_df.to_csv(file_path, index=False)


# =========================
# VISUALIZATION
# =========================
plot_cluster_sizes(sizes)
plot_cluster_distribution(sizes)