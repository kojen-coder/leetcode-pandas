import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number')['order_number'].count().reset_index(name='count')
    return df[df['count'] == df['count'].max()][['customer_number']]
