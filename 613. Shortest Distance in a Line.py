import pandas as pd

def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    df = point.merge(point, how='cross')
    df = df[df['x_x'] != df['x_y']]
    return pd.DataFrame({'shortest': [min(abs(df['x_x'] - df['x_y']))]})