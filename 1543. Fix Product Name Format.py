import pandas as pd

def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:
    sales['sale_date'] = pd.to_datetime(sales['sale_date']).dt.strftime("%Y-%m")
    sales['product_name'] = sales['product_name'].str.lower().str.strip()
    return sales.groupby(['product_name', 'sale_date']).agg(total=('sale_id', 'nunique')).reset_index().sort_values(['product_name', 'sale_date'], ascending=[True, True])