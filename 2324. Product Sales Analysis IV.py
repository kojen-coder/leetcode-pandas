import pandas as pd
def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge ( product, on="product_id", how="left" )
    df['total'] = df['quantity'] * df['price']
    df_result = df.groupby ( ['user_id', 'product_id'] ).agg ( total=('total', 'sum') ).reset_index ()
    df_result['rank'] = df_result.groupby ( 'user_id' )['total'].rank ( method='dense', ascending=False )
    return df_result[df_result['rank'] == 1][['user_id', 'product_id']]
