import pandas as pd
import datetime

def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:
    content_list = tv_program[(tv_program['program_date'] >= datetime.datetime(2020, 6,1)) &
    (tv_program['program_date'] < datetime.datetime(2020, 7, 1))]['content_id'].tolist()
    df = content[(content['Kids_content'] == 'Y') & (content['content_type'] == 'Movies')]
    df['content_id'] = df['content_id'].astype(int)
    return df[df['content_id'].isin(content_list)][['title']]
