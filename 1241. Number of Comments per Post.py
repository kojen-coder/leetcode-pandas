import pandas as pd

def count_comments(submissions: pd.DataFrame) -> pd.DataFrame:
    sub_list = submissions.drop_duplicates(subset='sub_id')
    sub_list = sub_list[sub_list['parent_id'].isnull()]
    return submissions.groupby(['parent_id'])['sub_id'].nunique().reset_index(name='number_of_comments')\
    .merge(sub_list, left_on='parent_id', right_on='sub_id', how='right')\
    .rename(columns={'sub_id': 'post_id'}).fillna(0)[['post_id', 'number_of_comments']]\
    .sort_values('post_id')
