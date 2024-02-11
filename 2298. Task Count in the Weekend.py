import pandas as pd
def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:
    tasks['submit_date'] = pd.to_datetime(tasks['submit_date'])
    tasks['day_of_week'] = tasks['submit_date'].dt.dayofweek

    tasks.loc[tasks['day_of_week'].isin([5, 6]), 'weekend_cnt'] = 1
    tasks.loc[tasks['day_of_week'].isin([0, 1, 2, 3, 4]), 'working_cnt'] = 1
    tasks.fillna(0, inplace=True)
    df = pd.DataFrame()
    df['weekend_cnt'] = [tasks['weekend_cnt'].sum()]
    df['working_cnt'] = [tasks['working_cnt'].sum()]

    return df
