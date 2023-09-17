import pandas as pd
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result_row = []

    for index, row in products.iterrows():
        product_id = row['product_id']

        for store_col in ['store1', 'store2', 'store3']:
            price = row[store_col]
            if pd.notna(price):
                result_row.append((product_id, store_col, price))
    result_table = pd.DataFrame(result_row, columns=['product_id', 'store', 'price'])
    return result_table