import pandas as pd
import numpy as np

def create_node_attributes(G):

    np.random.seed(42)
    nodes = list(G.nodes())
    

    # numeric income
    income_numeric = np.random.randint(20000,100000,len(nodes))

    # categorize income
    income_category = pd.cut(
        income_numeric,
        bins=[0,40000,70000,200000],
        labels=["low","medium","high"]
    )

    data = {
        "node": nodes,
        "age": np.random.randint(18,60,len(nodes)),
        "gender": np.random.choice([0,1],len(nodes)),
        "location": np.random.randint(1,5,len(nodes)),
        "income_numeric": income_numeric,
        "income_category": income_category
    }

    df = pd.DataFrame(data)

    return df