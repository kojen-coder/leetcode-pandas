import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    df = department.pivot(index='id', columns='month', values='revenue').add_suffix('_Revenue').reset_index()

    new_columns = ['id'] + [f"{month}_Revenue" for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]]
    df = df.reindex(columns=new_columns)

    return df