import pandas as pd

def reported_posts(actions: pd.DataFrame) -> pd.DataFrame:
    df = actions[(actions['action_date'] == '2019-07-04') & (actions['action'] =='report')]
    return df.groupby('extra')['post_id'].nunique().reset_index(name='report_count').rename(columns={'extra': 'report_reason'})[['report_reason', 'report_count']]