import networkx as nx

def load_facebook_graph(path):

    G = nx.read_edgelist(
        path,
        create_using=nx.Graph(),
        nodetype=int
    )

    print("Nodes:", G.number_of_nodes())
    print("Edges:", G.number_of_edges())

    return G