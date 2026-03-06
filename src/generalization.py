import pandas as pd

def generalize_attributes(df):

    # Age generalization
    df["age_generalized"] = pd.cut(
        df["age"],
        bins=[18,30,45,60],
        labels=["18-30","31-45","46-60"]
    )

    # Location generalization
    df["location_generalized"] = df["location"].replace({
        1:"Region-A",
        2:"Region-A",
        3:"Region-B",
        4:"Region-B"
    })

    return df