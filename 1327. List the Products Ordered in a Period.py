import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders[(orders['order_date']>='2020-02-01') & (orders['order_date']<'2020-03-01')]\
    .groupby('product_id').agg(unit=('unit', 'sum'))
    return df[df['unit']>=100].merge(products, on='product_id', how='inner')[['product_name', 'unit']]
