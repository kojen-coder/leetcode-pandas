import pandas as pd

def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = warehouse.merge(products, on='product_id', how='inner')
    df['volume'] = df['units'] * df['Width'] * df['Length'] * df['Height']
    return df.groupby('name').agg(volume=('volume', 'sum')).reset_index().rename(columns={'name': 'warehouse_name'})