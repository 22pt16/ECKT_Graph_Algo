import matplotlib.pyplot as plt


def plot_cluster_sizes(cluster_sizes):

    plt.figure(figsize=(8,4))

    plt.bar(range(len(cluster_sizes)), cluster_sizes)

    plt.xlabel("Cluster ID")
    plt.ylabel("Cluster Size")

    plt.title("Cluster Size Distribution")

    plt.tight_layout()

    plt.savefig("output/cluster_sizes.png")

    plt.close()


def plot_cluster_distribution(cluster_sizes):

    plt.figure(figsize=(8,4))

    plt.hist(cluster_sizes, bins=10)

    plt.xlabel("Cluster Size")
    plt.ylabel("Frequency")

    plt.title("Cluster Size Frequency Distribution")

    plt.tight_layout()

    plt.savefig("output/cluster_distribution.png")

    plt.close()