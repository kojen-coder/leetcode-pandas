import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    count = store[store['amount'] > 500].drop_duplicates('customer_id').shape[0]
    return pd.DataFrame({'rich_count': [count]})