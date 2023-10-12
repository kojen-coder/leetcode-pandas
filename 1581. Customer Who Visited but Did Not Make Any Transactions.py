import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = visits.merge(transactions, on="visit_id", how="left")
    df1 = df[df['transaction_id'].isnull()]
    return df1.groupby('customer_id').agg(count_no_trans=('transaction_id', 'size')).reset_index()
