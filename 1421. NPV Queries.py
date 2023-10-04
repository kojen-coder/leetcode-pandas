import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    df = queries.merge(npv, on=['id', 'year'], how='left')
    return df.fillna(0)[['id', 'year', 'npv']]
