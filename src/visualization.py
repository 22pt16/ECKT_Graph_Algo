import matplotlib.pyplot as plt

def plot_cluster_sizes(sizes):

    plt.figure(figsize=(8,4))

    plt.bar(range(len(sizes)), sizes)

    plt.xlabel("Cluster ID")
    plt.ylabel("Cluster Size")

    plt.title("Cluster Size Distribution")

    plt.tight_layout()

    plt.show()