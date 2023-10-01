import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.merge(units_sold, on=['product_id'], how="inner")
    df = df[(df["start_date"] <= df["purchase_date"]) & (
        df["end_date"] >= df["purchase_date"])].reset_index(drop=True)
    p2 = prices[['product_id']].drop_duplicates(subset=['product_id']).reset_index(drop=True)
    df['total_p'] = df['price'] * df['units']
    df2 = df.groupby(['product_id']).agg(total=('total_p', 'sum'),
    total_u=('units', 'sum')).reset_index()
    df2['average_price'] = (df2['total'] / df2['total_u']).round(2)
    df2 = df2.merge(p2, on='product_id', how='right').fillna(0)
    return df2[["product_id", 'average_price']]

