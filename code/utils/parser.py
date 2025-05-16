import pandas as pd

def load_relationship_matrix(path='data/seating_data.xlsx'):
    df = pd.read_excel(path, index_col=0)
    return df.values