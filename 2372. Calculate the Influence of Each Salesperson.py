def calculate_influence(salesperson: pd.DataFrame, customer: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(sales, customer, on='customer_id', how="left").merge(
        salesperson, on="salesperson_id", how="right")
    return df.groupby(["salesperson_id", "name"]).agg(total=("price", "sum")).reset_index()
