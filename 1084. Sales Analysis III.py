import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby('product_id').agg(mindate=('sale_date', 'min'), maxdate=('sale_date', 'max')).reset_index()
    range_product_id = df[(df['mindate'] >= '2019-01-01') & (df['maxdate'] <= '2019-03-31')][['product_id']]
    return range_product_id.merge(product, on='product_id', how='inner')[['product_id', 'product_name']]