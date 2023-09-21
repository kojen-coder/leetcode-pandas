import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = product.merge(sales, on='product_id', how='inner')
    s8_buyer = df[df['product_name'] == 'S8'][['buyer_id']].drop_duplicates()
    iphone_buyer = df[df['product_name'] == 'iPhone']['buyer_id'].drop_duplicates()
    return s8_buyer[~s8_buyer['buyer_id'].isin(iphone_buyer)]