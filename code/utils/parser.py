import pandas as pd
from pathlib import Path

def load_relationship_matrix():
    data_path = Path(__file__).resolve().parent.parent.parent / 'data' / 'seating_data.xlsx'
    df = pd.read_excel(data_path, index_col=0)
    return df
