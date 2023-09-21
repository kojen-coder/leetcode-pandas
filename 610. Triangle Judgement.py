import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    condition = (triangle['x']+triangle['y'] > triangle['z']) & (triangle['y']+triangle['z'] > triangle['x']) & (triangle['x']+triangle['z'] > triangle['y'])
    triangle.loc[condition, 'triangle'] = 'Yes'
    triangle.loc[~condition, 'triangle'] = 'No'
    return triangle