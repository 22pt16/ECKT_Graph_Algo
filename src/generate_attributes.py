import pandas as pd
import numpy as np

def create_node_attributes(G):

    nodes = list(G.nodes())

    data = {
        "node": nodes,
        "age": np.random.randint(18,60,len(nodes)),
        "gender": np.random.choice([0,1],len(nodes)),
        "location": np.random.randint(1,5,len(nodes)),
        "income": np.random.randint(20000,100000,len(nodes))
    }

    df = pd.DataFrame(data)

    return df