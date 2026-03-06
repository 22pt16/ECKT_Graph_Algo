from src.load_graph import load_facebook_graph
from src.generate_attributes import create_node_attributes
from src.clustering import perform_clustering
from src.kanonymity import enforce_k_anonymity
from src.tcloseness import check_t_closeness

def main():

    print("Loading graph...")

    G = load_facebook_graph("data/facebook_combined.txt")

    print("Generating attributes...")

    df = create_node_attributes(G)

    print("Running clustering...")

    df = perform_clustering(df, k=20)

    print("Applying k-anonymity...")

    df = enforce_k_anonymity(df, k=5)

    print("Checking t-closeness...")

    valid = check_t_closeness(df,"income",t=0.3)

    print("Valid clusters:",valid)

    df.to_csv("output/anonymized_data.csv",index=False)

if __name__ == "__main__":
    main()