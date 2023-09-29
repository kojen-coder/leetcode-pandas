import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating'] / queries['position']
    queries['poor'] = queries.apply(lambda row: 1 if row['rating'] < 3 else 0, axis = 1)

    df = queries.groupby('query_name').agg(
        quality=('quality', 'mean'), poor_query_percentage=('poor', 'mean')).reset_index()
    df['quality'] = round(df['quality'], 2)
    df['poor_query_percentage'] = round(df['poor_query_percentage']*100, 2)
    return df

