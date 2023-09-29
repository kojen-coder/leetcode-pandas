import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df_imm = delivery[delivery['order_date']==delivery['customer_pref_delivery_date']].shape[0]
    df_all = delivery.shape[0]
    return pd.DataFrame({'immediate_percentage': [round(df_imm/df_all*100, 2)]})

