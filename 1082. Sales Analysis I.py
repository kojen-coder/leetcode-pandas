import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    seller_price = sales.groupby('seller_id')['price'].sum().reset_index(name='count')
    return seller_price[seller_price['count'] == seller_price['count'].max()][['seller_id']]