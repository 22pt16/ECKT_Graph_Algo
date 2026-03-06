import pandas as pd
import numpy as np

def create_node_attributes(G):

    nodes = list(G.nodes())
    income_levels = ["low","medium","high"]
    data = {
        "node": nodes,
        "age": np.random.randint(18,60,len(nodes)),
        "gender": np.random.choice([0,1],len(nodes)),
        "location": np.random.randint(1,5,len(nodes)),
        "income": np.random.choice(income_levels,len(nodes))
    }

    df = pd.DataFrame(data)

    return df