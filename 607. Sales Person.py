import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(company, on ='com_id', how='inner')
    red_sales_id = df[df['name'] == 'RED']['sales_id']
    return sales_person[~sales_person['sales_id'].isin(red_sales_id)][['name']]